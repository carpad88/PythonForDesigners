### Módulos
from colorsys import hls_to_rgb

### Constantes
CIRCULO_COMPLETO = 360


### Funciones
def donut(partes):
    for cadaParte in range(partes):
        factorMatiz = cadaParte / (partes - 1)
        colorRGB = hls_to_rgb(factorMatiz, .7, .7)
        stroke(*colorRGB)
        newPath()

        anguloInicio = (cadaParte - .5) / (partes - 1) * CIRCULO_COMPLETO
        anguloFinal = (cadaParte + .5) / (partes - 1) * CIRCULO_COMPLETO
        arc((0, 0), 100, anguloInicio, anguloFinal, clockwise=False)
        drawPath()


### Instrucciones
newPage(952, 340)
translate(width() * .2, height() / 2)

strokeWidth(30)
fill(None)
donut(4)

translate(width() * .3, 0)
donut(12)

translate(width() * .3, 0)
donut(36)
