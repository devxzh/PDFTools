# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 16:26:13 2020

@author: cherish
"""

import sys,fitz
from enhance_UI import Ui_Enhance_Dialog
from enhanceFunctions import *
from PyQt5.QtWidgets import QApplication,QDialog,QFileDialog

class EnhanceForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Enhance_Dialog()
        self.ui.setupUi(self)

        self.colorValue=1.0
        self.contrastValue=2.0
        self.sharpnessValue=1.0
        self.brightnessValue=1.0
        self.saveFlag=False

        self.ui.pushButton_w2_openPDF.clicked.connect(self.w2_openPDF)

        self.ui.Slider_w2_colorSet.sliderMoved.connect(self.w2_colorValue)
        self.ui.Slider_w2_contrastSet.sliderMoved.connect(self.w2_contrastValue)
        self.ui.Slider_w2_sharpnessSet.sliderMoved.connect(self.w2_sharpnessValue)
        self.ui.Slider_w2_brightnessSet.sliderMoved.connect(self.w2_brightnessValue)
        
        self.ui.checkBox_w2_saveAllImage.stateChanged.connect(self.w2_saveOption)
        self.ui.pushButton_w2_start.clicked.connect(self.w2_start)
        self.show()
    # w2 means windows 2
    def w2_openPDF(self):
        file_name = QFileDialog.getOpenFileName(self, 
                        'Open File', 
                        "/Users/user_name/Desktop/",
                        "PDF Files (*.pdf)")
        #print(type(file_name))
        self.ui.lineEdit_w2_openPDF.setText(file_name[0])
        self.ui.label_w2_tips.setText("请设置增强因子后，按开始处理按钮\n1.0表示原始图像")
            

    def w2_colorValue(self,value):
        self.colorValue=value/10.0
        self.ui.label_w2_colorValue.setText(str(value/10.0))
        
    def w2_contrastValue(self,value):
        self.contrastValue=value/10.0
        self.ui.label_w2_contrastValue.setText(str(value/10.0))
           
    def w2_sharpnessValue(self,value):
        self.sharpnessValue=value/10.0
        self.ui.label_w2_sharpnessValue.setText(str(value/10.0))
            
    def w2_brightnessValue(self,value):
        self.brightnessValue=value/10.0
        self.ui.label_w2_brightnessValue.setText(str(value/10.0))

    def w2_saveOption(self):
        self.saveFlag=False
        if self.ui.checkBox_w2_saveAllImage.isChecked():
            self.saveFlag=True
            
    def w2_start(self):
        oldFileName=self.ui.lineEdit_w2_openPDF.text()
        newFileName=oldFileName.replace(".pdf","[enhanced].pdf")
        
        if oldFileName!='':
            doc=fitz.open(oldFileName)
            enhanceDoc=fitz.open()
            num=doc.pageCount
            baseBar=1.0/num*100

            for i in range(num):
                imgpdf=getEnhancedPdf(doc[i],i,self.saveFlag,
                [self.colorValue,self.contrastValue,self.sharpnessValue,self.brightnessValue],2)

                enhanceDoc.insertPDF(imgpdf)
                self.ui.label_w2_tips.setText("正在处理第 %d 页" % i)
                self.ui.progressBar_w2.setValue(i*baseBar)
            
            enhanceDoc.save(newFileName)
            doc.close()
            enhanceDoc.close()

            self.ui.progressBar_w2.setValue(100)
            self.ui.label_w2_tips.setText("处理完毕")
        
    
if __name__=="__main__":
    app=QApplication(sys.argv)
   
    w=EnhanceForm()
    w.show()
    sys.exit(app.exec_())  