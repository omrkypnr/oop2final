# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Scripts.\final_working_q2.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(499, 386)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setMinimumSize(QtCore.QSize(361, 121))
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_enterNumber = QtWidgets.QLabel(self.centralwidget)
        self.label_enterNumber.setMinimumSize(QtCore.QSize(111, 31))
        self.label_enterNumber.setObjectName("label_enterNumber")
        self.horizontalLayout_2.addWidget(self.label_enterNumber)
        self.lineEdit_enterNumber = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_enterNumber.setMinimumSize(QtCore.QSize(251, 31))
        self.lineEdit_enterNumber.setObjectName("lineEdit_enterNumber")
        self.horizontalLayout_2.addWidget(self.lineEdit_enterNumber)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setMinimumSize(QtCore.QSize(251, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton_run = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_run.setMinimumSize(QtCore.QSize(101, 31))
        self.pushButton_run.setObjectName("pushButton_run")
        self.horizontalLayout.addWidget(self.pushButton_run)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setMinimumSize(QtCore.QSize(111, 31))
        self.label_status.setObjectName("label_status")
        self.verticalLayout.addWidget(self.label_status)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 499, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_run.clicked.connect(self.run_prime_logic)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_enterNumber.setText(_translate("MainWindow", "Enter Number"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Print the text box"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Write the file"))
        self.pushButton_run.setText(_translate("MainWindow", "RUN"))
        self.label_status.setText(_translate("MainWindow", "Status"))


    def run_prime_logic(self):
        self.textEdit.clear()
        self.label_status.setText("Status")

        try:
            # 1. Kullanıcıdan sayı al ve kontrol et
            number = int(self.lineEdit_enterNumber.text())
            if number < 2:
                raise ValueError("Number must be >= 2")

            # 2. Asal sayı listesini hesapla
            prime_list = self.calculate_primes(number)

            # 3. Seçilen işleme göre devam et
            selected_action = self.comboBox.currentText()

            if selected_action == "Print the text box":
                self.print_text_box(prime_list)
                self.label_status.setText("Printing the text box")
            elif selected_action == "Write the file":
                self.print_file(prime_list)
                self.label_status.setText("Writing to the file")

        except ValueError:
            self.label_status.setText("ERROR: Input must be valid number")

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
        self.textEdit.setText(text)

    def print_file(self, prime_list):
        with open("primes.txt", "w") as f:
            for prime in prime_list:
                f.write(f"{prime}\n")