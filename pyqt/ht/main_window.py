# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(895, 774)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tab_main = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_main.setObjectName("tab_main")
        self.graph = QtWidgets.QWidget()
        self.graph.setObjectName("graph")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.graph)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter = QtWidgets.QSplitter(self.graph)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.graph_container = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.graph_container.setObjectName("graph_container")
        self.frame = QtWidgets.QFrame(self.splitter)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.label_2 = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.line_graph_year = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_graph_year.sizePolicy().hasHeightForWidth())
        self.line_graph_year.setSizePolicy(sizePolicy)
        self.line_graph_year.setObjectName("line_graph_year")
        self.verticalLayout_4.addWidget(self.line_graph_year)
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.line_graph_month = QtWidgets.QLineEdit(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_graph_month.sizePolicy().hasHeightForWidth())
        self.line_graph_month.setSizePolicy(sizePolicy)
        self.line_graph_month.setObjectName("line_graph_month")
        self.verticalLayout_4.addWidget(self.line_graph_month)
        self.btn_update_graph = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_update_graph.sizePolicy().hasHeightForWidth())
        self.btn_update_graph.setSizePolicy(sizePolicy)
        self.btn_update_graph.setObjectName("btn_update_graph")
        self.verticalLayout_4.addWidget(self.btn_update_graph)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem)
        self.toolBox = QtWidgets.QToolBox(self.frame)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 819, 380))
        self.page.setObjectName("page")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 819, 380))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.cmb_thread_select = QtWidgets.QComboBox(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb_thread_select.sizePolicy().hasHeightForWidth())
        self.cmb_thread_select.setSizePolicy(sizePolicy)
        self.cmb_thread_select.setObjectName("cmb_thread_select")
        self.verticalLayout_7.addWidget(self.cmb_thread_select)
        self.btn_add_graph_item = QtWidgets.QPushButton(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add_graph_item.sizePolicy().hasHeightForWidth())
        self.btn_add_graph_item.setSizePolicy(sizePolicy)
        self.btn_add_graph_item.setObjectName("btn_add_graph_item")
        self.verticalLayout_7.addWidget(self.btn_add_graph_item)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem1)
        self.label_9 = QtWidgets.QLabel(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        self.lst_active_graph_items = QtWidgets.QListWidget(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lst_active_graph_items.sizePolicy().hasHeightForWidth())
        self.lst_active_graph_items.setSizePolicy(sizePolicy)
        self.lst_active_graph_items.setObjectName("lst_active_graph_items")
        self.verticalLayout_7.addWidget(self.lst_active_graph_items)
        self.btn_remove_graph_item = QtWidgets.QPushButton(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_remove_graph_item.sizePolicy().hasHeightForWidth())
        self.btn_remove_graph_item.setSizePolicy(sizePolicy)
        self.btn_remove_graph_item.setObjectName("btn_remove_graph_item")
        self.verticalLayout_7.addWidget(self.btn_remove_graph_item)
        self.btn_remove_graph_item.raise_()
        self.label_9.raise_()
        self.lst_active_graph_items.raise_()
        self.cmb_thread_select.raise_()
        self.label_6.raise_()
        self.btn_add_graph_item.raise_()
        self.toolBox.addItem(self.page_2, "")
        self.verticalLayout_4.addWidget(self.toolBox)
        self.verticalLayout_3.addWidget(self.splitter)
        self.tab_main.addTab(self.graph, "")
        self.diary = QtWidgets.QWidget()
        self.diary.setObjectName("diary")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.diary)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.diary)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.line_diary_year = QtWidgets.QLineEdit(self.diary)
        self.line_diary_year.setObjectName("line_diary_year")
        self.horizontalLayout_2.addWidget(self.line_diary_year)
        self.label_3 = QtWidgets.QLabel(self.diary)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.line_diary_month = QtWidgets.QLineEdit(self.diary)
        self.line_diary_month.setObjectName("line_diary_month")
        self.horizontalLayout_2.addWidget(self.line_diary_month)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.btn_diary_update = QtWidgets.QPushButton(self.diary)
        self.btn_diary_update.setObjectName("btn_diary_update")
        self.verticalLayout_2.addWidget(self.btn_diary_update)
        self.line = QtWidgets.QFrame(self.diary)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.scrollArea = QtWidgets.QScrollArea(self.diary)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 98, 96))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.diary_text = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.diary_text.setObjectName("diary_text")
        self.verticalLayout_5.addWidget(self.diary_text)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.btn_new_diary_entry = QtWidgets.QPushButton(self.diary)
        self.btn_new_diary_entry.setObjectName("btn_new_diary_entry")
        self.verticalLayout_2.addWidget(self.btn_new_diary_entry)
        self.tab_main.addTab(self.diary, "")
        self.settings = QtWidgets.QWidget()
        self.settings.setObjectName("settings")
        self.tab_main.addTab(self.settings, "")
        self.about = QtWidgets.QWidget()
        self.about.setObjectName("about")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.about)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.about)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.tab_main.addTab(self.about, "")
        self.verticalLayout.addWidget(self.tab_main)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.btn_test = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_test.sizePolicy().hasHeightForWidth())
        self.btn_test.setSizePolicy(sizePolicy)
        self.btn_test.setObjectName("btn_test")
        self.horizontalLayout_3.addWidget(self.btn_test)
        self.btn_quit = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_quit.sizePolicy().hasHeightForWidth())
        self.btn_quit.setSizePolicy(sizePolicy)
        self.btn_quit.setObjectName("btn_quit")
        self.horizontalLayout_3.addWidget(self.btn_quit, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tab_main.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "HealthTracker"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Graph Settings</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Year: "))
        self.label.setText(_translate("MainWindow", "Month:"))
        self.btn_update_graph.setText(_translate("MainWindow", "Update Data"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "New Event"))
        self.label_6.setText(_translate("MainWindow", "Thread"))
        self.btn_add_graph_item.setText(_translate("MainWindow", "Add To Graph"))
        self.label_9.setText(_translate("MainWindow", "Current Graph Items:"))
        self.btn_remove_graph_item.setText(_translate("MainWindow", "Remove From Graph"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Customize Graph"))
        self.tab_main.setTabText(self.tab_main.indexOf(self.graph), _translate("MainWindow", "Graph"))
        self.label_4.setText(_translate("MainWindow", "Year"))
        self.label_3.setText(_translate("MainWindow", "Month"))
        self.btn_diary_update.setText(_translate("MainWindow", "Show"))
        self.btn_new_diary_entry.setText(_translate("MainWindow", "New Diary Entry"))
        self.tab_main.setTabText(self.tab_main.indexOf(self.diary), _translate("MainWindow", "Diary"))
        self.tab_main.setTabText(self.tab_main.indexOf(self.settings), _translate("MainWindow", "Settings"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">HealthTracker</span> is a program to help you and your doctor communicate</p><p align=\"center\">and effectively manage your health. Moreover, it is a useful tool to help</p><p align=\"center\">you set and keep track of personal goals such as diet and</p><p align=\"center\">exercise, and monitor their effect on your wellbeing.</p><p align=\"center\"><br/></p><p align=\"center\">This is a prototype intended to explore and refine eventual features.</p><p align=\"center\"><br/></p><p align=\"center\">Copyright Oleg Petelin 2016</p></body></html>"))
        self.tab_main.setTabText(self.tab_main.indexOf(self.about), _translate("MainWindow", "About"))
        self.btn_test.setText(_translate("MainWindow", "QuickThreads"))
        self.btn_quit.setText(_translate("MainWindow", "Quit"))

