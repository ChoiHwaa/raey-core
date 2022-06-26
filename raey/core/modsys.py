import os
from raey.admin import Admin
from raey import string_utils
from importlib import import_module, reload

def init(path, client):
    global modules; modules = {}
    
    print("Loading modules.")
    for filename in os.listdir(path):
        if filename.endswith(".py"):
            modname = filename[:filename.find(".")]
            print(modname)
            mod = import_module(path + "." + modname, modname)
            if hasattr(mod, "entryPoint"):
                mod.entryPoint()
                
            admin = Admin
            admin.setClient(client)
            mod.admin = admin
            
            modules[modname] = mod

async def handle(event):
    command, params, username = string_utils.splitCommand(event.text)
    me = await event.client.get_me()
    
    if username and username != me.username:
        return
    
    if command == "help":
        methodsOnly = False
        method = None
        
        if len(params) == 0:
            doc = \
            """
                Help
                Get info on modules and methods.
                `Commands:
                  /help <module>
                  /help methods <module>
                  /help method <module> <method>`
            """
            await event.respond(string_utils.strip_heredoc(doc))
            return
        if len(params) > 0 and params[0] == "methods":
            methodsOnly = True
            del params[0]
        if len(params) > 2 and params[0] == "method":
            method = params[2]
            del params[0]
            del params[1]
        if len(params) == 1 and params[0] in modules.keys():
            await event.respond(modules[params[0]].moduleInfo.get_help(method, methodsOnly))
        else:
            await event.respond("Module not found.")
        
    if command == "modules":
        await event.respond("Modules\n`" + "- " + "\n- ".join(modules.keys()) + "`")
        return
        
    if command == "reload":
        if len(params) == 1:
            if params[0] in modules.keys():
                try:
                    reload(modules[params[0]])
                    await event.respond("My modules have been updated!")
                except Exception as error:
                    await event.respond("Check console.")
                    print(error)
        return

    for module in modules.values():
        method = module.moduleInfo.get_command(command)
        if method:
            await method(event, params)
