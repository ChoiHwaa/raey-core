import raey.core.module

moduleInfo = raey.core.module.ModuleInfo(__name__.split(".")[1])

# Dummy method to perform initializing.
def entryPoint():
    print("Initializing module %s..." % moduleInfo.name)

async def get_admins(event, params):
    "Get admins list."
    
    await event.respond(await admin.fmt(event.chat))

async def is_admin(event, params):
    """
        Check whether the user is admin. Reply to a message.
    """
    
    if event.reply:
        replyMsg = await event.get_reply_message()
        bool = str(await admin.check(event.chat, replyMsg.sender))
        await event.respond(bool + ".")

async def update_admins(event, params):
    # If the admin list isn't initialized don't update the list.
    # admin.check will update it for you.
    update = False
    if admin.get(event.chat): # Get the admin list or None.
        update = True
    
    # Check whether the user that called this method is an admin.
    isAdmin = await admin.check(event.chat, event.sender)
    
    if isAdmin:
        if update:
            await admin.update(event.chat)
        await event.respond(await admin.fmt(event.chat))
    else:
        await event.respond("You're not admin.")

moduleInfo.add_command(get_admins)
moduleInfo.add_command(is_admin)
moduleInfo.add_command(update_admins)
