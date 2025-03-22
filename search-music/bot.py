import os
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from dotenv import load_dotenv

# بارگذاری متغیرهای محیطی
load_dotenv()

# توکن‌ها
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
GENIUS_API_TOKEN = os.getenv('GENIUS_API_TOKEN')
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

# تابع برای جستجوی آهنگ با استفاده از Spotify API
def search_song_spotify(query):
    url = "https://api.spotify.com/v1/search"
    headers = {
        "Authorization": f"Bearer {get_spotify_token()}"
    }
    params = {
        "q": query,
        "type": "track",
        "limit": 5
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get('tracks', {}).get('items', [])
    return []

# تابع برای دریافت توکن Spotify
def get_spotify_token():
    url = "https://accounts.spotify.com/api/token"
    data = {
        "grant_type": "client_credentials"
    }
    auth = (SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET)
    response = requests.post(url, data=data, auth=auth)
    if response.status_code == 200:
        return response.json().get('access_token')
    return None

# تابع برای جستجوی متن آهنگ با استفاده از Genius API
def search_lyrics(query):
    url = "https://api.genius.com/search"
    headers = {
        "Authorization": f"Bearer {GENIUS_API_TOKEN}"
    }
    params = {
        "q": query
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get('response', {}).get('hits', [])
    return []

# تابع شروع
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "سلام! من ربات جستجوی آهنگ هستم. 🎵\n"
        "از دستورات زیر استفاده کنید:\n"
        "/search <نام آهنگ> - جستجوی آهنگ\n"
        "/lyrics <نام آهنگ> - جستجوی متن آهنگ"
    )

# تابع جستجوی آهنگ
def search_song(update: Update, context: CallbackContext):
    query = ' '.join(context.args)
    if not query:
        update.message.reply_text("لطفاً نام آهنگ را وارد کنید.")
        return

    results = search_song_spotify(query)
    if results:
        keyboard = []
        for track in results:
            name = track['name']
            artist = track['artists'][0]['name']
            url = track['external_urls']['spotify']
            keyboard.append([InlineKeyboardButton(f"{name} - {artist}", url=url)])
        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text("نتایج جستجو:", reply_markup=reply_markup)
    else:
        update.message.reply_text("هیچ آهنگی یافت نشد.")

# تابع جستجوی متن آهنگ
def search_lyrics_command(update: Update, context: CallbackContext):
    query = ' '.join(context.args)
    if not query:
        update.message.reply_text("لطفاً نام آهنگ را وارد کنید.")
        return

    results = search_lyrics(query)
    if results:
        lyrics_url = results[0]['result']['url']
        update.message.reply_text(f"متن آهنگ پیدا شد: {lyrics_url}")
    else:
        update.message.reply_text("متن آهنگ یافت نشد.")

# تابع اصلی
def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # دستورات
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("search", search_song))
    dp.add_handler(CommandHandler("lyrics", search_lyrics_command))

    # شروع ربات
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
