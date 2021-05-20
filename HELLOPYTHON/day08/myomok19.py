import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic, QtGui 
from PyQt5.Qt import QPushButton, QSize, QRect
from _threading_local import local

form_class = uic.loadUiType("myomok02.ui")[0]


class MyApp(QMainWindow, form_class):  # 상속

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.arr2D = [
                
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0 ,0,0,0,0,0 ,0,0,0,0],

            ]
        
        self.pb2D = []

        for i in range(19):
            pb_line = []
            for j in range(19):
                tmp = QPushButton(self)
                tmp.setToolTip(str(i)+","+str(j))
                tmp.setIconSize(QSize(40, 40))
                tmp.setGeometry(QRect(j*40, i*40, 40, 40))
                tmp.setIcon(QtGui.QIcon("0.jpg"))
                tmp.clicked.connect(self.btnClick)
                pb_line.append(tmp)
            self.pb2D.append(pb_line)
            
        self.myrender()
        
    def myrender(self):
        for i in range(19):
            for j in range(19):
                if self.arr2D[i][j] == 0:
                    self.pb2D[i][j].setIcon(QtGui.QIcon("0.jpg"))
                if self.arr2D[i][j] == 1:
                    self.pb2D[i][j].setIcon(QtGui.QIcon("1.jpg"))
                if self.arr2D[i][j] == 2:
                    self.pb2D[i][j].setIcon(QtGui.QIcon("2.jpg"))
        
    def btnClick(self):
        print("test")
        loca = self.sender().toolTip().split(",")
        i = int(loca[0])
        j = int(loca[1])
        print(i)
        print(j)
        self.arr2D[i][j] = 2
        
        self.myrender()
        #self.pb2D[0][9].setIcon(QtGui.QIcon("1.jpg"))
        
        
if __name__ == '__main__': 
   app = QApplication(sys.argv)
   myWindow = MyApp()
   myWindow.show()
   app.exec_()
