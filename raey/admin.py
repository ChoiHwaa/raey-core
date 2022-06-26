from telethon.tl.types import ChannelParticipantsAdmins
from telethon.utils import get_display_name

class Admin:
    admins = {}
    
    @classmethod
    def setClient(self, client):
        self.client = client
    
    @classmethod
    def get(self, chat):
        return self.admins.get(chat.id, None)
    
    @classmethod
    async def fmt(self, chat):
        if chat.id not in self.admins:
            await self.update(chat)
        info = "Admins\n"
        for user in self.admins[chat.id]:
            info += "- [%s](tg://user?id=%s)\n" % (get_display_name(user), user.id)
        return info
        
    @classmethod
    async def update(self, chat):
        self.admins[chat.id] = await self.client.get_participants(chat, filter=ChannelParticipantsAdmins)
        await self.client.send_message(chat.id, "Updated admin database.")
        
    @classmethod
    async def check(self, chat, user):
        "Check if the user calling the command is an admin."
        
        if not self.admins.get(chat.id, None):
            await self.client.send_message(chat, "Initialising admin database.")
            self.admins[chat.id] = await self.client.get_participants(chat, filter=ChannelParticipantsAdmins)
            
        return True if user in self.admins[chat.id] else False
