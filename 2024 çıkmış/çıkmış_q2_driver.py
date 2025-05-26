# -*- coding: utf-8 -*-
"""
Created on Tue May 27 00:04:05 2025

@author: omrky
"""

import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from çıkmış_q2 import Ui_MainWindow  # ui dosyasının pyuic5 ile çevrilmiş hali

class NumberOperationsApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Başlangıçta toggle butonlar ve combobox pasif
        self.ui.radioButton_max.setEnabled(False)
        self.ui.radioButton_min.setEnabled(False)
        self.ui.radioButton_sort.setEnabled(False)
        self.ui.comboBox.setEnabled(False)
        self.ui.radioButton_reverse.setEnabled(False)

        self.numbers = []

        # Buton tıklama eventleri
        self.ui.pushButton_generate.clicked.connect(self.generate_numbers)
        self.ui.radioButton_max.toggled.connect(self.max_number)
        self.ui.radioButton_min.toggled.connect(self.min_number)
        self.ui.radioButton_sort.toggled.connect(self.sort_numbers)
        self.ui.comboBox.currentIndexChanged.connect(self.sort_numbers)  # combo box değişince de sort yenilensin
        self.ui.radioButton_reverse.toggled.connect(self.reverse_numbers)

    def generate_numbers(self):
        self.numbers = [random.randint(0, 100) for _ in range(40)]
        self.ui.textEdit_numbers.setPlainText(", ".join(map(str, self.numbers)))
        self.ui.label_numbers.setText("Numbers are generated")
        
        # Toggle butonları ve combo box etkinleştir
        self.ui.radioButton_max.setEnabled(True)
        self.ui.radioButton_min.setEnabled(True)
        self.ui.radioButton_sort.setEnabled(True)
        self.ui.comboBox.setEnabled(False)  # Combo box sadece sort seçilince aktif olur
        self.ui.radioButton_reverse.setEnabled(True)
        self.ui.label_status.setText("Numbers are generated")
        
        # Toggle butonları sıfırla (pasif)
        self.ui.radioButton_max.setChecked(False)
        self.ui.radioButton_min.setChecked(False)
        self.ui.radioButton_sort.setChecked(False)
        self.ui.radioButton_reverse.setChecked(False)

    def max_number(self, checked):
        if checked:
            maximum = max(self.numbers)
            self.ui.textEdit_result.setPlainText(str(maximum))
            self.ui.label_status.setText("Maximum number is determined")
            self.ui.comboBox.setEnabled(False)

    def min_number(self, checked):
        if checked:
            minimum = min(self.numbers)
            self.ui.textEdit_result.setPlainText(str(minimum))
            self.ui.label_status.setText("Minimum number is determined")
            self.ui.comboBox.setEnabled(False)

    def sort_numbers(self):
        if not self.ui.radioButton_sort.isChecked():
            return
        
        ascending = self.ui.comboBox.currentIndex() == 0
        sorted_list = sorted(self.numbers, reverse=not ascending)
        self.ui.textEdit_result.setPlainText(", ".join(map(str, sorted_list)))
        
        if ascending:
            self.ui.label_status.setText("Numbers are sorted in ascending order")
        else:
            self.ui.label_status.setText("Numbers are sorted in descending order")
        
        self.ui.comboBox.setEnabled(True)

    def reverse_numbers(self, checked):
        if checked:
            reversed_list = list(reversed(self.numbers))
            self.ui.textEdit_result.setPlainText(", ".join(map(str, reversed_list)))
            self.ui.label_status.setText("Numbers are reversed")
            self.ui.comboBox.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NumberOperationsApp()
    window.show()
    sys.exit(app.exec_())
