# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reddit_content_downloader.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(649, 336)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(330, 20, 296, 161))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.topComboBox = QtWidgets.QComboBox(self.groupBox)
        self.topComboBox.setObjectName("topComboBox")
        self.topComboBox.addItem("")
        self.topComboBox.addItem("")
        self.topComboBox.addItem("")
        self.topComboBox.addItem("")
        self.topComboBox.addItem("")
        self.horizontalLayout.addWidget(self.topComboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.limitSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.limitSpinBox.setMinimum(1)
        self.limitSpinBox.setMaximum(1000)
        self.limitSpinBox.setObjectName("limitSpinBox")
        self.horizontalLayout_2.addWidget(self.limitSpinBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.downloadButton = QtWidgets.QPushButton(self.widget)
        self.downloadButton.setObjectName("downloadButton")
        self.horizontalLayout_3.addWidget(self.downloadButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cancelButton = QtWidgets.QPushButton(self.widget)
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_4.addWidget(self.cancelButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(10, 20, 261, 238))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.treeViewSubs = QtWidgets.QTreeView(self.widget1)
        self.treeViewSubs.setObjectName("treeViewSubs")
        self.verticalLayout_2.addWidget(self.treeViewSubs)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.subredditName = QtWidgets.QLineEdit(self.widget1)
        self.subredditName.setObjectName("subredditName")
        self.horizontalLayout_5.addWidget(self.subredditName)
        self.addButton = QtWidgets.QPushButton(self.widget1)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout_5.addWidget(self.addButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(10, 260, 131, 32))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.deleteButton = QtWidgets.QPushButton(self.widget2)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout_9.addWidget(self.deleteButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 649, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.menuFile.addAction(self.actionImport)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reddit Content Downloader"))
        self.groupBox.setTitle(_translate("MainWindow", "Parameters"))
        self.label.setText(_translate("MainWindow", "Top"))
        self.topComboBox.setItemText(0, _translate("MainWindow", "Day"))
        self.topComboBox.setItemText(1, _translate("MainWindow", "Week"))
        self.topComboBox.setItemText(2, _translate("MainWindow", "Month"))
        self.topComboBox.setItemText(3, _translate("MainWindow", "Year"))
        self.topComboBox.setItemText(4, _translate("MainWindow", "All time"))
        self.label_2.setText(_translate("MainWindow", "Download limit"))
        self.downloadButton.setText(_translate("MainWindow", "Download"))
        self.cancelButton.setText(_translate("MainWindow", "Cancel"))
        self.addButton.setText(_translate("MainWindow", "Add"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
