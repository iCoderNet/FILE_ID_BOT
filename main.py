import logging, json, hashlib

from aiogram import Bot, Dispatcher, executor, types
from sql import *

API_TOKEN = '5758980803:AAGAfBYIZDKiWBP1zaLuSYqWkcpWrJrcPK4'
CHANNELS = ['iCoderNet']
f = open('lang.json')
lang_t = json.load(f)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def language_selection(message: types.Message):
    cid = message.from_user.id
    code = sql_code(f"SELECT * FROM Users WHERE `tgid`={cid};")
    if len(code) == 0:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("English", callback_data="lang=en"), types.InlineKeyboardButton("Русский", callback_data="lang=ru"))
        markup.add(types.InlineKeyboardButton("O'zbekcha", callback_data="lang=uz"), types.InlineKeyboardButton("Türkçe", callback_data="lang=tr"))
        markup.add(types.InlineKeyboardButton("عربي", callback_data="lang=ar"), types.InlineKeyboardButton("भारतीय", callback_data="lang=in"))
        await message.reply("Select a language:", reply_markup=markup)
        return False
    else:
        return True


@dp.callback_query_handler()
async def callback_lang(callb: types.CallbackQuery):
    cid = callb.from_user.id
    mid = callb.message.message_id
    if "lang=" in callb.data:
        lang = callb.data.split("=")[-1]
        sql_code(f'''INSERT INTO Users (`tgid`, `lang`) VALUES ("{cid}", "{lang}");''')
        await bot.edit_message_text(lang_t[lang]['start'], cid, mid)
    elif "langedit=" in callb.data:
        lang = callb.data.split("=")[-1]
        sql_code(f'''UPDATE Users SET `lang` = '{lang}' WHERE `tgid` = {cid};''')
        await bot.edit_message_text(lang_t[lang]['start'], cid, mid)




@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    if 2 == len(message.text.split(' ')) > 0:
        return await read_id(message, message.text.split(' ')[1])
    else:
        if await language_selection(message):
            lang = sql_code(f"SELECT `lang` FROM Users WHERE `tgid`={message.from_user.id};")[0][0]
            await message.reply(lang_t[lang]['start'])


@dp.message_handler(commands=['lang'])
async def send_welcome(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("English", callback_data="langedit=en"), types.InlineKeyboardButton("Русский", callback_data="langedit=ru"))
    markup.add(types.InlineKeyboardButton("O'zbekcha", callback_data="langedit=uz"), types.InlineKeyboardButton("Türkçe", callback_data="langedit=tr"))
    markup.add(types.InlineKeyboardButton("عربي", callback_data="langedit=ar"), types.InlineKeyboardButton("भारतीय", callback_data="langedit=in"))
    await message.reply("Select a language:", reply_markup=markup)





@dp.message_handler(content_types=['document'])
async def echo(message: types.Message):
    try:
        file_id = message.document.file_id
        caption = message.caption
        if caption == None: caption = ''
        user_id = message.from_user.id
        sql_code(f'''INSERT INTO Files (`type`, `file_id`, `caption`, `user_id`) VALUES ("document", "{file_id}", "{caption}", "{user_id}");''')
        r =  sql_code(f''' SELECT id FROM Files WHERE `user_id` = '{user_id}' ORDER BY -id''')
        sql_id = r[0][0]
        lang = sql_code(f"SELECT `lang` FROM Users WHERE `tgid`={message.from_user.id};")[0][0]
        markup = types.InlineKeyboardMarkup()
        inl_b = types.InlineKeyboardButton(lang_t[lang]['inline'], switch_inline_query=sql_id)
        markup.add(inl_b)
        await message.answer(f"{lang_t[lang]['id']} {sql_id}", reply_markup=markup)
    except:
        lang = sql_code(f"SELECT `lang` FROM Users WHERE `tgid`={message.from_user.id};")[0][0]
        await message.answer(lang_t[lang]['error'])



@dp.message_handler(content_types=['video'])
async def echo(message: types.Message):
    try:
        file_id = message.video.file_id
        caption = message.caption
        if caption == None: caption = ''
        user_id = message.from_user.id
        sql_code(f'''INSERT INTO Files (`type`, `file_id`, `caption`, `user_id`) VALUES ("video", "{file_id}", "{caption}", "{user_id}");''')
        r =  sql_code(f''' SELECT id FROM Files WHERE `user_id` = '{user_id}' ORDER BY -id''')
        sql_id = r[0][0]
        lang = sql_code(f"SELECT `lang` FROM Users WHERE `tgid`={message.from_user.id};")[0][0]
        markup = types.InlineKeyboardMarkup()
        inl_b = types.InlineKeyboardButton(lang_t[lang]['inline'], switch_inline_query=sql_id)
        markup.add(inl_b)
        await message.answer(f"{lang_t[lang]['id']} {sql_id}", reply_markup=markup)
    except:
        lang = sql_code(f"SELECT `lang` FROM Users WHERE `tgid`={message.from_user.id};")[0][0]
        await message.answer(lang_t[lang]['error'])



@dp.message_handler(content_types=['animation'])
async def echo(message: types.Message):
    try:
        file_id = message.animation.file_id
        caption = message.caption
        if caption == None: caption = ''
        user_id = message.from_user.id
        sql_code(f'''INSERT INTO Files (`type`, `file_id`, `caption`, `user_id`) VALUES ("animation", "{file_id}", "{caption}", "{user_id}");''')
        r =  sql_code(f''' SELECT id FROM Files WHERE `user_id` = '{user_id}' ORDER BY -id''')
        sql_id = r[0][0]
        lang = sql_code(f"SELECT `lang` FROM Users WHERE `tgid`={message.from_user.id};")[0][0]
        markup = types.InlineKeyboardMarkup()
        inl_b = types.InlineKeyboardButton(lang_t[lang]['inline'], switch_inline_query=sql_id)
        markup.add(inl_b)
        await message.answer(f"{lang_t[lang]['id']} {sql_id}", reply_markup=markup)
    except:
        lang = sql_code(f"SELECT `lang` FROM Users WHERE `tgid`={message.from_user.id};")[0][0]
        await message.answer(lang_t[lang]['error'])



@dp.message_handler(content_types=['audio'])
async def echo(message: types.Message):
    try:
        file_id = message.audio.file_id
        caption = message.caption
        if caption == None: caption = ''
        user_id = message.from_user.id
        sql_code(f'''INSERT INTO Files (`type`, `file_id`, `caption`, `user_id`) VALUES ("audio", "{file_id}", "{caption}", "{user_id}");''')
        r =  sql_code(f''' SELECT id FROM Files WHERE `user_id` = '{user_id}' ORDER BY -id''')
        sql_id = r[0][0]
        lang = sql_code(f"SELECT `lang` FROM Users WHERE `tgid`={message.from_user.id};")[0][0]
        markup = types.InlineKeyboardMarkup()
        inl_b = types.InlineKeyboardButton(lang_t[lang]['inline'], switch_inline_query=sql_id)
        markup.add(inl_b)
        await message.answer(f"{lang_t[lang]['id']} {sql_id}", reply_markup=markup)
    except:
        lang = sql_code(f"SELECT `lang` FROM Users WHERE `tgid`={message.from_user.id};")[0][0]
        await message.answer(lang_t[lang]['error'])


@dp.message_handler(content_types=['photo'])
async def echo(message: types.Message):
    try:
        file_id = message.photo[0].file_id
        caption = message.caption
        if caption == None: caption = ''
        user_id = message.from_user.id
        sql_code(f'''INSERT INTO Files (`type`, `file_id`, `caption`, `user_id`) VALUES ("photo", "{file_id}", "{caption}", "{user_id}");''')
        r =  sql_code(f''' SELECT id FROM Files WHERE `user_id` = '{user_id}' ORDER BY -id''')
        sql_id = r[0][0]
        lang = sql_code(f"SELECT `lang` FROM Users WHERE `tgid`={message.from_user.id};")[0][0]
        markup = types.InlineKeyboardMarkup()
        inl_b = types.InlineKeyboardButton(lang_t[lang]['inline'], switch_inline_query=sql_id)
        markup.add(inl_b)
        await message.answer(f"{lang_t[lang]['id']} {sql_id}", reply_markup=markup)
    except:
        lang = sql_code(f"SELECT `lang` FROM Users WHERE `tgid`={message.from_user.id};")[0][0]
        await message.answer(lang_t[lang]['error'])


@dp.message_handler(content_types=['voice'])
async def echo(message: types.Message):
    try:
        file_id = message.voice.file_id
        caption = message.caption
        if caption == None: caption = ''
        user_id = message.from_user.id
        sql_code(f'''INSERT INTO Files (`type`, `file_id`, `caption`, `user_id`) VALUES ("voice", "{file_id}", "{caption}", "{user_id}");''')
        r =  sql_code(f''' SELECT id FROM Files WHERE `user_id` = '{user_id}' ORDER BY -id''')
        sql_id = r[0][0]
        lang = sql_code(f"SELECT `lang` FROM Users WHERE `tgid`={message.from_user.id};")[0][0]
        markup = types.InlineKeyboardMarkup()
        inl_b = types.InlineKeyboardButton(lang_t[lang]['inline'], switch_inline_query=sql_id)
        markup.add(inl_b)
        await message.answer(f"{lang_t[lang]['id']} {sql_id}", reply_markup=markup)
    except:
        lang = sql_code(f"SELECT `lang` FROM Users WHERE `tgid`={message.from_user.id};")[0][0]
        await message.answer(lang_t[lang]['error'])


@dp.message_handler()
async def read_id(message: types.Message, text = None):
    try:
        if text == None: text = message.text
        if text.isdigit():
            r =  sql_code(f''' SELECT * FROM Files WHERE `id` = '{text}' ORDER BY -id''')
            if len(r) > 0:
                r = r[0]
                if r[1] == 'document':
                    await message.answer_document(r[2], caption=r[3])
                elif r[1] == 'video':
                    await message.answer_video(r[2], caption=r[3])
                elif r[1] == 'animation':
                    await message.answer_animation(r[2], caption=r[3])
                elif r[1] == 'photo':
                    await message.answer_photo(r[2], caption=r[3])
                elif r[1] == 'audio':
                    await message.answer_audio(r[2], caption=r[3])
                elif r[1] == 'voice':
                    await message.answer_voice(r[2], caption=r[3])
            else:
                lang = sql_code(f"SELECT `lang` FROM Users WHERE `tgid`={message.from_user.id};")[0][0]
                await message.answer(lang_t[lang]['empty'])
    except:
        lang = sql_code(f"SELECT `lang` FROM Users WHERE `tgid`={message.from_user.id};")[0][0]
        await message.answer(lang_t[lang]['error'])








#INLINE
@dp.inline_handler()
async def inline_usage(inline_query: types.InlineQuery):
    text = inline_query.query or '0'
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    try:
        if text.isdigit():
            r =  sql_code(f''' SELECT * FROM Files WHERE `id` = '{text}' ORDER BY -id''')
            if len(r) > 0:
                r = r[0]
                if r[1] == 'document':
                    item = types.InlineQueryResultDocument(id=result_id, title=f"Document - {text}", description=r[3], document_url=r[2], mime_type="application/zip", caption=r[3])
                elif r[1] == 'video':
                    item = types.InlineQueryResultVideo(id=result_id, title=f"Video - {text}", description=r[3], video_url=r[2], mime_type="video/mp4", thumb_url=r[2], caption=r[3])
                elif r[1] == 'animation':
                    item = types.InlineQueryResultGif(id=result_id, title=f"Gif - {text}", description=r[3], gif_url=r[2], thumb_url=r[2], caption=r[3])
                elif r[1] == 'photo':
                    item = types.InlineQueryResultPhoto(id=result_id, title=f"Photo - {text}", description=r[3], photo_url=r[2], thumb_url=r[2], caption=r[3])
                elif r[1] == 'audio':
                    item = types.InlineQueryResultAudio(id=result_id, title=f"Audio - {text}", audio_url=r[2], caption=r[3])
                elif r[1] == 'voice':
                    item = types.InlineQueryResultVoice(id=result_id, title=f"Voice - {text}", voice_url=r[2], caption=r[3])
            else:
                lang = sql_code(f"SELECT `lang` FROM Users WHERE `tgid`={inline_query.from_user.id};")[0][0]
                empty = f"{lang_t[lang]['empty']}"
                input_content = types.InputTextMessageContent(empty)
                item = types.InlineQueryResultArticle(id=result_id,title=empty,input_message_content=input_content)
        
        await bot.answer_inline_query(inline_query.id, results=[item], cache_time=1)
    except:
        lang = sql_code(f"SELECT `lang` FROM Users WHERE `tgid`={inline_query.from_user.id};")[0][0]
        error = f"{lang_t[lang]['error']}"
        input_content = types.InputTextMessageContent(error)
        item = types.InlineQueryResultArticle(id=result_id,title=error,input_message_content=input_content)





if __name__ == '__main__':
    #iCoderNet kanali uchun #UzbProMax dan
    executor.start_polling(dp, skip_updates=True)
