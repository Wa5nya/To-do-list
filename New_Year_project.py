import sys
import sqlite3
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, \
QPushButton, QMainWindow, QVBoxLayout, QHBoxLayout, QInputDialog, QListWidget
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

class Ui_MainWindow(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("MainWindow")
		self.resize(600, 600)
		self.vbox = QVBoxLayout()
		self.hbox = QHBoxLayout()
		self.hbox2 = QHBoxLayout()
		self.hbox3 = QHBoxLayout()
		self.hbox4 = QHBoxLayout()
		self.active_task_list = QListWidget()
		self.complete_task_list = QListWidget()
		self.additem_pushButton = QPushButton("Добавить задачу", self)
		self.deleteitem_pushButton_2 = QPushButton("Удалить", self)
		self.completeitem_pushButton_3 = QPushButton("Выполнить", self)
		self.additem_lineEdit = QLineEdit("Введите задачу",self)	
		self.initUI()
		self.create_db()


	def initUI(self):
		self.SetStructure()
		self.show()
	
	def SetStructure(self):
		self.hbox4.addWidget(self.active_task_list)
		self.hbox4.addWidget(self.complete_task_list)
		self.vbox.addLayout(self.hbox4)
		
		self.hbox.addWidget(self.deleteitem_pushButton_2)
		self.hbox.addWidget(self.completeitem_pushButton_3)
		self.hbox2.addWidget(self.additem_pushButton)
		self.hbox3.addWidget(self.additem_lineEdit)
		self.vbox.addLayout(self.hbox)
		self.vbox.addLayout(self.hbox3)
		self.vbox.addLayout(self.hbox2)


		self.setLayout(self.vbox)


	def create_db(self):
		self.db = QSqlDatabase.addDatabase(" QSQLITE")
		self.db.setDatabaseName("tasklist.sqlite")
		#создали дб
		self.db.open()
		
		self.query = QSqlQuery() # запрос
		self.query.exec('''CREATE TABLE IF NOT EXIST tasklist(
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			task_name VARCHAR(255) NOT NULL,
			active BOOL NOT NULL DEFAULT TRUE

		)''')
		#создание таблицы с 3-мя полями




if __name__ == "__main__":
	app = QApplication(sys.argv)
	mw = Ui_MainWindow()
	sys.exit(app.exec_())