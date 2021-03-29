
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox,QLabel
from PyQt5.uic import loadUiType
import os
from os import path
import sys
import numpy as np
import pyqtgraph as pg
from pyqtgraph import PlotWidget
import time
import datetime
import matplotlib.pyplot as plot
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
from scipy import signal
from PyQt5.QtGui import QIcon, QPixmap
import tempfile
import shutil


class Ui_mainwindow(QtGui.QMainWindow):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.setEnabled(True)
        mainwindow.resize(1604, 946)
        mainwindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(24)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.show_ch1 = QtWidgets.QCheckBox(self.centralwidget)
        self.show_ch1.setEnabled(True)
        self.show_ch1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.show_ch1.setCheckable(True)
        self.show_ch1.setChecked(True)
        self.show_ch1.setTristate(False)
        self.show_ch1.setObjectName("show_ch1")
        self.horizontalLayout_4.addWidget(self.show_ch1)
        self.graphicsView = pg.PlotWidget(self.centralwidget)
        self.graphicsView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_4.addWidget(self.graphicsView)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.up1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.up1.sizePolicy().hasHeightForWidth())
        self.up1.setSizePolicy(sizePolicy)
        self.up1.setMinimumSize(QtCore.QSize(40, 40))
        self.up1.setMaximumSize(QtCore.QSize(40, 40))
        self.up1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.up1.setObjectName("up1")
        self.verticalLayout_4.addWidget(self.up1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_7.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.left1 = QtWidgets.QPushButton(self.centralwidget)
        self.left1.setMinimumSize(QtCore.QSize(40, 40))
        self.left1.setMaximumSize(QtCore.QSize(40, 40))
        self.left1.setObjectName("left1")
        self.horizontalLayout_7.addWidget(self.left1)
        self.right1 = QtWidgets.QPushButton(self.centralwidget)
        self.right1.setMinimumSize(QtCore.QSize(40, 40))
        self.right1.setMaximumSize(QtCore.QSize(40, 40))
        self.right1.setObjectName("right1")
        self.horizontalLayout_7.addWidget(self.right1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.down1 = QtWidgets.QPushButton(self.centralwidget)
        self.down1.setMinimumSize(QtCore.QSize(40, 40))
        self.down1.setMaximumSize(QtCore.QSize(40, 40))
        self.down1.setObjectName("down1")
        self.verticalLayout_4.addWidget(self.down1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 5, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.zoomin1 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomin1.setObjectName("zoomin1")
        self.horizontalLayout.addWidget(self.zoomin1)
        self.zoomout1 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomout1.setObjectName("zoomout1")
        self.horizontalLayout.addWidget(self.zoomout1)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_12.addLayout(self.verticalLayout_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pause1 = QtWidgets.QPushButton(self.centralwidget)
        self.pause1.setObjectName("pause1")
        self.verticalLayout.addWidget(self.pause1)
        self.resume1 = QtWidgets.QPushButton(self.centralwidget)
        self.resume1.setObjectName("resume1")
        self.verticalLayout.addWidget(self.resume1)
        self.horizontalLayout_12.addLayout(self.verticalLayout)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(24)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.show_ch2 = QtWidgets.QCheckBox(self.centralwidget)
        self.show_ch2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.show_ch2.setChecked(True)
        self.show_ch2.setObjectName("show_ch2")
        self.horizontalLayout_5.addWidget(self.show_ch2)
        self.graphicsView_2 = pg.PlotWidget(self.centralwidget)
        self.graphicsView_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.horizontalLayout_5.addWidget(self.graphicsView_2)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.up2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.up2.sizePolicy().hasHeightForWidth())
        self.up2.setSizePolicy(sizePolicy)
        self.up2.setMinimumSize(QtCore.QSize(40, 40))
        self.up2.setMaximumSize(QtCore.QSize(40, 40))
        self.up2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.up2.setObjectName("up2")
        self.verticalLayout_5.addWidget(self.up2)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_8.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.left2 = QtWidgets.QPushButton(self.centralwidget)
        self.left2.setMinimumSize(QtCore.QSize(40, 40))
        self.left2.setMaximumSize(QtCore.QSize(40, 40))
        self.left2.setObjectName("left2")
        self.horizontalLayout_8.addWidget(self.left2)
        self.right2 = QtWidgets.QPushButton(self.centralwidget)
        self.right2.setMinimumSize(QtCore.QSize(40, 40))
        self.right2.setMaximumSize(QtCore.QSize(40, 40))
        self.right2.setObjectName("right2")
        self.horizontalLayout_8.addWidget(self.right2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.down2 = QtWidgets.QPushButton(self.centralwidget)
        self.down2.setMinimumSize(QtCore.QSize(40, 40))
        self.down2.setMaximumSize(QtCore.QSize(40, 40))
        self.down2.setObjectName("down2")
        self.verticalLayout_5.addWidget(self.down2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 5, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.zoomin2 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomin2.setObjectName("zoomin2")
        self.horizontalLayout_2.addWidget(self.zoomin2)
        self.zoomout2 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomout2.setObjectName("zoomout2")
        self.horizontalLayout_2.addWidget(self.zoomout2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_13.addLayout(self.verticalLayout_5)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pause2 = QtWidgets.QPushButton(self.centralwidget)
        self.pause2.setObjectName("pause2")
        self.verticalLayout_2.addWidget(self.pause2)
        self.resume2 = QtWidgets.QPushButton(self.centralwidget)
        self.resume2.setObjectName("resume2")
        self.verticalLayout_2.addWidget(self.resume2)
        self.horizontalLayout_13.addLayout(self.verticalLayout_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(24)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.show_ch3 = QtWidgets.QCheckBox(self.centralwidget)
        self.show_ch3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.show_ch3.setChecked(True)
        self.show_ch3.setObjectName("show_ch3")
        self.horizontalLayout_6.addWidget(self.show_ch3)
        self.graphicsView_3 = pg.PlotWidget(self.centralwidget)
        self.graphicsView_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.horizontalLayout_6.addWidget(self.graphicsView_3)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_6)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.up3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.up3.sizePolicy().hasHeightForWidth())
        self.up3.setSizePolicy(sizePolicy)
        self.up3.setMinimumSize(QtCore.QSize(40, 40))
        self.up3.setMaximumSize(QtCore.QSize(40, 40))
        self.up3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.up3.setObjectName("up3")
        self.verticalLayout_6.addWidget(self.up3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_9.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.left3 = QtWidgets.QPushButton(self.centralwidget)
        self.left3.setMinimumSize(QtCore.QSize(40, 40))
        self.left3.setMaximumSize(QtCore.QSize(40, 40))
        self.left3.setObjectName("left3")
        self.horizontalLayout_9.addWidget(self.left3)
        self.right3 = QtWidgets.QPushButton(self.centralwidget)
        self.right3.setMinimumSize(QtCore.QSize(40, 40))
        self.right3.setMaximumSize(QtCore.QSize(40, 40))
        self.right3.setObjectName("right3")
        self.horizontalLayout_9.addWidget(self.right3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.down3 = QtWidgets.QPushButton(self.centralwidget)
        self.down3.setMinimumSize(QtCore.QSize(40, 40))
        self.down3.setMaximumSize(QtCore.QSize(40, 40))
        self.down3.setObjectName("down3")
        self.verticalLayout_6.addWidget(self.down3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.zoomin3 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomin3.setObjectName("zoomin3")
        self.horizontalLayout_3.addWidget(self.zoomin3)
        self.zoomout3 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomout3.setObjectName("zoomout3")
        self.horizontalLayout_3.addWidget(self.zoomout3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_14.addLayout(self.verticalLayout_6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pause3 = QtWidgets.QPushButton(self.centralwidget)
        self.pause3.setObjectName("pause3")
        self.verticalLayout_3.addWidget(self.pause3)
        self.resume3 = QtWidgets.QPushButton(self.centralwidget)
        self.resume3.setObjectName("resume3")
        self.verticalLayout_3.addWidget(self.resume3)
        self.horizontalLayout_14.addLayout(self.verticalLayout_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_14)
        self.gridLayout_4.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setContentsMargins(-1, 5, -1, -1)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.show_spect = QtWidgets.QCheckBox(self.centralwidget)
        self.show_spect.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.show_spect.setChecked(True)
        self.show_spect.setObjectName("show_spect")
        self.horizontalLayout_10.addWidget(self.show_spect)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.spectrogram_1 = QtWidgets.QWidget()
        self.spectrogram_1.setObjectName("spectrogram_1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.spectrogram_1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.spectView_1 = QtWidgets.QLabel(self.spectrogram_1)
        self.spectView_1.setText("")
        self.spectView_1.setObjectName("spectView_1")
        self.gridLayout_2.addWidget(self.spectView_1, 0, 0, 1, 1)
        self.tabWidget.addTab(self.spectrogram_1, "")
        self.spectrogram_2 = QtWidgets.QWidget()
        self.spectrogram_2.setObjectName("spectrogram_2")
        self.gridLayout = QtWidgets.QGridLayout(self.spectrogram_2)
        self.gridLayout.setObjectName("gridLayout")
        self.spectView_2 = QtWidgets.QLabel(self.spectrogram_2)
        self.spectView_2.setText("")
        self.spectView_2.setObjectName("spectView_2")
        self.gridLayout.addWidget(self.spectView_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.spectrogram_2, "")
        self.spectrogram_3 = QtWidgets.QWidget()
        self.spectrogram_3.setObjectName("spectrogram_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.spectrogram_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.spectView_3 = QtWidgets.QLabel(self.spectrogram_3)
        self.spectView_3.setText("")
        self.spectView_3.setObjectName("spectView_3")
        self.gridLayout_3.addWidget(self.spectView_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.spectrogram_3, "")
        self.horizontalLayout_10.addWidget(self.tabWidget)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_10)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(20, -1, 30, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setMinimumSize(QtCore.QSize(120, 100))
        self.clear.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.clear.setObjectName("clear")
        self.verticalLayout_8.addWidget(self.clear)
        self.horizontalLayout_15.addLayout(self.verticalLayout_8)
        self.gridLayout_4.addLayout(self.horizontalLayout_15, 1, 0, 1, 1)
        mainwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainwindow)
        self.statusbar.setBaseSize(QtCore.QSize(4, 8))
        self.statusbar.setObjectName("statusbar")
        mainwindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1604, 26))
        self.menubar.setAutoFillBackground(False)
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menusignal_processing = QtWidgets.QMenu(self.menubar)
        self.menusignal_processing.setBaseSize(QtCore.QSize(7, 7))
        self.menusignal_processing.setObjectName("menusignal_processing")
        self.ch1 = QtWidgets.QMenu(self.menubar)
        self.ch1.setObjectName("ch1")
        self.ch2 = QtWidgets.QMenu(self.menubar)
        self.ch2.setObjectName("ch2")
        self.ch3 = QtWidgets.QMenu(self.menubar)
        self.ch3.setObjectName("ch3")
        self.spect = QtWidgets.QMenu(self.menubar)
        self.spect.setObjectName("spect")
        self.help = QtWidgets.QMenu(self.menubar)
        self.help.setObjectName("help")
        mainwindow.setMenuBar(self.menubar)
        self.actionhelp = QtWidgets.QAction(mainwindow)
        self.actionhelp.setObjectName("actionhelp")
        self.close = QtWidgets.QAction(mainwindow)
        self.close.setObjectName("close")
        self.actionhelp_2 = QtWidgets.QAction(mainwindow)
        self.actionhelp_2.setObjectName("actionhelp_2")
        self.open_ch1 = QtWidgets.QAction(mainwindow)
        self.open_ch1.setObjectName("open_ch1")
        self.open_ch2 = QtWidgets.QAction(mainwindow)
        self.open_ch2.setObjectName("open_ch2")
        self.open_ch3 = QtWidgets.QAction(mainwindow)
        self.open_ch3.setObjectName("open_ch3")
        self.about = QtWidgets.QAction(mainwindow)
        self.about.setObjectName("about")
        self.savePDF = QtWidgets.QAction(mainwindow)
        self.savePDF.setObjectName("savePDF")
        self.menusignal_processing.addAction(self.savePDF)
        self.menusignal_processing.addAction(self.close)
        self.ch1.addAction(self.open_ch1)
        self.ch2.addAction(self.open_ch2)
        self.ch3.addAction(self.open_ch3)
        self.help.addAction(self.about)
        self.menubar.addAction(self.menusignal_processing.menuAction())
        self.menubar.addAction(self.ch1.menuAction())
        self.menubar.addAction(self.ch2.menuAction())
        self.menubar.addAction(self.ch3.menuAction())
        self.menubar.addAction(self.spect.menuAction())
        self.menubar.addAction(self.help.menuAction())

        
        self.a1=0
        self.b1=0
        self.c1=1
        self.d1=0
        self.a2=0
        self.b2=0
        self.c2=1
        self.a3=0
        self.b3=0
        self.c3=1

        self.retranslateUi(mainwindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)

        #timer for qt
        self.timer1 = QtCore.QTimer()
        self.timer2 = QtCore.QTimer()
        self.timer3 = QtCore.QTimer()



#reading dataaa ************************
    def read_data(self,ch):
        loadSignal= QtGui.QFileDialog.getOpenFileName( self, 'Open only CSV ', os.getenv('HOME') ,"csv(*.csv)")
        path=loadSignal[0]
        data=np.genfromtxt(path,delimiter = ' ')
        x1=data[: , 0]
        if ch==1:
            self.y1_array =data[: , 1]
            self.x1= list(x1[:])
            self.y1= list(self.y1_array [:])
            self.ch1=1
            self.spectro(1,data)
        if ch==2:
            self.y2_array =data[: , 1]
            self.x2= list(x1[:])
            self.y2= list(self.y2_array [:])
            self.ch2=1
            self.spectro(2,data)
        if ch==3:
            self.y3_array =data[: , 1]
            self.x3= list(x1[:])
            self.y3= list(self.y3_array [:])
            self.ch3=1
            self.spectro(3,data)
#function in qt timer to update the data
    def update1(self):
        if self.st_x1>len(self.x1):
            self.st_x1=10
        x=self.x1[:self.st_x1]
        y=self.y1[:self.st_x1]
        self.st_x1+=10
        self.graphicsView.plot(x,y,pen=pg.mkPen('b', width=1))
    def update2(self):
        x=self.x2[:self.st_x2]
        y=self.y2[:self.st_x2]
        self.st_x2+=10
        self.graphicsView_2.plot(x,y,pen=pg.mkPen('r', width=2))
        if self.st_x2>len(self.x2):
            self.st_x2=0
    def update3(self):
        x=self.x3[:self.st_x3]
        y=self.y3[:self.st_x3]
        self.st_x3+=10
        self.graphicsView_3.plot(x,y,pen=pg.mkPen('g', width=3))
        if self.st_x3>len(self.x3):
            self.st_x3=0
#playing data on adding the file

    def play1(self):
        self.read_data(1)
        self.timer1.start()
        self.st_x1=10
        self.timer1.setInterval(100)
        self.timer1.timeout.connect(self.update1)
        self.timer1.start()

    def play2(self):
        self.read_data(2)
        self.timer2.start()
        self.st_x2=10
        self.timer2.setInterval(100)
        self.timer2.timeout.connect(self.update2)
        self.timer2.start()

    def play3(self):
        self.read_data(3)
        self.timer3.start()
        self.st_x3=10
        self.timer3.setInterval(100)
        self.timer3.timeout.connect(self.update3)
        self.timer3.start()
#zooming
    def zi_1(self):
        if(self.b1 < 3):
            self.c1 -= 0.2
            self.c1=abs(self.c1)
            self.b1+=1
        self.graphicsView.setXRange(0,self.c1)
        
    def zi_2(self):
        if(self.b2 < 3):
            self.c2 -=0.2
            self.c2=abs(self.c2)
            self.b2+=1
        self.graphicsView_2.setXRange(0,self.c2)



    def zi_3(self):
        self.a3= self.a3 + 1
        if(self.b3 < 3):
            self.c3 -= 0.2
            self.c3=abs(self.c3)
            self.b3+=1
        self.graphicsView_3.setXRange(0,self.c3)


    def zo_1(self):
        if(self.b1 >0):
            self.c1 +=0.2
            self.b1-=1
        self.graphicsView.setXRange(0,self.c1)

    def zo_2(self):
        if(self.b2 >0):
            self.c2 +=0.2
            self.b2-=1
        self.graphicsView_2.setXRange(0,self.c2)


    def zo_3(self):
        if(self.b3 >0):
            self.c3 +=0.2
            self.b3-=1
        self.graphicsView_3.setXRange(0,self.c3)
#saving data
    def savepdf(self) :
         fig=plot.figure()
         if self.ch1==1:
             plot.subplot(2, 3, 1)
             plot.plot(self.x1,self.y1)
             plot.subplot(2, 3, 4)
             Pxx, freqs, bins, im = plot.specgram(self.y1_array)
         if self.ch2==1:
             plot.subplot(2, 3, 2)
             plot.plot(self.x2,self.y2)
             plot.subplot(2, 3, 5)
             Pxx, freqs, bins, im = plot.specgram(self.y2_array)
         if self.ch3==1:
             plot.subplot(2, 3, 3)
             plot.plot(self.x3,self.y3)
             plot.subplot(2, 3, 6)
             Pxx, freqs, bins, im = plot.specgram(self.y3_array)

         plot.show()
         fig.savefig("x.pdf")

#to clear data

    def delete(self):
        self.graphicsView.clear()
        self.graphicsView_2.clear()
        self.graphicsView_3.clear()
        self.timer1.stop()
        self.timer2.stop()
        self.timer3.stop()
        self.spectView_1.clear()
        self.spectView_2.clear()
        self.spectView_3.clear()


    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "MainWindow"))
        self.show_ch1.setText(_translate("mainwindow", "Channel 1"))
        self.up1.setText(_translate("mainwindow", "PushButton"))
        self.left1.setText(_translate("mainwindow", "PushButton"))
        self.right1.setText(_translate("mainwindow", "PushButton"))
        self.down1.setText(_translate("mainwindow", "PushButton"))
        self.zoomin1.setText(_translate("mainwindow", "Zoom In"))
        self.zoomout1.setText(_translate("mainwindow", "Zoom out"))
        self.pause1.setText(_translate("mainwindow", "Pause"))
        self.resume1.setText(_translate("mainwindow", "Play"))
        self.show_ch2.setText(_translate("mainwindow", "Channel 2"))
        self.up2.setText(_translate("mainwindow", "PushButton"))
        self.left2.setText(_translate("mainwindow", "PushButton"))
        self.right2.setText(_translate("mainwindow", "PushButton"))
        self.down2.setText(_translate("mainwindow", "PushButton"))
        self.zoomin2.setText(_translate("mainwindow", "Zoom In"))
        self.zoomout2.setText(_translate("mainwindow", "Zoom out"))
        self.pause2.setText(_translate("mainwindow", "Pause"))
        self.resume2.setText(_translate("mainwindow", "Play"))
        self.show_ch3.setText(_translate("mainwindow", "Channel 3"))
        self.up3.setText(_translate("mainwindow", "PushButton"))
        self.left3.setText(_translate("mainwindow", "PushButton"))
        self.right3.setText(_translate("mainwindow", "PushButton"))
        self.down3.setText(_translate("mainwindow", "PushButton"))
        self.zoomin3.setText(_translate("mainwindow", "Zoom In"))
        self.zoomout3.setText(_translate("mainwindow", "Zoom out"))
        self.pause3.setText(_translate("mainwindow", "Pause"))
        self.resume3.setText(_translate("mainwindow", "Play"))
        self.show_spect.setText(_translate("mainwindow", "Spectrogram"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.spectrogram_1), _translate("mainwindow", "Channel 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.spectrogram_2), _translate("mainwindow", "Channel 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.spectrogram_3), _translate("mainwindow", "Channel 3"))
        self.clear.setText(_translate("mainwindow", "Clear all"))
        self.menusignal_processing.setTitle(_translate("mainwindow", "file"))
        self.ch1.setTitle(_translate("mainwindow", "Channel 1"))
        self.ch2.setTitle(_translate("mainwindow", "Channel 2"))
        self.ch3.setTitle(_translate("mainwindow", "Channel 3"))
        self.spect.setTitle(_translate("mainwindow", "Spectrogram"))
        self.help.setTitle(_translate("mainwindow", "Help"))
        self.actionhelp.setText(_translate("mainwindow", "help"))
        self.close.setText(_translate("mainwindow", "Close "))
        self.actionhelp_2.setText(_translate("mainwindow", "help "))
        self.open_ch1.setText(_translate("mainwindow", "load signal"))
        self.open_ch2.setText(_translate("mainwindow", "load signal"))
        self.open_ch3.setText(_translate("mainwindow", "load signal"))
        self.about.setText(_translate("mainwindow", "About"))
        self.savePDF.setText(_translate("mainwindow", "Save PDF"))


        #resume buttoms actions
        self.resume1.clicked.connect(lambda :self.timer1.start())
        self.resume2.clicked.connect(lambda :self.timer3.start())
        self.resume3.clicked.connect(lambda :self.timer2.start())

        self.pause1.clicked.connect(lambda :self.timer1.stop())
        self.pause2.clicked.connect(lambda :self.timer3.stop())
        self.pause3.clicked.connect(lambda :self.timer2.stop())

        self.zoomin1.clicked.connect(lambda :self.zi_1())
        self.zoomin2.clicked.connect(lambda :self.zi_2())
        self.zoomin3.clicked.connect(lambda :self.zi_3())
        self.zoomout1.clicked.connect(lambda :self.zo_1())
        self.zoomout2.clicked.connect(lambda :self.zo_2())
        self.zoomout3.clicked.connect(lambda :self.zo_3())


        #aaahoooooooooooooooooooooo       ******************
        # self.savepdf.triggered.connect(lambda:self.savepdf())
        #************************************ysksh tshofooooo


        self.clear.clicked.connect(lambda:self.delete())

            ############## Hilal Events #############
        self.close.triggered.connect(sys.exit)
        self.about.triggered.connect(self.showDialog)
        self.open_ch1.triggered.connect(lambda: self.play1())
        self.open_ch2.triggered.connect(lambda: self.play2())
        self.open_ch3.triggered.connect(lambda: self.play3())

        self.show_ch1.stateChanged.connect(lambda: self.hide1(self.show_ch1,self.graphicsView))
        self.show_ch2.stateChanged.connect(lambda: self.hide2(self.show_ch2,self.graphicsView_2))
        self.show_ch3.stateChanged.connect(lambda: self.hide3(self.show_ch3,self.graphicsView_3))
        self.show_spect.stateChanged.connect(lambda: self.hide(self.show_spect,self.tabWidget))


        ############## Hilal Functions ################

    def handleUI(self):
        self.setWindowTitle("Signal Viewer")


    def handleButtons(self):
        pass
        
     #About message
    def showDialog(self):
        QMessageBox.information(self,"About","Signal Viewer is a software for visualizing signals \n (c) 2021 SBME Cairo University")

     #Hide Channel function
    def hide1 (self,channel,graphicsView):
        if (channel.isChecked()):
            graphicsView.show()
            self.pause1.show()
            self.resume1.show()
            self.zoomin1.show()
            self.zoomout1.show()
        else:
            graphicsView.hide()
            self.pause1.hide()
            self.resume1.hide()
            self.zoomin1.hide()
            self.zoomout1.hide()

    def hide2 (self,channel,graphicsView):
        if (channel.isChecked()):
            graphicsView.show()
            self.pause2.show()
            self.resume2.show()
            self.zoomin2.show()
            self.zoomout2.show()
        else:
            graphicsView.hide()
            self.pause2.hide()
            self.resume2.hide()
            self.zoomin2.hide()
            self.zoomout2.hide()

    def hide3 (self,channel,graphicsView):
        if (channel.isChecked()):
            graphicsView.show()
            self.pause3.show()
            self.resume3.show()
            self.zoomin3.show()
            self.zoomout3.show()
        else:
            graphicsView.hide()
            self.pause3.hide()
            self.resume3.hide()
            self.zoomin3.hide()
            self.zoomout3.hide()

    def hide (self,channel,graphicsView):
        if (channel.isChecked()):
            graphicsView.show()
        else:
            graphicsView.hide()


 #################### Spectrogram ###########################

    def spectro (self,ch,d):   #ch for channel  and  d for Data

        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        dirpath = tempfile.mkdtemp()
        y1 =d[: , 1]
        plot.specgram(y1)

        if ch ==1:
            plot.savefig(os.path.join(dirpath,"plot1.png"))
            plot1 = QPixmap(os.path.join(dirpath,"plot1.png"))
            self.spectView_1.setPixmap(plot1)

        elif ch ==2:
            plot.savefig(os.path.join(dirpath,"plot2.png"))
            plot2= QPixmap(os.path.join(dirpath,"plot2.png"))
            self.spectView_2.setPixmap(plot2)

        elif ch ==3:
            plot.savefig(os.path.join(dirpath,"plot3.png"))
            plot3 = QPixmap(os.path.join(dirpath,"plot3.png"))
            self.spectView_3.setPixmap(plot3)

        shutil.rmtree(dirpath)


############################## end hilal #####################################







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    ui = Ui_mainwindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())
