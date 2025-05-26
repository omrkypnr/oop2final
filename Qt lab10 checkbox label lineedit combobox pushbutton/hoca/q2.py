# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '2a.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import random

class Ui_Form(object):
    def setupUi(self, Form):
        
        self.points=0
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 50, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(270, 80, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(250, 50, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(60, 120, 233, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.addItem("One")
        self.comboBox.addItem("Two")
        self.comboBox.addItem("Three")
        self.comboBox.addItem("Four")
        self.comboBox.addItem("Five")
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    
	
	
        self.pushButton.clicked.connect(self.buttonConfirm)     ###
        self.pushButton_2.clicked.connect(self.buttonClicked)   ###
        self.comboBox.activated[str].connect(self.onActivated)	###
	
	
	
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Number"))
        self.label_2.setText(_translate("Form", "0"))
        self.label_3.setText(_translate("Form", "Points"))
        self.pushButton.setText(_translate("Form", "Confirm"))
        self.pushButton_2.setText(_translate("Form", "Next Number"))

    def onActivated(self,text): ###
        self.choice=text
        print(self.choice) 
        
    def buttonClicked(self):    ###
        self.num=random.randint(1,5)
        print(self.num)
        self.label.setText(str(self.num))
    
    def buttonConfirm(self):    ###
        if self.num==1 and self.choice=="One":
            self.points += 10
        elif self.num==2 and self.choice=="Two": 
            self.points += 10
        elif self.num==3 and self.choice=="Three":  
            self.points += 10
        elif self.num==4 and self.choice=="Four":   
            self.points += 10
        elif self.num==5 and self.choice=="Five":   
            self.points += 10
            
        self.label_2.setText(str(self.points))   
        print(self.points)
            
            
            
            
            
            