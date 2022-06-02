import pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit
import sys

class Janela (QMainWindow):
    def __init__(self):
        super().__init__()

        self.left = 100
        self.top = 100
        self.larg = 800
        self.altura = 600 
        self.tittle = "Janela"
        
        self.line_text = QLineEdit(self)
        self.line_text.move(25,20)
        self.line_text.resize(250,20)
        
        B1 = QPushButton("Ok", self)
        B1.move(350, 300)
        B1.resize(100,50)
        B1.setStyleSheet("QPushButton {background-color:#9370DB; font:bold; font-size:20px}")
        B1.clicked.connect(self.showResult)
        
        self.label_1 = QLabel(self)
        self.label_1.move(400, 100)
        self.label_1.setStyleSheet("QLabel {font-size:20px}")
        
        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.left, self.top, self.larg, self.altura)    
        self.setWindowTitle(self.tittle)
        self.show()
             
        
    def showResult(self):
        text = self.line_text.text()
        self.label_1.setText(text)
    

apk = QApplication(sys.argv)
j = Janela()
sys.exit(apk.exec_())
