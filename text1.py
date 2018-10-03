# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\anaconda3\Lib\site-packages\PyQt5\uic\qttext1\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 590)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.queren = QtWidgets.QPushButton(self.centralWidget)
        self.queren.setGeometry(QtCore.QRect(750, 40, 93, 28))
        self.queren.setObjectName("queren")
        self.Xzuobiao = QtWidgets.QLineEdit(self.centralWidget)
        self.Xzuobiao.setGeometry(QtCore.QRect(450, 40, 61, 31))
        self.Xzuobiao.setObjectName("Xzuobiao")
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(640, 110, 301, 381))
        self.textEdit.setObjectName("textEdit")
        self.Yzuobiao = QtWidgets.QLineEdit(self.centralWidget)
        self.Yzuobiao.setGeometry(QtCore.QRect(550, 40, 61, 31))
        self.Yzuobiao.setObjectName("Yzuobiao")
        self.Zzuobiao = QtWidgets.QLineEdit(self.centralWidget)
        self.Zzuobiao.setGeometry(QtCore.QRect(650, 40, 61, 31))
        self.Zzuobiao.setObjectName("Zzuobiao")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(420, 40, 41, 31))
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(520, 40, 41, 31))
        self.label_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(620, 40, 41, 31))
        self.label_3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 391, 31))
        self.label_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.queren.setText(_translate("MainWindow", "确认"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">X：</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Y：</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Z：</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">请在此分别输入想到到达的坐标</span></p></body></html>"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


