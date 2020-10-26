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
    glyphNames = 'ABCDE'

    ### Instrucciones
    newPage(400, 250)
    translate(TAMANO_CELDA * 1, TAMANO_CELDA * 2)
    dibujarMatrizLetras(glyphNames, esPrimeroVertical=True)

    translate(TAMANO_CELDA * 6, 0)
    dibujarMatrizLetras(glyphNames, esPrimeroVertical=False)

