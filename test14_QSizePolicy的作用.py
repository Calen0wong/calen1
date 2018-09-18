#! /usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QLabel, QSizePolicy, QVBoxLayout, QWidget


class PolicyWindow(QWidget):

    def __init__(self):
        super(PolicyWindow, self).__init__()

        self.setMinimumSize(400, 300)

        vbox = QVBoxLayout()
        top_label = QLabel("Top")
        top_label.setStyleSheet("background-color:rgb(191,146,63);")
        top_label.setSizePolicy(QSizePolicy.Expanding,
                                QSizePolicy.Expanding)

        bottom_label = QLabel("Bottom")
        bottom_label.setStyleSheet("background-color:rgb(205,157,214);")
        bottom_label.setMinimumSize(0, 100)

        vbox.addWidget(top_label)
        vbox.addWidget(bottom_label)

        self.setLayout(vbox)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    win = PolicyWindow()
    win.show()
    sys.exit(app.exec_())