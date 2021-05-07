import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

form_class = uic.loadUiType("myqt01.ui")[0]


class MyApp(QMainWindow, form_class):  # 상속

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.tb.clicked.connect(self.btnClick)
        
    def btnClick(self): 
        self.lbl.setText("집에가자")


if __name__ == '__main__': 
   app = QApplication(sys.argv)
   myWindow = MyApp()
   myWindow.show()
   app.exec_()
