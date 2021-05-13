import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic, QtGui 

form_class = uic.loadUiType("myqt01.ui")[0]


class MyApp(QMainWindow, form_class):  # 상속

    def __init__(self):
        super().__init__()
        self.index = 0
        self.setupUi(self)
        self.tb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        self.index += 1
        loc_index = self.index % 3
        print(str(loc_index) + ".jpg")
        self.tb.setIcon(QtGui.QIcon(str(loc_index) + ".jpg"))
        

if __name__ == '__main__': 
   app = QApplication(sys.argv)
   myWindow = MyApp()
   myWindow.show()
   app.exec_()
   