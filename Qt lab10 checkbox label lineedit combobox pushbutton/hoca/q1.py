# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1a_v2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Ui_Form(object):
    def setupUi(self, Form):
        
        self.flagBold=False
        self.flagItalic=False
        self.flagUnderline=False
        self.flagStrikeout=False
        
        Form.setObjectName("Form")
        Form.resize(563, 392)
        font = QtGui.QFont()
        font.setUnderline(False)
        Form.setFont(font)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 180, 51, 20))
        self.lineEdit.setObjectName("lineEdit")
        
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.addItem("Red")
        self.comboBox.addItem("Green")
        self.comboBox.addItem("Blue")
        self.comboBox.addItem("Black")
        self.comboBox.setGeometry(QtCore.QRect(230, 180, 69, 22))
        
        self.comboBox.setObjectName("comboBox")
        
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(330, 180, 75, 23))
        
        self.pushButton.setObjectName("pushButton")
        
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 160, 47, 13))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(240, 160, 47, 13))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(220, 70, 161, 61))
        
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(140, 260, 70, 17))
        
        self.checkBox.setObjectName("checkBox")
        
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(210, 260, 70, 17))
        
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(260, 260, 70, 17))
        
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setGeometry(QtCore.QRect(340, 260, 70, 17))
        
        self.checkBox_4.setObjectName("checkBox_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        
        self.lineEdit.textChanged[str].connect(self.onChanged)  ###
        self.comboBox.activated[str].connect(self.onActivated)  ###
        self.pushButton.clicked.connect(self.buttonClicked)     ###
        font = QtGui.QFont()                                    ###    
        font.setPointSize(20)                                   ###
        self.checkBox.stateChanged.connect(self.changeBold)     ###
        self.checkBox_2.stateChanged.connect(self.changeItalic) ###
        self.checkBox_3.stateChanged.connect(self.changeUnderline)  ###
        self.checkBox_4.stateChanged.connect(self.changeStrikeout)  ###
        
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Update Text"))
        self.label.setText(_translate("Form", "Size"))
        self.label_3.setText(_translate("Form", "Color"))
        self.label_4.setText(_translate("Form", "Python"))
        self.checkBox.setText(_translate("Form", "Bold"))
        self.checkBox_2.setText(_translate("Form", "Italic"))
        self.checkBox_3.setText(_translate("Form", "Underline"))
        self.checkBox_4.setText(_translate("Form", "Strikeout"))

    def onChanged(self,text):   ###
        self.font_size=int(text)   
        print(self.font_size)
        
    def onActivated(self,text): ###
        self.Color=text
        print(self.Color) 
        
    def changeBold(self,state): ###
        if state== Qt.Checked:
            self.flagBold=True
        else:
            self.flagBold=False
        
    def changeItalic(self,state):   ###
        if state== Qt.Checked:
            self.flagItalic=True
        else:
            self.flagItalic=False
    
    def changeUnderline(self,state):    ###
        if state== Qt.Checked:
            self.flagUnderline=True
        else:
            self.flagUnderline=False
    
    def changeStrikeout(self,state):    ###
        if state== Qt.Checked:
            self.flagStrikeout=True
        else:
            self.flagStrikeout=False
        
    def buttonClicked(self):    ###
        
        if self.Color == "Red":
            self.label_4.setStyleSheet("color: red")
        elif self.Color == "Green":
            self.label_4.setStyleSheet("color: green")
        elif self.Color == "Blue":
            self.label_4.setStyleSheet("color: blue")
        elif self.Color == "Black":
            self.label_4.setStyleSheet("color: black")
        
        font = QtGui.QFont()
        font.setPointSize(self.font_size)
        font.setBold(self.flagBold)
        font.setItalic(self.flagItalic)
        font.setUnderline(self.flagUnderline)
        font.setStrikeOut(self.flagStrikeout)
        self.label_4.setFont(font)    
        
       