import datetime
from sqlite import SQLData

db = SQLData('db/data.db')
tt = SQLData('db/timetable.db')


class ClassCheck:
	def check(self, l):
		global day
		if l == '9-А':
			if datetime.datetime.today().weekday() == 0:
				day = str(tt.mon('9a'))
			elif datetime.datetime.today().weekday() == 1:
				day = str(tt.tue('9a'))
			elif datetime.datetime.today().weekday() == 2:
				day = str(tt.wed('9a'))
			elif datetime.datetime.today().weekday() == 3:
				day = str(tt.thur('9a'))
			elif datetime.datetime.today().weekday() == 4:
				day = str(tt.fri('9a'))
			elif datetime.datetime.today().weekday() == 5:
				day = str(tt.sat('9a'))
		elif l == '9-Б':
			if datetime.datetime.today().weekday() == 0:
				day = str(tt.mon('9b'))
			elif datetime.datetime.today().weekday() == 1:
				day = str(tt.tue('9b'))
			elif datetime.datetime.today().weekday() == 2:
				day = str(tt.wed('9b'))
			elif datetime.datetime.today().weekday() == 3:
				day = str(tt.thur('9b'))
			elif datetime.datetime.today().weekday() == 4:
				day = str(tt.fri('9b'))
			elif datetime.datetime.today().weekday() == 5:
				day = str(tt.sat('9b'))
		elif l == '9-В':
			if datetime.datetime.today().weekday() == 0:
				day = str(tt.mon('9v'))
			elif datetime.datetime.today().weekday() == 1:
				day = str(tt.tue('9v'))
			elif datetime.datetime.today().weekday() == 2:
				day = str(tt.wed('9v'))
			elif datetime.datetime.today().weekday() == 3:
				day = str(tt.thur('9v'))
			elif datetime.datetime.today().weekday() == 4:
				day = str(tt.fri('9v'))
			elif datetime.datetime.today().weekday() == 5:
				day = str(tt.sat('9v'))
		elif l == '10-А':
			if datetime.datetime.today().weekday() == 0:
				day = str(tt.mon('10a'))
			elif datetime.datetime.today().weekday() == 1:
				day = str(tt.tue('10a'))
			elif datetime.datetime.today().weekday() == 2:
				day = str(tt.wed('10a'))
			elif datetime.datetime.today().weekday() == 3:
				day = str(tt.thur('10a'))
			elif datetime.datetime.today().weekday() == 4:
				day = str(tt.fri('10a'))
			elif datetime.datetime.today().weekday() == 5:
				day = str(tt.sat('10a'))
		elif l == '10-Б':
			if datetime.datetime.today().weekday() == 0:
				day = str(tt.mon('10b'))
			elif datetime.datetime.today().weekday() == 1:
				day = str(tt.tue('10b'))
			elif datetime.datetime.today().weekday() == 2:
				day = str(tt.wed('10b'))
			elif datetime.datetime.today().weekday() == 3:
				day = str(tt.thur('10b'))
			elif datetime.datetime.today().weekday() == 4:
				day = str(tt.fri('10b'))
			elif datetime.datetime.today().weekday() == 5:
				day = str(tt.sat('10b'))
		elif l == '10-В':
			if datetime.datetime.today().weekday() == 0:
				day = str(tt.mon('10v'))
			elif datetime.datetime.today().weekday() == 1:
				day = str(tt.tue('10v'))
			elif datetime.datetime.today().weekday() == 2:
				day = str(tt.wed('10v'))
			elif datetime.datetime.today().weekday() == 3:
				day = str(tt.thur('10v'))
			elif datetime.datetime.today().weekday() == 4:
				day = str(tt.fri('10v'))
			elif datetime.datetime.today().weekday() == 5:
				day = str(tt.sat('10v'))
		elif l == '11-А':
			if datetime.datetime.today().weekday() == 0:
				day = str(tt.mon('11a'))
			elif datetime.datetime.today().weekday() == 1:
				day = str(tt.tue('11a'))
			elif datetime.datetime.today().weekday() == 2:
				day = str(tt.wed('11a'))
			elif datetime.datetime.today().weekday() == 3:
				day = str(tt.thur('11a'))
			elif datetime.datetime.today().weekday() == 4:
				day = str(tt.fri('11a'))
			elif datetime.datetime.today().weekday() == 5:
				day = str(tt.sat('11a'))
		elif l == '11-Б':
			if datetime.datetime.today().weekday() == 0:
				day = str(tt.mon('11b'))
			elif datetime.datetime.today().weekday() == 1:
				day = str(tt.tue('11b'))
			elif datetime.datetime.today().weekday() == 2:
				day = str(tt.wed('11b'))
			elif datetime.datetime.today().weekday() == 3:
				day = str(tt.thur('11b'))
			elif datetime.datetime.today().weekday() == 4:
				day = str(tt.fri('11b'))
			elif datetime.datetime.today().weekday() == 5:
				day = str(tt.sat('11b'))
		elif l == '11-В':
			if datetime.datetime.today().weekday() == 0:
				day = str(tt.mon('11v'))
			elif datetime.datetime.today().weekday() == 1:
				day = str(tt.tue('11v'))
			elif datetime.datetime.today().weekday() == 2:
				day = str(tt.wed('11v'))
			elif datetime.datetime.today().weekday() == 3:
				day = str(tt.thur('11v'))
			elif datetime.datetime.today().weekday() == 4:
				day = str(tt.fri('11v'))
			elif datetime.datetime.today().weekday() == 5:
				day = str(tt.sat('11v'))
		return day