### Modules
from colorsys import hls_to_rgb

### Constants
CIRCULO_COMPLETO = 360

### Variables
columnas = filas = 10
anguloMatiz = 240

### Instructions
newPage(400, 400)

anchoPaso = width() / columnas
altoPaso = height() / filas
for jj in range(filas):
    saturacion = jj / (filas - 1)
    for ii in range(columnas):
        luminosidad = ii / (columnas - 1)
        colorRGB = hls_to_rgb(anguloMatiz / CIRCULO_COMPLETO, luminosidad, saturacion)
        fill(*colorRGB)
        rect(ii * anchoPaso, jj * altoPaso, anchoPaso, altoPaso)
