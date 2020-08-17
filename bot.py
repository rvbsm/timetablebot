from config import *
import threading
from vars import *
from messages import *
from func import *
from classcheck import ClassCheck
from sqlite import SQLData
import telebot
from telebot import types
import logging
from datetime import datetime
import os
from flask import Flask, request

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

bot = telebot.TeleBot(TOKEN, threaded=False)

db = SQLData('db/data.db')
cc = ClassCheck()
server = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
	user_id = message.chat.id
	if not db.user_exist(user_id):
		db.add_user(message.from_user.username, user_id)
		menu = menu_button()
		bot.send_message(user_id, HELLO_FIRST.format(message.from_user.first_name), reply_markup=menu, parse_mode='HTML')
		classes = class_button()
		bot.send_message(user_id, CLASS_TEXT, reply_markup=classes)
	elif db.user_exist(user_id):
		sl = db.check_class(user_id)
		classroom = "".join(sl)
		menu = menu_button()
		bot.send_message(user_id, START.format(str(classroom)), reply_markup=menu)
	else:
		drop = open('/pic/drop.jpg', ERROR)
		bot.send_photo(user_id, drop)
	sl = classroom = None

@bot.message_handler(commands=['settings'])
def settings(message):
	user_id = message.chat.id
	menu = settings_button()
	bot.send_message(user_id, SETTINGS_TEXT, reply_markup=menu)

@bot.message_handler(content_types=['text'])
def message(message):
	user_id = message.chat.id
	global z
	if message.text == TIMETABLE_BUTTON and db.class_exist(user_id):
		when = when_button()
		bot.send_message(user_id, 'На когда?', reply_markup=when)
		z = 0
	elif message.text == TIMETABLE_BUTTON or message.text == CHANGE_CLASS_BUTTON:
		classes = class_button()
		bot.send_message(user_id, CLASS_TEXT, reply_markup=classes)
	elif message.text in CLASS_LIST:
		classroom = message.text
		db.update_class(user_id, classroom)
		when = when_button()
		bot.send_message(user_id, 'На когда?', reply_markup=when)
		z = 0
	elif message.text == ATIMETABLE_BUTTON:
		classes = aclass_button()
		bot.send_message(user_id, CLASS_TEXT, reply_markup=classes)
	elif message.text in ACLASS_LIST:
		aclassroom = message.text.strip('.')
		db.update_aclass(user_id, aclassroom)
		when = when_button()
		bot.send_message(user_id, 'На когда?', reply_markup=when)
		z = 1
	elif message.text == 'Сегодня':
		if z == 0:
			timetable(message, 0)
		elif z == 1:
			atimetable(message, 0)
		z = None
	elif message.text == 'Завтра':
		if z == 0:
			timetable(message, 1)
		elif z == 1:
			atimetable(message, 1)
		z = None
	elif message.text == SETTINGS_BUTTON:
		settings(message)
	else:
		start(message)
	classroom = aclassrom = classes = itembtn9a = itembtn9b = itembtn9v = itembtn10a = itembtn10b = itembtn10v = itembtn11a = itembtn11b = itembtn11v = t = None

def timetable(message, x):
	user_id = message.chat.id
	sl = db.check_class(user_id)
	table_send(message, sl, x)
	sl = l = x = None

def atimetable(message, x):
	user_id = message.chat.id
	sl = db.check_aclass(user_id)
	table_send(message, sl, x)
	sl = l = x = None

def table_send(message, sl, x):
	user_id = message.chat.id
	classroom = "".join(sl)
	if datetime.today().weekday() != 6:
		day = cc.check(classroom)
		week = date(x)
		menu = menu_button()
		bot.send_message(user_id, TIMETABLE_TEXT.format(classroom, week, day), reply_markup=menu, parse_mode='HTML')
	elif datetime.datetime.today().weekday() == 6:
		week = date()
		bot.send_message(user_id, SUNDAY_TEXT.format(week))
	day = week = None

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
	bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
	return "!", 200

@server.route("/")
def webhook():
	bot.remove_webhook()
	bot.set_webhook(url='https://{}.herokuapp.com/'.format(APP_NAME) + TOKEN)
	return "Bot is working", 200


if __name__ == '__main__':
	server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
#	bot.polling(none_stop=True)
