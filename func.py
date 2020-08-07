from vars import *
from datetime import datetime
from telebot import types

def convert(result):
	s = [str(i) for i in result]
	res = "".join(s)
	res = res.strip()
	res = res.strip("()'")
	res = res.replace(".", '\n')
	return str(res.replace(',', '\n\n'))

def menu_button():
	menu = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
	timetab = types.KeyboardButton(TIMETABLE_BUTTON)
	anothertab = types.KeyboardButton(ATIMETABLE_BUTTON)	
	settings = types.KeyboardButton(SETTINGS_BUTTON)
	menu.add(timetab, anothertab, settings)
	return menu

def settings_button():
	menu = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
	change = types.KeyboardButton(CHANGE_CLASS_BUTTON)
	menu.add(change)
	return menu

def class_button():
	classes = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
	itembtn9a = types.KeyboardButton('9-А')
	itembtn9b = types.KeyboardButton('9-Б')
	itembtn9v = types.KeyboardButton('9-В')
	itembtn10a = types.KeyboardButton('10-А')
	itembtn10b = types.KeyboardButton('10-Б')
	itembtn10v = types.KeyboardButton('10-В')
	itembtn11a = types.KeyboardButton('11-А')
	itembtn11b = types.KeyboardButton('11-Б')
	itembtn11v = types.KeyboardButton('11-В')
	classes.add(itembtn9a, itembtn10a, itembtn11a, itembtn9b, itembtn10b, itembtn11b, itembtn9v, itembtn10v, itembtn11v)
	return classes

def aclass_button():
	classes = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
	itembtn9a = types.KeyboardButton('9-А.')
	itembtn9b = types.KeyboardButton('9-Б.')
	itembtn9v = types.KeyboardButton('9-В.')
	itembtn10a = types.KeyboardButton('10-А.')
	itembtn10b = types.KeyboardButton('10-Б.')
	itembtn10v = types.KeyboardButton('10-В.')
	itembtn11a = types.KeyboardButton('11-А.')
	itembtn11b = types.KeyboardButton('11-Б.')
	itembtn11v = types.KeyboardButton('11-В.')
	classes.add(itembtn9a, itembtn10a, itembtn11a, itembtn9b, itembtn10b, itembtn11b, itembtn9v, itembtn10v, itembtn11v)
	return classes	

def when_button():
	when = types.ReplyKeyboardMarkup(row_width=1, one_time_keyboard=True)
	today = types.KeyboardButton('Сегодня')
	tomorrow = types.KeyboardButton('Завтра')
	when.add(today, tomorrow)
	return when

def date(x):
	y = datetime.today().weekday()
	y += x
	if y == 0:
		week = 'Понедельник'
	elif y == 1:
		week = 'Вторник'
	elif y == 2:
		week = 'Среда'
	elif y == 3:
		week = 'Четверг'
	elif y == 4:
		week = 'Пятница'
	elif y == 5:
		week = 'Суббота'
	elif y == 6:
		week = 'Воскресенье'
	return week
