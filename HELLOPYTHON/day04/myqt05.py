import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from random import randint

form_class = uic.loadUiType("myqt05.ui")[0]


class MyApp(QMainWindow, form_class):  # 상속

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        hum = self.le1.text()
        print("1")
        ran = randint(1, 10)
        
        print(ran)
        if(ran % 2 == 0):
            com = "홀"
        elif(ran % 2 == 1):
            com = "짝"
        print(hum)
        self.le2.setText(com)
        if hum == com:
            self.le3.setText("정답")
        else:
            self.le3.setText("틀림")


if __name__ == '__main__': 
   app = QApplication(sys.argv)
   myWindow = MyApp()
   myWindow.show()
   app.exec_()
