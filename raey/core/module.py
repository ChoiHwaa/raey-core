from raey import string_utils

class ModuleInfo:
    def __init__(self, name):
        self.name = name
        self.commands = []
        self.command_names = []
    
    def add_command(self, method):
        self.commands.append(method)
        self.command_names.append(method.__name__)
    
    def get_command(self, name):
        value = None
        for method in self.commands:
            if name == method.__name__:
                value = method
                break
        return value
        
    # Archived
    #def get_help(self):
    #	if self.help == None:
    #		self.help = self.name.capitalize() + " module.\n`Commands:\n"
    #		for command in self.commands:
    #			self.help += "  Method: " + command.__name__ + "\n"
    #			self.help += "   " + command.__doc__.replace("\n", "\n   ") + "\n"
    #		self.help = self.help.strip() + "`"
    #	return self.help
    
    def get_help(self, method=None, methodsOnly=False):
        help = self.name.capitalize() + " module.\n`Commands:\n"
        if method:
            if command := self.get_command(method):
                help += "  Method: " + command.__name__ + "\n"
                docString = "No help." if not command.__doc__ else command.__doc__
                docString = string_utils.strip_heredoc(
                    docString).replace("\n", "\n   ").strip()
                help += "   " + docString + "\n"
                help = help.strip() + "`"
            else:
                help = "Help not found."
        else:
            for command in self.commands:
                help += "  Method: " + command.__name__ + "\n"
                if not methodsOnly:
                    docString = "No help." if not command.__doc__ else command.__doc__
                    docString = string_utils.strip_heredoc(
                        docString).replace("\n", "\n   ").strip()
                    help += "   " + docString + "\n"
            help = help.strip() + "`"
        return help

if __name__ == "__main__":
    def inspect(event, params):
        """
        Inspect stickers.
        Args
          sticker_pack
        """
        pass
    def archive(event, params):
        """
            Archive stickers to local storage.
        """
        pass
    module = ModuleInfo("sickers")
    module.add_command(inspect)
    module.add_command(archive)
    print(module.command_names)
    print(module.get_help())
