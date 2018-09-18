from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(653, 483)

        self.hxx = QtWidgets.QGraphicsView(Form)
        self.hxx.setGeometry(QtCore.QRect(-5, 1, 661, 481))
        self.hxx.setObjectName("hxx")  # 以上代码是eirc6编译窗口后自动生成的

        self.hxx.scene = QtWidgets.QGraphicsScene()  # 创建一个图片元素的对象
        item = QtWidgets.QGraphicsPixmapItem(p)  # 创建一个变量用于承载加载后的图片
        self.hxx.scene.addItem(item)  # 将加载后的图片传递给scene对象
        self.hxx.setScene(self.hxx.scene)  # 这个我也不知道是做了个啥

        self.retranslateUi(Form)  # eirc6编译窗口后自动生成
        QtCore.QMetaObject.connectSlotsByName(Form)  # eirc6编译窗口后自动生成

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()  # 以上代码是eirc6编译窗口后自动生成的
    p = QtGui.QPixmap()
    p.load("./newPrefix/line3.png")  # 加载图片
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())