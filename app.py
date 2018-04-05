#!/usr/bin/env python
# -*- coding: utf-8 -*-
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

def math(bot, update):
    expressao = update.message.text
    expressao = expressao.split('/math ')[1]
    try:
        solve = eval(expressao)
    except Exception as error:
        solve = 'Error - '+str(error)
    update.message.reply_text('Calcular: {}\nSolução: {}'.format(expressao,solve))

def math_lista(bot,update):
    update.message.reply_text(msgs.math_lista)
    db.save(update.message)

def dx(bot, update):
    expressao = update.message.text
    expressao = expressao.split('/dx ')[1]
    solve = differential.dx(expressao)
    update.message.reply_text('Calcular: dx( {} )\nSolução: {}'.format(expressao,solve))

def integral(bot, update):
    expressao = update.message.text
    expressao = expressao.split('/integral ')[1]
    solve = differential.integ(expressao)
    update.message.reply_text(u'Calcular: integral( {} )\nSolução: {}'.format(expressao,solve))

def plot(bot, update):
    expressao = update.message.text
    expressao = expressao.split('/plot ')[1]
    differential.create_graph(expressao)
    update.message.reply_photo(photo=open("graph.png",'rb'))
    differential.delete_graph()

def plot3d(bot, update):
    expressao = update.message.text
    expressao = expressao.split('/plot3d ')[1]
    differential.create_graph3d(expressao)
    update.message.reply_photo(photo=open("graph.png",'rb'))
    differential.delete_graph()

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler(['help','start'], help))
updater.dispatcher.add_handler(CommandHandler('math', math))
updater.dispatcher.add_handler(CommandHandler('dx', dx))
updater.dispatcher.add_handler(CommandHandler('integral', integral))
updater.dispatcher.add_handler(CommandHandler('plot', plot))
updater.dispatcher.add_handler(CommandHandler('plot3d', plot3d))
updater.dispatcher.add_handler(CommandHandler('math_lista',math_lista))
updater.start_polling()
updater.idle()
