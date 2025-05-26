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

        self.ui.pushButton_run.clicked.connect(self.run_prime_logic)

    def run_prime_logic(self):
        self.ui.textEdit.clear()
        self.ui.label_status.setText("Status")

        try:
            # 1. Kullanıcıdan sayı al ve kontrol et
            number = int(self.ui.lineEdit_enterNumber.text())
            if number < 2:
                raise ValueError("Number must be >= 2")

            # 2. Asal sayı listesini hesapla
            prime_list = self.calculate_primes(number)

            # 3. Seçilen işleme göre devam et
            selected_action = self.ui.comboBox.currentText()

            if selected_action == "Print the text box":
                self.print_text_box(prime_list)
                self.ui.label_status.setText("Printing the text box")
            elif selected_action == "Write the file":
                self.print_file(prime_list)
                self.ui.label_status.setText("Writing to the file")

        except ValueError:
            self.ui.label_status.setText("ERROR: Input must be valid number")

    def calculate_primes(self, n):
        primes = []
        for num in range(2, n + 1):
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
        return primes

    def print_text_box(self, prime_list):
        text = " ".join(str(p) for p in prime_list)
        self.ui.textEdit.setText(text)

    def print_file(self, prime_list):
        with open("primes.txt", "w") as f:
            for prime in prime_list:
                f.write(f"{prime}\n")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = PrimeApp()
    win.show()
    sys.exit(app.exec_())
