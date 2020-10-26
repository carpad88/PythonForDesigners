### Módulos
from colorsys import hls_to_rgb

### Constantes
CIRCULO_COMPLETO = 360
ESCALA_LINEAL = 100

### Variables
pasoMatiz = 5
pasosLineales = 10
esLuminosidadConst = False
zz = .75

### Instrucciones
newPage(400, 400)
translate(width() / 2, height() / 2)

for angulo in range(0, CIRCULO_COMPLETO, pasoMatiz):
    for linear in range(0, ESCALA_LINEAL, pasosLineales):
        radio = 150 * linear / ESCALA_LINEAL

        if esLuminosidadConst:
            colorRGB = hls_to_rgb(angulo / CIRCULO_COMPLETO, zz, linear / ESCALA_LINEAL)
        else:
            colorRGB = hls_to_rgb(angulo / CIRCULO_COMPLETO, linear / ESCALA_LINEAL, zz)
        fill(*colorRGB)

        with savedState():
            rotate(angulo)
            translate(radio, 0)
            oval(-4, -4, 8, 8)

