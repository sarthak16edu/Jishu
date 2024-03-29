from datetime import date as date_
import datetime
import os, re
import asyncio
import random
from script import *
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
from pyrogram import Client, filters, enums
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
import humanize
from helper.progress import humanbytes
from helper.database import botdata, find_one, total_user
from helper.database import insert, find_one, used_limit, usertype, uploadlimit, addpredata, total_rename, total_size
from pyrogram.file_id import FileId
from helper.database import daily as daily_
from helper.date import check_expi
from config import *

bot_username = BOT_USERNAME
log_channel = LOG_CHANNEL
token = BOT_TOKEN
botid = token.split(':')[0]

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    user_id = message.chat.id
    old = insert(int(user_id))
    
    try:
        id = message.text.split(' ')[1]
    except IndexError:
        id = None

    loading_sticker_message = await message.reply_sticker("CAACAgIAAxkBAALmzGXSSt3ppnOsSl_spnAP8wHC26jpAAJEGQACCOHZSVKp6_XqghKoHgQ")
    await asyncio.sleep(2)
    await loading_sticker_message.delete()
    txt=f"""Hello {message.from_user.mention} \ɴ\ɴ➻ ᴛʜɪꜱ ɪꜱ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀɴᴅ ʏᴇᴛ ᴘᴏᴡᴇʀꜰᴜʟ ʀᴇɴᴀᴍᴇ ʙᴏᴛ.\n\n➻ ᴜꜱɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ʏᴏᴜ ᴄᴀɴ ʀᴇɴᴀᴍᴇ ᴀɴᴅ ᴄʜᴀɴɢᴇ ᴛʜᴜᴍʙɴᴀɪʟ ᴏꜰ ʏᴏᴜʀ ꜰɪʟᴇꜱ.\n\n➻ ʏᴏᴜ ᴄᴀɴ ᴀʟꜱᴏ ᴄᴏɴᴠᴇʀᴛ ᴠɪᴅᴇᴏ ᴛᴏ ꜰɪʟᴇ ᴀND ꜰɪʟᴇ ᴛᴏ ᴠɪᴅᴇᴏ.\n\n ➻ ᴛʜɪꜱ ʙᴏᴛ ᴀʟꜱᴏ ꜱᴜᴘᴘᴏʀᴛꜱ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴀɴᴅ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.\n\n<ʙ>ʙᴏᴛ ɪꜱ ᴍᴀᴅᴇ ʙʏ\n © @rb1bots & © @requestbox1official</b>"""
    await message.reply_photo(photo=BOT_PIC,
                                caption=txt,
                                reply_markup=InlineKeyboardMarkup([
                                      [InlineKeyboardButton("✰ ＰＯＷＥＲＥＤ ＢＹ ✰", url="https://t.me/rb1bots")],
				      [InlineKeyboardButton("✪ ʙᴏʟʟʏᴡᴏᴏᴅ ✪", url='https://t.me/helpsarthak_bot'),
                                      InlineKeyboardButton("✪ ᴍᴏᴠɪᴇs ✪", url="https://t.me/requestbox1")],
                                      [InlineKeyboardButton("⍟ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ ʙᴏᴛ ⍟", url='https://t.me/helpsarthak_bot'),
                                      InlineKeyboardButton("⍟ ɪɴᴅᴇx ⍟", url='https://t.me/rb1index')],
                                      [InlineKeyboardButton("✮ ᴘʀᴇᴍɪᴜᴍ ✮", url='https://t.me/rb1official'),
                                      InlineKeyboardButton("✮ ᴅᴏɴᴀᴛᴇ ✮", url='https://t.me/sarthakkale16')],
                                      ]))
    return

@Client.on_message((filters.private & (filters.document | filters.audio | filters.video)) | filters.channel & (filters.document | filters.audio | filters.video))
async def send_doc(client, message):
    update_channel = FORCE_SUBS
    user_id = message.from_user.id
    if update_channel:
        try:
            await client.get_chat_member(update_channel, user_id)
        except UserNotParticipant:
            _newus = find_one(message.from_user.id)
            user = _newus["usertype"]
            await message.reply_text("<b>Hello Dear \n\nʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ɪɴ ᴍʏ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜꜱᴇ ᴍᴇ\n\n ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ @requestbox1official & ᴛʀʏ ᴀɢᴀɪɴ</b>",
                                     reply_to_message_id=message.id,
                                     reply_markup=InlineKeyboardMarkup(
                                         [[InlineKeyboardButton("✭ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟs✭", url=f"https://t.me/{update_channel}")]]))
            await client.send_message(log_channel,f"➪ #RubyUser ✭,\n\n➪ **ID** : `{user_id}`\n➪ **Name**: {message.from_user.first_name} {message.from_user.last_name}\n➪ **User-Plan** : {user}\n\n ",
                                                                                                       reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✘ Restrict User ( **pm** ) ✘", callback_data="ceasepower")]]))
            return
		
    botdata(int(botid))
    bot_data = find_one(int(botid))
    prrename = bot_data['total_rename']
    prsize = bot_data['total_size']
    user_deta = find_one(user_id)
    used_date = user_deta["date"]
    buy_date = user_deta["prexdate"]
    daily = user_deta["daily"]
    user_type = user_deta["usertype"]

    c_time = time.time()

    if user_type == "Free":
        LIMIT = 120
    else:
        LIMIT = 10
    then = used_date + LIMIT
    left = round(then - c_time)
    conversion = datetime.timedelta(seconds=left)
    ltime = str(conversion)
    if left > 0:
        await message.reply_text(f"<b>Sorry Dude I Am Not Only For You \n\nFlood Control Is Active So Please Wait For {ltime} </b>", reply_to_message_id=message.id)
    else:
        # Forward a single message
        media = await client.get_messages(message.chat.id, message.id)
        file = media.document or media.video or media.audio
        dcid = FileId.decode(file.file_id).dc_id
        filename = file.file_name
        file_id = file.file_id
        value = 2147483648
        used_ = find_one(message.from_user.id)
        used = used_["used_limit"]
        limit = used_["uploadlimit"]
        expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
        if expi != 0:
            today = date_.today()
            pattern = '%Y-%m-%d'
            epcho = int(time.mktime(time.strptime(str(today), pattern)))
            daily_(message.from_user.id, epcho)
            used_limit(message.from_user.id, 0)
        remain = limit - used
        if remain < int(file.file_size):
            await message.reply_text(f"100% Of Daily {humanbytes(limit)} Data Quota Exhausted.\n\n<b>File Size Detected :</b> {humanbytes(file.file_size)}\n<b>Used Daily Limit :</b> {humanbytes(used)}\n\nYou Have Only <b>{humanbytes(remain)}</b> Left On Your Account.\n\nIf U Want To Rename Large File Upgrade Your Plan", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💳 Upgrade", callback_data="my_pl_call")]]))
            return
        if value < file.file_size:
            
            if STRING:
                if buy_date == None:
                    await message.reply_text(f" Yᴏᴜ Cᴀɴ'ᴛ Uᴘʟᴏᴀᴅ Mᴏʀᴇ Tʜᴀɴ 2GB Fɪʟᴇ\n\nYᴏᴜʀ Pʟᴀɴ Dᴏᴇsɴ'ᴛ Aʟʟᴏᴡ Tᴏ Uᴘʟᴏᴀᴅ Fɪʟᴇs Tʜᴀᴛ Aʀᴇ Lᴀʀɢᴇʀ Tʜᴀɴ 2GB\n\nUpgrade Yᴏᴜʀ Pʟᴀɴ Tᴏ Rᴇɴᴀᴍᴇ Fɪʟᴇs Lᴀʀɢᴇʀ Tʜᴀɴ 2GB", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💳 Upgrade", callback_data="upgrade")]]))
                    return
                pre_check = check_expi(buy_date)
                if pre_check == True:
                    await message.reply_text(f"""__Wʜᴀᴛ Dᴏ Yᴏᴜ Wᴀɴᴛ Mᴇ Tᴏ Dᴏ Wɪᴛʜ Tʜɪs Fɪʟᴇ ?__\n\n**Fɪʟᴇ Nᴀᴍᴇ** :- `{filename}`\n**Fɪʟᴇ Sɪᴢᴇ** :- {humanize.naturalsize(file.file_size)}\n**DC ID** :- {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 Rename", callback_data="rename"), InlineKeyboardButton("✖️ Cancel", callback_data="cancel")]]))
                    total_rename(int(botid), prrename)
                    total_size(int(botid), prsize, file.file_size)
                else:
                    uploadlimit(message.from_user.id, 2147483648)
                    usertype(message.from_user.id, "Free")

                    await message.reply_text(f'Yᴏᴜʀ Pʟᴀɴ Exᴘɪʀᴇᴅ Oɴ {buy_date}', quote=True)
                    return
            else:
                await message.reply_text("Yᴏᴜ Cᴀɴ'ᴛ Uᴘʟᴏᴀᴅ Mᴏʀᴇ Tʜᴀɴ 2GB Fɪʟᴇ\n\nYᴏᴜʀ Pʟᴀɴ Dᴏᴇsɴ'ᴛ Aʟʟᴏᴡ Tᴏ Uᴘʟᴏᴀᴅ Fɪʟᴇs Tʜᴀᴛ Aʀᴇ Lᴀʀɢᴇʀ Tʜᴀɴ 2GB\n\nUpgrade Yᴏᴜʀ Pʟᴀɴ Tᴏ Rᴇɴᴀᴍᴇ Fɪʟᴇs Lᴀʀɢᴇʀ Tʜᴀɴ 2GB")
                return
        else:
            if buy_date:
                pre_check = check_expi(buy_date)
                if pre_check == False:
                    uploadlimit(message.from_user.id, 2147483648)
                    usertype(message.from_user.id, "Free")
            
            filesize = humanize.naturalsize(file.file_size)
            fileid = file.file_id
            total_rename(int(botid), prrename)
            total_size(int(botid), prsize, file.file_size)
            await message.reply_text(f"""__Wʜᴀᴛ Dᴏ Yᴏᴜ Wᴀɴᴛ Mᴇ Tᴏ Dᴏ Wɪᴛʜ Tʜɪs Fɪʟᴇ ?__\n\n**Fɪʟᴇ Nᴀᴍᴇ** :- `{filename}`\n**Fɪʟᴇ Sɪᴢᴇ** :- {filesize}\n**DC ID** :- {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("📝 Rᴇɴᴀᴍᴇ", callback_data="rename"),
                  InlineKeyboardButton("✖️ Cᴀɴᴄᴇʟ", callback_data="cancel")]]))
              
              
              
