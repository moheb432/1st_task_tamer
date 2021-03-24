from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUiType
import os
from os import path
import sys
import numpy as np
import pyqtgraph as pg
from pyqtgraph import PlotWidget
class Ui_mainwindow(object):
    def setupUi(self, mainwindow):
        mainwindow.setObjectName("mainwindow")
        mainwindow.setEnabled(True)
        mainwindow.resize(1204, 700)
        self.centralwidget = QtWidgets.QWidget(mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(160, 100, 801, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = pg.PlotWidget(self.verticalLayoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.graphicsView_3 = pg.PlotWidget(self.verticalLayoutWidget)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.verticalLayout.addWidget(self.graphicsView_3)
        self.graphicsView_2 =  pg.PlotWidget(self.verticalLayoutWidget)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout.addWidget(self.graphicsView_2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 80, 91, 541))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(990, 100, 191, 391))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.channels = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.channels.setObjectName("channels")
        self.verticalLayout_3.addWidget(self.channels)
        self.resume = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.resume.setObjectName("resume")
        self.verticalLayout_3.addWidget(self.resume)
        self.pause = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pause.setObjectName("pause")
        self.verticalLayout_3.addWidget(self.pause)
        self.clear = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.clear.setObjectName("clear")
        self.verticalLayout_3.addWidget(self.clear)
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_4.setGeometry(QtCore.QRect(160, 500, 799, 116))
        self.graphicsView_4.setObjectName("graphicsView_4")
        mainwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainwindow)
        self.statusbar.setBaseSize(QtCore.QSize(4, 8))
        self.statusbar.setObjectName("statusbar")
        mainwindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(mainwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1204, 26))
        self.menubar.setAutoFillBackground(False)
        self.menubar.setDefaultUp(True)
        self.menubar.setObjectName("menubar")
        self.menusignal_processing = QtWidgets.QMenu(self.menubar)
        self.menusignal_processing.setBaseSize(QtCore.QSize(7, 7))
        self.menusignal_processing.setObjectName("menusignal_processing")
        self.open_ch1 = QtWidgets.QMenu(self.menubar)
        self.open_ch1.setObjectName("open_ch1")
        self.open_ch2 = QtWidgets.QMenu(self.menubar)
        self.open_ch2.setObjectName("open_ch2")
        self.open_ch3 = QtWidgets.QMenu(self.menubar)
        self.open_ch3.setObjectName("open_ch3")
        self.spect = QtWidgets.QMenu(self.menubar)
        self.spect.setObjectName("spect")
        self.help = QtWidgets.QMenu(self.menubar)
        self.help.setObjectName("help")
        mainwindow.setMenuBar(self.menubar)
        self.actionopen = QtWidgets.QAction(mainwindow)
        self.actionopen.setObjectName("actionopen")
        self.actionhelp = QtWidgets.QAction(mainwindow)
        self.actionhelp.setObjectName("actionhelp")
        self.close = QtWidgets.QAction(mainwindow)
        self.close.setObjectName("close")
        self.actionhelp_2 = QtWidgets.QAction(mainwindow)
        self.actionhelp_2.setObjectName("actionhelp_2")
        self.about = QtWidgets.QAction(mainwindow)
        self.about.setObjectName("about")
        self.menusignal_processing.addAction(self.about)
        self.menusignal_processing.addAction(self.close)
        self.menubar.addAction(self.menusignal_processing.menuAction())
        self.menubar.addAction(self.open_ch1.menuAction())
        self.menubar.addAction(self.open_ch3.menuAction())
        self.menubar.addAction(self.spect.menuAction())
        self.menubar.addAction(self.open_ch2.menuAction())
        self.menubar.addAction(self.help.menuAction())

        self.retranslateUi(mainwindow)
        QtCore.QMetaObject.connectSlotsByName(mainwindow)
#rannia+ moheb ***************************************
    def play(self):
        data=np.genfromtxt(r"C:\Users\Lenovo\Desktop\OD\Multi-Channel-Signals-Viewer-master\emg.csv",delimiter = ' ')
        x1=data[: , 0]
        y1 =data[: , 1]
        x1= list(x1[:])
        y1= list(y1[:])
        if (1) :
            self.graphicsView.plot(x1,y1)
        elif(1):
            self.graphicsView_3.plot(x1,y1)
        elif(1):
            self.graphicsView_2.plot(x1,y1)

    #******************************************************
    def retranslateUi(self, mainwindow):
        _translate = QtCore.QCoreApplication.translate
        mainwindow.setWindowTitle(_translate("mainwindow", "MainWindow"))
        self.label.setText(_translate("mainwindow", "channel 1"))
        self.label_2.setText(_translate("mainwindow", "channel 2"))
        self.label_3.setText(_translate("mainwindow", "channel 3"))
        self.label_4.setText(_translate("mainwindow", "spectrogram"))
        self.resume.setText(_translate("mainwindow", "play"))
        self.pause.setText(_translate("mainwindow", "pause"))
        self.clear.setText(_translate("mainwindow", "clear"))
        self.menusignal_processing.setTitle(_translate("mainwindow", "file"))
        self.open_ch1.setTitle(_translate("mainwindow", "channel 1"))
        self.open_ch2.setTitle(_translate("mainwindow", "channel 2"))
        self.open_ch3.setTitle(_translate("mainwindow", "channel 3"))
        self.spect.setTitle(_translate("mainwindow", "spectrogram"))
        self.help.setTitle(_translate("mainwindow", "help"))
        self.actionopen.setText(_translate("mainwindow", "open "))
        self.actionhelp.setText(_translate("mainwindow", "help"))
        self.close.setText(_translate("mainwindow", "close "))
        self.actionhelp_2.setText(_translate("mainwindow", "help "))
        self.about.setText(_translate("mainwindow", "about"))
        self.channels.addItem(" ")
        self.channels.addItem("channel_1")
        self.channels.addItem("channel_2")
        self.channels.addItem("channel_3")
        #rannia + moheb
        self.resume.clicked.connect(lambda:self.play())


#open channels 2 zoom navigation moheb + rannia *********************************************




#helil bar + combobox ***************************************************





#nouran play and pause and clear




#spectogram







def main():
    app = QtWidgets.QApplication(sys.argv)
    window= MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
