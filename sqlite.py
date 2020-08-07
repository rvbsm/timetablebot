from func import *
import sqlite3
import threading

class SQLData:
	def __init__(self, database):
		self.connection = sqlite3.connect(database, check_same_thread=False)
		self.cursor = self.connection.cursor()
		self.lock = threading.Lock()

	def user_status(self, user_id):
		with self.connection:
			return self.cursor.execute('''SELECT `status` FROM `users` WHERE user_id = ?''', (user_id,)).fetchall()

	def user_exist(self, user_id):
		with self.connection:
			try:
				self.lock.acquire(True)
				result = self.cursor.execute('''SELECT * FROM `users` WHERE `user_id` = ?''', (user_id,)).fetchall()
				return bool(len(result))
			finally:
				self.lock.release()

	def add_user(self, username, user_id):
		with self.connection:
			return self.cursor.execute('''INSERT INTO `users` (`username` ,`user_id`) VALUES(?,?)''', (username,user_id))

	def update_user(self, username, user_id):
		with self.connection:
			return self.cursor.execute('''UPDATE `users` SET `username` = ? WHERE `user_id` = ?''', (username,user_id))

	def update_class(self, user_id, l):
		with self.connection:
			return self.cursor.execute('''UPDATE `users` SET `classroom` = ? WHERE `user_id` = ?''', (l,user_id))

	def update_aclass(self, user_id, al):
		with self.connection:
			return self.cursor.execute('''UPDATE `users` SET `aclassroom` = ? WHERE `user_id` = ?''', (al,user_id))

	def check_class(self, user_id):
		with self.connection:
			result = self.cursor.execute('''SELECT `classroom` FROM `users` WHERE `user_id` = ?''', (user_id,)).fetchall()
			for i in result:
				return [i[0] for i in result]

	def check_aclass(self, user_id):
		with self.connection:
			result = self.cursor.execute('''SELECT `aclassroom` FROM `users` WHERE `user_id` = ?''', (user_id,)).fetchall()
			for i in result:
				return [i[0] for i in result]

	def mon(self):
		with self.connection:
			result = self.cursor.execute('''SELECT * FROM `monday`''').fetchall()
			result = convert(result)
			return result
	def tue(self):
		with self.connection:
			result = self.cursor.execute('''SELECT * FROM `tuesday`''').fetchall()
			result = convert(result)
			return result

	def wed(self):
		with self.connection:
			result = self.cursor.execute('''SELECT * FROM `wednesday`''').fetchall()
			result = convert(result)
			return result

	def thur(self):
		with self.connection:
			result = self.cursor.execute('''SELECT * FROM `thursday`''').fetchall()
			result = convert(result)
			return result

	def fri(self):
		with self.connection:
			result = self.cursor.execute('''SELECT * FROM `friday`''').fetchall()
			result = convert(result)
			return result

	def sat(self):
		with self.connection:
			result = self.cursor.execute('''SELECT * FROM `saturday`''').fetchall()
			result = convert(result)
			return result

	def close(self):
		self.connection.close()
