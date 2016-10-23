# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'err_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Error(object):
    def setupUi(self, Error):
        Error.setObjectName("Error")
        Error.resize(288, 187)
        self.verticalLayout = QtWidgets.QVBoxLayout(Error)
        self.verticalLayout.setObjectName("verticalLayout")
        self.err_label = QtWidgets.QLabel(Error)
        self.err_label.setObjectName("err_label")
        self.verticalLayout.addWidget(self.err_label)
        self.btn_ok = QtWidgets.QPushButton(Error)
        self.btn_ok.setObjectName("btn_ok")
        self.verticalLayout.addWidget(self.btn_ok)

        self.retranslateUi(Error)
        QtCore.QMetaObject.connectSlotsByName(Error)

    def retranslateUi(self, Error):
        _translate = QtCore.QCoreApplication.translate
        Error.setWindowTitle(_translate("Error", "Dialog"))
        self.err_label.setText(_translate("Error", "<html><head/><body><p align=\"center\">Error Text</p></body></html>"))
        self.btn_ok.setText(_translate("Error", "OK"))

