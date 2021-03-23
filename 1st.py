from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.uic import loadUiType
import os
from os import path
import sys
import numpy as np
import pandas as pd
from pyqtgraph import PlotWidget ,PlotItem
import pyqtgraph as pg 
import pathlib

#Import UI File
FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__), "1st.ui"))


class MainApp(QtWidgets.QMainWindow,FORM_CLASS):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)




#open channels 2 zoom navigation moheb + rannia *********************************************
data=np.genfromtxt(r"C:\Users\Lenovo\Desktop\OD\Multi-Channel-Signals-Viewer-master\emg.csv",delimiter = ' ')
x1=data[: , 0]
y1 =data[: , 1]
x1= list(x1[:])
y1= list(y1[:])



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






