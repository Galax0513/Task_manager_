# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task_write1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(686, 425)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 691, 381))
        self.frame.setStyleSheet("QFrame{\n"
"background: rgb(231, 249, 255);\n"
"opacity: 3;\n"
"border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 280, 221, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 10, 221, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"background: rgb(17, 195, 206);\n"
"padding: 10px, 10 px;\n"
"margin: 10 px, 20 px;\n"
"border-radius: 10px;}")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(270, 20, 371, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 70, 371, 201))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 60, 221, 41))
        self.label_2.setStyleSheet("QLabel{\n"
"background: rgb(17, 206, 202);\n"
"padding: 10px, 10 px;\n"
"margin: 10 px, 20 px;\n"
"border-radius: 10px;}")
        self.label_2.setObjectName("label_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget.setGeometry(QtCore.QRect(10, 130, 251, 181))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setStyleSheet("QCalendarWidget{\n"
"background: rgb(17, 206, 202);\n"
"border-radius: 10px;}")
        self.calendarWidget.setObjectName("calendarWidget")
        self.timeEdit = QtWidgets.QTimeEdit(self.frame)
        self.timeEdit.setGeometry(QtCore.QRect(10, 333, 271, 21))
        self.timeEdit.setObjectName("timeEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 686, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Добавить"))
        self.label.setText(_translate("MainWindow", "Название задачи"))
        self.label_2.setText(_translate("MainWindow", "Комментарии"))
