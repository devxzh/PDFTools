# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\add_UI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Add_Dialog(object):
    def setupUi(self, Add_Dialog):
        Add_Dialog.setObjectName("Add_Dialog")
        Add_Dialog.resize(595, 392)
        Add_Dialog.setMinimumSize(QtCore.QSize(595, 392))
        Add_Dialog.setMaximumSize(QtCore.QSize(595, 392))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        Add_Dialog.setFont(font)
        self.lineEdit_PDF = QtWidgets.QLineEdit(Add_Dialog)
        self.lineEdit_PDF.setGeometry(QtCore.QRect(26, 22, 350, 35))
        self.lineEdit_PDF.setText("")
        self.lineEdit_PDF.setObjectName("lineEdit_PDF")
        self.lineEdit_TXT = QtWidgets.QLineEdit(Add_Dialog)
        self.lineEdit_TXT.setGeometry(QtCore.QRect(26, 70, 350, 35))
        self.lineEdit_TXT.setText("")
        self.lineEdit_TXT.setObjectName("lineEdit_TXT")
        self.pushButton_OpenPDF = QtWidgets.QPushButton(Add_Dialog)
        self.pushButton_OpenPDF.setGeometry(QtCore.QRect(394, 22, 80, 35))
        self.pushButton_OpenPDF.setObjectName("pushButton_OpenPDF")
        self.pushButton_OpenTXT = QtWidgets.QPushButton(Add_Dialog)
        self.pushButton_OpenTXT.setGeometry(QtCore.QRect(394, 70, 80, 35))
        self.pushButton_OpenTXT.setObjectName("pushButton_OpenTXT")
        self.groupBox = QtWidgets.QGroupBox(Add_Dialog)
        self.groupBox.setGeometry(QtCore.QRect(14, 114, 565, 263))
        self.groupBox.setObjectName("groupBox")
        self.textEdit_progress = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_progress.setGeometry(QtCore.QRect(12, 28, 539, 223))
        self.textEdit_progress.setObjectName("textEdit_progress")
        self.spinBox_offset = QtWidgets.QSpinBox(Add_Dialog)
        self.spinBox_offset.setGeometry(QtCore.QRect(486, 22, 80, 35))
        self.spinBox_offset.setMinimum(-100)
        self.spinBox_offset.setMaximum(100)
        self.spinBox_offset.setObjectName("spinBox_offset")
        self.pushButton_Start = QtWidgets.QPushButton(Add_Dialog)
        self.pushButton_Start.setGeometry(QtCore.QRect(486, 70, 80, 35))
        self.pushButton_Start.setObjectName("pushButton_Start")

        self.retranslateUi(Add_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Add_Dialog)

    def retranslateUi(self, Add_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Add_Dialog.setWindowTitle(_translate("Add_Dialog", "添加目录"))
        self.pushButton_OpenPDF.setText(_translate("Add_Dialog", "打开PDF"))
        self.pushButton_OpenTXT.setText(_translate("Add_Dialog", "打开目录"))
        self.groupBox.setTitle(_translate("Add_Dialog", "处理进度"))
        self.spinBox_offset.setToolTip(_translate("Add_Dialog", "页码偏差"))
        self.pushButton_Start.setText(_translate("Add_Dialog", "开始"))

