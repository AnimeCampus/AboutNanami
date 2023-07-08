from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random
import subprocess
import os
import logging
from pyrogram import Client, filters
from pyrogram.types import Message
from PIL import Image, ImageDraw
import asyncio


# Set your bot token here
TOKEN = '6399531735:AAF_AApdKiGskN0-gkNR1ZfeqczOU5CDXg0'

# Replace 'YOUR_API_ID' and 'YOUR_API_HASH' with your own API credentials
API_ID = '16743442'
API_HASH = '12bbd720f4097ba7713c5e40a11dfd2a'

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=TOKEN)


import requests


# Replace 'YOUR_PIXABAY_API_KEY' with your own Pixabay API key
PIXABAY_API_KEY = '37055792-a3457117bfde7b1012045092b'

@app.on_message(filters.command("start"))
def start_command(client, message):
    # Fetch a random item (image, video, or gif) based on the 'anime' category from the Pixabay API
    url = f'https://pixabay.com/api/?key={PIXABAY_API_KEY}&q=anime&per_page=100'
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        if 'hits' in json_data:
            hits = json_data['hits']
            if hits:
                random_item = random.choice(hits)
                if 'webformatURL' in random_item:
                    item_url = random_item['webformatURL']
                    item_type = random_item['type']
                    if item_type == 'video':
                        # Send the fetched video as a video message
                        client.send_video(
                            chat_id=message.chat.id,
                            video=item_url,
                            caption="""➖➖➖➖➖➖➖➖➖➖➖➖
🟢ɴᴀᴍᴇ : Vinay Kumar Singh 
🟢ᴜꜱᴇʀɴᴀᴍᴇ : @The_NanamiiKento 
🟢ᴜꜱᴇʀ ɪᴅ : 6265459491 
🟢ʜᴏʙʙʏ : Anime Uploading , Thumbnail And Video Editing
🟢ᴀɢᴇ :  18+
🟢ꜰʀᴏᴍ : Bihar 
➖➖➖➖➖➖➖➖➖➖➖➖
ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ ᴄʟɪᴄᴋ ʜᴇʀᴇ /help"""
                        )
                    elif item_type == 'gif':
                        # Send the fetched gif as an animation message
                        client.send_animation(
                            chat_id=message.chat.id,
                            animation=item_url,
                            caption="""➖➖➖➖➖➖➖➖➖➖➖➖
🟢ɴᴀᴍᴇ : Vinay Kumar Singh 
🟢ᴜꜱᴇʀɴᴀᴍᴇ : @The_NanamiiKento 
🟢ᴜꜱᴇʀ ɪᴅ : 6265459491 
🟢ʜᴏʙʙʏ : Anime Uploading , Thumbnail And Video Editing 
🟢ᴀɢᴇ :  18+
🟢ꜰʀᴏᴍ : Bihar 
➖➖➖➖➖➖➖➖➖➖➖➖
ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ ᴄʟɪᴄᴋ ʜᴇʀᴇ /help"""
                        )
                    else:
                        # Send the fetched image as a photo message
                        client.send_photo(
                            chat_id=message.chat.id,
                            photo=item_url,
                            caption="""➖➖➖➖➖➖➖➖➖➖➖➖
🟢ɴᴀᴍᴇ : Vinay Kumar Singh 
🟢ᴜꜱᴇʀɴᴀᴍᴇ : @The_NanamiiKento 
🟢ᴜꜱᴇʀ ɪᴅ : 6265459491 
🟢ʜᴏʙʙʏ : Anime Uploading , Thumbnail And Video Editing
🟢ᴀɢᴇ :  18+
🟢ꜰʀᴏᴍ : Bihar 
➖➖➖➖➖➖➖➖➖➖➖➖
ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ ᴄʟɪᴄᴋ ʜᴇʀᴇ /help"""
                        )
                    

@app.on_message(filters.command("help"))
def help_command(client, message):
    help_text = (
        "Available commands:\n\n"
        "/start - Start the bot\n"
        "/help - Display this help message\n"
        "/mybots - Show my bots\n"
        "/img [text] - Generate image through API\n"
        "✧━━━━━▣✧❅✦❅✧▣━━━━━✧"
    )

    inline_keyboard = [
        [InlineKeyboardButton("Instagram", url="https://www.instagram.com/The_NanamiiKento")],
        [InlineKeyboardButton("WhatsApp", url="https://wa.me/14302478798")],
        [InlineKeyboardButton("Personal HeadSpace", url="https://t.me/TheGodly_Being")],
        [InlineKeyboardButton("Channel", url="https://t.me/Anime_Campus")]       
    ]

    reply_markup = InlineKeyboardMarkup(inline_keyboard)

    client.send_message(chat_id=message.chat.id, text=help_text, reply_markup=reply_markup)



@app.on_message(filters.command("mybots"))
def inline_command(client, message):
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Ken Kaneki", callback_data="btn1"),
                InlineKeyboardButton("Komi", callback_data="btn2")
            ],
            [
                InlineKeyboardButton("Ego", callback_data="btn3"),
                InlineKeyboardButton("Madara Uchiha", callback_data="btn4")
            ]
        ]
    )
    client.send_message(chat_id=message.chat.id, text="My All Bot List More Bot Coming Soon:", reply_markup=keyboard)


@app.on_callback_query()
def handle_callback(client, callback_query):
    data = callback_query.data
    message = callback_query.message
    if data == "btn1":
        client.send_message(chat_id=message.chat.id, text="ᴛʜᴇ ᴍᴏsᴛ ᴩᴏᴡᴇʀғᴜʟ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴩ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ᴀɴᴅ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs. ʙᴏᴛ : @Ken_Kaneki_ProBot")
    elif data == "btn2":
        client.send_message(chat_id=message.chat.id, text="ᴛʜᴇ ᴍᴏsᴛ ᴩᴏᴡᴇʀғᴜʟ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴩ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ᴀɴᴅ ᴜsᴇғᴜʟ ғᴇᴀᴛᴜʀᴇs. ʙᴏᴛ : @TheKomi_Bot")
    elif data == "btn3":
        client.send_message(chat_id=message.chat.id, text="ᴀ sɪᴍᴘʟᴇ ғɪʟᴇ ʀᴇɴᴀᴍᴇ + ғɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ ᴄᴏɴᴠᴇʀᴛᴇʀ ʙᴏᴛ ᴡɪᴛʜ ᴘᴇʀᴍᴀɴᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ & ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ sᴜᴘᴘᴏʀᴛ : @JinpachiEgo_RenameBot")
    elif data == "btn4":
        client.send_message(chat_id=message.chat.id, text="Powerfull Telegram Bot Base on Anime Theme : @MadaraUchiha_xBot")

        
import requests
import urllib.parse

@app.on_message(filters.command("img"))
def send_image(client, message):
    # Get the query from the command arguments
    command_args = message.command[1:]  # Exclude the command itself
    query = ' '.join(command_args) if command_args else 'random'

    # Fetch an image based on the user's query from the Pixabay API
    encoded_query = urllib.parse.quote(query)
    url = f'https://pixabay.com/api/?key={PIXABAY_API_KEY}&q={encoded_query}&image_type=photo&per_page=100'
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        if 'hits' in json_data:
            hits = json_data['hits']
            if hits:
                random_image = random.choice(hits)
                if 'webformatURL' in random_image:
                    image_url = random_image['webformatURL']
                    # Send the fetched image as a photo message
                    client.send_photo(
                        chat_id=message.chat.id,
                        photo=image_url,
                        caption=f'Here is an image for "{query}"'
                    )



app.run()
idle()

print("bot started....")
    
