# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'myMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 521)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.selectButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectButton.setMaximumSize(QtCore.QSize(80, 25))
        self.selectButton.setObjectName("selectButton")
        self.horizontalLayout.addWidget(self.selectButton)
        self.iniButton = QtWidgets.QPushButton(self.centralwidget)
        self.iniButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iniButton.sizePolicy().hasHeightForWidth())
        self.iniButton.setSizePolicy(sizePolicy)
        self.iniButton.setMaximumSize(QtCore.QSize(40, 25))
        self.iniButton.setObjectName("iniButton")
        self.horizontalLayout.addWidget(self.iniButton)
        self.buttonCursor = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCursor.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonCursor.sizePolicy().hasHeightForWidth())
        self.buttonCursor.setSizePolicy(sizePolicy)
        self.buttonCursor.setMaximumSize(QtCore.QSize(40, 25))
        self.buttonCursor.setObjectName("buttonCursor")
        self.horizontalLayout.addWidget(self.buttonCursor)
        self.buttonK = QtWidgets.QPushButton(self.centralwidget)
        self.buttonK.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonK.sizePolicy().hasHeightForWidth())
        self.buttonK.setSizePolicy(sizePolicy)
        self.buttonK.setMaximumSize(QtCore.QSize(40, 25))
        self.buttonK.setObjectName("buttonK")
        self.horizontalLayout.addWidget(self.buttonK)
        self.labelDateFrom = QtWidgets.QLabel(self.centralwidget)
        self.labelDateFrom.setMinimumSize(QtCore.QSize(70, 25))
        self.labelDateFrom.setMaximumSize(QtCore.QSize(100, 25))
        self.labelDateFrom.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.labelDateFrom.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelDateFrom.setObjectName("labelDateFrom")
        self.horizontalLayout.addWidget(self.labelDateFrom)
        self.spinBoxFrom = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxFrom.setMaximumSize(QtCore.QSize(40, 25))
        self.spinBoxFrom.setObjectName("spinBoxFrom")
        self.horizontalLayout.addWidget(self.spinBoxFrom)
        self.labelDateTo = QtWidgets.QLabel(self.centralwidget)
        self.labelDateTo.setMinimumSize(QtCore.QSize(70, 25))
        self.labelDateTo.setMaximumSize(QtCore.QSize(100, 25))
        self.labelDateTo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelDateTo.setObjectName("labelDateTo")
        self.horizontalLayout.addWidget(self.labelDateTo)
        self.spinBoxTo = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBoxTo.setMaximumSize(QtCore.QSize(40, 25))
        self.spinBoxTo.setObjectName("spinBoxTo")
        self.horizontalLayout.addWidget(self.spinBoxTo)
        self.labelDays = QtWidgets.QLabel(self.centralwidget)
        self.labelDays.setMinimumSize(QtCore.QSize(50, 0))
        self.labelDays.setMaximumSize(QtCore.QSize(50, 25))
        self.labelDays.setObjectName("labelDays")
        self.horizontalLayout.addWidget(self.labelDays)
        spacerItem = QtWidgets.QSpacerItem(40, 25, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.applyButton = QtWidgets.QPushButton(self.centralwidget)
        self.applyButton.setMaximumSize(QtCore.QSize(100, 25))
        self.applyButton.setObjectName("applyButton")
        self.horizontalLayout.addWidget(self.applyButton)
        self.loadstButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadstButton.setEnabled(False)
        self.loadstButton.setMaximumSize(QtCore.QSize(80, 25))
        self.loadstButton.setAutoRepeat(False)
        self.loadstButton.setObjectName("loadstButton")
        self.horizontalLayout.addWidget(self.loadstButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelResult.sizePolicy().hasHeightForWidth())
        self.labelResult.setSizePolicy(sizePolicy)
        self.labelResult.setMaximumSize(QtCore.QSize(10000, 25))
        self.labelResult.setBaseSize(QtCore.QSize(0, 0))
        self.labelResult.setAutoFillBackground(False)
        self.labelResult.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelResult.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.labelResult.setWordWrap(True)
        self.labelResult.setObjectName("labelResult")
        self.horizontalLayout_2.addWidget(self.labelResult)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.labelX = QtWidgets.QLabel(self.centralwidget)
        self.labelX.setMinimumSize(QtCore.QSize(80, 0))
        self.labelX.setMaximumSize(QtCore.QSize(10000, 25))
        self.labelX.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.labelX.setObjectName("labelX")
        self.horizontalLayout_2.addWidget(self.labelX)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.mainWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainWidget.sizePolicy().hasHeightForWidth())
        self.mainWidget.setSizePolicy(sizePolicy)
        self.mainWidget.setMinimumSize(QtCore.QSize(400, 10))
        self.mainWidget.setObjectName("mainWidget")
        self.verticalLayout.addWidget(self.mainWidget)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 23))
        self.menubar.setObjectName("menubar")
        self.menuMy_system = QtWidgets.QMenu(self.menubar)
        self.menuMy_system.setObjectName("menuMy_system")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.menuMy_system.addAction(self.actionOpen_File)
        self.menubar.addAction(self.menuMy_system.menuAction())

        self.retranslateUi(MainWindow)
        self.selectButton.clicked.connect(MainWindow.openButtonClicked)
        self.applyButton.clicked.connect(MainWindow.applyButtonClicked)
        self.loadstButton.clicked.connect(MainWindow.lookbackButtonClicked)
        self.iniButton.clicked.connect(MainWindow.iniButtonClicked)
        self.spinBoxFrom.valueChanged['int'].connect(MainWindow.fromOneDayChanged)
        self.spinBoxTo.valueChanged['int'].connect(MainWindow.toOneDayChanged)
        self.buttonCursor.clicked.connect(MainWindow.cursorButtonClicked)
        self.buttonK.clicked.connect(MainWindow.kButtonClicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.selectButton.setText(_translate("MainWindow", "Select File"))
        self.iniButton.setText(_translate("MainWindow", "I"))
        self.buttonCursor.setText(_translate("MainWindow", "+"))
        self.buttonK.setText(_translate("MainWindow", "K"))
        self.labelDateFrom.setText(_translate("MainWindow", "Date From"))
        self.labelDateTo.setText(_translate("MainWindow", "Date To"))
        self.labelDays.setText(_translate("MainWindow", "  xx Days"))
        self.applyButton.setText(_translate("MainWindow", "Set Strategy"))
        self.loadstButton.setText(_translate("MainWindow", "computing"))
        self.labelResult.setText(_translate("MainWindow", "Hello, welcome to my analysis system"))
        self.labelX.setText(_translate("MainWindow", "  x value"))
        self.menuMy_system.setTitle(_translate("MainWindow", "Files"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))

