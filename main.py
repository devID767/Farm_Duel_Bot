from pyrogram import Client, filters
from time import sleep
from pyrogram.errors import FloodWait

app = Client("farm_duel")

@app.on_message(filters.text & filters.reply)
def Duel(client, message):
        if message.text.lower() == "дуэль":
           Oldmessage = app.get_messages(message.chat.id, reply_to_message_ids = message.message_id)
           if Oldmessage.from_user.is_self:
                try:
                   message.reply_text("Реанимировать жабу", quote = False)
                   message.reply_text("дуэль принять", quote=True)
                   message.reply_text("дуэль старт", quote = False)
                except FloodWait as e:
                   sleep(e.x)
app.run()
