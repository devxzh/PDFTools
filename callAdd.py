# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 12:15:16 2020

@author: cherish
"""

import sys
import fitz
from addFunctins import *
from add_UI import Ui_Add_Dialog
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog


class AddForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Add_Dialog()
        self.ui.setupUi(self)
        self.offsetNum = 0
        self.ui.pushButton_OpenPDF.clicked.connect(self.openPDF)
        self.ui.pushButton_OpenTXT.clicked.connect(self.openTXT)
        self.ui.spinBox_offset.valueChanged.connect(self.offsetFunc)
        self.ui.pushButton_Start.clicked.connect(self.start)
        self.ui.textEdit_progress.setText(shorthelp)
        generate_txtdemo()
        self.show()

    def tipShow(self):
        self.ui.textEdit_progress.setText(
            "PDF文件: "+self.ui.lineEdit_PDF.text()+'\n' +
            "TXT文件: "+self.ui.lineEdit_TXT.text()+'\n' +
            "页码补偿: "+str(self.offsetNum)+'\n')

    def openPDF(self):
        file_name = QFileDialog.getOpenFileName(self,
                                                'Open File',
                                                "/Users/user_name/Desktop/",
                                                "PDF Files (*.pdf)")

        self.ui.lineEdit_PDF.setText(file_name[0])
        try:
            self.doc = fitz.open(file_name[0])
            self.ui.textEdit_progress.setText("😀 PDF打开成功 !\n")
            self.tipShow()

        except:
            self.ui.textEdit_progress.setText("🙃 该PDF文件损坏或有误, 请重试!\n")
            self.ui.lineEdit_PDF.setText("")

    def openTXT(self):
        file_name = QFileDialog.getOpenFileName(self,
                                                'Open File',
                                                "/Users/user_name/Desktop/",
                                                "TXT Files (*.txt)")
        self.ui.lineEdit_TXT.setText(file_name[0])
        try:
            self.txt = open(file_name[0], encoding='UTF-8', errors='ignore')
            self.ui.textEdit_progress.setText("😀 TXT打开成功 !\n")
            self.tipShow()
        except:
            self.ui.textEdit_progress.setText("🙃 该TXT文件损坏或有误, 请重试!\n")
            self.ui.lineEdit_TXT.setText("")

    def offsetFunc(self):
        self.offsetNum = int(self.ui.spinBox_offset.text())
        self.tipShow()

    def start(self):
        if self.ui.lineEdit_PDF.text() != "" and self.ui.lineEdit_TXT.text() != "":
            self.ui.textEdit_progress.setText("可以")
            self.pdf=add2pdf(self.doc, self.txt, self.offsetNum)
            if self.pdf != None:
                newname=self.ui.lineEdit_PDF.text().replace(".pdf","-new.pdf")
                self.pdf.save(newname)
                self.ui.textEdit_progress.setText("目录添加成功")
        else:
            self.ui.textEdit_progress.setText("缺少文件")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = AddForm()
    w.show()
    sys.exit(app.exec_())
