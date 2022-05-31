### Bienvenido a la documentacion de AngleDisplay 

# ¿Qué es AngleDisplay?

AngleDisplay es un widget personalizable desarrollado en Qt. Está diseñado para mostrar, de forma gráfica, el angulo de rumbo en cartas de navegación.


## Anatomia del codigo
  El codigo consta de 4 funciones, 3 de ellas siendo overrides de funciones ya establecidas en clases QWidget
### __init__(self,colors)

Parametros:
+ colors: Lista de colores (en hex)
  - Valor por defecto: [0x498BD1,"#FF0000","#00FF00","#0000FF"]
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
### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
