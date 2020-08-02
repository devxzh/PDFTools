# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 18:45:54 2020

@author: cherish
"""

import sys
import fitz

from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QTableWidgetItem
from merge_UI import Ui_Merge_Dialog


class MergeForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Merge_Dialog()
        self.ui.setupUi(self)
        self.currentRow = 0
        self.rowCount = 0
        self.ui.pushButton_w4_add.clicked.connect(self.w4_add)
        self.ui.pushButton_w4_remove.clicked.connect(self.w4_remove)
        self.ui.pushButton_w4_down.clicked.connect(self.w4_down)
        self.ui.pushButton_w4_up.clicked.connect(self.w4_up)
        self.ui.pushButton_w4_start.clicked.connect(self.w4_start)
        self.show()

    # w4 means windows 4
    def w4_add(self):

        file_names = QFileDialog.getOpenFileNames(self,
                                                  'Add PDF',
                                                  "/Users/user_name/Desktop/",
                                                  "PDF Files (*.pdf)")
        file_names = file_names[0]
        self.rowCount = len(file_names) + self.rowCount
        self.ui.tableWidget_w4_fileList.setRowCount(self.rowCount)

        # set items

        for name in file_names:
            doc = fitz.open(name)

            page = doc.pageCount
            self.ui.tableWidget_w4_fileList.setItem(self.currentRow, 0, QTableWidgetItem(name))
            self.ui.tableWidget_w4_fileList.setItem(self.currentRow, 1, QTableWidgetItem(str(page)))

            # print(self.currentRow)
            self.currentRow = self.currentRow + 1
        # doc.close()

    def w4_remove(self):
        current_rows = self.ui.tableWidget_w4_fileList.selectedIndexes()
        # manage row
        self.currentRow = self.rowCount = self.rowCount - len(current_rows)
        for i in current_rows:
            self.ui.tableWidget_w4_fileList.removeRow(i.row())

    def w4_up(self):

        row = self.ui.tableWidget_w4_fileList.currentRow()
        if row > 0:  # base first line(row)
            current = [self.ui.tableWidget_w4_fileList.item(row, 0).text(),
                       self.ui.tableWidget_w4_fileList.item(row, 1).text()]
            last = [self.ui.tableWidget_w4_fileList.item(row - 1, 0).text(),
                    self.ui.tableWidget_w4_fileList.item(row - 1, 1).text()]
            self.ui.tableWidget_w4_fileList.setItem(row - 1, 0, QTableWidgetItem(current[0]))
            self.ui.tableWidget_w4_fileList.setItem(row - 1, 1, QTableWidgetItem(current[1]))
            self.ui.tableWidget_w4_fileList.setItem(row, 0, QTableWidgetItem(last[0]))
            self.ui.tableWidget_w4_fileList.setItem(row, 1, QTableWidgetItem(last[1]))

    def w4_down(self):
        row = self.ui.tableWidget_w4_fileList.currentRow()
        if row < self.rowCount - 1:  # base first line(row)
            current = [self.ui.tableWidget_w4_fileList.item(row, 0).text(),
                       self.ui.tableWidget_w4_fileList.item(row, 1).text()]
            nextItem = [self.ui.tableWidget_w4_fileList.item(row + 1, 0).text(),
                        self.ui.tableWidget_w4_fileList.item(row + 1, 1).text()]
            self.ui.tableWidget_w4_fileList.setItem(row + 1, 0, QTableWidgetItem(current[0]))
            self.ui.tableWidget_w4_fileList.setItem(row + 1, 1, QTableWidgetItem(current[1]))
            self.ui.tableWidget_w4_fileList.setItem(row, 0, QTableWidgetItem(nextItem[0]))
            self.ui.tableWidget_w4_fileList.setItem(row, 1, QTableWidgetItem(nextItem[1]))

    def w4_start(self):
        if self.rowCount != 0:
            doc = fitz.open(self.ui.tableWidget_w4_fileList.item(0, 0).text())
            basebar = int(1.0 / self.rowCount * 100)

            for i in range(1, self.rowCount):
                doc1 = fitz.open(self.ui.tableWidget_w4_fileList.item(i, 0).text())
                doc.insertPDF(doc1)
                self.ui.progressBar_w4_bar.setValue(i * basebar)
            self.ui.progressBar_w4_bar.setValue(100)
            doc.save("merge.pdf")
            doc.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MergeForm()
    w.show()
    sys.exit(app.exec_())
