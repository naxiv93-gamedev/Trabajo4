from PySide6.QtCore import *
from PySide6.QtGui import * 
from PySide6.QtWidgets import *
class AngleDisplay(QWidget):
    clickedEvent = Signal(int)
    def __init__(self,colors = [0x498BD1,"#FF0000","#00FF00","#0000FF"]):
        QWidget.__init__(self)
        
        #CUSTOM PROPERTIES
        self.colorIndex = 0
        self.colors = colors
        self.value = 0
        self.width = 200
        self.height = 200
        self.progress_width = 10
        self.progress_rounded_cap = False
        self.color = self.colors[self.colorIndex]
        self.max_value = 360
        self.font_family = "Segoe UI"
        self.font_size = 16
        self.suffix = "º"
        self.enable_shadow = True
   
    def paintEvent(self, event):
        width = self.width - self.progress_width
        height = self.height - self.progress_width
        margin = self.progress_width / 2
        value = self.value * 360 / self.max_value
        
        paint = QPainter()
        paint.begin(self)
        paint.setRenderHint(QPainter.Antialiasing)
        paint.setFont(QFont(self.font_family,self.font_size)) 
        rect = QRect(0,0, self.width,self.height)
        paint.setPen(Qt.NoPen)
        paint.drawRect(rect)
        
        pen = QPen()
        pen.setColor(QColor(self.color))
        pen.setWidth(self.progress_width)
        if self.progress_rounded_cap:
            pen.setCapStyle(Qt.RoundCap)
        
        paint.setPen(pen)
        paint.drawArc(margin,margin, width, height,90*16, -value * 16)
        pen.setColor(QColor(self.color))
        paint.setPen(pen)
        paint.drawText(rect,Qt.AlignCenter,f"{self.value}{self.suffix}")
        paint.end()  
    def mousePressEvent(self, e):
        self.colorIndex += 1
        if self.colorIndex >= len(self.colors):
            self.colorIndex = 0
        self.color = self.colors[self.colorIndex]
        self.clickedEvent.emit(self.value)
        self.update()
    def getStringValue(self,value):
        return str(value) + self.suffix
    