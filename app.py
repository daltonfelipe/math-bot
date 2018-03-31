from __future__ import division
import logging
from telegram.ext import Updater, CommandHandler
import differential
from numpy import *
import msgs
import os
help_msg = msgs.help_msgs

TOKEN = os.environ['BOT_API_TOKEN']


def help(bot, update):
    update.message.reply_text(help_msg)

def math(bot, update):
    expressao = update.message.text
    expressao = expressao.split('/math ')[1]
    try:
        solve = eval(expressao)
    except Exception as error:
        solve = 'Error - '+str(error)
    update.message.reply_text('Calcular: {}\nSolucao: {}'.format(expressao,solve))

def dx(bot, update):
    expressao = update.message.text
    expressao = expressao.split('/dx ')[1]
    solve = differential.dx(expressao)
    update.message.reply_text('Calcular: dx( {} )\nSolucao: {}'.format(expressao,solve))

def integral(bot, update):
    expressao = update.message.text
    expressao = expressao.split('/integral ')[1]
    solve = differential.integ(expressao)
    update.message.reply_text('Calcular: integral( {} )\nSolucao: {}'.format(expressao,solve))


updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('math', math))
updater.dispatcher.add_handler(CommandHandler('dx', dx))
updater.dispatcher.add_handler(CommandHandler('integral', integral))

updater.start_polling()
updater.idle()
