from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from pytube import YouTube
import subprocess
import os
import logging

API_TOKEN = 'توکن_ربات_تلگرام_تو'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

# تشخیص لینک
def detect_platform(url):
    if 'youtube.com' in url or 'youtu.be' in url:
        return 'youtube'
    elif 'instagram.com' in url:
        return 'instagram'
    elif 'twitter.com' in url or 'x.com' in url:
        return 'twitter'
    return 'unknown'

# دانلود از یوتیوب
def download_youtube(url, quality='high'):
    yt = YouTube(url)
    if quality == 'high':
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    else:
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').asc().first()
    filename = stream.download()
    return filename

# دانلود از اینستاگرام (استوری یا پست عمومی)
def download_instagram(url):
    command = f"instaloader {url} --dirname-prefix=downloads --quiet"
    subprocess.call(command, shell=True)
    return "فایل‌ها در پوشه downloads ذخیره شدند."

# دانلود از توییتر با yt_dlp
def download_twitter(url):
    filename = "twitter_video.mp4"
    command = f"yt-dlp -o {filename} {url}"
    subprocess.call(command, shell=True)
    return filename

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(InlineKeyboardButton(text="📹 دانلود از یوتیوب", callback_data="youtube"),
                 InlineKeyboardButton(text="📸 دانلود از اینستاگرام", callback_data="instagram"),
                 InlineKeyboardButton(text="🐦 دانلود از توییتر", callback_data="twitter"))
    await message.reply("سلام! لطفا پلتفرم مورد نظر را انتخاب کنید:", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data in ['youtube', 'instagram', 'twitter'])
async def process_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f"لطفا لینک {callback_query.data} را ارسال کنید.")

@dp.message_handler()
async def handle_message(message: Message):
    url = message.text.strip()
    platform = detect_platform(url)

    try:
        if platform == 'youtube':
            keyboard = InlineKeyboardMarkup(row_width=2)
            keyboard.add(InlineKeyboardButton(text="🎥 کیفیت بالا", callback_data=f"quality_high_{url}"),
                         InlineKeyboardButton(text="🎥 کیفیت پایین", callback_data=f"quality_low_{url}"))
            await message.reply("لطفا کیفیت ویدیو را انتخاب کنید:", reply_markup=keyboard)

        elif platform == 'instagram':
            await message.reply("در حال دانلود از اینستاگرام...")
            msg = download_instagram(url)
            await message.reply(msg)

        elif platform == 'twitter':
            await message.reply("در حال دانلود از توییتر...")
            file = download_twitter(url)
            await message.reply_video(open(file, 'rb'))
            os.remove(file)

        else:
            await message.reply("لینک معتبر نیست یا پشتیبانی نمی‌شود.")

    except Exception as e:
        await message.reply(f"خطا: {str(e)}")

@dp.callback_query_handler(lambda c: c.data.startswith('quality_'))
async def process_quality_callback(callback_query: types.CallbackQuery):
    quality, url = callback_query.data.split('_')[1], callback_query.data.split('_')[2]
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f"در حال دانلود با کیفیت {quality}...")
    file = download_youtube(url, quality)
    await bot.send_video(callback_query.from_user.id, open(file, 'rb'))
    os.remove(file)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
