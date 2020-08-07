import datetime
from sqlite import SQLData

db = SQLData('db/data.db')
tt9a = SQLData('db/timetable9a.db')
tt9b = SQLData('db/timetable9b.db')
tt9v = SQLData('db/timetable9v.db')
tt10a = SQLData('db/timetable10a.db')
tt10b = SQLData('db/timetable10b.db')
tt10v = SQLData('db/timetable10v.db')
tt11a = SQLData('db/timetable11a.db')
tt11b = SQLData('db/timetable11b.db')
tt11v = SQLData('db/timetable11v.db')


class ClassCheck:
	def check(self, l):
		if l == '9-А':
			if datetime.datetime.today().weekday() == 0:
				day = str(tt9a.mon())
			elif datetime.datetime.today().weekday() == 1:
				day = str(tt9a.tue())
			elif datetime.datetime.today().weekday() == 2:
				day = str(tt9a.wed())
			elif datetime.datetime.today().weekday() == 3:
				day = str(tt9a.thur())
			elif datetime.datetime.today().weekday() == 4:
				day = str(tt9a.fri())
			elif datetime.datetime.today().weekday() == 5:
				day = str(tt9a.sat())
		elif l == '9-Б':
			if datetime.datetime.today().weekday() == 0:
				day = str(tt9b.mon())
			elif datetime.datetime.today().weekday() == 1:
				day = str(tt9b.tue())
			elif datetime.datetime.today().weekday() == 2:
				day = str(tt9b.wed())
			elif datetime.datetime.today().weekday() == 3:
				day = str(tt9b.thur())
			elif datetime.datetime.today().weekday() == 4:
				day = str(tt9b.fri())
			elif datetime.datetime.today().weekday() == 5:
				day = str(tt9b.sat())
		elif l == '9-В':
			if datetime.datetime.today().weekday() == 0:
				day = str(tt9v.mon())
			elif datetime.datetime.today().weekday() == 1:
				day = str(tt9v.tue())
			elif datetime.datetime.today().weekday() == 2:
				day = str(tt9v.wed())
			elif datetime.datetime.today().weekday() == 3:
				day = str(tt9v.thur())
			elif datetime.datetime.today().weekday() == 4:
				day = str(tt9v.fri())
			elif datetime.datetime.today().weekday() == 5:
				day = str(tt9v.sat())
		elif l == '10-А':
			if datetime.datetime.today().weekday() == 0:
				day = str(tt10a.mon())
			elif datetime.datetime.today().weekday() == 1:
				day = str(tt10a.tue())
			elif datetime.datetime.today().weekday() == 2:
				day = str(tt10a.wed())
			elif datetime.datetime.today().weekday() == 3:
				day = str(tt10a.thur())
			elif datetime.datetime.today().weekday() == 4:
				day = str(tt10a.fri())
			elif datetime.datetime.today().weekday() == 5:
				day = str(tt10a.sat())
		elif l == '10-Б':
			if datetime.datetime.today().weekday() == 0:
				day = str(tt10b.mon())
			elif datetime.datetime.today().weekday() == 1:
				day = str(tt10b.tue())
			elif datetime.datetime.today().weekday() == 2:
				day = str(tt10b.wed())
			elif datetime.datetime.today().weekday() == 3:
				day = str(tt10b.thur())
			elif datetime.datetime.today().weekday() == 4:
				day = str(tt10b.fri())
			elif datetime.datetime.today().weekday() == 5:
				day = str(tt10b.sat())
		elif l == '10-В':
			if datetime.datetime.today().weekday() == 0:
				day = str(tt10v.mon())
			elif datetime.datetime.today().weekday() == 1:
				day = str(tt10v.tue())
			elif datetime.datetime.today().weekday() == 2:
				day = str(tt10v.wed())
			elif datetime.datetime.today().weekday() == 3:
				day = str(tt10v.thur())
			elif datetime.datetime.today().weekday() == 4:
				day = str(tt10v.fri())
			elif datetime.datetime.today().weekday() == 5:
				day = str(tt10v.sat())
		elif l == '11-А':
			if datetime.datetime.today().weekday() == 0:
				day = str(tt11a.mon())
			elif datetime.datetime.today().weekday() == 1:
				day = str(tt11a.tue())
			elif datetime.datetime.today().weekday() == 2:
				day = str(tt11a.wed())
			elif datetime.datetime.today().weekday() == 3:
				day = str(tt11a.thur())
			elif datetime.datetime.today().weekday() == 4:
				day = str(tt11a.fri())
			elif datetime.datetime.today().weekday() == 5:
				day = str(tt11a.sat())
		elif l == '11-Б':
			if datetime.datetime.today().weekday() == 0:
				day = str(tt11b.mon())
			elif datetime.datetime.today().weekday() == 1:
				day = str(tt11b.tue())
			elif datetime.datetime.today().weekday() == 2:
				day = str(tt11b.wed())
			elif datetime.datetime.today().weekday() == 3:
				day = str(tt11b.thur())
			elif datetime.datetime.today().weekday() == 4:
				day = str(tt11b.fri())
			elif datetime.datetime.today().weekday() == 5:
				day = str(tt11b.sat())
		elif l == '11-В':
			if datetime.datetime.today().weekday() == 0:
				day = str(tt11v.mon())
			elif datetime.datetime.today().weekday() == 1:
				day = str(tt11v.tue())
			elif datetime.datetime.today().weekday() == 2:
				day = str(tt11v.wed())
			elif datetime.datetime.today().weekday() == 3:
				day = str(tt11v.thur())
			elif datetime.datetime.today().weekday() == 4:
				day = str(tt11v.fri())
			elif datetime.datetime.today().weekday() == 5:
				day = str(tt11v.sat())
		return day