"""
=======================================================================================
    ImageEnhance.Color(image)      色彩平衡。 0-黑白,1-原图(可为小数,可 > 1)
    ImageEnhance.Contrast(image)   对比度。   0-灰色图像,1-原图
    ImageEnhance.Brightness(image) 亮度。     0.0-黑色图像,1-原图
    ImageEnhacne.Sharpness(image)  清晰度(锐化)。0.0是模糊图像,1.0是原始图像,2.0是锐化图像
=======================================================================================
    上述类的增强方法都为 enhance(factor), 显示用show(),见下例子
=======================================================================================
    from PIL import Image,ImageEnhance

    img=Image.open("name.png")
    # 下面的 Contrast 可换为 Color, Brightness, Sharpness 之一, 其他不变
    enhanceImg=ImageEnhance.Contrast(img)
    newImage=enhanceImg.enhance(2)
    newImage.show()
    newImage.save("new.png")
=======================================================================================
"""

import os,fitz
from PIL import Image, ImageEnhance


def setZoom(zoom_xy):# 设置为 2
    rotate = int(0)  # 设置图片的旋转角度
    zoom_x = zoom_xy  # 设置图片相对于PDF文件在X轴上的缩放比例
    zoom_y = zoom_xy  # 设置图片相对于PDF文件在Y轴上的缩放比例
    trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
    return trans

def getEnhancedPdf(docPage,index,saveFlag=False,factor=[1.0,1.0,1.0,1.0],zoom_xy=2):
    """
    获取图像，并增加对比度
    :param : docPage: doc[i]
    :param :factor : color, contrast, sharpness, brightness
    :param :zoom_xy : enlargement factor
    :return : a page of enhanced pdf 
    """
    pix=docPage.getPixmap(matrix=setZoom(zoom_xy),alpha=False)
    img=Image.frombytes("RGB",[pix.width,pix.height],pix.samples)
    
    enhanceTemp1= ImageEnhance.Color(img)
    pilImg1 = enhanceTemp1.enhance(factor[0]) # PIL img

    enhanceTemp2= ImageEnhance.Contrast(pilImg1)
    pilImg2 = enhanceTemp2.enhance(factor[1]) # PIL img

    enhanceTemp3= ImageEnhance.Sharpness(pilImg2)
    pilImg3 = enhanceTemp3.enhance(factor[2]) # PIL img

    enhanceTemp4= ImageEnhance.Brightness(pilImg3)
    pilImg4 = enhanceTemp4.enhance(factor[3]) # PIL img
        
    #pilImg.show()
    folder=os.getcwd()+'/split' # 创建文件夹
    if not os.path.exists(folder):
        os.makedirs(folder)
    imgName= folder + "/splitImage("+"%04d" % index +").png"
    pilImg4.save(imgName)
    fitImg=fitz.open(imgName)
    if saveFlag==False:
        os.remove(imgName)
    pdfBytes=fitImg.convertToPDF()
    imgpdf=fitz.open("pdf",pdfBytes)
    return imgpdf








