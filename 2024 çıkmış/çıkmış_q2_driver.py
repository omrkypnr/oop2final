# -*- coding: utf-8 -*-
"""
Created on Tue May 27 00:04:05 2025

@author: omrky
"""

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from çıkmış_q2 import Ui_MainWindow  # ui dosyasının pyuic5 ile çevrilmiş hali

class NumberOperationsApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NumberOperationsApp()
    window.show()
    sys.exit(app.exec_())
