# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\pyqt5_doc\三腔气体透过率测定仪.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QWidget, QVBoxLayout, QSizePolicy, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.ticker import MultipleLocator, FormatStrFormatter


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 598)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(110, 0, 671, 501))
        self.label.setText("")
        # self.label.setPixmap(QtGui.QPixmap(":/newPrefix/line3.png"))
        # self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 802, 23))
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
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "GBPI-三腔气体透过率测定仪"))
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
        if num > 12:
            self.timer.stop()


class ApplicationWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("PyQt5 与 Matplotlib 例子")
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowTitle("程序主窗口")
        self.showMaximized()

        self.file_menu = QMenu('&File', self)
        self.file_menu.addAction('&Quit', self.fileQuit,
                                 QtCore.Qt.CTRL + QtCore.Qt.Key_Q)
        self.menuBar().addMenu(self.file_menu)

        self.help_menu = QMenu('&Help', self)
        self.menuBar().addSeparator()
        self.menuBar().addMenu(self.help_menu)
        self.help_menu.addAction('&About', self.about)
        self.main_widget = QWidget(self)
        l = QVBoxLayout(self.main_widget)
        # sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        print("dc")
        # l.addWidget(sc)
        l.addWidget(dc)
        print("dchahaha")
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)
        # 状态条显示2秒
        self.statusBar().showMessage("matplotlib 万岁!", 2000)

    def fileQuit(self):
        self.close()

    def closeEvent(self, ce):
        self.fileQuit()

    def about(self):
        QMessageBox.about(self, "About",
        """embedding_in_qt5.py example
        Copyright 2015 BoxControL

        This program is a simple example of a Qt5 application embedding matplotlib
        canvases. It is base on example from matplolib documentation, and initially was
        developed from Florent Rougon and Darren Dale.

        http://matplotlib.org/examples/user_interfaces/embedding_in_qt4.html

        It may be used and modified with no restriction; raw copies as well as
        modified versions may be distributed without limitation.
        """
        )
import one_rc

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = ApplicationWindow()
    MainWindow.setWindowTitle("PyQt5 与 Matplotlib 例子")
    ui = Ui_MainWindow()
    print("cool")
    ui.setupUi(MainWindow)
    print("hot")
    MainWindow.show()
    print("sexy")
    sys.exit(app.exec_())

