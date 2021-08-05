# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\split_UI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Split_Dialog(object):
    def setupUi(self, Split_Dialog):
        Split_Dialog.setObjectName("Split_Dialog")
        Split_Dialog.resize(611, 331)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Split_Dialog.sizePolicy().hasHeightForWidth())
        Split_Dialog.setSizePolicy(sizePolicy)
        Split_Dialog.setMinimumSize(QtCore.QSize(611, 331))
        Split_Dialog.setMaximumSize(QtCore.QSize(611, 331))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        Split_Dialog.setFont(font)
        self.lineEdit_w3_openPDF = QtWidgets.QLineEdit(Split_Dialog)
        self.lineEdit_w3_openPDF.setGeometry(QtCore.QRect(29, 30, 460, 30))
        self.lineEdit_w3_openPDF.setObjectName("lineEdit_w3_openPDF")
        self.pushButton_w3_openPDF = QtWidgets.QPushButton(Split_Dialog)
        self.pushButton_w3_openPDF.setGeometry(QtCore.QRect(500, 30, 80, 30))
        self.pushButton_w3_openPDF.setObjectName("pushButton_w3_openPDF")
        self.groupBox_w3_mode = QtWidgets.QGroupBox(Split_Dialog)
        self.groupBox_w3_mode.setGeometry(QtCore.QRect(28, 86, 460, 140))
        self.groupBox_w3_mode.setObjectName("groupBox_w3_mode")
        self.radioButton_w3_everyPage = QtWidgets.QRadioButton(self.groupBox_w3_mode)
        self.radioButton_w3_everyPage.setGeometry(QtCore.QRect(20, 30, 153, 31))
        self.radioButton_w3_everyPage.setObjectName("radioButton_w3_everyPage")
        self.radioButton_w3_selfSet = QtWidgets.QRadioButton(self.groupBox_w3_mode)
        self.radioButton_w3_selfSet.setGeometry(QtCore.QRect(20, 68, 423, 23))
        self.radioButton_w3_selfSet.setObjectName("radioButton_w3_selfSet")
        self.spinBox_w3_page = QtWidgets.QSpinBox(self.groupBox_w3_mode)
        self.spinBox_w3_page.setGeometry(QtCore.QRect(66, 34, 51, 25))
        self.spinBox_w3_page.setObjectName("spinBox_w3_page")
        self.lineEdit_w3_pageSet = QtWidgets.QLineEdit(self.groupBox_w3_mode)
        self.lineEdit_w3_pageSet.setGeometry(QtCore.QRect(20, 100, 429, 31))
        self.lineEdit_w3_pageSet.setObjectName("lineEdit_w3_pageSet")
        self.pushButton_w3_start = QtWidgets.QPushButton(Split_Dialog)
        self.pushButton_w3_start.setGeometry(QtCore.QRect(500, 96, 80, 130))
        self.pushButton_w3_start.setObjectName("pushButton_w3_start")
        self.label_w3_tip = QtWidgets.QLabel(Split_Dialog)
        self.label_w3_tip.setGeometry(QtCore.QRect(26, 248, 549, 51))
        self.label_w3_tip.setObjectName("label_w3_tip")

        self.retranslateUi(Split_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Split_Dialog)

    def retranslateUi(self, Split_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Split_Dialog.setWindowTitle(_translate("Split_Dialog", "拆分文档"))
        self.pushButton_w3_openPDF.setText(_translate("Split_Dialog", "打开PDF"))
        self.groupBox_w3_mode.setTitle(_translate("Split_Dialog", "拆分模式"))
        self.radioButton_w3_everyPage.setText(_translate("Split_Dialog", "每                  页"))
        self.radioButton_w3_selfSet.setText(_translate("Split_Dialog", "自定义提取为单个或多个pdf文件(如 1,3,5-7,8-18,10-81)"))
        self.pushButton_w3_start.setText(_translate("Split_Dialog", "开始"))
        self.label_w3_tip.setText(_translate("Split_Dialog", "1.打开pdf文件  2.设置拆分模式  3.点击开始"))

