# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pythonpro.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import os

def hprint():
        print("你好啊")
class Ui_pythonpro(object):
    def setupUi(self, pythonpro):
        pythonpro.setObjectName("pythonpro")
        pythonpro.resize(1920, 990)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(pythonpro.sizePolicy().hasHeightForWidth())
        pythonpro.setSizePolicy(sizePolicy)
        pythonpro.setMaximumSize(QtCore.QSize(1920, 1010))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        pythonpro.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pythonpro.setWindowIcon(icon)
        pythonpro.setStyleSheet("background-color:#000000;\n"
"border-radius:8px;\n"
"")
        self.listWidget = QtWidgets.QListWidget(pythonpro)
        self.listWidget.setGeometry(QtCore.QRect(15, 15, 330, 965))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setKerning(True)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background-color:rgb(210,210,210);\n"
"border-radius:8px;\n"
"")
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(pythonpro)
        self.listWidget_2.setGeometry(QtCore.QRect(1575, 10, 330, 970))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setKerning(True)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setStyleSheet("background-color:rgb(210,210,210);\n"
"border-radius:8px;\n"
"")
        self.listWidget_2.setObjectName("listWidget_2")
        self.label_99 = QtWidgets.QLabel(pythonpro)
        self.label_99.setGeometry(QtCore.QRect(360, 10, 1200, 970))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_99.setFont(font)
        png = QtGui.QPixmap("img/index.jpg")
        self.label_99.setPixmap(png)
        self.label_99.setStyleSheet("background-color:#d2d2d2;\n"
                                    "text-align:center;\n"
                                    "font-size:20px;\n"
                                    "border-radius:0px\n"
                                    )
        self.label_99.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.label_99.setObjectName("label_99")
        self.label = QtWidgets.QLabel(pythonpro)
        self.label.setGeometry(QtCore.QRect(15, 10, 330, 40))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:#999999;\n"
"text-align:center;\n"
"font-size:20px;\n"
"border-radius:8px 8px 0px 0px;" )
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(pythonpro)
        self.pushButton.setGeometry(QtCore.QRect(15, 90, 330, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setKerning(True)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("border-radius:0px;\n"
"background-color:rgb(210,210,210);\n"
"border-top:1.2px solid #222222;\n"
"border-bottom:1.2px solid #222222;\n"
"color:#353535;\n" )
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/Brightness & Text Size.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(pythonpro)
        self.label_2.setGeometry(QtCore.QRect(15, 55, 330, 35))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color:#999999;\n"
"text-align:center;\n"
"font-size:20px;\n"
"border-radius:0px\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_2.setGeometry(QtCore.QRect(15, 120, 330, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setKerning(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("border-radius:0px;\n"
"background-color:rgb(210,210,210);\n"
"border-top:1.2px solid #222222;\n"
"border-bottom:1.2px solid #222222;\n"
"color:#353535;")
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_3.setGeometry(QtCore.QRect(15, 150, 330, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setKerning(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("border-radius:0px;\n"
"background-color:rgb(210,210,210);\n"
"border-top:1.2px solid #222222;\n"
"border-bottom:1.2px solid #222222;\n"
"color:#353535;")
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_4.setGeometry(QtCore.QRect(15, 180, 330, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setKerning(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("border-radius:0px;\n"
"background-color:rgb(210,210,210);\n"
"border-top:1.2px solid #222222;\n"
"border-bottom:1.2px solid #222222;\n"
"color:#353535;")
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_5.setGeometry(QtCore.QRect(15, 210, 330, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setKerning(True)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("border-radius:0px;\n"
"background-color:rgb(210,210,210);\n"
"border-top:1.2px solid #222222;\n"
"border-bottom:1.2px solid #222222;\n"
"color:#353535;")
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_6.setGeometry(QtCore.QRect(15, 275, 330, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setKerning(True)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("border-radius:0px;\n"
"background-color:rgb(210,210,210);\n"
"border-top:1.2px solid #222222;\n"
"border-bottom:1.2px solid #222222;\n"
"color:#353535;")
        self.pushButton_6.setIcon(icon1)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_7.setGeometry(QtCore.QRect(15, 305, 330, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setKerning(True)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("border-radius:0px;\n"
"background-color:rgb(210,210,210);\n"
"border-top:1.2px solid #222222;\n"
"border-bottom:1.2px solid #222222;\n"
"color:#353535;")
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_8.setGeometry(QtCore.QRect(15, 335, 330, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setKerning(True)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("border-radius:0px;\n"
"background-color:rgb(210,210,210);\n"
"border-top:1.2px solid #222222;\n"
"border-bottom:1.2px solid #222222;\n"
"color:#353535;")
        self.pushButton_8.setIcon(icon1)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_9.setGeometry(QtCore.QRect(15, 365, 330, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setKerning(True)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setMouseTracking(True)
        self.pushButton_9.setTabletTracking(True)
        self.pushButton_9.setStyleSheet("border-radius:0px;\n"
"background-color:rgb(210,210,210);\n"
"border-top:1.2px solid #222222;\n"
"border-bottom:1.2px solid #222222;\n"
"color:#353535;")
        self.pushButton_9.setIcon(icon1)
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_3 = QtWidgets.QLabel(pythonpro)
        self.label_3.setGeometry(QtCore.QRect(15, 240, 330, 35))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color:#999999;\n"
"text-align:center;\n"
"font-size:20px;\n"
"border-radius:0px\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton_10 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_10.setGeometry(QtCore.QRect(15, 395, 330, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setKerning(True)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setMouseTracking(True)
        self.pushButton_10.setTabletTracking(True)
        self.pushButton_10.setStyleSheet("border-radius:0px;\n"
"background-color:rgb(210,210,210);\n"
"border-top:1.2px solid #222222;\n"
"border-bottom:1.2px solid #222222;\n"
"color:#353535;")
        self.pushButton_10.setIcon(icon1)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_11.setGeometry(QtCore.QRect(15, 675, 330, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setKerning(True)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("border-radius:0px;\n"
"background-color:rgb(210,210,210);\n"
"border-top:1.2px solid #222222;\n"
"border-bottom:1.2px solid #222222;\n"
"color:#353535;")
        self.pushButton_11.setIcon(icon1)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_12.setGeometry(QtCore.QRect(15, 645, 330, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setKerning(True)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet("border-radius:0px;\n"
"background-color:rgb(210,210,210);\n"
"border-top:1.2px solid #222222;\n"
"border-bottom:1.2px solid #222222;\n"
"color:#353535;")
        self.pushButton_12.setIcon(icon1)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_13.setGeometry(QtCore.QRect(15, 460, 330, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setKerning(True)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet("border-radius:0px;\n"
"background-color:rgb(210,210,210);\n"
"border-top:1.2px solid #222222;\n"
"border-bottom:1.2px solid #222222;\n"
"color:#353535;")
        self.pushButton_13.setIcon(icon1)
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_14.setGeometry(QtCore.QRect(15, 550, 330, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setKerning(True)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_14.setStyleSheet("border-radius:0px;\n"
"background-color:rgb(210,210,210);\n"
"border-top:1.2px solid #222222;\n"
"border-bottom:1.2px solid #222222;\n"
"color:#353535;")
        self.pushButton_14.setIcon(icon1)
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_4 = QtWidgets.QLabel(pythonpro)
        self.label_4.setGeometry(QtCore.QRect(15, 610, 330, 35))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color:#999999;\n"
"text-align:center;\n"
"font-size:20px;\n"
"border-radius:0px\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton_15 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_15.setGeometry(QtCore.QRect(15, 520, 330, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setKerning(True)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_15.setStyleSheet("border-radius:0px;\n"
"background-color:rgb(210,210,210);\n"
"border-top:1.2px solid #222222;\n"
"border-bottom:1.2px solid #222222;\n"
"color:#353535;")
        self.pushButton_15.setIcon(icon1)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_16.setGeometry(QtCore.QRect(15, 735, 330, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setKerning(True)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_16.setMouseTracking(True)
        self.pushButton_16.setTabletTracking(True)
        self.pushButton_16.setStyleSheet("border-radius:0px;\n"
"background-color:rgb(210,210,210);\n"
"border-top:1.2px solid #222222;\n"
"border-bottom:1.2px solid #222222;\n"
"color:#353535;")
        self.pushButton_16.setIcon(icon1)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_17.setGeometry(QtCore.QRect(15, 765, 330, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setKerning(True)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_17.setMouseTracking(True)
        self.pushButton_17.setTabletTracking(True)
        self.pushButton_17.setStyleSheet("border-radius:0px;\n"
"background-color:rgb(210,210,210);\n"
"border-top:1.2px solid #222222;\n"
"border-bottom:1.2px solid #222222;\n"
"color:#353535;")
        self.pushButton_17.setIcon(icon1)
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_18.setGeometry(QtCore.QRect(15, 490, 330, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setKerning(True)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_18.setStyleSheet("border-radius:0px;\n"
"background-color:rgb(210,210,210);\n"
"border-top:1.2px solid #222222;\n"
"border-bottom:1.2px solid #222222;\n"
"color:#353535;")
        self.pushButton_18.setIcon(icon1)
        self.pushButton_18.setObjectName("pushButton_18")
        self.label_5 = QtWidgets.QLabel(pythonpro)
        self.label_5.setGeometry(QtCore.QRect(15, 425, 330, 35))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color:#999999;\n"
"text-align:center;\n"
"font-size:20px;\n"
"border-radius:0px\n"
"")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.pushButton_19 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_19.setGeometry(QtCore.QRect(15, 705, 330, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setKerning(True)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_19.setStyleSheet("border-radius:0px;\n"
"background-color:rgb(210,210,210);\n"
"border-top:1.2px solid #222222;\n"
"border-bottom:1.2px solid #222222;\n"
"color:#353535;")
        self.pushButton_19.setIcon(icon1)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_20.setGeometry(QtCore.QRect(15, 580, 330, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setKerning(True)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_20.setStyleSheet("border-radius:0px;\n"
"background-color:rgb(210,210,210);\n"
"border-top:1.2px solid #222222;\n"
"border-bottom:1.2px solid #222222;\n"
"color:#353535;")
        self.pushButton_20.setIcon(icon1)
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_21.setGeometry(QtCore.QRect(15, 890, 330, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setKerning(True)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_21.setStyleSheet("border-radius:0px;\n"
"background-color:rgb(210,210,210);\n"
"border-top:1.2px solid #222222;\n"
"border-bottom:1.2px solid #222222;\n"
"color:#353535;")
        self.pushButton_21.setIcon(icon1)
        self.pushButton_21.setObjectName("pushButton_21")
        self.label_6 = QtWidgets.QLabel(pythonpro)
        self.label_6.setGeometry(QtCore.QRect(15, 795, 330, 35))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color:#999999;\n"
"text-align:center;\n"
"font-size:20px;\n"
"border-radius:0px\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.pushButton_22 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_22.setGeometry(QtCore.QRect(15, 920, 330, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setKerning(True)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_22.setMouseTracking(True)
        self.pushButton_22.setTabletTracking(True)
        self.pushButton_22.setStyleSheet("border-radius:0px;\n"
"background-color:rgb(210,210,210);\n"
"border-top:1.2px solid #222222;\n"
"border-bottom:1.2px solid #222222;\n"
"color:#353535;")
        self.pushButton_22.setIcon(icon1)
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_23.setGeometry(QtCore.QRect(15, 950, 330, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setKerning(True)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_23.setMouseTracking(True)
        self.pushButton_23.setTabletTracking(True)
        self.pushButton_23.setStyleSheet("border-radius:0px;\n"
"background-color:rgb(210,210,210);\n"
"border-top:1.2px solid #222222;\n"
"border-bottom:1.2px solid #222222;\n"
"color:#353535;")
        self.pushButton_23.setIcon(icon1)
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_24.setGeometry(QtCore.QRect(15, 830, 330, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setKerning(True)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_24.setStyleSheet("border-radius:0px;\n"
"background-color:rgb(210,210,210);\n"
"border-top:1.2px solid #222222;\n"
"border-bottom:1.2px solid #222222;\n"
"color:#353535;")
        self.pushButton_24.setIcon(icon1)
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_25.setGeometry(QtCore.QRect(15, 860, 330, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setKerning(True)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_25.setStyleSheet("border-radius:0px;\n"
"background-color:rgb(210,210,210);\n"
"border-top:1.2px solid #222222;\n"
"border-bottom:1.2px solid #222222;\n"
"color:#353535;")
        self.pushButton_25.setIcon(icon1)
        self.pushButton_25.setObjectName("pushButton_25")
        self.label_7 = QtWidgets.QLabel(pythonpro)
        self.label_7.setGeometry(QtCore.QRect(1575, 10, 330, 191))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color:#999999;\n"
"text-align:center;\n"
"font-size:20px;\n"
"border-radius:8px 8px 0px 0px;")
        self.label_7.setText("")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.pushButton_26 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_26.setGeometry(QtCore.QRect(1590, 77, 70, 70))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_26.setFont(font)
        self.pushButton_26.setStyleSheet("background-color:#999999\n"
"")
        self.pushButton_26.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_26.setIcon(icon2)
        self.pushButton_26.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_26.setObjectName("pushButton_26")
        self.label_8 = QtWidgets.QLabel(pythonpro)
        self.label_8.setGeometry(QtCore.QRect(1670, 80, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_8.setFont(font)
        self.label_8.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.label_8.setAcceptDrops(True)
        self.label_8.setStyleSheet("background-color:#999999;\n"
"text-align:center;\n"
"font-size:13px;\n"
"border-radius:8px 8px 0px 0px;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(pythonpro)
        self.label_9.setGeometry(QtCore.QRect(1680, 110, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color:#999999;\n"
"text-align:center;\n"
"font-size:13px;\n"
"border-radius:8px 8px 0px 0px;")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.pushButton_27 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_27.setGeometry(QtCore.QRect(1590, 225, 50, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_27.setFont(font)
        self.pushButton_27.setStyleSheet("background-color:#d2d2d2;")
        self.pushButton_27.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/brightness_L.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_27.setIcon(icon3)
        self.pushButton_27.setIconSize(QtCore.QSize(40, 38))
        self.pushButton_27.setObjectName("pushButton_27")
        self.label_10 = QtWidgets.QLabel(pythonpro)
        self.label_10.setGeometry(QtCore.QRect(1645, 225, 91, 50))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color:#d4d4d4;\n"
"text-align:center;\n"
"font-size:20px;\n"
"border-radius:8px 8px 0px 0px;")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalSlider = QtWidgets.QSlider(pythonpro)
        self.horizontalSlider.setGeometry(QtCore.QRect(1645, 275, 231, 8))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.horizontalSlider.setFont(font)
        self.horizontalSlider.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.horizontalSlider.setStyleSheet("background-color:#d2d2d2;")
        self.horizontalSlider.setMinimum(-99)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.label_11 = QtWidgets.QLabel(pythonpro)
        self.label_11.setGeometry(QtCore.QRect(1645, 305, 91, 50))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color:#d4d4d4;\n"
"text-align:center;\n"
"font-size:20px;\n"
"border-radius:8px 8px 0px 0px;")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalSlider_2 = QtWidgets.QSlider(pythonpro)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(1645, 355, 231, 8))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.horizontalSlider_2.setFont(font)
        self.horizontalSlider_2.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.horizontalSlider_2.setStyleSheet("background-color:#d2d2d2;")
        self.horizontalSlider_2.setMinimum(-99)
        self.horizontalSlider_2.setPageStep(1)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.pushButton_28 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_28.setGeometry(QtCore.QRect(1590, 305, 50, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_28.setFont(font)
        self.pushButton_28.setStyleSheet("background-color:#d2d2d2;")
        self.pushButton_28.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/contrast.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_28.setIcon(icon4)
        self.pushButton_28.setIconSize(QtCore.QSize(40, 38))
        self.pushButton_28.setObjectName("pushButton_28")
        self.label_12 = QtWidgets.QLabel(pythonpro)
        self.label_12.setGeometry(QtCore.QRect(1645, 385, 91, 50))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color:#d4d4d4;\n"
"text-align:center;\n"
"font-size:20px;\n"
"border-radius:8px 8px 0px 0px;")
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalSlider_3 = QtWidgets.QSlider(pythonpro)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(1645, 435, 231, 8))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.horizontalSlider_3.setFont(font)
        self.horizontalSlider_3.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.horizontalSlider_3.setStyleSheet("background-color:#d2d2d2;")
        self.horizontalSlider_3.setMinimum(-99)
        self.horizontalSlider_3.setPageStep(1)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.pushButton_29 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_29.setGeometry(QtCore.QRect(1590, 385, 50, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_29.setFont(font)
        self.pushButton_29.setStyleSheet("background-color:#d2d2d2;")
        self.pushButton_29.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/tonality.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_29.setIcon(icon5)
        self.pushButton_29.setIconSize(QtCore.QSize(44, 40))
        self.pushButton_29.setObjectName("pushButton_29")
        self.label_13 = QtWidgets.QLabel(pythonpro)
        self.label_13.setGeometry(QtCore.QRect(1645, 465, 91, 50))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color:#d4d4d4;\n"
"text-align:center;\n"
"font-size:20px;\n"
"border-radius:8px 8px 0px 0px;")
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalSlider_4 = QtWidgets.QSlider(pythonpro)
        self.horizontalSlider_4.setGeometry(QtCore.QRect(1645, 515, 231, 8))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.horizontalSlider_4.setFont(font)
        self.horizontalSlider_4.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.horizontalSlider_4.setStyleSheet("background-color:#d2d2d2;")
        self.horizontalSlider_4.setMinimum(-99)
        self.horizontalSlider_4.setPageStep(1)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.pushButton_30 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_30.setGeometry(QtCore.QRect(1590, 465, 50, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_30.setFont(font)
        self.pushButton_30.setStyleSheet("background-color:#d2d2d2;")
        self.pushButton_30.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("img/锐度.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_30.setIcon(icon6)
        self.pushButton_30.setIconSize(QtCore.QSize(32, 40))
        self.pushButton_30.setObjectName("pushButton_30")
        self.label_14 = QtWidgets.QLabel(pythonpro)
        self.label_14.setGeometry(QtCore.QRect(1645, 545, 91, 50))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color:#d4d4d4;\n"
"text-align:center;\n"
"font-size:20px;\n"
"border-radius:8px 8px 0px 0px;")
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalSlider_5 = QtWidgets.QSlider(pythonpro)
        self.horizontalSlider_5.setGeometry(QtCore.QRect(1645, 595, 231, 8))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.horizontalSlider_5.setFont(font)
        self.horizontalSlider_5.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.horizontalSlider_5.setStyleSheet("background-color:#d2d2d2;")
        self.horizontalSlider_5.setMinimum(-99)
        self.horizontalSlider_5.setPageStep(1)
        self.horizontalSlider_5.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_5.setObjectName("horizontalSlider_5")
        self.pushButton_31 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_31.setGeometry(QtCore.QRect(1590, 545, 50, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_31.setFont(font)
        self.pushButton_31.setStyleSheet("background-color:#d2d2d2;")
        self.pushButton_31.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("img/高光.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_31.setIcon(icon7)
        self.pushButton_31.setIconSize(QtCore.QSize(34, 40))
        self.pushButton_31.setObjectName("pushButton_31")
        self.label_15 = QtWidgets.QLabel(pythonpro)
        self.label_15.setGeometry(QtCore.QRect(1645, 625, 91, 50))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color:#d4d4d4;\n"
"text-align:center;\n"
"font-size:20px;\n"
"border-radius:8px 8px 0px 0px;")
        self.label_15.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalSlider_6 = QtWidgets.QSlider(pythonpro)
        self.horizontalSlider_6.setGeometry(QtCore.QRect(1645, 675, 231, 8))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.horizontalSlider_6.setFont(font)
        self.horizontalSlider_6.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.horizontalSlider_6.setStyleSheet("background-color:#d2d2d2;")
        self.horizontalSlider_6.setMinimum(-99)
        self.horizontalSlider_6.setPageStep(1)
        self.horizontalSlider_6.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_6.setObjectName("horizontalSlider_6")
        self.pushButton_32 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_32.setGeometry(QtCore.QRect(1590, 625, 50, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_32.setFont(font)
        self.pushButton_32.setStyleSheet("background-color:#d2d2d2;")
        self.pushButton_32.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("img/ShadowControl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_32.setIcon(icon8)
        self.pushButton_32.setIconSize(QtCore.QSize(34, 40))
        self.pushButton_32.setObjectName("pushButton_32")
        self.label_16 = QtWidgets.QLabel(pythonpro)
        self.label_16.setGeometry(QtCore.QRect(1645, 705, 91, 50))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color:#d4d4d4;\n"
"text-align:center;\n"
"font-size:20px;\n"
"border-radius:8px 8px 0px 0px;")
        self.label_16.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalSlider_7 = QtWidgets.QSlider(pythonpro)
        self.horizontalSlider_7.setGeometry(QtCore.QRect(1645, 755, 231, 8))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.horizontalSlider_7.setFont(font)
        self.horizontalSlider_7.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.horizontalSlider_7.setStyleSheet("background-color:#d2d2d2;")
        self.horizontalSlider_7.setMinimum(-99)
        self.horizontalSlider_7.setPageStep(1)
        self.horizontalSlider_7.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_7.setObjectName("horizontalSlider_7")
        self.pushButton_33 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_33.setGeometry(QtCore.QRect(1590, 705, 50, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_33.setFont(font)
        self.pushButton_33.setStyleSheet("background-color:#d2d2d2;")
        self.pushButton_33.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("img/色温.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_33.setIcon(icon9)
        self.pushButton_33.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_33.setObjectName("pushButton_33")
        self.label_17 = QtWidgets.QLabel(pythonpro)
        self.label_17.setGeometry(QtCore.QRect(1645, 785, 91, 50))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background-color:#d4d4d4;\n"
"text-align:center;\n"
"font-size:20px;\n"
"border-radius:8px 8px 0px 0px;")
        self.label_17.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalSlider_8 = QtWidgets.QSlider(pythonpro)
        self.horizontalSlider_8.setGeometry(QtCore.QRect(1645, 835, 231, 8))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.horizontalSlider_8.setFont(font)
        self.horizontalSlider_8.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.horizontalSlider_8.setStyleSheet("background-color:#d2d2d2;")
        self.horizontalSlider_8.setMinimum(-99)
        self.horizontalSlider_8.setPageStep(1)
        self.horizontalSlider_8.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_8.setObjectName("horizontalSlider_8")
        self.pushButton_34 = QtWidgets.QPushButton(pythonpro)
        self.pushButton_34.setGeometry(QtCore.QRect(1590, 785, 50, 50))
        font = QtGui.QFont()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton_34.setFont(font)
        self.pushButton_34.setStyleSheet("background-color:#d2d2d2;")
        self.pushButton_34.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("img/平滑工具.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_34.setIcon(icon10)
        self.pushButton_34.setIconSize(QtCore.QSize(30, 40))
        self.pushButton_34.setObjectName("pushButton_34")
        self.toolButton = QtWidgets.QToolButton(pythonpro)
        self.toolButton.setGeometry(QtCore.QRect(1610, 900, 110, 35))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.toolButton.setFont(font)
        self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton.setStyleSheet("background-color:#999999;\n"
"font-size:18px;")
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(pythonpro)
        self.toolButton_2.setGeometry(QtCore.QRect(1760, 900, 110, 35))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton_2.setStyleSheet("background-color:#999999;\n"
"font-size:18px;")
        self.toolButton_2.setObjectName("toolButton_2")

        self.retranslateUi(pythonpro)
        QtCore.QMetaObject.connectSlotsByName(pythonpro)
    def retranslateUi(self, pythonpro):
        _translate = QtCore.QCoreApplication.translate
        pythonpro.setWindowTitle(_translate("pythonpro", "PS-PythonShop"))
        self.label.setText(_translate("pythonpro", "滤镜"))
        self.pushButton.setText(_translate("pythonpro", "ins        "))
        self.label_2.setText(_translate("pythonpro", " ▼胶片"))
        self.pushButton_2.setText(_translate("pythonpro", "浅白      "))
        self.pushButton_3.setText(_translate("pythonpro", "日系      "))
        self.pushButton_4.setText(_translate("pythonpro", "西柚      "))
        self.pushButton_5.setText(_translate("pythonpro", "小森林   "))
        self.pushButton_6.setText(_translate("pythonpro", "氧气      "))
        self.pushButton_7.setText(_translate("pythonpro", "樱花      "))
        self.pushButton_8.setText(_translate("pythonpro", "芝士      "))
        self.pushButton_9.setText(_translate("pythonpro", "冰激凌   "))
        self.label_3.setText(_translate("pythonpro", " ▼现代"))
        self.pushButton_10.setText(_translate("pythonpro", "复古     "))
        self.pushButton_11.setText(_translate("pythonpro", "果酱     "))
        self.pushButton_12.setText(_translate("pythonpro", "桔梗     "))
        self.pushButton_13.setText(_translate("pythonpro", "白茶     "))
        self.pushButton_14.setText(_translate("pythonpro", "珍珠     "))
        self.label_4.setText(_translate("pythonpro", " ▼Unsplash"))
        self.pushButton_15.setText(_translate("pythonpro", "海盐     "))
        self.pushButton_16.setText(_translate("pythonpro", "黄油     "))
        self.pushButton_17.setText(_translate("pythonpro", "质感     "))
        self.pushButton_18.setText(_translate("pythonpro", "蜜桃     "))
        self.label_5.setText(_translate("pythonpro", " ▼艺术"))
        self.pushButton_19.setText(_translate("pythonpro", "奶油     "))
        self.pushButton_20.setText(_translate("pythonpro", "葡萄     "))
        self.pushButton_21.setText(_translate("pythonpro", "色彩翻转"))
        self.label_6.setText(_translate("pythonpro", " ▼特殊"))
        self.pushButton_22.setText(_translate("pythonpro", "模糊      "))
        self.pushButton_23.setText(_translate("pythonpro", "去色      "))
        self.pushButton_24.setText(_translate("pythonpro", "浮雕      "))
        self.pushButton_25.setText(_translate("pythonpro", "马赛克   "))
        self.label_8.setText(_translate("pythonpro", "© 2018 Designed by PYAwesome"))
        self.label_9.setText(_translate("pythonpro", "All rights reserved"))
        self.label_10.setText(_translate("pythonpro", "亮度"))
        self.label_11.setText(_translate("pythonpro", "对比度"))
        self.label_12.setText(_translate("pythonpro", "饱和度"))
        self.label_13.setText(_translate("pythonpro", "锐度"))
        self.label_14.setText(_translate("pythonpro", "红光"))
        self.label_15.setText(_translate("pythonpro", "绿光"))
        self.label_16.setText(_translate("pythonpro", "蓝光"))
        self.label_17.setText(_translate("pythonpro", "平滑"))
        self.toolButton.setText(_translate("pythonpro", "打开"))
        self.toolButton_2.setText(_translate("pythonpro", "保存"))
