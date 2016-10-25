# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_slider_threads_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(601, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2, 0, QtCore.Qt.AlignTop)
        self.chk_high_is_good = QtWidgets.QCheckBox(Dialog)
        self.chk_high_is_good.setEnabled(True)
        self.chk_high_is_good.setChecked(True)
        self.chk_high_is_good.setObjectName("chk_high_is_good")
        self.verticalLayout_4.addWidget(self.chk_high_is_good)
        self.text_entry = QtWidgets.QLineEdit(Dialog)
        self.text_entry.setObjectName("text_entry")
        self.verticalLayout_4.addWidget(self.text_entry)
        self.btn_add = QtWidgets.QPushButton(Dialog)
        self.btn_add.setObjectName("btn_add")
        self.verticalLayout_4.addWidget(self.btn_add)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.thread_list = QtWidgets.QListWidget(Dialog)
        self.thread_list.setObjectName("thread_list")
        self.verticalLayout_3.addWidget(self.thread_list)
        self.btn_remove = QtWidgets.QPushButton(Dialog)
        self.btn_remove.setObjectName("btn_remove")
        self.verticalLayout_3.addWidget(self.btn_remove)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_ok = QtWidgets.QPushButton(Dialog)
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout.addWidget(self.btn_ok)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; text-decoration: underline;\">New QuickThread:</span></p><p align=\"center\">Add a new QuickThread name below, </p><p align=\"center\">then press Add</p></body></html>"))
        self.chk_high_is_good.setText(_translate("Dialog", "High score is good"))
        self.btn_add.setText(_translate("Dialog", "Add"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; text-decoration: underline;\">Current QuickThreads:</span></p><p align=\"center\">To remove, select entry and press Remove</p></body></html>"))
        self.btn_remove.setText(_translate("Dialog", "Remove"))
        self.btn_ok.setText(_translate("Dialog", "OK"))

