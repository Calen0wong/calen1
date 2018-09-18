# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\pyqt5_doc\三腔气体透过率测定仪.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QWidget, QVBoxLayout, QMessageBox, QSizePolicy, \
    QDesktopWidget
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(1296, 598)
        """
        全屏窗口
        """
        screen = QDesktopWidget().screenGeometry()
        MainWindow.resize(screen.width(), screen.height())

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 90, 1251, 391))
        self.tabWidget.setObjectName("tabWidget")
        self.A = QtWidgets.QWidget()
        self.A.setObjectName("A")
        self.pushButton = QtWidgets.QPushButton(self.A)
        self.pushButton.setGeometry(QtCore.QRect(90, 10, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.A)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 10, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox = QtWidgets.QComboBox(self.A)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 71, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.checkBox = QtWidgets.QCheckBox(self.A)
        self.checkBox.setGeometry(QtCore.QRect(260, 10, 81, 21))
        self.checkBox.setObjectName("checkBox")
        self.widget_9 = QtWidgets.QWidget(self.A)
        self.widget_9.setGeometry(QtCore.QRect(10, 40, 1221, 321))
        self.widget_9.setObjectName("widget_9")

        """
        将用matplotlib绘制的动态图控件插入到窗口当中，这个控件是self.widget_9，插入的固定格式如下：
        如果想插入窗口当中，应该先创建一个新控件，然后将控件放入widget_9相应的位置当中
        vbox = QtWidgets.QVBoxLayout(self.widget_9)
        dc = MyDynamicMplCanvas(self.widget_9, width=5, height=4, dpi=100)
        vbox.addWidget(dc)
        self.widget_9.setFocus()
        """
        # self.main_widget = QWidget(self)
        vbox = QtWidgets.QVBoxLayout(self.widget_9)
        # sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        dc = MyDynamicMplCanvas(self.widget_9, width=5, height=4, dpi=100)
        # l.addWidget(sc)
        vbox.addWidget(dc)
        self.widget_9.setFocus()
        # self.setCentralWidget(self.widget_7)

        # self.graphicsView = QtWidgets.QGraphicsView(self.widget_9)
        # self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1221, 321))
        # self.graphicsView.setObjectName("graphicsView")
        #
        # # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # # 添加图片
        # self.graphicsView.scene = QtWidgets.QGraphicsScene()  # 创建一个图片元素的对象
        # p = QtGui.QPixmap()
        # p.load("./newPrefix/line3.png")  # 加载图片
        # item = QtWidgets.QGraphicsPixmapItem(p)  # 创建一个变量用于承载加载后的图片
        # self.graphicsView.scene.addItem(item)  # 将加载后的图片传递给scene对象
        # self.graphicsView.setScene(self.graphicsView.scene)  # 这个我也不知道是做了个啥
        # # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        self.tabWidget.addTab(self.A, "")
        self.B = QtWidgets.QWidget()
        self.B.setObjectName("B")
        self.comboBox_2 = QtWidgets.QComboBox(self.B)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 10, 71, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_3 = QtWidgets.QPushButton(self.B)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 10, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.B)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 10, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.checkBox_2 = QtWidgets.QCheckBox(self.B)
        self.checkBox_2.setGeometry(QtCore.QRect(260, 10, 81, 21))
        self.checkBox_2.setObjectName("checkBox_2")
        self.widget_8 = QtWidgets.QWidget(self.B)
        self.widget_8.setGeometry(QtCore.QRect(10, 40, 1221, 321))
        self.widget_8.setObjectName("widget_8")

        """
        将用matplotlib绘制的动态图控件插入到窗口当中，这个控件是self.widget_9，插入的固定格式如下：
        如果想插入窗口当中，应该先创建一个新控件，然后将控件放入widget_9相应的位置当中
        vbox = QtWidgets.QVBoxLayout(self.widget_8)
        dc = MyDynamicMplCanvas(self.widget_8, width=5, height=4, dpi=100)
        vbox.addWidget(dc)
        self.widget_8.setFocus()
        """
        # self.main_widget = QWidget(self)
        vbox = QtWidgets.QVBoxLayout(self.widget_8)
        # sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        dc = MyDynamicMplCanvas(self.widget_8, width=5, height=4, dpi=100)
        # l.addWidget(sc)
        vbox.addWidget(dc)
        self.widget_8.setFocus()
        # self.setCentralWidget(self.widget_7)

        # self.graphicsView_2 = QtWidgets.QGraphicsView(self.widget_8)
        # self.graphicsView_2.setGeometry(QtCore.QRect(0, 0, 1221, 321))
        # self.graphicsView_2.setObjectName("graphicsView_2")
        #
        # # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # # 添加图片
        # self.graphicsView_2.scene = QtWidgets.QGraphicsScene()  # 创建一个图片元素的对象
        # p = QtGui.QPixmap()
        # p.load("./newPrefix/line3.png")  # 加载图片
        # item = QtWidgets.QGraphicsPixmapItem(p)  # 创建一个变量用于承载加载后的图片
        # self.graphicsView_2.scene.addItem(item)  # 将加载后的图片传递给scene对象
        # self.graphicsView_2.setScene(self.graphicsView_2.scene)  # 这个我也不知道是做了个啥
        # # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        self.tabWidget.addTab(self.B, "")
        self.C = QtWidgets.QWidget()
        self.C.setObjectName("C")
        self.comboBox_3 = QtWidgets.QComboBox(self.C)
        self.comboBox_3.setGeometry(QtCore.QRect(10, 10, 71, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.pushButton_5 = QtWidgets.QPushButton(self.C)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 10, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.C)
        self.pushButton_6.setGeometry(QtCore.QRect(170, 10, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.checkBox_3 = QtWidgets.QCheckBox(self.C)
        self.checkBox_3.setGeometry(QtCore.QRect(260, 10, 81, 21))
        self.checkBox_3.setObjectName("checkBox_3")
        self.widget_7 = QtWidgets.QWidget(self.C)
        self.widget_7.setGeometry(QtCore.QRect(10, 40, 1221, 321))
        self.widget_7.setObjectName("widget_7")
        # #####################################################

        """
        将用matplotlib绘制的动态图控件插入到窗口当中，这个控件是self.widget_9，插入的固定格式如下：
        如果想插入窗口当中，应该先创建一个新控件，然后将控件放入widget_9相应的位置当中
        vbox = QtWidgets.QVBoxLayout(self.widget_7)
        dc = MyDynamicMplCanvas(self.widget_7, width=5, height=4, dpi=100)
        vbox.addWidget(dc)
        self.widget_7.setFocus()
        """
        # self.main_widget = QWidget(self)
        vbox = QtWidgets.QVBoxLayout(self.widget_7)
        # sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        dc = MyDynamicMplCanvas(self.widget_7, width=5, height=4, dpi=100)
        # l.addWidget(sc)
        vbox.addWidget(dc)
        self.widget_7.setFocus()
        # self.setCentralWidget(self.widget_7)

        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        # self.graphicsView_3 = QtWidgets.QGraphicsView(self.widget_7)
        # self.graphicsView_3.setGeometry(QtCore.QRect(0, 0, 1221, 321))
        # self.graphicsView_3.setObjectName("graphicsView_3")
        #
        # # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # # 添加图片
        # self.graphicsView_3.scene = QtWidgets.QGraphicsScene()  # 创建一个图片元素的对象
        # p = QtGui.QPixmap()
        # p.load("./newPrefix/line3.png")  # 加载图片
        # item = QtWidgets.QGraphicsPixmapItem(p)  # 创建一个变量用于承载加载后的图片
        # self.graphicsView_3.scene.addItem(item)  # 将加载后的图片传递给scene对象
        # self.graphicsView_3.setScene(self.graphicsView_3.scene)  # 这个我也不知道是做了个啥
        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        self.tabWidget.addTab(self.C, "")
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(20, 10, 201, 71))
        self.widget.setObjectName("widget")
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 101, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_7.setGeometry(QtCore.QRect(120, 10, 81, 21))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_8.setGeometry(QtCore.QRect(120, 40, 81, 21))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.widget_4 = QtWidgets.QWidget(self.centralWidget)
        self.widget_4.setGeometry(QtCore.QRect(230, 10, 201, 71))
        self.widget_4.setObjectName("widget_4")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.widget_4)
        self.textBrowser_4.setGeometry(QtCore.QRect(10, 10, 101, 51))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.widget_4)
        self.textBrowser_9.setGeometry(QtCore.QRect(120, 10, 81, 21))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.widget_4)
        self.textBrowser_10.setGeometry(QtCore.QRect(120, 40, 81, 21))
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.widget_3 = QtWidgets.QWidget(self.centralWidget)
        self.widget_3.setGeometry(QtCore.QRect(440, 10, 201, 71))
        self.widget_3.setObjectName("widget_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.widget_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 10, 101, 51))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.widget_3)
        self.textBrowser_11.setGeometry(QtCore.QRect(120, 10, 81, 21))
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.widget_3)
        self.textBrowser_12.setGeometry(QtCore.QRect(120, 40, 81, 21))
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.widget_2 = QtWidgets.QWidget(self.centralWidget)
        self.widget_2.setGeometry(QtCore.QRect(650, 10, 201, 71))
        self.widget_2.setObjectName("widget_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.widget_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 10, 101, 51))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_14 = QtWidgets.QTextBrowser(self.widget_2)
        self.textBrowser_14.setGeometry(QtCore.QRect(120, 10, 81, 21))
        self.textBrowser_14.setObjectName("textBrowser_14")
        self.widget_5 = QtWidgets.QWidget(self.centralWidget)
        self.widget_5.setGeometry(QtCore.QRect(860, 10, 201, 71))
        self.widget_5.setObjectName("widget_5")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.widget_5)
        self.textBrowser_5.setGeometry(QtCore.QRect(10, 10, 101, 51))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_16 = QtWidgets.QTextBrowser(self.widget_5)
        self.textBrowser_16.setGeometry(QtCore.QRect(120, 10, 81, 21))
        self.textBrowser_16.setObjectName("textBrowser_16")
        self.textBrowser_17 = QtWidgets.QTextBrowser(self.widget_5)
        self.textBrowser_17.setGeometry(QtCore.QRect(120, 40, 81, 21))
        self.textBrowser_17.setObjectName("textBrowser_17")
        self.widget_6 = QtWidgets.QWidget(self.centralWidget)
        self.widget_6.setGeometry(QtCore.QRect(1070, 10, 201, 71))
        self.widget_6.setObjectName("widget_6")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.widget_6)
        self.textBrowser_6.setGeometry(QtCore.QRect(10, 10, 101, 51))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_18 = QtWidgets.QTextBrowser(self.widget_6)
        self.textBrowser_18.setGeometry(QtCore.QRect(120, 40, 81, 21))
        self.textBrowser_18.setObjectName("textBrowser_18")
        self.textBrowser_19 = QtWidgets.QTextBrowser(self.widget_6)
        self.textBrowser_19.setGeometry(QtCore.QRect(120, 10, 81, 21))
        self.textBrowser_19.setObjectName("textBrowser_19")
        self.textBrowser_15 = QtWidgets.QTextBrowser(self.centralWidget)
        self.textBrowser_15.setGeometry(QtCore.QRect(770, 50, 81, 21))
        self.textBrowser_15.setObjectName("textBrowser_15")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1296, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu_F = QtWidgets.QMenu(self.menuBar)
        self.menu_F.setObjectName("menu_F")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        self.menu_T = QtWidgets.QMenu(self.menuBar)
        self.menu_T.setObjectName("menu_T")
        self.menu_D = QtWidgets.QMenu(self.menuBar)
        self.menu_D.setObjectName("menu_D")
        self.menu_S = QtWidgets.QMenu(self.menuBar)
        self.menu_S.setObjectName("menu_S")
        self.menu_C = QtWidgets.QMenu(self.menuBar)
        self.menu_C.setObjectName("menu_C")
        self.menu_M = QtWidgets.QMenu(self.menuBar)
        self.menu_M.setObjectName("menu_M")
        self.menu_L = QtWidgets.QMenu(self.menuBar)
        self.menu_L.setObjectName("menu_L")
        self.menu_E = QtWidgets.QMenu(self.menuBar)
        self.menu_E.setObjectName("menu_E")
        self.menu_V = QtWidgets.QMenu(self.menuBar)
        self.menu_V.setObjectName("menu_V")
        self.menu_H = QtWidgets.QMenu(self.menuBar)
        self.menu_H.setObjectName("menu_H")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(30, 30))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_S = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/set.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_S.setIcon(icon)
        self.action_S.setObjectName("action_S")
        self.action_T = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/QT_DESIGNER_TEST/test.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/test.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_T.setIcon(icon1)
        self.action_T.setObjectName("action_T")
        self.action_H = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/stop.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/stop.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_H.setIcon(icon2)
        self.action_H.setObjectName("action_H")
        self.action_P = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/print.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_P.setIcon(icon3)
        self.action_P.setObjectName("action_P")
        self.action_Z = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/zero.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/QT_DESIGNER_TEST/zero.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_Z.setIcon(icon4)
        self.action_Z.setObjectName("action_Z")
        self.action_C = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/community.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_C.setIcon(icon5)
        self.action_C.setObjectName("action_C")
        self.action_B = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/gas.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_B.setIcon(icon6)
        self.action_B.setObjectName("action_B")
        self.action_H_2 = QtWidgets.QAction(MainWindow)
        self.action_H_2.setObjectName("action_H_2")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_S_2 = QtWidgets.QAction(MainWindow)
        self.action_S_2.setObjectName("action_S_2")
        self.action_U_Ctrl_Z = QtWidgets.QAction(MainWindow)
        self.action_U_Ctrl_Z.setObjectName("action_U_Ctrl_Z")
        self.action_T_Ctrl_X = QtWidgets.QAction(MainWindow)
        self.action_T_Ctrl_X.setObjectName("action_T_Ctrl_X")
        self.action_C_Crtl_C = QtWidgets.QAction(MainWindow)
        self.action_C_Crtl_C.setObjectName("action_C_Crtl_C")
        self.actionZhantie = QtWidgets.QAction(MainWindow)
        self.actionZhantie.setObjectName("actionZhantie")
        self.action_P_Ctrl_V = QtWidgets.QAction(MainWindow)
        self.action_P_Ctrl_V.setObjectName("action_P_Ctrl_V")
        self.action_C_2 = QtWidgets.QAction(MainWindow)
        self.action_C_2.setObjectName("action_C_2")
        self.actionEnglish_E = QtWidgets.QAction(MainWindow)
        self.actionEnglish_E.setObjectName("actionEnglish_E")
        self.action_M = QtWidgets.QAction(MainWindow)
        self.action_M.setObjectName("action_M")
        self.action_D = QtWidgets.QAction(MainWindow)
        self.action_D.setObjectName("action_D")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_D_2 = QtWidgets.QAction(MainWindow)
        self.action_D_2.setObjectName("action_D_2")
        self.action_C_3 = QtWidgets.QAction(MainWindow)
        self.action_C_3.setObjectName("action_C_3")
        self.action_C_4 = QtWidgets.QAction(MainWindow)
        self.action_C_4.setObjectName("action_C_4")
        self.action_D_3 = QtWidgets.QAction(MainWindow)
        self.action_D_3.setObjectName("action_D_3")
        self.action_S_3 = QtWidgets.QAction(MainWindow)
        self.action_S_3.setObjectName("action_S_3")
        self.action_J = QtWidgets.QAction(MainWindow)
        self.action_J.setObjectName("action_J")
        self.action_C_5 = QtWidgets.QAction(MainWindow)
        self.action_C_5.setObjectName("action_C_5")
        self.action_P_2 = QtWidgets.QAction(MainWindow)
        self.action_P_2.setObjectName("action_P_2")
        self.action_L = QtWidgets.QAction(MainWindow)
        self.action_L.setObjectName("action_L")
        self.action_M_2 = QtWidgets.QAction(MainWindow)
        self.action_M_2.setObjectName("action_M_2")
        self.action_H_3 = QtWidgets.QAction(MainWindow)
        self.action_H_3.setObjectName("action_H_3")
        self.action_P_3 = QtWidgets.QAction(MainWindow)
        self.action_P_3.setObjectName("action_P_3")
        self.action_E = QtWidgets.QAction(MainWindow)
        self.action_E.setObjectName("action_E")
        self.action_R = QtWidgets.QAction(MainWindow)
        self.action_R.setObjectName("action_R")
        self.action_S_4 = QtWidgets.QAction(MainWindow)
        self.action_S_4.setObjectName("action_S_4")
        self.action_C_6 = QtWidgets.QAction(MainWindow)
        self.action_C_6.setObjectName("action_C_6")
        self.action_P_4 = QtWidgets.QAction(MainWindow)
        self.action_P_4.setObjectName("action_P_4")
        self.actionA = QtWidgets.QAction(MainWindow)
        self.actionA.setObjectName("actionA")
        self.actionB = QtWidgets.QAction(MainWindow)
        self.actionB.setObjectName("actionB")
        self.actionC = QtWidgets.QAction(MainWindow)
        self.actionC.setObjectName("actionC")
        self.action_L_2 = QtWidgets.QAction(MainWindow)
        self.action_L_2.setObjectName("action_L_2")
        self.action_O = QtWidgets.QAction(MainWindow)
        self.action_O.setObjectName("action_O")
        self.action_M_3 = QtWidgets.QAction(MainWindow)
        self.action_M_3.setObjectName("action_M_3")
        self.action_T_2 = QtWidgets.QAction(MainWindow)
        self.action_T_2.setObjectName("action_T_2")
        self.action_R_2 = QtWidgets.QAction(MainWindow)
        self.action_R_2.setObjectName("action_R_2")
        self.action_M_4 = QtWidgets.QAction(MainWindow)
        self.action_M_4.setObjectName("action_M_4")
        self.action_O_2 = QtWidgets.QAction(MainWindow)
        self.action_O_2.setObjectName("action_O_2")
        self.action_S_5 = QtWidgets.QAction(MainWindow)
        self.action_S_5.setObjectName("action_S_5")
        self.action_X = QtWidgets.QAction(MainWindow)
        self.action_X.setObjectName("action_X")
        self.menu_F.addAction(self.action_O_2)
        self.menu_F.addAction(self.action_S_5)
        self.menu_F.addAction(self.action_X)
        self.menu.addAction(self.action_L_2)
        self.menu.addAction(self.action_O)
        self.menu.addAction(self.action_M_3)
        self.menu.addAction(self.action_R_2)
        self.menu.addAction(self.action_M_4)
        self.menu.addAction(self.action_T_2)
        self.menu_2.addAction(self.actionA)
        self.menu_2.addAction(self.actionB)
        self.menu_2.addAction(self.actionC)
        self.menu_T.addAction(self.action_P_3)
        self.menu_T.addAction(self.action_E)
        self.menu_T.addAction(self.action_R)
        self.menu_T.addAction(self.action_S_4)
        self.menu_T.addAction(self.action_C_6)
        self.menu_T.addAction(self.action_P_4)
        self.menu_D.addAction(self.action_L)
        self.menu_D.addAction(self.action_M_2)
        self.menu_D.addAction(self.action_H_3)
        self.menu_S.addAction(self.action_J)
        self.menu_S.addAction(self.action_C_5)
        self.menu_S.addAction(self.action_P_2)
        self.menu_C.addAction(self.action_C_4)
        self.menu_C.addAction(self.action_D_3)
        self.menu_C.addAction(self.action_S_3)
        self.menu_M.addAction(self.action_M)
        self.menu_M.addAction(self.action_D)
        self.menu_M.addAction(self.action_D_2)
        self.menu_M.addAction(self.action_C_3)
        self.menu_L.addAction(self.action_C_2)
        self.menu_L.addAction(self.actionEnglish_E)
        self.menu_E.addAction(self.action_U_Ctrl_Z)
        self.menu_E.addAction(self.action_T_Ctrl_X)
        self.menu_E.addAction(self.action_C_Crtl_C)
        self.menu_E.addAction(self.action_P_Ctrl_V)
        self.menu_V.addAction(self.action_S_2)
        self.menu_H.addAction(self.action_H_2)
        self.menu_H.addAction(self.action)
        self.menuBar.addAction(self.menu_F.menuAction())
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menuBar.addAction(self.menu_T.menuAction())
        self.menuBar.addAction(self.menu_D.menuAction())
        self.menuBar.addAction(self.menu_S.menuAction())
        self.menuBar.addAction(self.menu_C.menuAction())
        self.menuBar.addAction(self.menu_M.menuAction())
        self.menuBar.addAction(self.menu_L.menuAction())
        self.menuBar.addAction(self.menu_E.menuAction())
        self.menuBar.addAction(self.menu_V.menuAction())
        self.menuBar.addAction(self.menu_H.menuAction())
        self.toolBar.addAction(self.action_S)
        self.toolBar.addAction(self.action_T)
        self.toolBar.addAction(self.action_Z)
        self.toolBar.addAction(self.action_H)
        self.toolBar.addAction(self.action_P)
        self.toolBar.addAction(self.action_C)
        self.toolBar.addAction(self.action_B)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GBPI-三腔气体透过率测定仪"))
        self.pushButton.setText(_translate("MainWindow", "设置曲线"))
        self.pushButton_2.setText(_translate("MainWindow", "显示全部"))
        self.comboBox.setItemText(0, _translate("MainWindow", "压差变化"))
        self.comboBox.setItemText(1, _translate("MainWindow", "湿度变化"))
        self.comboBox.setItemText(2, _translate("MainWindow", "温差变化"))
        self.checkBox.setText(_translate("MainWindow", "自动滚动"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.A), _translate("MainWindow", "A腔"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "压差变化"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "湿度变化"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "温差变化"))
        self.pushButton_3.setText(_translate("MainWindow", "设置曲线"))
        self.pushButton_4.setText(_translate("MainWindow", "显示全部"))
        self.checkBox_2.setText(_translate("MainWindow", "自动滚动"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.B), _translate("MainWindow", "B腔"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "压差变化"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "湿度变化"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "温差变化"))
        self.pushButton_5.setText(_translate("MainWindow", "设置曲线"))
        self.pushButton_6.setText(_translate("MainWindow", "显示全部"))
        self.checkBox_3.setText(_translate("MainWindow", "自动滚动"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.C), _translate("MainWindow", "C腔"))
        self.textBrowser_7.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600;\">n</span><span style=\" font-size:7pt; font-weight:600; vertical-align:super;\">3 </span><span style=\" font-size:7pt; font-weight:600;\">/(m</span><span style=\" font-size:7pt; font-weight:600; vertical-align:super;\">2 </span><span style=\" font-size:7pt; font-weight:600;\">.24) </span></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600;\">透过量</span></p></body></html>"))
        self.textBrowser_9.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:7pt; font-weight:600;\">KPa</span></p></body></html>"))
        self.textBrowser_10.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600;\">下压</span></p></body></html>"))
        self.textBrowser_11.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri,sans-serif\'; font-size:7pt; font-weight:600;\">KPa</span></p></body></html>"))
        self.textBrowser_12.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600;\">上压</span></p></body></html>"))
        self.textBrowser_14.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600;\">cc/cm</span></p></body></html>"))
        self.textBrowser_16.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,宋体,sans-serif,Microsoft YaHei,tahoma\'; font-size:7pt; font-weight:600; color:#333333;\">℃</span></p></body></html>"))
        self.textBrowser_17.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt;\">温度一</span></p></body></html>"))
        self.textBrowser_18.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt;\">温度二</span></p></body></html>"))
        self.textBrowser_19.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial,宋体,sans-serif,Microsoft YaHei,tahoma\'; font-size:7pt; font-weight:600; color:#333333;\">℃</span></p></body></html>"))
        self.textBrowser_15.setHtml(_translate("MainWindow",
                                               "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                               "p, li { white-space: pre-wrap; }\n"
                                               "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:7pt; font-weight:600;\">透过系数</span></p></body></html>"))
        self.menu_F.setTitle(_translate("MainWindow", "文件(F)"))
        self.menu.setTitle(_translate("MainWindow", "权限和追踪"))
        self.menu_2.setTitle(_translate("MainWindow", "测试腔"))
        self.menu_T.setTitle(_translate("MainWindow", "测试(T)"))
        self.menu_D.setTitle(_translate("MainWindow", "测试模式(D)"))
        self.menu_S.setTitle(_translate("MainWindow", "设置(S)"))
        self.menu_C.setTitle(_translate("MainWindow", "通讯(C)"))
        self.menu_M.setTitle(_translate("MainWindow", "维护(M)"))
        self.menu_L.setTitle(_translate("MainWindow", "语言(L)"))
        self.menu_E.setTitle(_translate("MainWindow", "编辑(E)"))
        self.menu_V.setTitle(_translate("MainWindow", "查看(V)"))
        self.menu_H.setTitle(_translate("MainWindow", "帮助(H)"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_S.setText(_translate("MainWindow", "设置(S)"))
        self.action_S.setToolTip(_translate("MainWindow", "设置"))
        self.action_T.setText(_translate("MainWindow", "测试(T)"))
        self.action_H.setText(_translate("MainWindow", "停止测试(H)"))
        self.action_P.setText(_translate("MainWindow", "打印(P)"))
        self.action_Z.setText(_translate("MainWindow", "清零(Z)"))
        self.action_C.setText(_translate("MainWindow", "通讯(C)"))
        self.action_B.setText(_translate("MainWindow", "放气(B)"))
        self.action_H_2.setText(_translate("MainWindow", "帮助主题(H)"))
        self.action.setText(_translate("MainWindow", "关于本软件"))
        self.action_S_2.setText(_translate("MainWindow", "状态栏(S)"))
        self.action_U_Ctrl_Z.setText(_translate("MainWindow", "撤销(U)   Ctrl+Z"))
        self.action_T_Ctrl_X.setText(_translate("MainWindow", "剪切(T)   Ctrl+X"))
        self.action_C_Crtl_C.setText(_translate("MainWindow", "复制(C)   Crtl+C"))
        self.actionZhantie.setText(_translate("MainWindow", "粘贴(P)   Ctrl+V"))
        self.action_P_Ctrl_V.setText(_translate("MainWindow", "粘贴(P)   Ctrl+V"))
        self.action_C_2.setText(_translate("MainWindow", "中文(C)"))
        self.actionEnglish_E.setText(_translate("MainWindow", "English(E)"))
        self.action_M.setText(_translate("MainWindow", "系统维护(M)"))
        self.action_D.setText(_translate("MainWindow", "标定设置(D)"))
        self.action_2.setText(_translate("MainWindow", "调试窗口"))
        self.action_D_2.setText(_translate("MainWindow", "调试窗口(D)"))
        self.action_C_3.setText(_translate("MainWindow", "控制设置(C)"))
        self.action_C_4.setText(_translate("MainWindow", "连接(C)"))
        self.action_D_3.setText(_translate("MainWindow", "断开(D)"))
        self.action_S_3.setText(_translate("MainWindow", "通讯设置(S)"))
        self.action_J.setText(_translate("MainWindow", "自动判断(J)"))
        self.action_C_5.setText(_translate("MainWindow", "参数设置(C)"))
        self.action_P_2.setText(_translate("MainWindow", "保存路径(P)"))
        self.action_L.setText(_translate("MainWindow", "低阻模式(L)"))
        self.action_M_2.setText(_translate("MainWindow", "中阻模式(M)"))
        self.action_H_3.setText(_translate("MainWindow", "高阻模式(H)"))
        self.action_P_3.setText(_translate("MainWindow", "测试准备(P)"))
        self.action_E.setText(_translate("MainWindow", "结束(E)"))
        self.action_R.setText(_translate("MainWindow", "运行(R)"))
        self.action_S_4.setText(_translate("MainWindow", "复位(S)"))
        self.action_C_6.setText(_translate("MainWindow", "校正(C)"))
        self.action_P_4.setText(_translate("MainWindow", "过程设置(P)"))
        self.actionA.setText(_translate("MainWindow", "A腔"))
        self.actionB.setText(_translate("MainWindow", "B腔"))
        self.actionC.setText(_translate("MainWindow", "C腔"))
        self.action_L_2.setText(_translate("MainWindow", "登录(L)"))
        self.action_O.setText(_translate("MainWindow", "退出(O)"))
        self.action_M_3.setText(_translate("MainWindow", "修改密码(C)"))
        self.action_T_2.setText(_translate("MainWindow", "数据追踪(T)"))
        self.action_R_2.setText(_translate("MainWindow", "系统权限管理(R)"))
        self.action_M_4.setText(_translate("MainWindow", "用户管理(M)"))
        self.action_O_2.setText(_translate("MainWindow", "打开(O)"))
        self.action_S_5.setText(_translate("MainWindow", "保存(S)"))
        self.action_X.setText(_translate("MainWindow", "退出(X)"))

class MyMplCanvas(FigureCanvas):
    """这是一个窗口部件，即QWidget（当然也是FigureCanvasAgg）"""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # 每次plot()调用的时候，我们希望原来的坐标轴被清除(所以False)
        self.axes.hold(False)
        self.axes.set_xlim(-5, 12)  # 设置x轴的坐标范围并且按默认的间隔显示出来
        self.axes.set_ylim(-5, 300)
        self.axes.xaxis.grid(True, which='major')  # x坐标轴的网格使用定义的主刻度格式
        self.axes.yaxis.grid(True, which='major')  # x坐标轴的网格使用定义的主刻度格式
        # self.plt = plt

        self.compute_initial_figure()
        #
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass


class DecorationCount(object):
    def __init__(self):
        print("装饰器")
        pass

    def __call__(self, func):
        num = [0]  # 外部函数的变量不会改变
        print("装饰器__call__")
        def call_fun(*args, **kw):
            num[0] += 1
            print("函数调用了%s 次" % num[0])
            return func(*args, num[0])
        print(1)
        return call_fun


# class MyStaticMplCanvas(MyMplCanvas):
#     """静态画布：一条正弦线"""
#     def compute_initial_figure(self):
#         t = arange(0.0, 3.0, 0.01)
#         s = sin(2*pi*t)
#         self.axes.plot(t, s)


class MyDynamicMplCanvas(MyMplCanvas):
    """动态画布：每秒自动更新，更换一条折线。"""
    def __init__(self, *args, **kwargs):
        MyMplCanvas.__init__(self, *args, **kwargs)


        # self.update_figure()
        print("__init__")
        self.timer = QtCore.QTimer(self)
        self.timer.setSingleShot(False)
        self.timer.timeout.connect(self.update_figure)
        self.timer.start(1000)
        print("timer.start")

    def compute_initial_figure(self):
        self.axes.get_xaxis().get_major_formatter().set_useOffset(False)
        self.axes.set_xlim(0, 12)
        self.axes.set_ylim(0, 300)
        self.axes.xaxis.grid(True, which='major')  # x坐标轴的网格使用定义的主刻度格式
        self.axes.yaxis.grid(True, which='major')  # x坐标轴的网格使用定义的主刻度格式
        xmajorLocator = MultipleLocator(0.5)  # 将x主刻度标签设置为20的倍数
        xmajorFormatter = FormatStrFormatter('%5.1f')  # 设置x轴标签文本的格式
        ymajorLocator = MultipleLocator(10)  # 将y轴主刻度标签设置为0.5的倍数
        ymajorFormatter = FormatStrFormatter('%1.1f')  # 设置y轴标签文本的格式
        self.axes.xaxis.set_major_locator(xmajorLocator)
        self.axes.xaxis.set_major_formatter(xmajorFormatter)
        self.axes.yaxis.set_major_locator(ymajorLocator)
        self.axes.yaxis.set_major_formatter(ymajorFormatter)
        self.axes.grid(True)

    @DecorationCount()
    def update_figure(self, num):
        # 构建4个随机整数，位于闭区间[0, 10]
        # l = [random.randint(0, 3) for i in range(4)]
        # self.axes.get_xaxis().get_major_formatter().set_useOffset(True)  # 关闭间隔标注的使用
        self.num = num
        # self.compute_initial_figure()
        print(num)

        # 设置主刻度标签的位置,标签文本的格式

        # self.axes.xaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度
        # self.axes.yaxis.grid(True, which='minor')  # y坐标轴的网格使用次刻度
        # self.axes.plot(x, y, "b")  "b"代表的是线条的颜色
        # 需求：每小时温度的变化。时间t/h（0，1,2,3,4,5,6,7,8,9,10,11,12），温度T/.c(0,10,20,30,40,50,60,70,80,90,100,110,120)
        X = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        Y = [0, 20, 50, 60, 90, 150, 160, 170, 180, 190, 240, 250, 280]
        x = [X[i] for i in range(0, num) if num <= len(X)]
        y = [Y[i] for i in range(0, num) if num <= len(Y)]

        self.axes.set_xticklabels(X)
        self.axes.set_yticklabels(Y)
        self.axes.xaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度
        self.axes.yaxis.grid(True, which='minor')  # y坐标轴的网格使用次刻度
        self.axes.plot(x, y, color="r", markerfacecolor='yellow', marker='o')
        # for a, b in zip(x, y):
        #     self.plt.text(a, b, (a, b), ha='center', va='bottom', fontsize=10)

        # self.axes.set_xticklabels(X)
        # self.axes.set_yticklabels(Y)
        self.axes.set_xlim(0, 12)
        self.axes.set_ylim(0, 300)
        # 修改次刻度
        xmajorLocator = MultipleLocator(0.5)  # 将x主刻度标签设置为20的倍数
        xmajorFormatter = FormatStrFormatter('%5.1f')  # 设置x轴标签文本的格式
        ymajorLocator = MultipleLocator(10)  # 将y轴主刻度标签设置为0.5的倍数
        ymajorFormatter = FormatStrFormatter('%1.1f')  # 设置y轴标签文本的格式
        self.axes.xaxis.set_major_locator(xmajorLocator)
        self.axes.xaxis.set_major_formatter(xmajorFormatter)
        self.axes.yaxis.set_major_locator(ymajorLocator)
        self.axes.yaxis.set_major_formatter(ymajorFormatter)
        self.axes.grid(True)
        # self.axes.plot([0, 1, 2, 3], l, 'b')
        # self.plt.legend()
        # self.plt.show()
        self.draw()  # 绘画图像
        if num > 10:
            self.timer.stop()


# class ApplicationWindow(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         self.setWindowTitle("PyQt5 与 Matplotlib 例子")
#         self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
#         self.setWindowTitle("程序主窗口")
#         self.showMaximized()
#
#         self.file_menu = QMenu('&File', self)
#         self.file_menu.addAction('&Quit', self.fileQuit,
#                                  QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
#         self.menuBar().addMenu(self.file_menu)
#
#         self.help_menu = QMenu('&Help', self)
#         self.menuBar().addSeparator()
#         self.menuBar().addMenu(self.help_menu)
#         self.help_menu.addAction('&About', self.about)
#         self.main_widget = QWidget(self)
#         l = QVBoxLayout(self.main_widget)
#         # sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
#         dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
#         print("dc")
#         # l.addWidget(sc)
#         l.addWidget(dc)
#         print("dchahaha")
#         self.main_widget.setFocus()
#         self.setCentralWidget(self.main_widget)
#         # 状态条显示2秒
#         self.statusBar().showMessage("matplotlib 万岁!", 2000)
#
#     def fileQuit(self):
#         self.close()
#
#     def closeEvent(self, ce):
#         self.fileQuit()
#
#     def about(self):
#         QMessageBox.about(self, "About",
#         """embedding_in_qt5.py example
#         Copyright 2015 BoxControL
#
#         This program is a simple example of a Qt5 application embedding matplotlib
#         canvases. It is base on example from matplolib documentation, and initially was
#         developed from Florent Rougon and Darren Dale.
#
#         http://matplotlib.org/examples/user_interfaces/embedding_in_qt4.html
#
#         It may be used and modified with no restriction; raw copies as well as
#         modified versions may be distributed without limitation.
#         """
#         )

import one_rc


if __name__ == "__main__":
    # import sys
    # app = QApplication(sys.argv)
    # MainWindow = ApplicationWindow()
    # MainWindow.setWindowTitle("PyQt5 与 Matplotlib 例子")
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())

    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




