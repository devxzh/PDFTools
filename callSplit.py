# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 17:22:31 2020

@author: cherish
"""

import sys,fitz

from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog

from splitFunctions import *
from split_UI import Ui_Split_Dialog


class SplitForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Split_Dialog()
        self.ui.setupUi(self)
        self.splitMode = 0  # 0 = invalid, 1 is splitSame, 2 is splitCustom
        self.pathStr = ""
        self.tipStr = ""
        self.pageSame = 0
        self.pageStr = ""
        self.ui.pushButton_w3_openPDF.clicked.connect(self.w3_openPDF)
        self.ui.radioButton_w3_everyPage.toggled.connect(self.w3_splitSame)
        self.ui.radioButton_w3_selfSet.toggled.connect(self.w3_splitCustom)
        self.ui.spinBox_w3_page.editingFinished.connect(self.w3_changePageSame)
        self.ui.lineEdit_w3_pageSet.textChanged.connect(self.w3_changePageStr)
        self.ui.pushButton_w3_start.clicked.connect(self.w3_startSplit)
        self.show()

    # w3 means windows 3
    def w3_openPDF(self):
        file_name = QFileDialog.getOpenFileName(self,
                                                'Open File',
                                                "/Users/user_name/Desktop/",
                                                "PDF Files (*.pdf)")
        # print(type(file_name))
        self.ui.lineEdit_w3_openPDF.setText(file_name[0])
        self.pathStr = file_name[0]  # self.ui.lineEdit_w3_openPDF.text()

    def w3_splitSame(self):
        self.splitMode = 1
        # self.ui.spinBox_w3_page.lineEdit().setReadOnly(False)
        self.ui.spinBox_w3_page.setReadOnly(False)
        self.ui.lineEdit_w3_pageSet.setReadOnly(True)

    def w3_splitCustom(self):
        self.splitMode = 2
        self.ui.spinBox_w3_page.setReadOnly(True)
        self.ui.lineEdit_w3_pageSet.setReadOnly(False)

    def w3_changePageSame(self):
        self.pageSame = int(self.ui.spinBox_w3_page.text())

    def w3_changePageStr(self):
        self.pageStr = self.ui.lineEdit_w3_pageSet.text()
        self.ui.label_w3_tip.setText(self.pageStr)

    def w3_startSplit(self):
        if self.splitMode == 0 or self.pathStr == '':
            self.tipStr = "未添加pdf文件 或 未设置拆分模式 ! "
        elif self.splitMode == 1:
            self.tipStr = split_pdf_same_page(self.pathStr, self.pageSame)
        elif self.splitMode == 2:
            self.tipStr = split_pdf_custom_page(self.pathStr, self.pageStr)
        else:
            pass
        self.ui.label_w3_tip.setText(self.tipStr)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = SplitForm()
    w.show()
    sys.exit(app.exec_())
