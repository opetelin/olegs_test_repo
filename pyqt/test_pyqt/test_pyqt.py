# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_pyqt.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(582, 579)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setObjectName(_fromUtf8("tab"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.tab)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.listWidget = QtGui.QListWidget(self.tab)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout_3.addWidget(self.listWidget)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.open_folder_button = QtGui.QPushButton(self.tab)
        self.open_folder_button.setObjectName(_fromUtf8("open_folder_button"))
        self.horizontalLayout_3.addWidget(self.open_folder_button)
        self.btn_dialog = QtGui.QPushButton(self.tab)
        self.btn_dialog.setObjectName(_fromUtf8("btn_dialog"))
        self.horizontalLayout_3.addWidget(self.btn_dialog)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.tab_2)
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_5.addWidget(self.label)
        self.lcd = QtGui.QLCDNumber(self.tab_2)
        self.lcd.setObjectName(_fromUtf8("lcd"))
        self.verticalLayout_5.addWidget(self.lcd)
        self.lcd_slider = QtGui.QSlider(self.tab_2)
        self.lcd_slider.setOrientation(QtCore.Qt.Horizontal)
        self.lcd_slider.setObjectName(_fromUtf8("lcd_slider"))
        self.verticalLayout_5.addWidget(self.lcd_slider)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.graph_container = QtGui.QVBoxLayout()
        self.graph_container.setObjectName(_fromUtf8("graph_container"))
        self.verticalLayout_2.addLayout(self.graph_container)
        self.toolbar_container = QtGui.QVBoxLayout()
        self.toolbar_container.setObjectName(_fromUtf8("toolbar_container"))
        self.verticalLayout_2.addLayout(self.toolbar_container)
        self.btn_plot = QtGui.QPushButton(self.tab_3)
        self.btn_plot.setObjectName(_fromUtf8("btn_plot"))
        self.verticalLayout_2.addWidget(self.btn_plot)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.open_folder_button.setText(_translate("MainWindow", "Open Folder", None))
        self.btn_dialog.setText(_translate("MainWindow", "Show Test Dialog", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Button Test", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Move the slider to change LCD value.</p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Slider Test", None))
        self.btn_plot.setText(_translate("MainWindow", "Plot Stuff", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Graph Test", None))

