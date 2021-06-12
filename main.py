import json

from pyrogram import Client, filters
from time import sleep
from pyrogram.errors import FloodWait

app = Client("farm_duel")

@app.on_message(filters.text & filters.command('help', prefixes='.'))
def Help(client, message):
    customer = app.get_messages(message.chat.id, reply_to_message_ids=message.message_id).from_user
    if customer.is_self:
        message.reply_text(f'Commands for all:\n'
                            f'твой инвентарь (ответом на мое сообщение)\n'
                            f'твой балланс (ответом на мое сообщение)\n\n'
                            f'Commands for customers:\n'
                            f'Дуєль (Ответом на мое сообщение)\n\n'
                            f'Commands for admins:'
                            f'.admins'
                            f'.customers'
                            f'.reapeat [message]'
                            f'.add [customer]'
                            f'.remove [customer]')

@app.on_message(filters.text & filters.command('admins', prefixes='.'))
def ShowAdmins(client, message):
    if message.from_user.is_self or str(message.from_user.id) in Admins:
         for admin in Admins:
             message.reply_text(f'{admin} - {Admins[admin]}', quote=False)

@app.on_message(filters.text & filters.command('customers', prefixes='.'))
def ShowAdmins(client, message):
    if message.from_user.is_self or str(message.from_user.id) in Admins:
        for customer in Customers:
            message.reply_text(f'{customer} - {Customers[customer]}', quote=False)

@app.on_message(filters.text & filters.command('repeat', prefixes='.'))
def Repeat(client, message):
    customer = app.get_messages(message.chat.id, reply_to_message_ids=message.message_id).from_user
    if customer.is_self and str(message.from_user.id) in Admins:
        message.reply_text(message.text.split(maxsplit=1)[1])

@app.on_message(filters.reply & filters.command("add", prefixes="."))
def Add(client, message):
    customer = app.get_messages(message.chat.id, reply_to_message_ids=message.message_id).from_user
    if message.text.split()[1] == 'admin' and message.from_user.is_self:
        list = Admins
        filename = 'Admins'
    elif message.text.split()[1] == 'customer' and (message.from_user.is_self or str(message.from_user.id) in Admins):
        list = Customers
        filename = 'Customers'
    elif not message.from_user.is_self:
        message.reply_text('У вас нет прав!')


    if IsInList(str(customer.id), list):
        message.reply_text(f"{customer.first_name} уже добавлен в {filename}!")
    else:
        list[str(customer.id)] = customer.first_name
        message.reply_text(f"{customer.first_name} добавлен в {filename}")
        saveList(list, filename)

@app.on_message(filters.command("remove", prefixes="."))
def Remove(client, message):
    try:
        customer_id = app.get_messages(message.chat.id, reply_to_message_ids=message.message_id).from_user.id
    except:
        customer_id = message.text.split()[1]

    if message.text.split()[1] == 'admin' and message.from_user.is_self:
        list = Admins
        filename = 'Admins'
    elif message.text.split()[1] == 'customer' and (message.from_user.is_self or str(message.from_user.id) in Admins):
        list = Customers
        filename = 'Customers'
    elif not message.from_user.is_self:
        message.reply_text('У вас нет прав!')

    if IsInList(str(customer_id), list):
        message.reply_text(f"{list[str(customer_id)]} удален из {filename}!")
        del list[str(customer_id)]
        saveList(list, filename)
    else:
        message.reply_text(f"{list[str(customer_id)]} не находится в {filename}!")

@app.on_message(filters.text & filters.reply)
def Duel(client, message):
        if message.text.lower() == "дуэль":
           Oldmessage = app.get_messages(message.chat.id, reply_to_message_ids = message.message_id)
           if Oldmessage.from_user.is_self & IsInList(str(message.from_user.id), Customers):
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
        elif message.text.lower() == "твой баланс":
            message.reply_text("Мой баланс")

def IsInList(id, list):
    IsInCustomer = False
    for item in list:
        if id == item:
            IsInCustomer = True
    return IsInCustomer

def saveList(myList, filename):
    filename += '.json'
    with open(filename, 'w') as f:
        # indent=2 is not needed but makes the file more
        # human-readable for more complicated data
        json.dump(myList, f, indent=2)
    print("Saved successfully!")

def loadList(filename):
    filename += '.json'
    with open(filename, 'r') as f:
        return json.load(f)
    print("Load successfully!")

Customers = loadList("Customers")
Admins = loadList('Admins')

app.run()
