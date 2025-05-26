# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'q2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
 
 
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(429, 151)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 2, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 3, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 2, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 1, 0, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(Form)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 2, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 2, 3, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 1, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.pushButton.clicked.connect(partial(self.buttonClicked,"1"))    ###
        self.pushButton_2.clicked.connect(partial(self.buttonClicked,"2"))  ###
        self.pushButton_3.clicked.connect(partial(self.buttonClicked,"3"))  ### 
        self.pushButton_8.clicked.connect(partial(self.buttonClicked,"4"))  ###
        self.pushButton_5.clicked.connect(partial(self.buttonClicked,"5"))  ###
        self.pushButton_6.clicked.connect(partial(self.buttonClicked,"6"))  ###
        self.pushButton_12.clicked.connect(partial(self.buttonClicked,"7")) ###
        self.pushButton_9.clicked.connect(partial(self.buttonClicked,"8"))  ###
        self.pushButton_10.clicked.connect(partial(self.buttonClicked,"9")) ###
        self.pushButton_4.clicked.connect(partial(self.buttonClicked,"+"))  ###
        self.pushButton_7.clicked.connect(partial(self.buttonClicked,"-"))  ###
        self.pushButton_11.clicked.connect(partial(self.buttonClicked,"*")) ###

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "0"))
        self.pushButton_10.setText(_translate("Form", "9"))
        self.pushButton.setText(_translate("Form", "1"))
        self.pushButton_2.setText(_translate("Form", "2"))
        self.pushButton_4.setText(_translate("Form", "+"))
        self.pushButton_5.setText(_translate("Form", "5"))
        self.pushButton_3.setText(_translate("Form", "3"))
        self.pushButton_9.setText(_translate("Form", "8"))
        self.pushButton_8.setText(_translate("Form", "4"))
        self.pushButton_12.setText(_translate("Form", "7"))
        self.pushButton_6.setText(_translate("Form", "6"))
        self.pushButton_11.setText(_translate("Form", "*"))
        self.pushButton_7.setText(_translate("Form", "-"))

        self.flag=0 ###
        
    
    def buttonClicked(self,text): ###
      
        if self.flag==0:
            self.num1=int(text)
            self.label.setText(text)
            self.flag=1
        elif self.flag==1:
            self.operator=text
            self.label.setText(str(self.num1) + self.operator)
            self.flag=2
        elif self.flag==2:
            self.num2=int(text)
            self.flag=3
        
            
        if self.flag==3:
            if self.operator=="+":
                res = self.num1+self.num2
            elif self.operator=="-":
                res = self.num1-self.num2
            else:
                res = self.num1*self.num2
            out=(str(self.num1) + self.operator + str(self.num2) + "=" + str(res))
            self.label.setText(out)
            self.flag=0
    