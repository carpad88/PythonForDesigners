### Módulos
from colorsys import hls_to_rgb

### Constantes
CIRCULO_COMPLETO = 360
NEGRO = 0, 0, 0


### Funciones
def cualidadesFuente(nombreFuente='Arnold_v0.3-Regular', tamañoCuerpo=9):
    # agradece a Rüdiger 👋
    font(nombreFuente, tamañoCuerpo)
    fill(*NEGRO)
    stroke(None)


def cualidadesLinea(color=NEGRO, grosor=1):
    stroke(*color)
    strokeWidth(grosor)
    fill(None)


### Variables
esLuminosidadConst = True
zz = .75
anillos = 8

radioAgujero = 45
grosorAnillo = 15

### Instructions
newPage(400, 400)
translate(width() / 2, height() / 2)

for angulo in range(CIRCULO_COMPLETO):
    for cadaAnillo in range(anillos):
        factorAnillo = cadaAnillo / (anillos - 1)
        radio = radioAgujero + cadaAnillo * grosorAnillo

        if esLuminosidadConst:
            colorRGB = hls_to_rgb(angulo / CIRCULO_COMPLETO, zz, factorAnillo)
        else:
            colorRGB = hls_to_rgb(angulo / CIRCULO_COMPLETO, factorAnillo, zz)
        cualidadesLinea(colorRGB, grosorAnillo)

        newPath()
        arc((0, 0), radio, angulo - .5, angulo + .5, clockwise=False)
        drawPath()

    with savedState():
        if angulo % 10 == 0:
            captionRadius = radio + grosorAnillo
            rotate(angulo)

            cualidadesLinea(grosor=.5)
            line((captionRadius - 2, 0), (captionRadius + 2, 0))

            cualidadesFuente()
            text(f'{angulo}', (radio + grosorAnillo + 6, 0))

