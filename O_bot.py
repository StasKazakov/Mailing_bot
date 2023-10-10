'''This is main module in project. This file must be run for the bot to work.'''
from pyrogram import Client
from Config import admin
from pyrogram.types import InputPhoneContact
import json
import tempfile
from Functions import *

# Text for mailing.
ads_text = 'Вітаю! 👋 Можливо вам цікаво набрати більше підписників у вашу телеграм групу й отримати нових клієнтів. Якщо так, то хочу вам запропонувати рекламу у @search7kmBot, це бот для пошуку виробників по фото.\n\nЗараз у бота 3500+ підписників і на 95 відсотків це активні дропшиппери. Кожен підписник отримає вашу рекламну пропозицію у приватні повідомлення📩. Вартість рекламної розсилки 450 грн.\n\nВи можете підписатися на бота і самостійно побачити як приходять повідомлення і які результати отримують рекламодавці. До речі, можу долучити вас до списку пошуку бота, якщо вас ще в ньому немає.'

app = Client("Olga")

# Function for recive Telegram id user.
async def get_user_id(phone_num):
    temp_contact_name = tempfile.NamedTemporaryFile().name.split('\\')[-1]
    good_res = list()
    with app:
        await app.import_contacts([InputPhoneContact(phone=phone_num, first_name=temp_contact_name)])
        contacts = await app.get_contacts()
        for contact in contacts:
            contact_data = json.loads(str(contact))
            if contact_data['first_name'] == temp_contact_name:
                good_res.append(contact_data)
                await app.delete_contacts(contact_data['id'])
    try:
        good_res = good_res[0]['id']
    except:
        good_res = None
    return good_res

# Hendler for caching messages.
@app.on_message()
async def my_handler(client, message):
    if message.chat.id == admin:
        if message.text.startswith('+'):
            query = message.text.split(' ')
            shop = query[1]
            contact = query[0]
            user_id = await get_user_id(contact)
            if user_id is not None:
                await app.send_message(user_id, ads_text)
                add_entry(shop, contact)
                record = [shop, contact]
                append_record(record)
                await app.send_message(admin, 'Message sent sucsessful!')
            else:
                await app.send_message(admin, 'Bad number')
        elif message.text.startswith('@'):
            query = message.text.split(' ')
            shop = query[1]
            contact = query[0]
            user_name = contact[1:]
            await app.send_message(user_name, ads_text)
            add_entry(shop, contact)
            record = [shop, contact]
            append_record(record)
            await app.send_message(admin, 'Message sent sucsessful!')
        elif message.text == 'stat':
            executed = get_data()
            table = ''
            for value in executed:
                row = str(value[0]) + ' ' + str(value[1]) + ' ' + str(value[2]) + '\n'
                table = table + row
            await app.send_message(admin, table)

    else:
        #await app.send_message(message.chat.id, 'Ваше повідомлення передано @staskazakovcom')
        await app.forward_messages(admin, message.chat.id, message.id)
app.run()

