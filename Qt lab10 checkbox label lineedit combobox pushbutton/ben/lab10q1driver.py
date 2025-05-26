# -*- coding: utf-8 -*-
"""
Created on Fri May 23 19:39:05 2025

@author: omrky
"""

from PyQt5 import QtWidgets
 
from lab10q1 import Ui_MainWindow  # importing our generated file
 
import sys

class mywindow(QtWidgets.QMainWindow):
 
    def __init__(self):
 
        super(mywindow, self).__init__()
 
        self.ui = Ui_MainWindow()
    
        self.ui.setupUi(self)
 
app = QtWidgets.QApplication([])
 
application = mywindow()
 
application.show()
 
sys.exit(app.exec())