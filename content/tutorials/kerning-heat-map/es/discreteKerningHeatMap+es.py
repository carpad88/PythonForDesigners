### Módulos
from fontParts.world import OpenFont
from flatKerningDefault import flatKerning
from string import ascii_uppercase

### Constantes
TAMANO_CELDA = 30

BLANCO = 1, 1, 1
NEGRO = 0, 0, 0

ROJO = 1, 0, 0
VERDE = 0, 1, 0


### Funciones
def cualidadesTipo(color=NEGRO, tamanoCuerpo=8, interlinea=9, nombreFuente=None):
    if nombreFuente is None:
        font('Obviously-NarwSemi', tamanoCuerpo)
    else:
        font(nombreFuente, tamanoCuerpo)
    lineHeight(interlinea)
    cualidadesForma(color)


def cualidadesForma(color=NEGRO):
    fill(*color)
    stroke(None)


def mapaCalorKerning(kerning, nombresGlifos, esPrimeroVertical):
    for jj, glifoY in enumerate(nombresGlifos):
        for ii, glifoX in enumerate(nombresGlifos):
            par = (glifoY, glifoX) if esPrimeroVertical else (glifoX, glifoY)
            correccion = kerning[par]

            with savedState():
                translate(ii * TAMANO_CELDA, jj * TAMANO_CELDA)

                if correccion == 0:
                    cualidadesForma(NEGRO)
                elif correccion < 0:
                    cualidadesForma(ROJO)
                else:
                    cualidadesForma(VERDE)
                rect(0, 0, TAMANO_CELDA, TAMANO_CELDA)

                cualidadesTipo(color=BLANCO)
                text(f'{par[0]}, {par[1]}\n{correccion}',
                     (TAMANO_CELDA * .1, TAMANO_CELDA * .5))


if __name__ == '__main__':
    ### Variables
    nombreFuente = 'Source Serif Pro Regular.ufo'
    nombresGlifos = 'AVRT'

    ### Instrucciones
    estaFuente = OpenFont(nombreFuente)
    flat = flatKerning(estaFuente)

    # small heat map
    tamanoLienzo = (len(nombresGlifos) + 2) * TAMANO_CELDA
    newPage(tamanoLienzo, tamanoLienzo)
    with savedState():
        translate(TAMANO_CELDA, TAMANO_CELDA * 1.4)
        mapaCalorKerning(flat, nombresGlifos, esPrimeroVertical=True)

