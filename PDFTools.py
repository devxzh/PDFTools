# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\PDFTools.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 350)
        Dialog.setMinimumSize(QtCore.QSize(500, 350))
        Dialog.setMaximumSize(QtCore.QSize(500, 350))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("PDF.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("")
        Dialog.setSizeGripEnabled(False)
        self.pushButton_add = QtWidgets.QPushButton(Dialog)
        self.pushButton_add.setGeometry(QtCore.QRect(70, 70, 160, 85))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_add.setFont(font)
        self.pushButton_add.setIconSize(QtCore.QSize(80, 80))
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_split = QtWidgets.QPushButton(Dialog)
        self.pushButton_split.setGeometry(QtCore.QRect(70, 200, 160, 85))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_split.setFont(font)
        self.pushButton_split.setObjectName("pushButton_split")
        self.pushButton_merge = QtWidgets.QPushButton(Dialog)
        self.pushButton_merge.setGeometry(QtCore.QRect(270, 200, 160, 85))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_merge.setFont(font)
        self.pushButton_merge.setObjectName("pushButton_merge")
        self.pushButton_enhance = QtWidgets.QPushButton(Dialog)
        self.pushButton_enhance.setGeometry(QtCore.QRect(270, 70, 160, 85))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_enhance.setFont(font)
        self.pushButton_enhance.setObjectName("pushButton_enhance")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PDF Tools"))
        self.pushButton_add.setText(_translate("Dialog", "添加目录"))
        self.pushButton_split.setText(_translate("Dialog", "拆分文档"))
        self.pushButton_merge.setText(_translate("Dialog", "合并文档"))
        self.pushButton_enhance.setText(_translate("Dialog", "文本增强"))

