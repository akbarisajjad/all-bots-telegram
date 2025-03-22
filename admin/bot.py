import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# تنظیمات لاگ‌گیری
logging.basicConfig(level=logging.INFO)

# توکن ربات خود را اینجا وارد کنید
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# تنظیمات ربات
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())

# حالت‌های ربات (State Management)
class AdminStates(StatesGroup):
    waiting_for_user_id = State()
    waiting_for_message = State()

# دستور شروع /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton(text="محدود کردن کاربر", callback_data="mute_user"),
        InlineKeyboardButton(text="برداشتن محدودیت", callback_data="unmute_user"),
        InlineKeyboardButton(text="اخراج کاربر", callback_data="ban_user"),
        InlineKeyboardButton(text="بازگرداندن کاربر", callback_data="unban_user"),
        InlineKeyboardButton(text="ارسال پیام به کاربر", callback_data="send_message"),
    ]
    keyboard.add(*buttons)
    await message.reply("سلام! من ربات مدیریت کانال و گروه شما هستم. لطفاً یک گزینه را انتخاب کنید:", reply_markup=keyboard)

# مدیریت CallbackQuery
@dp.callback_query_handler(lambda c: c.data == 'mute_user')
async def process_callback_mute_user(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "لطفاً شناسه کاربری (User ID) را وارد کنید:")
    await AdminStates.waiting_for_user_id.set()

@dp.callback_query_handler(lambda c: c.data == 'unmute_user')
async def process_callback_unmute_user(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "لطفاً شناسه کاربری (User ID) را وارد کنید:")
    await AdminStates.waiting_for_user_id.set()

@dp.callback_query_handler(lambda c: c.data == 'ban_user')
async def process_callback_ban_user(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "لطفاً شناسه کاربری (User ID) را وارد کنید:")
    await AdminStates.waiting_for_user_id.set()

@dp.callback_query_handler(lambda c: c.data == 'unban_user')
async def process_callback_unban_user(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "لطفاً شناسه کاربری (User ID) را وارد کنید:")
    await AdminStates.waiting_for_user_id.set()

@dp.callback_query_handler(lambda c: c.data == 'send_message')
async def process_callback_send_message(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "لطفاً شناسه کاربری (User ID) را وارد کنید:")
    await AdminStates.waiting_for_user_id.set()

# مدیریت وضعیت‌ها
@dp.message_handler(state=AdminStates.waiting_for_user_id)
async def process_user_id(message: types.Message, state: FSMContext):
    user_id = message.text
    await state.update_data(user_id=user_id)
    await message.reply("لطفاً پیام خود را وارد کنید:")
    await AdminStates.waiting_for_message.set()

@dp.message_handler(state=AdminStates.waiting_for_message)
async def process_message(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    user_id = user_data['user_id']
    await bot.send_message(user_id, message.text)
    await message.reply("پیام با موفقیت ارسال شد.")
    await state.finish()

# شروع ربات
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
