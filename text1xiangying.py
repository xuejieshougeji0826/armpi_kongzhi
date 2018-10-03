# -*- coding: utf-8 -*-import sys
import sys
import nijie
from PyQt5.QtWidgets import QApplication, QMainWindow
from text1 import Ui_MainWindow
from PyQt5.QtCore import pyqtSignal, Qt
#nijie.nijiehanshu(8,8,8)
class MyMainWindow(QMainWindow, Ui_MainWindow):#定义几个信号
    printSignal = pyqtSignal(float)
    helpSignal = pyqtSignal(str)
    def __init__( self, parent=None ):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)
        self.initUI()

    def initUI( self ):#将信号和槽绑定
        #self.printSignal.connect(self.printqueren)
        self.queren.clicked.connect(self.emitPrintSignal)
        self.helpSignal.connect(self.showHelpMessage)
        #self.printButton.clicked.connect(self.emitPrintzuobiaoSignal)
    def emitPrintSignal( self ):
        xzb= int(self.Xzuobiao.text())
        yzb = int(self.Yzuobiao.text())
        zzb = int(self.Zzuobiao.text())
        self.textEdit.setText("要达到的坐标为："+"("+bytes(xzb)+" "+bytes(yzb)+" "+bytes(zzb)+")")
        a=nijie.nijiezuobiao(float(xzb),float(yzb),float(zzb))
        b = nijie.nijiejiaodu(float(xzb), float(yzb), float(zzb))
        self.textEdit.append(("当前坐标为："+bytes(a)))
        self.textEdit.append(("当前各个关节角度为："+ bytes(b)))
        #self.printSignal.emit(mesg)
    def keyPressEvent( self, event ):
        if event.key() == Qt.Key_F1:
            self.helpSignal.emit("help message")

    #def printqueren( self, int):
    #def printqueren(self,int):
        #int=self.Xzuobiao.getText()
        #self.textEdit.setText("打印: " + "份数：" +int )
        #self.printSignal.emit(name)
    def showHelpMessage( self, message ):
        self.textEdit.setText(message)
        #self.statusBar().showMessage(message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MyMainWindow()
    win.show()
    sys.exit(app.exec_())
