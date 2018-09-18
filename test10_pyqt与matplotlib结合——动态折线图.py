import sys
import random
import time
import numpy as np
import matplotlib
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.pyplot as plt
matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QSizePolicy, QMessageBox, QWidget, \
    QGraphicsScene
# QSizePolicy主要是控制控件是在Layout中遇到窗体尺寸改变时控件本身该如何适应新的尺寸
from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MyMplCanvas(FigureCanvas):
    """这是一个窗口部件，即QWidget（当然也是FigureCanvasAgg）"""
    def __init__(self, parent=None, width=1, height=1, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # 每次plot()调用的时候，我们希望原来的坐标轴被清除(所以False)
        self.axes.hold(False)
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
        pass

    def __call__(self, func):
        num = [0]  # 外部函数的变量不会改变

        def call_fun(*args, **kw):
            num[0] += 1
            print("函数调用了%s 次" % num[0])
            return func(*args, num[0])
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
        self.num = num
        print(num)

        # 设置主刻度标签的位置,标签文本的格式
        #  需求：每小时温度的变化。时间t/h（0，1,2,3,4,5,6,7,8,9,10,11,12），温度T/.c(0,10,20,30,40,50,60,70,80,90,100,110,120)
        X = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        Y = [0, 20, 50, 60, 90, 150, 160, 170, 180, 190, 240, 250, 280]
        x = [X[i] for i in range(0, num) if num <= len(X)]
        y = [Y[i] for i in range(0, num) if num <= len(Y)]

        self.axes.set_xticklabels(X)
        self.axes.set_yticklabels(Y)
        self.axes.xaxis.grid(True, which='major')  # x坐标轴的网格使用主刻度
        self.axes.yaxis.grid(True, which='minor')  # y坐标轴的网格使用次刻度
        self.axes.plot(x, y, color="r", markerfacecolor='yellow', marker='o')
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
        self.draw()  # 绘画图像
        if num > 12:
            self.timer.stop()


class ApplicationWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
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

        # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        self.main_widget = QWidget(self)
        vbox = QVBoxLayout(self.main_widget)
        # sc = MyStaticMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        dc = MyDynamicMplCanvas(self.main_widget, width=5, height=4, dpi=100)
        # l.addWidget(sc)
        vbox.addWidget(dc)
        self.main_widget.setFocus()
        self.setCentralWidget(self.main_widget)
        # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    aw = ApplicationWindow()
    aw.setWindowTitle("PyQt5 与 Matplotlib 例子")
    aw.show()
    #sys.exit(qApp.exec_())
    app.exec_()