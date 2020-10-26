#!/usr/bin/env python3
# coding: utf-8

# --------- #
# HSL DONUT #
# --------- #

### Módulos
# librería estándar
from colorsys import hls_to_rgb

# dependencias
from drawBot import font, fill, stroke, strokeWidth, newPath, arc, drawPath
from drawBot import savedState, rotate, line, text, newPage, translate
from drawBot import width, height, newDrawing, endDrawing, saveImage, rect

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


def hslDonut(anillos, grosorAnillo, radioAgujero, valorFijo, esLuminosidadConst, captions=True):
    for angulo in range(CIRCULO_COMPLETO):
        for cadaAnillo in range(anillos):
            factorAnillo = cadaAnillo / (anillos - 1)
            radio = radioAgujero + cadaAnillo * grosorAnillo

            if esLuminosidadConst:
                colorRGB = hls_to_rgb(angulo / CIRCULO_COMPLETO, valorFijo, factorAnillo)
            else:
                colorRGB = hls_to_rgb(angulo / CIRCULO_COMPLETO, factorAnillo, valorFijo)
            cualidadesLinea(colorRGB, grosorAnillo)

            newPath()
            arc((0, 0), radio, angulo - .5, angulo + .5, clockwise=False)
            drawPath()

        with savedState():
            if angulo % 10 == 0 and captions:
                radioSubtitulo = radio + grosorAnillo
                rotate(angulo)

                cualidadesLinea(grosor=.5)
                line((radioSubtitulo - 2, 0), (radioSubtitulo + 2, 0))

                cualidadesFuente()
                text(f'{angulo}', (radio + grosorAnillo + 6, 0))


### Instrucciones
if __name__ == '__main__':
    newDrawing()
    newPage(400, 400)

    fill(.8)
    rect(0, 0, width(), height())

    translate(width() / 2, height() / 2)
    hslDonut(anillos=8,
             grosorAnillo=15,
             radioAgujero=45,
             valorFijo=.75,
             esLuminosidadConst=False)
    saveImage('HSL Donut L.pdf')
    endDrawing()

