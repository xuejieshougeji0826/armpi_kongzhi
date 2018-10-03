# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWinSignalSlog02.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(715, 225)
        self.controlsGroup = QtWidgets.QGroupBox(MainWindow)
        self.controlsGroup.setGeometry(QtCore.QRect(10, 20, 451, 151))
        self.controlsGroup.setObjectName("controlsGroup")
        self.widget = QtWidgets.QWidget(self.controlsGroup)
        self.widget.setGeometry(QtCore.QRect(10, 40, 411, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.numberSpinBox = QtWidgets.QSpinBox(self.widget)
        self.numberSpinBox.setObjectName("numberSpinBox")
        self.horizontalLayout.addWidget(self.numberSpinBox)
        self.styleCombo = QtWidgets.QComboBox(self.widget)
        self.styleCombo.setObjectName("styleCombo")
        self.styleCombo.addItem("")
        self.styleCombo.addItem("")
        self.styleCombo.addItem("")
        self.horizontalLayout.addWidget(self.styleCombo)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.printButton = QtWidgets.QPushButton(self.widget)
        self.printButton.setObjectName("printButton")
        self.horizontalLayout.addWidget(self.printButton)
        self.widget1 = QtWidgets.QWidget(self.controlsGroup)
        self.widget1.setGeometry(QtCore.QRect(10, 100, 201, 30))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.previewStatus = QtWidgets.QCheckBox(self.widget1)
        self.previewStatus.setObjectName("previewStatus")
        self.horizontalLayout_2.addWidget(self.previewStatus)
        self.previewButton = QtWidgets.QPushButton(self.widget1)
        self.previewButton.setObjectName("previewButton")
        self.horizontalLayout_2.addWidget(self.previewButton)
        self.resultGroup = QtWidgets.QGroupBox(MainWindow)
        self.resultGroup.setGeometry(QtCore.QRect(470, 20, 231, 151))
        self.resultGroup.setObjectName("resultGroup")
        self.resultLabel = QtWidgets.QLabel(self.resultGroup)
        self.resultLabel.setGeometry(QtCore.QRect(20, 30, 191, 101))
        self.resultLabel.setObjectName("resultLabel")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "打印控件"))
        self.controlsGroup.setTitle(_translate("MainWindow", "打印控制"))
        self.label.setText(_translate("MainWindow", "打印份数:"))
        self.styleCombo.setItemText(0, _translate("MainWindow", "A3"))
        self.styleCombo.setItemText(1, _translate("MainWindow", "A4"))
        self.styleCombo.setItemText(2, _translate("MainWindow", "A5"))
        self.label_2.setText(_translate("MainWindow", "纸张类型:"))
        self.printButton.setText(_translate("MainWindow", "打印"))
        self.previewStatus.setText(_translate("MainWindow", "全屏预览"))
        self.previewButton.setText(_translate("MainWindow", "预览"))
        self.resultGroup.setTitle(_translate("MainWindow", "操作结果"))
        self.resultLabel.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
