# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_diary_entry.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(399, 361)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.lbl_date = QtWidgets.QLabel(Dialog)
        self.lbl_date.setObjectName("lbl_date")
        self.verticalLayout.addWidget(self.lbl_date)
        self.lbl_time = QtWidgets.QLabel(Dialog)
        self.lbl_time.setObjectName("lbl_time")
        self.verticalLayout.addWidget(self.lbl_time)
        self.txt_diary = QtWidgets.QTextEdit(Dialog)
        self.txt_diary.setObjectName("txt_diary")
        self.verticalLayout.addWidget(self.txt_diary)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_cancel = QtWidgets.QPushButton(Dialog)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.btn_save = QtWidgets.QPushButton(Dialog)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; text-decoration: underline;\">New Diary Entry</span></p></body></html>"))
        self.lbl_date.setText(_translate("Dialog", "Date"))
        self.lbl_time.setText(_translate("Dialog", "Time"))
        self.btn_cancel.setText(_translate("Dialog", "Cancel"))
        self.btn_save.setText(_translate("Dialog", "Save"))

