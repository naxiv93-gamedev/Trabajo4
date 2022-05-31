import sys
import os
from PySide6.QtCore import *
from PySide6.QtGui import * 
from PySide6.QtWidgets import *

from AngleDisplay import AngleDisplay
class Mainwindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        
        self.resize(500, 500)
        
        self.container = QFrame()
        self.container.setStyleSheet("background-color:transparent")
        self.layout = QVBoxLayout()
        
        self.progress = AngleDisplay()
        self.progress.setMinimumSize(self.progress.width,self.progress.height)
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0,360)
        self.slider.valueChanged.connect(self.changeSliderValue)
        self.text = QLineEdit()
        self.text.textEdited.connect(self.changeTextValue)
        self.layout.addWidget(self.progress,Qt.AlignCenter,Qt.AlignCenter)
        self.layout.addWidget(self.slider,Qt.AlignCenter,Qt.AlignCenter)
        self.layout.addWidget(self.text,Qt.AlignCenter,Qt.AlignCenter)
        self.container.setLayout(self.layout)  
        self.setCentralWidget(self.container)
        self.show()

    def changeSliderValue(self,value):
        self.progress.value = value
        self.progress.repaint()
        self.text.setText(str(value))
    def changeTextValue(self,value):
        if(value.isnumeric()):
            if int(value) > 360:
                self.text.setText("360")
            self.slider.setValue(int(value))
        else:
            self.text.setText("0")
            self.slider.setValue(0)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Mainwindow()
    sys.exit(app.exec())