# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName(_fromUtf8("dialog"))
        dialog.resize(210, 125)
        self.verticalLayout = QtGui.QVBoxLayout(dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.btn_exit = QtGui.QPushButton(dialog)
        self.btn_exit.setObjectName(_fromUtf8("btn_exit"))
        self.verticalLayout.addWidget(self.btn_exit)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(_translate("dialog", "Dialog", None))
        self.label.setText(_translate("dialog", "<html><head/><body><p align=\"center\">This is a new window!</p></body></html>", None))
        self.btn_exit.setText(_translate("dialog", "Get me out of here!", None))

