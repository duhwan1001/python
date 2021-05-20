import sys

from PyQt5 import uic, QtGui, QtWidgets 
from PyQt5.Qt import QPushButton, QSize, QRect
from PyQt5.QtWidgets import QApplication, QMainWindow
from numba.core.cgutils import terminate


form_class = uic.loadUiType("myomok02.ui")[0]


class MyApp(QMainWindow, form_class):  # 상속

    def __init__(self):
        super().__init__()
        self.flag_wb = True # 전역변수
        self.flag_ing = True
        self.setupUi(self)
        self.pb_reset.clicked.connect(self.pbBtnClick)
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
                tmp.setToolTip(str(i) + "," + str(j))
                tmp.setIconSize(QSize(40, 40))
                tmp.setGeometry(QRect(j * 40, i * 40, 40, 40))
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
        
    def pbBtnClick(self):
        if self.flag_ing:
            QtWidgets.QMessageBox.about(self, "오목", "아직 게임이 진행중입니다.")
        else:
            self.flag_wb = True
            self.flag_ing = True
            
            for i in range(19):
                for j in range(19):
                    self.arr2D[i][j] = 0
            self.myrender()
        
    def btnClick(self):
        #if self.flag_ing == False:
        if not self.flag_ing:
            return
        
        loca = self.sender().toolTip().split(",")
        i = int(loca[0])
        j = int(loca[1])
        
        if self.arr2D[i][j] > 0:
            return
        
        stone = 0
        if self.flag_wb:
            self.arr2D[i][j] = 1
            stone = 1
        else:
            self.arr2D[i][j] = 2
            stone = 2
        
        up = self.getUp(i, j, stone)
        dw = self.getDw(i, j, stone)
        le = self.getLe(i, j, stone)
        ri = self.getRi(i, j, stone)
        
        ur = self.getUr(i, j, stone)
        dl = self.getDl(i, j, stone)
        ul = self.getUl(i, j, stone)
        dr = self.getDr(i, j, stone)
        
        d1 = up + 1 + dw
        d2 = le + 1 + ri
        d3 = ur + 1 + dl
        d4 = ul + 1 + dr

        self.myrender()
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5 :
            if self.flag_wb :
                QtWidgets.QMessageBox.about(self, "오목", "백돌 승리")
            else:
                QtWidgets.QMessageBox.about(self, "오목", "흑돌 승리")
            self.flag_ing = False
        
        self.flag_wb = not self.flag_wb
    
    def getDr(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i += 1
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return(cnt)
            print("error")
    
    def getUl(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i += -1
                j += -1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return(cnt)
            print("error")
            
    def getDl(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i += 1
                j += -1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return(cnt)
            print("error")
    
    def getUr(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i += -1
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return(cnt)
            print("error")
    
    def getLe(self, i, j, stone):
        cnt = 0
        try:
            while True:
                j += -1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return(cnt)
            print("error")

    def getRi(self, i, j, stone):
        cnt = 0
        try:
            while True:
                j += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return(cnt)
            print("error")
            
    def getUp(self, i, j, stone):
        cnt = 0
        while True:
            i += -1
            if i < 0:
                return cnt
            if j < 0:
                return cnt
            if self.arr2D[i][j] == stone:
                cnt += 1
            else:
                return cnt

    def getDw(self, i, j, stone):
        cnt = 0
        try:
            while True:
                i += 1
                if i < 0:
                    return cnt
                if j < 0:
                    return cnt
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return(cnt)
            print("error")

                
                
if __name__ == '__main__': 
   app = QApplication(sys.argv)
   myWindow = MyApp()
   myWindow.show()
   app.exec_()
