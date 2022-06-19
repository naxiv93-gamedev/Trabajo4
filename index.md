### Bienvenido a la documentacion de AngleDisplay 

# ¿Qué es AngleDisplay?

AngleDisplay es un widget personalizable desarrollado en Qt. Está diseñado para mostrar, de forma gráfica, el angulo de rumbo en cartas de navegación.


## Anatomia del codigo
  El codigo consta de 4 funciones, 3 de ellas siendo overrides de funciones ya establecidas en clases QWidget
### init (self,colors):

Parametros:
+ colors: Lista de colores (en hex)
  - Valor por defecto: [0x498BD1,"#FF0000","#00FF00","#0000FF"]
+ Implementacion de la funcion:
```
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
```
Funcion overrideada desde QWidget
Este codigo inicializa los parametros por defecto del QWidget personalizado.
Al ser inicializado, puede ser otorgado una lista de colores para mostrarse en el primero y poder rotar colores entre ellos. De no ser asi, se inicializara una lista basica de colores en su lugar.


### paintEvent (self,event):

Parametros:
+ event: El evento por el que se ha activado la funcion
+ Implementacion de la funcion:
```
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
```
Funcion overrideada desde QWidget
Este codigo realiza la funcion de dibujado del trazo circular que representa el angulo.
### mouseEventPress (self,e)

Parametros:
+ e: el evento de presionar boton
+ Implementacion de la funcion:
```
 def mousePressEvent(self, e):
        self.colorIndex += 1
        if self.colorIndex >= len(self.colors):
            self.colorIndex = 0
        self.color = self.colors[self.colorIndex]
        self.clickedEvent.emit(self.value)
        self.update()
```
Funcion overrideada desde QWidget
Esta funcion cambia el color al ser presionado el componente al siguiente valor que contiene la lista de colores. Finalmente, se llama al metodo update() del componente para actualizar la apariencia.

### getStringValue (self,value)

Parametros:
+ value: el valor que se desea convertir a un string
+ returns: String
+ Implementacion de la funcion:
```
def getStringValue(self,value):
        return str(value) + self.suffix
```
Funcion simple que devuelve el valor del angulo en un string 

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.

