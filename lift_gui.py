# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LIFT_GUI.ui'
#
# Created: Thu Nov 10 12:44:37 2016
#      by: PyQt4 UI code generator 4.11.3
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
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 551))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_general = QtGui.QWidget()
        self.tab_general.setObjectName(_fromUtf8("tab_general"))
        self.tabWidget.addTab(self.tab_general, _fromUtf8(""))
        self.tab_donor = QtGui.QWidget()
        self.tab_donor.setObjectName(_fromUtf8("tab_donor"))
        self.tabWidget.addTab(self.tab_donor, _fromUtf8(""))
        self.tab_receiver_stepper = QtGui.QWidget()
        self.tab_receiver_stepper.setObjectName(_fromUtf8("tab_receiver_stepper"))
        self.groupBox = QtGui.QGroupBox(self.tab_receiver_stepper)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 751, 161))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lcdNumber_receiver_stepper_x = QtGui.QLCDNumber(self.groupBox)
        self.lcdNumber_receiver_stepper_x.setGeometry(QtCore.QRect(20, 30, 121, 23))
        self.lcdNumber_receiver_stepper_x.setObjectName(_fromUtf8("lcdNumber_receiver_stepper_x"))
        self.pushButton_receiver_stepper_x_home = QtGui.QPushButton(self.groupBox)
        self.pushButton_receiver_stepper_x_home.setGeometry(QtCore.QRect(20, 60, 121, 28))
        self.pushButton_receiver_stepper_x_home.setObjectName(_fromUtf8("pushButton_receiver_stepper_x_home"))
        self.pushButton_receiver_stepper_x_move_rel = QtGui.QPushButton(self.groupBox)
        self.pushButton_receiver_stepper_x_move_rel.setGeometry(QtCore.QRect(160, 60, 111, 28))
        self.pushButton_receiver_stepper_x_move_rel.setObjectName(_fromUtf8("pushButton_receiver_stepper_x_move_rel"))
        self.lineEdit_receiver_stepper_x_move_rel = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_receiver_stepper_x_move_rel.setGeometry(QtCore.QRect(160, 30, 113, 22))
        self.lineEdit_receiver_stepper_x_move_rel.setObjectName(_fromUtf8("lineEdit_receiver_stepper_x_move_rel"))
        self.lineEdit_receiver_stepper_x_move_abs = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_receiver_stepper_x_move_abs.setGeometry(QtCore.QRect(290, 30, 113, 22))
        self.lineEdit_receiver_stepper_x_move_abs.setObjectName(_fromUtf8("lineEdit_receiver_stepper_x_move_abs"))
        self.pushButton_receiver_stepper_x_move_abs = QtGui.QPushButton(self.groupBox)
        self.pushButton_receiver_stepper_x_move_abs.setGeometry(QtCore.QRect(290, 60, 111, 28))
        self.pushButton_receiver_stepper_x_move_abs.setObjectName(_fromUtf8("pushButton_receiver_stepper_x_move_abs"))
        self.tabWidget.addTab(self.tab_receiver_stepper, _fromUtf8(""))
        self.tab_receiver_piezo = QtGui.QWidget()
        self.tab_receiver_piezo.setObjectName(_fromUtf8("tab_receiver_piezo"))
        self.tabWidget.addTab(self.tab_receiver_piezo, _fromUtf8(""))
        self.tab_laser = QtGui.QWidget()
        self.tab_laser.setObjectName(_fromUtf8("tab_laser"))
        self.tabWidget.addTab(self.tab_laser, _fromUtf8(""))
        self.tab_scripts = QtGui.QWidget()
        self.tab_scripts.setObjectName(_fromUtf8("tab_scripts"))
        self.tabWidget.addTab(self.tab_scripts, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_general), _translate("MainWindow", "General", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_donor), _translate("MainWindow", "Donor", None))
        self.groupBox.setTitle(_translate("MainWindow", "receiver_stepper_x", None))
        self.pushButton_receiver_stepper_x_home.setText(_translate("MainWindow", "home", None))
        self.pushButton_receiver_stepper_x_move_rel.setText(_translate("MainWindow", "move rel", None))
        self.pushButton_receiver_stepper_x_move_abs.setText(_translate("MainWindow", "move abs", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_receiver_stepper), _translate("MainWindow", "Receiver_stepper", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_receiver_piezo), _translate("MainWindow", "Receiver_piezo", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_laser), _translate("MainWindow", "Laser", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_scripts), _translate("MainWindow", "Scripts", None))

