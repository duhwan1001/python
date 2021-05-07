import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from random import randint

form_class = uic.loadUiType("myqt09.ui")[0]


class MyApp(QMainWindow, form_class):  # 상속

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.n1.clicked.connect(self.btnN1)
        self.n2.clicked.connect(self.btnN2)
        self.n3.clicked.connect(self.btnN3)
        self.n4.clicked.connect(self.btnN4)
        self.n5.clicked.connect(self.btnN5)
        self.n6.clicked.connect(self.btnN6)
        self.n7.clicked.connect(self.btnN7)
        self.n8.clicked.connect(self.btnN8)
        self.n9.clicked.connect(self.btnN9)
        self.n0.clicked.connect(self.btnN0)
        
        self.call.clicked.connect(self.btnCall)
        
    def btnN1(self):
        self.result.append("1")
    def btnN2(self):
        self.result.append("2")
    def btnN3(self):
        self.result.append("3")
    def btnN4(self):
        self.result.append("4")
    def btnN5(self):
        self.result.append("5")
    def btnN6(self):
        self.result.append("6")
    def btnN7(self):
        self.result.append("7")
    def btnN8(self):
        self.result.append("8")
    def btnN9(self):
        self.result.append("9")
    def btnN0(self):
        self.result.append("0")
    def btnCall(self):
        self.result.clear()
if __name__ == '__main__': 
   app = QApplication(sys.argv)
   myWindow = MyApp()
   myWindow.show()
   app.exec_()
