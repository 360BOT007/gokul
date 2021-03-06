#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
from pyrogram.errors import UserNotParticipant
from bot import FORCESUB_CHANNEL

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    update_channel = FORCESUB_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked":
               await update.reply_text("š¤­ Sorry Dude, You are **B A N N E D š¤£š¤£š¤£**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text="š ą“ą“ąµą“ą“³ąµą“ąµ šššš£ š¾ššš£š£šš” ą“ąµą“Æą“æąµ» ą“ąµą“Æąµą“¤ą“¾ąµ½ ą“®ą“¾ą“¤ąµą“°ą“®ąµ ą“øą“æą“Øą“æą“® ą“²ą“­ą“æą“ąµą“ąµą“ą“Æąµą“³ąµą“³ąµ.š¤·āą“ą“¾ą“Øą“²ą“æąµ½ š·š¼š¶š» ą“ąµą“Æąµą“¤ą“æą“ąµą“ąµ ą“ą“Øąµą“Øąµą“ąµą“ą“æ š§šæš ą“ąµą“Æąµą“Æąµ. ā¤ļøš\n\nšā¬ā¬ā¬ā¬ā¬ā¬ā¬ā¬ā¬ā¬ā¬ā¬ā¬ā¬š\n\nšš§šµš² š š¼šš¶š² š¶š š¢š»š¹š ššš®š¶š¹š®šÆš¹š² š¶š³ šš¼š šš¼š¶š» š¢ššæ ššµš®š»š»š²š¹.š¤·ā š¦š¼, šš¼š¶š» š”š¼š & š§šæš šš“š®š¶š». ā„ļøš",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text="šš¢šš” & š§š„š¬", url=f"https://t.me/{update_channel}")]
              ])
            )
            return
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = caption,
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'ā­ššš ššššššā­', url="https://t.me/CCM_Movies"
                                )
                        ]
                    ]
                )
            )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'ā­ššš ššššššā­', url="https://t.me/CCM_Movies"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'ā­ššš ššššššā­', url="https://t.me/CCM_Movies"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('š° šš³š°š¶š±š°', url='https://t.me/moviesmediagroup'),
        InlineKeyboardButton('š°šš©š¢šÆšÆš¦š­š°', url ='https://t.me/CCM_Movies')
    ],[
        InlineKeyboardButton('š°šš¶š±š±š°š³šµš°', url='http://t.me/moviesmediamanagerbot')
    ],[
        InlineKeyboardButton('Help ā', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        disable_web_page_preview=True, 
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home ā”', callback_data='start'),
        InlineKeyboardButton('About š©', callback_data='about')
    ],[
        InlineKeyboardButton('Close š', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home ā”', callback_data='start'),
        InlineKeyboardButton('Close š', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
