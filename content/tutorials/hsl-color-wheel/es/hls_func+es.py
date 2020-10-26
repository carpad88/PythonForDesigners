### Módulos
from colorsys import hls_to_rgb

### Variables
matiz = 120 / 360
saturacion = 80 / 100
luminosidad = 60 / 100

### Instructiones
newPage(400, 400)
color = hls_to_rgb(matiz, luminosidad, saturacion)
print(color)
fill(*color)
rect(0, 0, width(), height())
