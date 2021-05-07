import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from random import randint

form_class = uic.loadUiType("myqt07.ui")[0]


class MyApp(QMainWindow, form_class):  # 상속

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        hum = self.le1.text()
        ran = randint(1, 3)
        
        if(ran == 1):
            com = "가위"
        elif(ran == 2):
            com = "바위"
        elif(ran == 3):
            com = "보"
        
        self.le2.setText(com)
        
        if hum == com:
            self.le3.setText("비김")
        
        if hum == "가위" and com == "바위":
            self.le3.setText("짐")
        elif hum == "가위" and com == "보":
            self.le3.setText("이김")
            
        if hum == "바위" and com == "보":
            self.le3.setText("짐")
        elif hum == "바위" and com == "가위":
            self.le3.setText("이김")
            
        if hum == "보" and com == "가위":
            self.le3.setText("짐")
        elif hum == "보" and com == "바위":
            self.le3.setText("이김")
        
        

if __name__ == '__main__': 
   app = QApplication(sys.argv)
   myWindow = MyApp()
   myWindow.show()
   app.exec_()
