# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\merge_UI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Merge_Dialog(object):
    def setupUi(self, Merge_Dialog):
        Merge_Dialog.setObjectName("Merge_Dialog")
        Merge_Dialog.resize(670, 405)
        Merge_Dialog.setMinimumSize(QtCore.QSize(670, 405))
        Merge_Dialog.setMaximumSize(QtCore.QSize(670, 405))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        Merge_Dialog.setFont(font)
        self.pushButton_w4_add = QtWidgets.QPushButton(Merge_Dialog)
        self.pushButton_w4_add.setGeometry(QtCore.QRect(550, 22, 100, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.pushButton_w4_add.setFont(font)
        self.pushButton_w4_add.setObjectName("pushButton_w4_add")
        self.pushButton_w4_start = QtWidgets.QPushButton(Merge_Dialog)
        self.pushButton_w4_start.setGeometry(QtCore.QRect(550, 232, 100, 100))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.pushButton_w4_start.setFont(font)
        self.pushButton_w4_start.setObjectName("pushButton_w4_start")
        self.pushButton_w4_remove = QtWidgets.QPushButton(Merge_Dialog)
        self.pushButton_w4_remove.setGeometry(QtCore.QRect(550, 74, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_w4_remove.setFont(font)
        self.pushButton_w4_remove.setObjectName("pushButton_w4_remove")
        self.pushButton_w4_up = QtWidgets.QPushButton(Merge_Dialog)
        self.pushButton_w4_up.setGeometry(QtCore.QRect(550, 126, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_w4_up.setFont(font)
        self.pushButton_w4_up.setObjectName("pushButton_w4_up")
        self.pushButton_w4_down = QtWidgets.QPushButton(Merge_Dialog)
        self.pushButton_w4_down.setGeometry(QtCore.QRect(550, 178, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_w4_down.setFont(font)
        self.pushButton_w4_down.setObjectName("pushButton_w4_down")
        self.tableWidget_w4_fileList = QtWidgets.QTableWidget(Merge_Dialog)
        self.tableWidget_w4_fileList.setGeometry(QtCore.QRect(18, 22, 520, 310))
        self.tableWidget_w4_fileList.setShowGrid(True)
        self.tableWidget_w4_fileList.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_w4_fileList.setObjectName("tableWidget_w4_fileList")
        self.tableWidget_w4_fileList.setColumnCount(2)
        self.tableWidget_w4_fileList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_w4_fileList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_w4_fileList.setHorizontalHeaderItem(1, item)
        self.progressBar_w4_bar = QtWidgets.QProgressBar(Merge_Dialog)
        self.progressBar_w4_bar.setGeometry(QtCore.QRect(18, 358, 635, 23))
        self.progressBar_w4_bar.setProperty("value", 0)
        self.progressBar_w4_bar.setObjectName("progressBar_w4_bar")

        self.retranslateUi(Merge_Dialog)
        QtCore.QMetaObject.connectSlotsByName(Merge_Dialog)

    def retranslateUi(self, Merge_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Merge_Dialog.setWindowTitle(_translate("Merge_Dialog", "合并文档"))
        self.pushButton_w4_add.setText(_translate("Merge_Dialog", "➕添加"))
        self.pushButton_w4_start.setText(_translate("Merge_Dialog", "开始"))
        self.pushButton_w4_remove.setText(_translate("Merge_Dialog", "➖移除"))
        self.pushButton_w4_up.setText(_translate("Merge_Dialog", "⬆上移"))
        self.pushButton_w4_down.setText(_translate("Merge_Dialog", "⬇下移"))
        item = self.tableWidget_w4_fileList.horizontalHeaderItem(0)
        item.setText(_translate("Merge_Dialog", "PDF 文件 ( 0 )"))
        item = self.tableWidget_w4_fileList.horizontalHeaderItem(1)
        item.setText(_translate("Merge_Dialog", "页数"))

