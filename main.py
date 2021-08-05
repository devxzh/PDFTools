import ctypes
import sys

from PyQt5.QtWidgets import QApplication, QDialog

from callAdd import AddForm
from callEnhance import EnhanceForm
from callMerge import MergeForm
from callSplit import SplitForm
from PDFTools import Ui_Dialog  # or import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_add.clicked.connect(self.add_Window)
        self.ui.pushButton_enhance.clicked.connect(self.enhance_Window)
        self.ui.pushButton_split.clicked.connect(self.split_Window)
        self.ui.pushButton_merge.clicked.connect(self.merge_Window)
        self.show()

    def add_Window(self):
        self.w1 = AddForm()
        self.w1.show()
        # self.hide()

    def enhance_Window(self):
        self.w2 = EnhanceForm()
        self.w2.show()

    def split_Window(self):
        self.w3 = SplitForm()
        self.w3.show()

    def merge_Window(self):
        self.w4 = MergeForm()
        self.w4.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # set taskbar icon
    myappid = 'mycompany.myproduct.subproduct.version'  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    w = MyForm()
    w.show()
    sys.exit(app.exec_())
