# -*- coding: utf-8 -*-
"""
Created on Mon May 26 17:20:59 2025

@author: omrky
"""

import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from lab10q2 import Ui_MainWindow  # .ui dosyasından pyuic5 ile çevrilen dosyanın adı

class GameApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = GameApp()
    win.show()
    sys.exit(app.exec_())