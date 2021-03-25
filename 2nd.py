# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1st-2nd.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.uic import loadUiType
import os
from os import path
import sys
import numpy as np
import pyqtgraph as pg
from pyqtgraph import PlotWidget
import time
import datetime
class Ui_mainwindow(QtGui.QMainWindow):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.setEnabled(True)
        mainwindow.resize(1486, 920)
        mainwindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(20, 20, 15, 15)
        self.horizontalLayout_5.setSpacing(56)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(14)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(25)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.show_ch1 = QtWidgets.QCheckBox(self.centralwidget)
        self.show_ch1.setEnabled(True)
        self.show_ch1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.show_ch1.setCheckable(True)
        self.show_ch1.setChecked(True)
        self.show_ch1.setTristate(False)
        self.show_ch1.setObjectName("show_ch1")
        self.horizontalLayout.addWidget(self.show_ch1)
        self.graphicsView = pg.PlotWidget(self.centralwidget)
        self.graphicsView.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout.addWidget(self.graphicsView)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(25)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.show_ch2 = QtWidgets.QCheckBox(self.centralwidget)
        self.show_ch2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.show_ch2.setChecked(True)
        self.show_ch2.setObjectName("show_ch2")
        self.horizontalLayout_2.addWidget(self.show_ch2)
        self.graphicsView_2 = pg.PlotWidget(self.centralwidget)
        self.graphicsView_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.horizontalLayout_2.addWidget(self.graphicsView_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(25)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.show_ch3 = QtWidgets.QCheckBox(self.centralwidget)
        self.show_ch3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.show_ch3.setChecked(True)
        self.show_ch3.setObjectName("show_ch3")
        self.horizontalLayout_3.addWidget(self.show_ch3)
        self.graphicsView_3 =pg.PlotWidget(self.centralwidget)
        self.graphicsView_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.horizontalLayout_3.addWidget(self.graphicsView_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.show_spect = QtWidgets.QCheckBox(self.centralwidget)
        self.show_spect.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.show_spect.setChecked(True)
        self.show_spect.setObjectName("show_spect")
        self.horizontalLayout_4.addWidget(self.show_spect)
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.horizontalLayout_4.addWidget(self.graphicsView_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")


        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.clear.setObjectName("clear")
        self.verticalLayout_3.addWidget(self.clear)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        mainwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainwindow)
        self.statusbar.setBaseSize(QtCore.QSize(4, 8))
        self.statusbar.setObjectName("statusbar")
        mainwindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1486, 26))
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

        self.zoomin1 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomin1.setObjectName("zoomin1")
        self.horizontalLayout.addWidget(self.zoomin1)
        self.zoomout1 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomout1.setObjectName("zoomout1")
        self.horizontalLayout.addWidget(self.zoomout1)


        self.zoomin2 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomin2.setObjectName("zoomin2")
        self.horizontalLayout_2.addWidget(self.zoomin2)
        self.zoomout2 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomout2.setObjectName("zoomout2")
        self.horizontalLayout_2.addWidget(self.zoomout2)

        self.zoomin3 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomin3.setObjectName("zoomin3")
        self.horizontalLayout_3.addWidget(self.zoomin3)
        self.zoomout3 = QtWidgets.QPushButton(self.centralwidget)
        self.zoomout3.setObjectName("zoomout3")
        self.horizontalLayout_3.addWidget(self.zoomout3)


        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(1150, 80, 95, 71))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")

        self.resume1 = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.resume1.setText("")
        self.resume1.setObjectName("resume1")
        self.verticalLayout_16.addWidget(self.resume1)
        self.pause1 = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.pause1.setText("")
        self.pause1.setObjectName("pause1")
        #adding icons
        self.pause1.setIcon(QtGui.QIcon("pause.png"))
        self.resume1.setIcon(QtGui.QIcon("play.png"))


        self.verticalLayout_16.addWidget(self.pause1)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(1150, 250, 95, 71))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.resume2 = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        self.resume2.setText("")
        self.resume2.setObjectName("resume2")
        self.verticalLayout_17.addWidget(self.resume2)
        self.pause2 = QtWidgets.QPushButton(self.verticalLayoutWidget_8)
        self.pause2.setText("")
        self.pause2.setObjectName("pause2")
        self.verticalLayout_17.addWidget(self.pause2)
        #adding icons
        self.pause2.setIcon(QtGui.QIcon("pause.png"))
        self.resume2.setIcon(QtGui.QIcon("play.png"))

        self.verticalLayout_17.addWidget(self.pause2)
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(1150, 410, 95, 71))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")

        self.resume3 = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        self.resume3.setText("")
        self.resume3.setObjectName("resume3")
        self.verticalLayout_18.addWidget(self.resume3)
        self.pause3 = QtWidgets.QPushButton(self.verticalLayoutWidget_9)
        self.pause3.setText("")
        self.pause3.setObjectName("pause3")
        self.verticalLayout_18.addWidget(self.pause3)
        mainwindow.setCentralWidget(self.centralwidget)
        #adding icons
        self.pause3.setIcon(QtGui.QIcon("pause.png"))
        self.resume3.setIcon(QtGui.QIcon("play.png"))

        self.retranslateUi(mainwindow)
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
        y1 =data[: , 1]
        if ch==1:
            self.x1= list(x1[:])
            self.y1= list(y1[:])
        if ch==2:
            self.x2= list(x1[:])
            self.y2= list(y1[:])
        if ch==3:
            self.x3= list(x1[:])
            self.y3= list(y1[:])
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
            self.graphicsView_3.plot(x,y,pen=pg.mkPen('r', width=2))
            if self.st_x2>len(self.x2):
                self.st_x2=0
    def update3(self):
            x=self.x3[:self.st_x3]
            y=self.y3[:self.st_x3]
            self.st_x3+=10
            self.graphicsView_2.plot(x,y,pen=pg.mkPen('g', width=3))
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

#to clear data
    def delete(self):
        self.graphicsView.clear()
        self.graphicsView_2.clear()
        self.graphicsView_3.clear()
        self.timer1.stop()
        self.timer2.stop()
        self.timer3.stop()


    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "Signal Viewer"))
        self.show_ch1.setText(_translate("mainwindow", "Channel 1"))
        self.show_ch2.setText(_translate("mainwindow", "Channel 2"))
        self.show_ch3.setText(_translate("mainwindow", "Channel 3"))
        self.show_spect.setText(_translate("mainwindow", "Spectrogram"))

        self.clear.setText(_translate("mainwindow", "clear all"))
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
        self.zoomin1.setText(_translate("mainwindow", "+"))
        self.zoomout1.setText(_translate("mainwindow", "-"))
        self.zoomin2.setText(_translate("mainwindow", "+"))
        self.zoomout2.setText(_translate("mainwindow", "-"))
        self.zoomin3.setText(_translate("mainwindow", "+"))
        self.zoomout3.setText(_translate("mainwindow", "-"))



        #resume buttoms actions
        self.resume1.clicked.connect(lambda :self.timer1.start())
        self.resume2.clicked.connect(lambda :self.timer3.start())
        self.resume3.clicked.connect(lambda :self.timer2.start())

        self.pause1.clicked.connect(lambda :self.timer1.stop())
        self.pause2.clicked.connect(lambda :self.timer3.stop())
        self.pause3.clicked.connect(lambda :self.timer2.stop())


        self.clear.clicked.connect(lambda:self.delete())

            ############## Hilal Events #############
        self.close.triggered.connect(sys.exit)
        self.about.triggered.connect(self.showDialog)
        self.open_ch1.triggered.connect(lambda: self.play1())
        self.open_ch2.triggered.connect(lambda: self.play3())
        self.open_ch3.triggered.connect(lambda: self.play2())

        self.show_ch1.stateChanged.connect(lambda: self.hide(self.show_ch1,self.graphicsView))
        self.show_ch2.stateChanged.connect(lambda: self.hide(self.show_ch2,self.graphicsView_2))
        self.show_ch3.stateChanged.connect(lambda: self.hide(self.show_ch3,self.graphicsView_3))
        self.show_spect.stateChanged.connect(lambda: self.hide(self.show_spect,self.graphicsView_4))

        ############## Hilal Functions ################

    def handleUI(self):
        self.setWindowTitle("Signal Viewer")


    def handleButtons(self):
        pass

     #About message
    def showDialog(self):
        QMessageBox.information(self,"About","Signal Viewer is a software for visualizing signals \n (c) 2021 SBME Cairo University")

     #Hide Channel function
    def hide (self,channel,graphicsView):
        if (channel.isChecked()):
            graphicsView.show()
        else:
            graphicsView.hide()

     #Load Signal file to channel function
    #def load(self,channel):
       # self.read_data(channel)


############################## end hilal #####################################




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = QtWidgets.QMainWindow()
    ui = Ui_mainwindow()
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())
