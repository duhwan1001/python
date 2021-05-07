import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from random import randint

form_class = uic.loadUiType("myqt08.ui")[0]


class MyApp(QMainWindow, form_class):  # 상속

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        dan = int(self.dan.text())
        
        for i in range(1, 10):
            temp = dan * i 
            res = str(dan) + "*" + str(i) + "=" + str(temp)
            print(res)
            self.tb.append(res)
        
        
        
        

if __name__ == '__main__': 
   app = QApplication(sys.argv)
   myWindow = MyApp()
   myWindow.show()
   app.exec_()
