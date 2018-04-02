from __future__ import division
import logging
from telegram.ext import Updater, CommandHandler
import differential
from numpy import *
import msgs
import os
#import mongo as db

help_msg = msgs.help_msgs
TOKEN = os.environ['BOT_API_TOKEN']

def help(bot, update):
    update.message.reply_text(help_msg)
<<<<<<< HEAD
    #db.save(update.message)
=======
>>>>>>> 794f405bb4df2a834de1391da363099e61d3515f

def math(bot, update):
    expressao = update.message.text
    expressao = expressao.split('/math ')[1]
    try:
        solve = eval(expressao)
    except Exception as error:
        solve = 'Error - '+str(error)
    update.message.reply_text('Calcular: {}\nSolucao: {}'.format(expressao,solve))
    #db.save(update.message)

def math_lista(bot,update):
    update.message.reply_text(msgs.math_lista)
    db.save(update.message)

def dx(bot, update):
    expressao = update.message.text
    expressao = expressao.split('/dx ')[1]
    solve = differential.dx(expressao)
    update.message.reply_text('Calcular: dx( {} )\nSolucao: {}'.format(expressao,solve))
    #db.save(update.message)

def integral(bot, update):
    expressao = update.message.text
    expressao = expressao.split('/integral ')[1]
    solve = differential.integ(expressao)
    update.message.reply_text('Calcular: integral( {} )\nSolucao: {}'.format(expressao,solve))
<<<<<<< HEAD
    #db.save(update.message)

=======

def grafico(bot, update):
    expressao = update.message.text
    expressao = expressao.split('/integral ')[1]
    graph = differential.create_graph(expressao,data)
    update.message.reply_photo(photo=open(graph,'rb'))
    differential.delete_graph(graph)
    
>>>>>>> 794f405bb4df2a834de1391da363099e61d3515f
updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler(['help','start'], help))
updater.dispatcher.add_handler(CommandHandler('math', math))
updater.dispatcher.add_handler(CommandHandler('dx', dx))
updater.dispatcher.add_handler(CommandHandler('integral', integral))
updater.dispatcher.add_handler(CommandHandler('graph', grafico))
updater.dispatcher.add_handler(CommandHandler('math_lista',math_lista))
updater.start_polling()
updater.idle()
