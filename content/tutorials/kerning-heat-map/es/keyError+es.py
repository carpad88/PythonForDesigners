### Módulos
from flatKerning import flatKerning
from fontParts.world import OpenFont

### Constantes
TAMANO_CELDA = 30


### Functions
def cualidadesTipo():
    font('Obviously-NarwSemi', 18)
    fill(0)
    stroke(None)


def dibujarMatrizLetras(nombresGlifos, esPrimeroVertical):
    for jj, glifoY in enumerate(nombresGlifos):
        for ii, glifoX in enumerate(nombresGlifos):
            pair = (glifoY, glifoX) if esPrimeroVertical else (glifoX, glifoY)

            with savedState():
                cualidadesTipo()
                translate((ii + .5) * TAMANO_CELDA, jj * TAMANO_CELDA)
                text(f'{pair[0]}{pair[1]}', (0, 0), align='center')


if __name__ == '__main__':
    ### Variables
    nombresGlifos = 'ABCDE'

    ### Instrucciones
    miFuente = OpenFont('Source Serif Pro Regular.ufo')
    flatK = flatKerning(miFuente)

    newPage(400, 250)
    translate(CELL_SIZE * 1, CELL_SIZE * 2)
    drawLettersMatrix(nombresGlifos, flatK, esPrimeroVertical=True)

    translate(CELL_SIZE * 6, 0)
    drawLettersMatrix(nombresGlifos, flatK, esPrimeroVertical=False)
