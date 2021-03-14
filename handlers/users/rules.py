from aiogram import types 
from aiogram.dispatcher.filters import Command 
from aiogram.types import CallbackQuery

from data.content import max_page_rules, rules
from keyboards.inline.callback_datas import close_callback 
from keyboards.inline.pagination import get_page_keyboards, pagination_call
from loader import dp 
from utils.pages import get_page 


@dp.message_handler(Command('rules'))
async def show_book(message: types.Message):
    text = get_page(rules)
    await message.answer(text,
                         reply_markup=get_page_keyboards(max_pages=max_page_rules))

@dp.callback_query_handler(pagination_call.filter(page='current_page'))
async def current_page_error(call: CallbackQuery):
    await call.answer(cache_time=60)


@dp.callback_query_handler(pagination_call.filter(key='rules'))
async def show_chose_page(call: CallbackQuery, callback_data: dict):
    current_page = int(callback_data.get('page'))
    text = get_page(rules, page=current_page)
    markup = get_page_keyboards(max_pages=max_page_rules, page=current_page)
    await call.message.edit_text(text=text, reply_markup=markup)

@dp.callback_query_handler(close_callback.filter(name='close'))
async def close(call: CallbackQuery):
    await call.message.delete()