# -*- coding: utf-8 -*-
"""
Created on Mon May 26 19:56:08 2025

@author: omrky
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from final_working_q2 import Ui_MainWindow  # .ui'den pyuic5 ile oluşturulmuş Python dosyası

class PrimeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = PrimeApp()
    win.show()
    sys.exit(app.exec_())
