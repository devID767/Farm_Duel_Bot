import json

from pyrogram import Client, filters
from time import sleep
from pyrogram.errors import FloodWait

app = Client("farm_duel")

@app.on_message(filters.reply & filters.me & filters.command("add", prefixes="."))
def Add(client, message):
    customer = app.get_messages(message.chat.id, reply_to_message_ids=message.message_id).from_user
    if IsInList(customer.id):
        message.reply_text(f"{customer.first_name} уже добавлен!")
    else:
        Customer.append(customer.id)
        message.reply_text(f"{customer.first_name} добавлен!")
        saveList(Customer, "Customers.json")

    #sleep() #sleep on [sec] time
    #Remove()

@app.on_message(filters.reply & filters.me & filters.command("remove", prefixes="."))
def Remove(client, message):
    customer = app.get_messages(message.chat.id, reply_to_message_ids=message.message_id).from_user
    if IsInList(customer.id):
        Customer.remove(customer.id)
        message.reply_text(f"{customer.first_name} удален!")
        saveList(Customer, "Customers.json")
    else:
        message.reply_text(f"{customer.first_name} не находится в списке!")

@app.on_message(filters.text & filters.reply)
def Duel(client, message):
        if message.text.lower() == "дуэль":
           Oldmessage = app.get_messages(message.chat.id, reply_to_message_ids = message.message_id)
           if Oldmessage.from_user.is_self & IsInList(message.from_user.id):
                try:
                   message.reply_text("Реанимировать жабу", quote = False)
                   sleep(0.1)
                   message.reply_text("дуэль принять", quote=True)
                   sleep(0.2)
                   message.reply_text("дуэль старт", quote = False)
                except FloodWait as e:
                   sleep(e.x)
        elif message.text.lower() == "твой инвентарь":
            message.reply_text("Мой инвентарь")

def IsInList(id):
    IsInCustomer = False
    for item in Customer:
        if id == item:
            IsInCustomer = True
    return IsInCustomer

def saveList(myList,filename):
    with open(filename, 'w') as f:
        # indent=2 is not needed but makes the file more
        # human-readable for more complicated data
        json.dump(myList, f, indent=2)
    print("Saved successfully!")

def loadList(filename):
    with open(filename, 'r') as f:
        return json.load(f)
    print("Load successfully!")

Customer = loadList("Customers.json")

app.run()
