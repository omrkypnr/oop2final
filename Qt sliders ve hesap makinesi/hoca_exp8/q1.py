# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'q1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        Form.setAutoFillBackground(True)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(40, 20, 301, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 120, 77, 81))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setText("0")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setText("0")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setAutoFillBackground(True)
        self.label_6.setText("0")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(90, 120, 211, 80))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalSlider = QtWidgets.QSlider(self.widget1)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_3.addWidget(self.horizontalSlider)
        self.horizontalSlider_2 = QtWidgets.QSlider(self.widget1)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.verticalLayout_3.addWidget(self.horizontalSlider_2)
        self.horizontalSlider_3 = QtWidgets.QSlider(self.widget1)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.verticalLayout_3.addWidget(self.horizontalSlider_3)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        
        self.horizontalSlider.valueChanged.connect(self.valuechange) ###
        self.horizontalSlider_3.valueChanged.connect(self.valuechange) ###
        self.horizontalSlider_2.valueChanged.connect(self.valuechange) ###
        
        self.frame.raise_()     ###
        self.label.raise_()     ###
        self.label_2.raise_()   ###
        self.label_3.raise_()   ###
        self.horizontalSlider.raise_()  ###
        self.horizontalSlider_2.raise_()###
        self.horizontalSlider_3.raise_()###
        self.horizontalSlider.raise_()  ###
        
        self.horizontalSlider.setMaximum(255)   ###
        self.horizontalSlider_2.setMaximum(255) ###
        self.horizontalSlider_3.setMaximum(255) ###

        
        self.horizontalSlider.valueChanged['int'].connect(self.label_5.setNum)   ###   
        self.horizontalSlider_2.valueChanged['int'].connect(self.label_4.setNum) ###
        self.horizontalSlider_3.valueChanged['int'].connect(self.label_6.setNum) ###
        
        self.col = QColor(0, 0, 0) ###

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "R:"))
        self.label_2.setText(_translate("Form", "G:"))
        self.label_3.setText(_translate("Form", "B:"))
		
	
    def valuechange(self): ###
        
        valR = self.horizontalSlider.value()
        valG = self.horizontalSlider_2.value()
        valB = self.horizontalSlider_3.value()
        
		
        self.col.setRed(valR)                
        self.col.setGreen(valG)             
        self.col.setBlue(valB) 
            
        self.frame.setStyleSheet("QFrame { background-color: %s }" %
            self.col.name())  

