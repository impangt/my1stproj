# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectPoliciesDialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(590, 529)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(360, 490, 161, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.listWidgetBuy = QtWidgets.QListWidget(Dialog)
        self.listWidgetBuy.setGeometry(QtCore.QRect(40, 40, 241, 181))
        self.listWidgetBuy.setObjectName("listWidgetBuy")
        self.listWidgetSell = QtWidgets.QListWidget(Dialog)
        self.listWidgetSell.setGeometry(QtCore.QRect(310, 40, 241, 181))
        self.listWidgetSell.setObjectName("listWidgetSell")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 20, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(320, 20, 91, 16))
        self.label_2.setObjectName("label_2")
        self.checkBoxBuySelectAll = QtWidgets.QCheckBox(Dialog)
        self.checkBoxBuySelectAll.setGeometry(QtCore.QRect(50, 230, 111, 16))
        self.checkBoxBuySelectAll.setObjectName("checkBoxBuySelectAll")
        self.checkBoxSellSelectAll = QtWidgets.QCheckBox(Dialog)
        self.checkBoxSellSelectAll.setGeometry(QtCore.QRect(330, 230, 111, 16))
        self.checkBoxSellSelectAll.setObjectName("checkBoxSellSelectAll")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(40, 310, 511, 131))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.tableWidget.setFont(font)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.Panel)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 280, 161, 16))
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 450, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 450, 91, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(47, 260, 501, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Dialog)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.pushButton_3.clicked.connect(Dialog.resetedit)
        self.pushButton_4.clicked.connect(Dialog.savechanges)
        self.checkBoxBuySelectAll.clicked.connect(Dialog.selectall1)
        self.checkBoxSellSelectAll.clicked.connect(Dialog.selectall2)
        self.buttonBox.accepted.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "buy policies"))
        self.label_2.setText(_translate("Dialog", "sell policies"))
        self.checkBoxBuySelectAll.setText(_translate("Dialog", "Select All"))
        self.checkBoxSellSelectAll.setText(_translate("Dialog", "Select All"))
        self.label_3.setText(_translate("Dialog", "properties setting"))
        self.pushButton_3.setText(_translate("Dialog", "Reset"))
        self.pushButton_4.setText(_translate("Dialog", "Save Changes"))

