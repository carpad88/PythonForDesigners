### Módulos
from fontParts.world import OpenFont
from flatKerningDefault import flatKerning
from string import ascii_uppercase
from itertools import product

### Constantes
TAMANO_CELDA = 30

BLANCO = 1, 1, 1
NEGRO = 0, 0, 0

ROJO = 1, 0, 0
VERDE = 0, 1, 0


### Funciones
def lerp(aa, bb, factor):
    return aa + (bb - aa) * factor


def lerpRGB(colorUno, colorDos, factor):
    rr = lerp(colorUno[0], colorDos[0], factor)
    gg = lerp(colorUno[1], colorDos[1], factor)
    bb = lerp(colorUno[2], colorDos[2], factor)
    return rr, gg, bb


def cualidadesTipo(color=NEGRO):
    font('Obviously-NarwSemi', 8)
    lineHeight(9)
    cualidadesForma(color)


def cualidadesForma(color=NEGRO):
    fill(*color)
    stroke(None)


def mapaCalorKerning(kerning, nombresGlifos, esPrimeroVertical):
    correcciones = [kerning[nn] for nn in product(nombresGlifos, repeat=2)]
    correcciones.sort()
    minCorreccion, maxCorreccion = abs(correcciones[0]), abs(correcciones[-1])
    referencia = maxCorreccion if minCorreccion < maxCorreccion else minCorreccion

    for jj, glifoY in enumerate(nombresGlifos):
        for ii, glifoX in enumerate(nombresGlifos):
            par = (glifoY, glifoX) if esPrimeroVertical else (glifoX, glifoY)
            correccion = kerning[par]

            with savedState():
                translate(ii * TAMANO_CELDA, jj * TAMANO_CELDA)

                factor = .5 + .5 * abs(correccion) / referencia
                if correccion == 0:
                    colorRect = NEGRO
                    colorTipo = BLANCO
                elif correccion < 0:
                    colorRect = lerpRGB(BLANCO, ROJO, factor)
                    colorTipo = BLANCO
                else:
                    colorRect = lerpRGB(BLANCO, VERDE, factor)
                    colorTipo = NEGRO
                cualidadesForma(colorRect)
                rect(0, 0, TAMANO_CELDA, TAMANO_CELDA)

                cualidadesTipo(color=colorTipo)
                text(f'{par[0]}\u2004{par[1]}\n{correccion}', (TAMANO_CELDA * .1, TAMANO_CELDA * .5))


if __name__ == '__main__':
    ### Variables
    nombreFuente = 'Source Serif Pro Regular.ufo'
    nombresGlifos = ascii_uppercase

    ### Instrucciones
    estaFuente = OpenFont(nombreFuente)
    flat = flatKerning(estaFuente)

    tamanoLienzo = (len(nombresGlifos) + 4) * TAMANO_CELDA
    newPage(tamanoLienzo, tamanoLienzo)
    translate(TAMANO_CELDA * 2, TAMANO_CELDA * 2)
    mapaCalorKerning(flat, nombresGlifos, esPrimeroVertical=True)
