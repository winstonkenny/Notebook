import sys
import os
import time
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication,QDockWidget,QListWidget,QFileDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()# 初始化UI界面

	def initUI(self):
		self.textEdit = QTextEdit()#新建文本输入控件
		self.setCentralWidget(self.textEdit)

		newAction = QAction(QIcon('./img/new.png'), 'New', self)#新建一个新建事件
		newAction.setShortcut('Ctrl+N')#事件快捷键
		newAction.setStatusTip('New file')#状态栏显示
		# newAction.triggered.connect()#事件连接到动作

		openAction = QAction(QIcon('./img/open.png'), 'Open', self)#新建一个打开事件
		openAction.setShortcut('Ctrl+O')#事件快捷键
		openAction.setStatusTip('Open file')#状态栏显示
		openAction.triggered.connect(self.open_file)#事件连接到动作

		saveAction = QAction(QIcon('./img/save.png'), 'Save', self)#新建一个保存事件
		saveAction.setShortcut('Ctrl+S')#事件快捷键
		saveAction.setStatusTip('Save file')#状态栏显示
		saveAction.triggered.connect(self.save_file)#事件连接到动作

		elsaveAction = QAction(QIcon('./img/elsave.png'), 'Save as', self)#新建一个另存为事件
		elsaveAction.setShortcut('Shift+Ctrl+S')#事件快捷键
		elsaveAction.setStatusTip('Save file as...')#状态栏显示
		# elsaveAction.triggered.connect()#事件连接到动作

		exitAction = QAction(QIcon('./img/exit.png'), 'Exit', self)#新建一个退出事件
		exitAction.setShortcut('Ctrl+Q')#事件快捷键
		exitAction.setStatusTip('Exit application')#状态栏显示
		exitAction.triggered.connect(self.close)#事件连接到动作

		cutAction = QAction(QIcon('./img/cut.png'), 'Cut', self)#新建一个剪切事件
		cutAction.setShortcut('Ctrl+X')#事件快捷键
		cutAction.setStatusTip('Save file as...')#状态栏显示
		# cutAction.triggered.connect()#事件连接到动作

		copyAction = QAction(QIcon('./img/copy.png'), 'Copy', self)#新建一个复制事件
		copyAction.setShortcut('Ctrl+C')#事件快捷键
		copyAction.setStatusTip('Save file as...')#状态栏显示
		# copyAction.triggered.connect()#事件连接到动作

		pasteAction = QAction(QIcon('./img/paste.png'), 'Paste', self)#新建一个粘贴事件
		pasteAction.setShortcut('Ctrl+V')#事件快捷键
		pasteAction.setStatusTip('Save file as...')#状态栏显示
		# pasteAction.triggered.connect()#事件连接到动作

		insertTimeAction = QAction(QIcon('./img/insert_time.png'), 'Insert Time', self)#新建一个插入时间事件
		insertTimeAction.setShortcut('Shift+Ctrl+F5')#事件快捷键
		insertTimeAction.setStatusTip('Insert time')#状态栏显示
		insertTimeAction.triggered.connect(self.insertTime)#事件连接到动作

		self.statusBar()# 用于显示状态栏
		menubar = self.menuBar()# 新建一个菜单栏

		fileMenu = menubar.addMenu('&File')# 工具栏里第一页(File)
		fileMenu.addAction(newAction)
		fileMenu.addAction(openAction)
		fileMenu.addAction(saveAction)
		fileMenu.addAction(elsaveAction)
		fileMenu.addAction(exitAction)

		toolbar1 = self.addToolBar('File')
		toolbar1.addAction(newAction)
		toolbar1.addAction(openAction)
		toolbar1.addAction(saveAction)
		toolbar1.addAction(elsaveAction)
		toolbar1.addAction(exitAction)

		editMenu = menubar.addMenu('&Edit')# 工具栏里第二页(Edit)
		editMenu.addAction(cutAction)
		editMenu.addAction(copyAction)
		editMenu.addAction(pasteAction)
		editMenu.addAction(insertTimeAction)

		toolbar2 = self.addToolBar('Edit')
		toolbar2.addAction(cutAction)
		toolbar2.addAction(copyAction)
		toolbar2.addAction(pasteAction)
		toolbar2.addAction(insertTimeAction)

		optionMenu = menubar.addMenu('&Option')# 工具栏里第三页(Option)
		helpMenu = menubar.addMenu('&Help')# 工具栏里第四页(Help)

		self.setGeometry(1000, 150, 500, 300)
		self.setWindowTitle('NoteBook')

		# self.resize(900, 480)				# 设置窗口初始大小
		# self.setFont('SimHei')				# 设置字体
		self.setWindowFlags(
			# Qt.WindowContextHelpButtonHint |	# 像对话框一样，有个问号和关闭按钮
			# Qt.WindowMaximizeButtonHint |
			# Qt.WindowTitleHint |
			# Qt.WindowMinimizeButtonHint |   # 使能最小化按钮
			# Qt.WindowCloseButtonHint |      # 使能关闭按钮
			Qt.WindowStaysOnTopHint)        # 窗体总在最前端
		# self.setFixedSize(self.width(), self.height())	# 固定窗体大小不能修改
		#窗口显示
		self.getFiles()# 得到文件列表用于在左边显示出来
		self.addDock()

		self.show()

	def insertTime(self):
		timenow = time.strftime("%Y-%m-%d %X", time.localtime())
		self.textEdit.insertPlainText('\n\n*************************\n*  '+timenow+'  *\n*************************\n')
		self.texttemp.seek(2,0)
		pass

	def open_file(self):
		openFilePathName, filetype = QFileDialog.getOpenFileName(self,
									"选取文件",
									"./files/",
									"All Files (*);;Text Files (*.txt)")   #设置文件扩展名过滤, 注意用双分号间隔
		fileNameTemp = os.path.splitext(openFilePathName.split('/')[-1])[0]# 获取路径下的文件名称(不带扩展名)
		self.texttemp = open(openFilePathName,'r+')
		if fileNameTemp in self.items:
			# fileNameTemp += ('('+openFilePathName.split('/')[-2]+')')
			# self.items.append(fileNameTemp)
			pass
		else:
			self.items.append(fileNameTemp)
		self.texttemp.seek(2,0)

	def save_file(self):
		self.texttemp.truncate(0)
		self.texttemp.seek(0,0)
		self.texttemp.write(self.textEdit.toPlainText())
		pass
	def getFiles(self):
		# 判断是否新建文件夹,没有'files'文件夹则创建此文件夹
		dirs = os.listdir('./')
		if 'files' in dirs:
			pass
		else:
			os.mkdir('files')

		self.items = []# 创建文件列表
		files = os.listdir('./files')# 列出files文件夹下的所有文件
		for filename in files:# 筛选符合条件的文件,把名字存在items列表中
			portion = os.path.splitext(filename)#分离文件名字和后缀
			if portion[1] ==".txt":#根据后缀来修改,如无后缀则空
				self.items.append(portion[0])
		str_today = time.strftime("%Y-%m-%d", time.localtime())
		if str_today in self.items:
			self.texttemp = open('./files/'+str_today+'.txt','r+')
		else:
			self.texttemp = open('./files/'+str_today+'.txt','a+')
			self.items.append(str_today)
		self.textEdit.setText(self.texttemp.read())
		self.texttemp.seek(2,0)

	def onDockListIndexChanged(self, index):
		self.save_file()
		item = self.items[index]
		self.texttemp = open('./files/'+item+'.txt','r+')
		self.textEdit.setText(self.texttemp.read())
		self.texttemp.seek(2,0)

	def addDock(self):
		dock1 = QDockWidget('Items')
		# dock1.setFeatures(QDockWidget.DockWidgetFloatable)
		# dock1.setFeatures(QDockWidget.DockWidgetClosable)
		# dock1.setFeatures(QDockWidget.DockWidgetMovable)
		dock1.setFeatures(QDockWidget.DockWidgetMovable|QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetClosable)
		# dock1.setFeatures(QDockWidget.DockWidgetVerticalTitleBar)
		# dock1.setFeatures(QDockWidget.NoDockWidgetFeatures)
		dock1.setAllowedAreas(Qt.RightDockWidgetArea|Qt.LeftDockWidgetArea)# 可停靠位置为左右
		listwidget = QListWidget()
		listwidget.addItems(self.items)
		listwidget.currentRowChanged.connect(self.onDockListIndexChanged)# 当选择有变化时的动作
		dock1.setWidget(listwidget)
		self.addDockWidget(Qt.LeftDockWidgetArea, dock1)# 初始显示位置


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = MainWindow()
	sys.exit(app.exec_())