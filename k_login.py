# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QCompleter, QComboBox
import os
import subprocess
import PyQt5_stylesheets
from custom_widgets import *

class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(291, 414)
        MainWindow.setStyleSheet(PyQt5_stylesheets.load_stylesheet_pyqt5(style="style_blue"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 301, 31))
        self.label.setStyleSheet("font: 63 20pt \"URW Bookman [UKWN]\";\n""")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(-10, -10, 301, 481))
        self.label_4.setStyleSheet("background-color: rgb(170, 255, 255)")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        
        self.comboBox = ComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(75, 120, 151, 31))
        self.comboBox.setObjectName("comboBox")
        
        self.comboBox.setEditable(True) 
        self.comboBox.completer().setCompletionMode(QtWidgets.QCompleter.PopupCompletion) 
        self.comboBox.setInsertPolicy(QComboBox.NoInsert) 
        
        self.comboBox.setCurrentIndex(-1)
        self.comboBox.lineEdit().setPlaceholderText("-- Select Preset --") 

        self.button_launch_ui = QtWidgets.QPushButton(self.centralwidget)
        self.button_launch_ui.setGeometry(QtCore.QRect(90, 200, 121, 50))
        self.button_launch_ui.setObjectName("launch_ui")

       
        self.label_4.raise_()
        self.label.raise_()
        self.comboBox.raise_()
        
       
        self.button_launch_ui.raise_()

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Automation Training"))
        
        
        self.button_launch_ui.setText(_translate("MainWindow", "Launch UI"))
    
        
            
            
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
