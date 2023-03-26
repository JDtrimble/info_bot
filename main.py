import logging
from telegram.ext import Application, MessageHandler, CommandHandler, filters
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from config import BOT_TOKEN
import datetime


reply_keyboard = [['/address', '/phone'],
                  ['/site', '/work_time']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)


async def help(update, context):
    await update.message.reply_text(
        "Я бот справочник по школе №218.")


async def address(update, context):
    await update.message.reply_text(
        "Адрес: г. Москва, Дмитровское ш. 5А")


async def phone(update, context):
    await update.message.reply_text("Телефон: +7 (499) 976-40-87")  # Это номер директора, не звонить!


async def site(update, context):
    await update.message.reply_text(
        "Сайт: https://sch218.mskobr.ru")


async def work_time(update, context):
    await update.message.reply_text(
        "Время работы: по настроению.")


def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("address", address))
    application.add_handler(CommandHandler("phone", phone))
    application.add_handler(CommandHandler("site", site))
    application.add_handler(CommandHandler("work_time", work_time))
    application.add_handler(CommandHandler("help", help))
    application.run_polling()
