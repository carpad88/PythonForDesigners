### Módulos
from colorsys import hls_to_rgb

### Constantes
CIRCULO_COMPLETO = 360

### Variables
rayas = 20
esLuminosidadConst = False
anguloMatiz = 120

### Instrucciones
newPage(400, 400)

anchoPasos = width() / rayas

# iterar sobre el número de rayas
for ii in range(rayas):
    factor = ii / (rayas - 1)

    # esta construcción condicional permite al usuario
    # cambiar el parámetro fijo de luminosidad a saturación
    if esLuminosidadConst:
        colorRGB = hls_to_rgb(anguloMatiz / CIRCULO_COMPLETO, .7, factor)
    else:
        colorRGB = hls_to_rgb(anguloMatiz / CIRCULO_COMPLETO, factor, .7)

    # Me encanta el operador de desempaquetado 🤩
    fill(*colorRGB)
    rect(0, 0, anchoPasos, height())
    translate(anchoPasos, 0)
