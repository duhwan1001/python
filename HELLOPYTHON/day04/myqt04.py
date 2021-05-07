import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

form_class = uic.loadUiType("myqt04.ui")[0]


class MyApp(QMainWindow, form_class):  # 상속

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        num1 = int(self.le1.text())
        num2 = int(self.le2.text())
        
        sum = 0
        for i in range(num1, num2 + 1):
            sum += i
            
        self.le3.setText(str(sum))
        

if __name__ == '__main__': 
   app = QApplication(sys.argv)
   myWindow = MyApp()
   myWindow.show()
   app.exec_()
