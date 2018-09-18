from PyQt5 import QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import uidesign
import sys
from PyQt5.QtWidgets import QFileDialog
from PIL import Image
import imagefn


class mainwindow(QMainWindow,uidesign.Ui_pythonpro):
    def __init__(self, parent=None,*args,**kwargs):
        super(mainwindow, self).__init__(parent,*args,**kwargs)
        self.setupUi(self)
        self.leftbutton1()
        self.leftbutton2()
        self.leftbutton3()
        self.leftbutton4()
        self.leftbutton5()
        self.leftbutton6()
        self.leftbutton7()
        self.leftbutton8()
        self.leftbutton9()
        self.leftbutton10()
        self.leftbutton11()
        self.leftbutton12()
        self.leftbutton13()
        self.leftbutton14()
        self.leftbutton15()
        self.leftbutton16()
        self.leftbutton17()
        self.leftbutton18()
        self.leftbutton19()
        self.leftbutton20()
        self.leftbutton21()
        self.leftbutton22()
        self.leftbutton23()
        self.leftbutton24()
        self.leftbutton25()
        self.rightslider1()
        self.rightslider2()
        self.rightslider3()
        self.rightslider4()
        self.rightslider5()
        self.rightslider6()
        self.rightslider7()
        self.rightslider8()
        self.bottombutton1()
        self.bottombutton2()
        self.imgName="img/index.jpg"
        self.imgName_2="img/index.jpg"
        self.flag=0
        self.brightnessvalue=1
        self.contrastvalue=1

    def leftbutton1(self):
        pushbutton1=self.pushButton
        pushbutton1.pressed.connect(self.default_1)

    def leftbutton2(self):
        pushbutton2 = self.pushButton_2
        pushbutton2.pressed.connect(self.default_2)

    def leftbutton3(self):
        pushbutton3 = self.pushButton_3
        pushbutton3.pressed.connect(self.default_3)

    def leftbutton4(self):
        pushbutton4 = self.pushButton_4
        pushbutton4.pressed.connect(self.default_4)

    def leftbutton5(self):
        pushbutton5 = self.pushButton_5
        pushbutton5.pressed.connect(self.default_5)

    def leftbutton6(self):
        pushbutton6 = self.pushButton_6
        pushbutton6.pressed.connect(self.default_6)

    def leftbutton7(self):
        pushbutton7 = self.pushButton_7
        pushbutton7.pressed.connect(self.default_7)

    def leftbutton8(self):
        pushbutton8 = self.pushButton_8
        pushbutton8.pressed.connect(self.default_8)

    def leftbutton9(self):
        pushbutton9 = self.pushButton_9
        pushbutton9.pressed.connect(self.default_9)

    def leftbutton10(self):
        pushbutton10 = self.pushButton_10
        pushbutton10.pressed.connect(self.default_10)

    def leftbutton11(self):
        pushbutton11 = self.pushButton_11
        pushbutton11.pressed.connect(self.default_11)

    def leftbutton12(self):
        pushbutton12 = self.pushButton_12
        pushbutton12.pressed.connect(self.default_12)

    def leftbutton13(self):
        pushbutton13 = self.pushButton_13
        pushbutton13.pressed.connect(self.default_13)

    def leftbutton14(self):
        pushbutton14 = self.pushButton_14
        pushbutton14.pressed.connect(self.default_14)

    def leftbutton15(self):
        pushbutton15 = self.pushButton_15
        pushbutton15.pressed.connect(self.default_15)

    def leftbutton16(self):
        pushbutton16 = self.pushButton_16
        pushbutton16.pressed.connect(self.default_16)

    def leftbutton17(self):
        pushbutton17 = self.pushButton_17
        pushbutton17.pressed.connect(self.default_17)

    def leftbutton18(self):
        pushbutton18 = self.pushButton_18
        pushbutton18.pressed.connect(self.default_18)

    def leftbutton19(self):
        pushbutton19 = self.pushButton_19
        pushbutton19.pressed.connect(self.default_19)

    def leftbutton20(self):
        pushbutton20 = self.pushButton_20
        pushbutton20.pressed.connect(self.default_20)

    def leftbutton21(self):
        pushbutton21 = self.pushButton_21
        pushbutton21.pressed.connect(self.default_21)

    def leftbutton22(self):
        pushbutton22 = self.pushButton_22
        pushbutton22.pressed.connect(self.default_22)

    def leftbutton23(self):
        pushbutton23 = self.pushButton_23
        pushbutton23.pressed.connect(self.default_23)

    def leftbutton24(self):
        pushbutton24 = self.pushButton_24
        pushbutton24.pressed.connect(self.default_24)

    def leftbutton25(self):
        pushbutton25 = self.pushButton_25
        pushbutton25.pressed.connect(self.default_25)

    def rightslider1(self):
        rightslider1 = self.horizontalSlider
        rightslider1.valueChanged.connect(self.setlable1)
        rightslider1.valueChanged.connect(lambda x: self.brightness(rightslider1.value()))

    def rightslider2(self):
        rightslider2 = self.horizontalSlider_2
        rightslider2.valueChanged.connect(self.setlable2)
        rightslider2.valueChanged.connect(lambda x: self.contrast(rightslider2.value()))


    def rightslider3(self):
        rightslider3 = self.horizontalSlider_3
        rightslider3.valueChanged.connect(self.setlable3)
        rightslider3.valueChanged.connect(lambda x: self.color(rightslider3.value()))


    def rightslider4(self):
        rightslider4 = self.horizontalSlider_4
        rightslider4.valueChanged.connect(self.setlable4)
        rightslider4.valueChanged.connect(lambda x: self.sharpness(rightslider4.value()))

    def rightslider5(self):
        rightslider5 = self.horizontalSlider_5
        rightslider5.valueChanged.connect(self.setlable5)
        rightslider5.valueChanged.connect(lambda x: self.red(rightslider5.value()))


    def rightslider6(self):
        rightslider6 = self.horizontalSlider_6
        rightslider6.valueChanged.connect(self.setlable6)
        rightslider6.valueChanged.connect(lambda x: self.green(rightslider6.value()))

    def rightslider7(self):
        rightslider7 = self.horizontalSlider_7
        rightslider7.valueChanged.connect(self.setlable7)
        rightslider7.valueChanged.connect(lambda x: self.blue(rightslider7.value()))

    def rightslider8(self):
        rightslider8 =self.horizontalSlider_8
        rightslider8.valueChanged.connect(self.setlable8)
        rightslider8.valueChanged.connect(lambda x: self.smoothness(rightslider8.value()))


    def bottombutton1(self):
        bottombutton1=self.toolButton
        bottombutton1.pressed.connect(self.openfile)

    def bottombutton2(self):
        bottombutton2 = self.toolButton_2
        bottombutton2.pressed.connect(self.savefile)

    def setlable1(self):
        self.label_10.setText("亮度  "+str(self.horizontalSlider.value()))

    def setlable2(self):
        self.label_11.setText("对比度" + str(self.horizontalSlider_2.value()))

    def setlable3(self):
        self.label_12.setText("饱和度" + str(self.horizontalSlider_3.value()))

    def setlable4(self):
        self.label_13.setText("锐度  " + str(self.horizontalSlider_4.value()))

    def setlable5(self):
        self.label_14.setText("红光  " + str(self.horizontalSlider_5.value()))

    def setlable6(self):
        self.label_15.setText("绿光  " + str(self.horizontalSlider_6.value()))

    def setlable7(self):
        self.label_16.setText("蓝光  " + str(self.horizontalSlider_7.value()))

    def setlable8(self):
        self.label_17.setText("平滑  " + str(self.horizontalSlider_8.value()))

    def openfile(self):
        global img
        try:
            self.imgName, imgType = QFileDialog.getOpenFileName(self,
                                                       "打开图片",
                                                       "",
                                                      " *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")
        except:
            self.label_99.setText("没有选择文件")
        self.imgName_2=self.imgName
        img = Image.open(self.imgName)
        png = QtGui.QPixmap(self.imgName)
        width = png.width()
        height = png.height()
        ratio=width/height
        if(ratio>=1):
            width=1200
            height=1200/ratio
        else:
            height=970
            width=970*ratio
        png=png.scaled(width,height)
        self.label_99.setPixmap(png)

    def savefile(self):
        file_path,file_type = QFileDialog.getSaveFileName(self, "save file", "C:\\Users\\Maple\\Desktop",
                                                "*.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")
        img.save(file_path)

    def brightness(self,n):
        self.label_99.setText("正在处理请稍候...")
        imagefn.imageenhancebrightness(self.imgName,n,self.flag)
        if(self.flag==1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag=0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag=1

        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def contrast(self,n):
        self.label_99.setText("正在处理请稍候...")
        imagefn.imageenhancecontrast(self.imgName,n,self.flag)
        if(self.flag==1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag=0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag=1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def sharpness(self,n):
        self.label_99.setText("正在处理请稍候...")
        imagefn.imageenhancesharpness(self.imgName, n, self.flag)
        if(self.flag==1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag=0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag=1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def color(self,n):
        self.label_99.setText("正在处理请稍候...")
        imagefn.imageenhancecolor(self.imgName, n, self.flag)
        if(self.flag==1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag=0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag=1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def red(self,n):
        self.label_99.setText("正在处理请稍候...")
        imagefn.imageenhancered(self.imgName_2, n,self.flag)
        if(self.flag==1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.imgName_2 = "img/copy1.jpg"
            self.flag=0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.imgName_2 = "img/copy0.jpg"
            self.flag=1

        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def green(self,n):
        self.label_99.setText("正在处理请稍候...")
        imagefn.imageenhancegreen(self.imgName_2, n,self.flag)
        if(self.flag==1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.imgName_2 = "img/copy1.jpg"
            self.flag=0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.imgName_2 = "img/copy0.jpg"
            self.flag=1

        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def blue(self,n):
        self.label_99.setText("正在处理请稍候...")
        imagefn.imageenhanceblue(self.imgName_2, n,self.flag)
        if(self.flag==1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.imgName_2 = "img/copy1.jpg"
            self.flag=0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.imgName_2 = "img/copy0.jpg"
            self.flag=1

        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def smoothness(self,n):
        self.label_99.setText("正在处理请稍候...")
        imagefn.imageenhancesmoothness(self.imgName, n, self.flag)
        if (self.flag == 1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag = 0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag = 1

        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def default_1(self):
        self.label_99.setText("正在处理请稍候...")
        imagefn.default_1(self.imgName, self.flag)
        if (self.flag == 1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag = 0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag = 1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def default_2(self):
        self.label_99.setText("正在处理请稍候...")
        imagefn.default_2(self.imgName, self.flag)
        if (self.flag == 1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag = 0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag = 1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def default_3(self):
        self.label_99.setText("正在处理请稍候...")
        imagefn.default_3(self.imgName, self.flag)
        if (self.flag == 1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag = 0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag = 1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def default_4(self):
        self.label_99.setText("正在处理请稍候...")
        imagefn.default_4(self.imgName, self.flag)
        if (self.flag == 1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag = 0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag = 1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def default_5(self):
        self.label_99.setText("正在处理请稍候...")
        imagefn.default_5(self.imgName, self.flag)
        if (self.flag == 1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag = 0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag = 1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def default_6(self):
        self.label_99.setText("正在处理请稍候...")
        imagefn.default_6(self.imgName, self.flag)
        if (self.flag == 1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag = 0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag = 1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def default_7(self):
        self.label_99.setText("正在处理请稍候...")
        imagefn.default_7(self.imgName, self.flag)
        if (self.flag == 1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag = 0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag = 1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def default_8(self):
        self.label_99.setText("正在处理请稍候...")
        imagefn.default_8(self.imgName, self.flag)
        if (self.flag == 1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag = 0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag = 1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def default_9(self):
        self.label_99.setText("正在处理请稍候...")
        imagefn.default_9(self.imgName, self.flag)
        if (self.flag == 1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag = 0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag = 1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def default_10(self):
        self.label_99.setText("正在处理请稍候...")
        imagefn.default_10(self.imgName, self.flag)
        if (self.flag == 1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag = 0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag = 1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def default_11(self):
        self.label_99.setText("正在处理请稍候...")
        imagefn.default_11(self.imgName, self.flag)
        if (self.flag == 1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag = 0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag = 1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def default_12(self):
        self.label_99.setText("正在处理请稍候...")
        imagefn.default_12(self.imgName, self.flag)
        if (self.flag == 1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag = 0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag = 1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def default_13(self):
        self.label_99.setText("正在处理请稍候...")
        imagefn.default_13(self.imgName, self.flag)
        if (self.flag == 1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag = 0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag = 1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)


    def default_14(self):
        self.label_99.setText("正在处理请稍候...")
        imagefn.default_14(self.imgName, self.flag)
        if (self.flag == 1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag = 0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag = 1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def default_15(self):
        self.label_99.setText("正在处理请稍候...")
        imagefn.default_15(self.imgName, self.flag)
        if (self.flag == 1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag = 0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag = 1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def default_16(self):
        self.label_99.setText("正在处理请稍候...")
        imagefn.default_16(self.imgName, self.flag)
        if (self.flag == 1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag = 0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag = 1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def default_17(self):
        self.label_99.setText("正在处理请稍候...")
        imagefn.default_17(self.imgName, self.flag)
        if (self.flag == 1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag = 0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag = 1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def default_18(self):
        self.label_99.setText("正在处理请稍候...")
        imagefn.default_18(self.imgName, self.flag)
        if (self.flag == 1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag = 0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag = 1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def default_19(self):
        self.label_99.setText("正在处理请稍候...")
        imagefn.default_19(self.imgName, self.flag)
        if (self.flag == 1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag = 0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag = 1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)
    def default_20(self):
        self.label_99.setText("正在处理请稍候...")
        imagefn.default_22(self.imgName, self.flag)
        if (self.flag == 1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag = 0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag = 1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)
        print("hhh")

    def default_21(self):
        self.label_99.setText("正在处理请稍候...")
        imagefn.default_21(self.imgName, self.flag)
        if (self.flag == 1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag = 0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag = 1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def default_22(self):
        self.label_99.setText("正在处理请稍候...")
        imagefn.default_22(self.imgName, self.flag)
        if (self.flag == 1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag = 0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag = 1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)


    def default_23(self):
        self.label_99.setText("正在处理请稍候...")
        imagefn.default_23(self.imgName, self.flag)
        if (self.flag == 1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag = 0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag = 1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def default_24(self):
        self.label_99.setText("正在处理请稍候...")
        imagefn.default_24(self.imgName, self.flag)
        if (self.flag == 1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag = 0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag = 1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

    def default_25(self):
        self.label_99.setText("正在处理请稍候...")
        imagefn.default_25(self.imgName, self.flag)
        if (self.flag == 1):
            png = QtGui.QPixmap("img/copy1.jpg")
            self.flag = 0
        else:
            png = QtGui.QPixmap("img/copy0.jpg")
            self.flag = 1
        width = png.width()
        height = png.height()
        ratio = width / height
        if (ratio >= 1):
            width = 1200
            height = 1200 / ratio
        else:
            height = 970
            width = 970 * ratio
        png = png.scaled(width, height)
        self.label_99.setPixmap(png)

app = QApplication(sys.argv)
w = mainwindow()  #生成一个uitest类w
w.show() #显示窗口w
app.exec_()