import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from pydub import AudioSegment
from PIL import Image
from moviepy.editor import VideoFileClip
from pdf2image import convert_from_path

# تنظیمات لاگ
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# توکن ربات
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# دستور شروع
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("تبدیل فایل صوتی", callback_data='convert_audio')],
        [InlineKeyboardButton("تبدیل تصویر", callback_data='convert_image')],
        [InlineKeyboardButton("تبدیل ویدیو", callback_data='convert_video')],
        [InlineKeyboardButton("تبدیل سند", callback_data='convert_document')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('لطفا نوع فایلی که می‌خواهید تبدیل کنید را انتخاب کنید:', reply_markup=reply_markup)

# مدیریت انتخاب نوع فایل
def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    conversion_type = query.data

    # ذخیره نوع تبدیل در user_data
    context.user_data['conversion_type'] = conversion_type

    # نمایش گزینه‌های فرمت خروجی
    if conversion_type == 'convert_audio':
        formats = ['mp3', 'wav', 'ogg', 'flac']
    elif conversion_type == 'convert_image':
        formats = ['jpg', 'png', 'bmp', 'webp']
    elif conversion_type == 'convert_video':
        formats = ['mp4', 'avi', 'mov', 'mkv']
    elif conversion_type == 'convert_document':
        formats = ['pdf', 'docx', 'txt']

    keyboard = [[InlineKeyboardButton(fmt, callback_data=f"format_{fmt}") for fmt in formats]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="لطفا فرمت خروجی را انتخاب کنید:", reply_markup=reply_markup)

# مدیریت انتخاب فرمت خروجی
def format_button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    output_format = query.data.replace("format_", "")

    # ذخیره فرمت خروجی در user_data
    context.user_data['output_format'] = output_format
    query.edit_message_text(text=f"فرمت خروجی {output_format} انتخاب شد. لطفا فایل خود را ارسال کنید.")

# تبدیل فایل صوتی
def convert_audio(file_path, output_format):
    audio = AudioSegment.from_file(file_path)
    output_path = f"{file_path}.{output_format}"
    audio.export(output_path, format=output_format)
    return output_path

# تبدیل تصویر
def convert_image(file_path, output_format):
    img = Image.open(file_path)
    output_path = f"{file_path}.{output_format}"
    img.save(output_path, format=output_format.upper() if output_format == 'jpg' else output_format)
    return output_path

# تبدیل ویدیو
def convert_video(file_path, output_format):
    video = VideoFileClip(file_path)
    output_path = f"{file_path}.{output_format}"
    video.write_videofile(output_path, codec='libx264')
    return output_path

# تبدیل سند
def convert_document(file_path, output_format):
    if output_format == 'pdf':
        return file_path  # اگر فرمت خروجی PDF باشد، نیازی به تبدیل نیست
    elif output_format == 'docx':
        # تبدیل PDF به DOCX (نیاز به کتابخانه‌های اضافی مانند pdf2docx)
        output_path = f"{file_path}.docx"
        # اینجا کد تبدیل PDF به DOCX قرار می‌گیرد
        os.rename(file_path, output_path)
        return output_path
    elif output_format == 'txt':
        # تبدیل PDF به TXT (نیاز به کتابخانه‌های اضافی مانند PyPDF2)
        output_path = f"{file_path}.txt"
        # اینجا کد تبدیل PDF به TXT قرار می‌گیرد
        os.rename(file_path, output_path)
        return output_path

# دریافت فایل و تبدیل آن
def handle_file(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    conversion_type = context.user_data.get('conversion_type')
    output_format = context.user_data.get('output_format')

    if not conversion_type or not output_format:
        update.message.reply_text('لطفا ابتدا نوع فایل و فرمت خروجی را انتخاب کنید.')
        return

    if conversion_type == 'convert_audio':
        file = update.message.audio.get_file()
    elif conversion_type == 'convert_image':
        file = update.message.photo[-1].get_file()
    elif conversion_type == 'convert_video':
        file = update.message.video.get_file()
    elif conversion_type == 'convert_document':
        file = update.message.document.get_file()
    else:
        update.message.reply_text('نوع فایل نامعتبر است.')
        return

    file_path = f"temp/{file.file_id}"
    file.download(file_path)

    try:
        if conversion_type == 'convert_audio':
            output_path = convert_audio(file_path, output_format)
        elif conversion_type == 'convert_image':
            output_path = convert_image(file_path, output_format)
        elif conversion_type == 'convert_video':
            output_path = convert_video(file_path, output_format)
        elif conversion_type == 'convert_document':
            output_path = convert_document(file_path, output_format)

        with open(output_path, 'rb') as f:
            if conversion_type == 'convert_audio':
                update.message.reply_audio(f)
            elif conversion_type == 'convert_image':
                update.message.reply_photo(f)
            elif conversion_type == 'convert_video':
                update.message.reply_video(f)
            elif conversion_type == 'convert_document':
                update.message.reply_document(f)

    except Exception as e:
        logger.error(f"Error converting file: {e}")
        update.message.reply_text('متاسفانه در تبدیل فایل مشکلی پیش آمد.')

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
        if os.path.exists(output_path):
            os.remove(output_path)

# مدیریت خطا
def error(update: Update, context: CallbackContext) -> None:
    logger.warning(f'Update {update} caused error {context.error}')

def main() -> None:
    # ایجاد دایرکتوری موقت
    if not os.path.exists('temp'):
        os.makedirs('temp')

    # ایجاد Updater و Dispatcher
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # ثبت دستورات
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button, pattern='^convert_'))
    dispatcher.add_handler(CallbackQueryHandler(format_button, pattern='^format_'))
    dispatcher.add_handler(MessageHandler(Filters.audio | Filters.photo | Filters.video | Filters.document, handle_file))

    # ثبت مدیریت خطا
    dispatcher.add_error_handler(error)

    # شروع ربات
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
