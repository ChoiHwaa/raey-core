# raey-core
A collection of basic modules for the core functionality of a bot and provides a basic mechanism for writing new commands.

This project makes writing bot modules effortless and the minimum you need for a module is this.
``` python
# Basic module you can drop in the modules folder.

import module

moduleInfo = module.ModuleInfo(__name__)

async def hello(event, params):
    "A basic command."
    
    await event.respond("Hello friend!")

moduleInfo.add_command(hello)
```
