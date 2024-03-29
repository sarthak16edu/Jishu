"""JishuDeveloper"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from pyrogram import Client , filters
from script import *
from config import *



@Client.on_callback_query(filters.regex('about'))
async def about(bot,update):
    text = script.ABOUT_TXT
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("🔙 Back",callback_data = "home")]
                  ])
    await update.message.edit(text = text,reply_markup = keybord)


@Client.on_message(filters.private & filters.command(["donate"]))
async def donatecm(bot,message):
	text = script.DONATE_TXT
	keybord = InlineKeyboardMarkup([
        			[InlineKeyboardButton("✘ ᴅᴇᴠᴇʟᴏᴘᴇʀ ✘",url = "https://t.me/sarthakkale16"), 
        			InlineKeyboardButton("𝐂𝐥𝐨𝐬𝐞",callback_data = "cancel") ]])
	await message.reply_text(text = text,reply_markup = keybord)

@Client.on_message(filters.private & filters.user(OWNER) & filters.command(["admin"]))
async def admincm(bot,message):
	text = script.ADMIN_TXT
	keybord = InlineKeyboardMarkup([
        			[InlineKeyboardButton("✖️ 𝐂𝐥𝐨𝐬𝐞 ✖️",callback_data = "cancel") ]])
	await message.reply_text(text = text,reply_markup = keybord)

@Client.on_callback_query(filters.regex('help'))
async def help(bot,update):
    text = script.HELP_TXT.format(update.from_user.mention)
    keybord = InlineKeyboardMarkup([ 
                    [InlineKeyboardButton('✘ ᴛʜᴜᴍʙɴᴀɪʟ ✘', callback_data='thumbnail'),
                    InlineKeyboardButton('✘ ᴄᴀᴘᴛɪᴏɴ ✘', callback_data='caption')],
                    [InlineKeyboardButton('✘ ʜᴏᴍᴇ ✘', callback_data='home'),
                    InlineKeyboardButton('✘ ᴅᴏɴᴀᴛᴇ ✘', callback_data='donate')]
                   ])
    await update.message.edit(text = text,reply_markup = keybord)

@Client.on_callback_query(filters.regex('thumbnail'))
async def thumbnail(bot,update):
    text = script.THUMBNAIL_TXT
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("🔙 ʙᴀᴄᴋ",callback_data = "help")]
		  ])
    await update.message.edit(text = text,reply_markup = keybord)

@Client.on_callback_query(filters.regex('caption'))
async def caption(bot,update):
    text = script.CAPTION_TXT
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("🔙 ʙᴀᴄᴋ",callback_data = "help")]
		  ])
    await update.message.edit(text = text,reply_markup = keybord)

@Client.on_callback_query(filters.regex('donate'))
async def donate(bot,update):
    text = script.DONATE_TXT
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("🔙 ʙᴀᴄᴋ",callback_data = "help")]
		  ])
    await update.message.edit(text = text,reply_markup = keybord)


@Client.on_callback_query(filters.regex('home'))
async def home_callback_handler(bot, query):
    text = f"""Hello {query.from_user.mention} \n\n➻ ➪ ᴍᴀɴᴀɢᴇᴅ ʙʏ :- <a href='https://t.me/rb1bots'> ʀʙ1 ʙᴏᴛs</a>\n➪ ᴄʀᴇᴀᴛᴏʀ :- <a href='https://t.me/sarthakkale16'>✰ ʀᴇǫᴜᴇsᴛʙᴏx1 ✰</a>\n➪ ʟᴀɴɢᴜᴀɢᴇ :- ᴘʏᴛʜᴏɴ 3\n➪ ʟɪʙʀᴀʀʏ:- ᴘʏʀᴏɢʀᴀᴍ 2.0\n➪ ᴅᴇᴠ : @know_sarthak16\n\n✭ ᴛʜᴀɴᴋ ʏᴏᴜ **<a href='https://t.me/sarthakkale16'>✰ ʀᴇǫᴜᴇsᴛʙᴏx1 ғᴀᴍɪʟʏ ✰</a>** \nғᴏʀ ʏᴏᴜʀ sᴜᴘᴘᴏʀᴛ\n✘ ᴡᴇ ʟᴏᴠᴇ ʏᴏᴜ ᴀɴᴅ sᴛᴀɴᴅ ʙʏ ʏᴏᴜ <a href='https://t.me/rb1bots'>**ʀʙ1 ʙᴏᴛs**</a> ❥"""
    keybord = InlineKeyboardMarkup([  
                    [InlineKeyboardButton("✘ ᴜᴘᴅᴀᴛᴇꜱ ✘", url="https://t.me/rb1bots"),
                    InlineKeyboardButton("✘ ꜱᴜᴘᴘᴏʀᴛ ✘", url="https://t.me/requestbox1")],
                    [InlineKeyboardButton("✘ ʜᴇʟᴘ ✘", callback_data='help'),
		            InlineKeyboardButton("✘ ᴀʙᴏᴜᴛ ✘", callback_data='about')],
                    [InlineKeyboardButton("✘ ᴅᴇᴠᴇʟᴏᴘᴇʀ ✘", url="https://t.me/sarthakkale16")]
		  ])
    await query.message.edit_text(text=text, reply_markup=keybord)
