# -*- coding: utf-8 -*-
"""
Created on Fri May 23 23:05:25 2025

@author: omrky
"""

from PyQt5 import QtWidgets, QtGui
from lab8q1 import Ui_MainWindow  # pyuic5 ile oluşturulan dosyanın adı
import sys

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Slider değer aralıklarını ayarla (0-255)
        self.ui.horizontalSlider.setRange(0, 255)
        self.ui.horizontalSlider_2.setRange(0, 255)
        self.ui.horizontalSlider_3.setRange(0, 255)

        # Varsayılan değerleri ayarla
        self.ui.horizontalSlider.setValue(255)
        self.ui.horizontalSlider_2.setValue(158)
        self.ui.horizontalSlider_3.setValue(79)

        # LineEdit'lere başlangıç değerlerini yaz
        self.ui.lineEdit.setText(str(255))
        self.ui.lineEdit_2.setText(str(158))
        self.ui.lineEdit_3.setText(str(79))

        # Slider hareketlerine tepki ver
        self.ui.horizontalSlider.valueChanged.connect(self.update_color)
        self.ui.horizontalSlider_2.valueChanged.connect(self.update_color)
        self.ui.horizontalSlider_3.valueChanged.connect(self.update_color)

        # Renk güncellemesi ilk başta da yapılmalı
        self.update_color()

    def update_color(self):
        r = self.ui.horizontalSlider.value()
        g = self.ui.horizontalSlider_2.value()
        b = self.ui.horizontalSlider_3.value()

        # LineEdit'leri güncelle
        self.ui.lineEdit.setText(str(r))
        self.ui.lineEdit_2.setText(str(g))
        self.ui.lineEdit_3.setText(str(b))

        # Yeni stili ayarla
        style = f"background-color: rgb({r}, {g}, {b});"
        self.ui.frame.setStyleSheet(style)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
