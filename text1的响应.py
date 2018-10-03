# -*- coding: utf-8 -*-import sys
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from text1 import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal, Qt


class MyMainWindow(QMainWindow, Ui_MainWindow):
    printSignal = pyqtSignal(list)
    helpSignal = pyqtSignal(str)
    def __init__( self, parent=None ):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    def initUI( self ):
        self.printSignal.connect(self.printqueren)
        self.queren.clicked.connect(self.emitPrintSignal)
        self.helpSignal.connect(self.showHelpMessage)
       # self.printButton.clicked.connect(self.emitPrintzuobiaoSignal)
    def emitPrintSignal( self ):
        pList = [ ]
        pList.append(self.label.value())

        self.printSignal.emit(pList)
    def keyPressEvent( self, event ):
        if event.key() == Qt.Key_F1:
            self.helpSignal.emit("help message")

    def printqueren( self, list ):
        self.label_4.setText("打印: " + "份数：" + str(list[ 0 ]))
    def showHelpMessage( self, message ):
        self.resultLabel.setText(message)
        #self.statusBar().showMessage(message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())