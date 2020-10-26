### Constantes
TAMANO_CELDA = 30

### Variables
nombresGlifos = 'ABCDE'
esPrimeroVertical = False

### Instrucciones
tamanoLienzo = (len(nombresGlifos) + 2) * TAMANO_CELDA
newPage(tamanoLienzo, tamanoLienzo)
translate(TAMANO_CELDA, TAMANO_CELDA)
font('.SFNS-Regular', 18)
for jj, glifoY in enumerate(nombresGlifos):
    for ii, glifoX in enumerate(nombresGlifos):
        par = (glifoY, glifoX) if esPrimeroVertical else (glifoX, glifoY)
        with savedState():
            translate(ii * TAMANO_CELDA, jj * TAMANO_CELDA)
            text(f'{par[0]}{par[1]}', (0, TAMANO_CELDA * .3))
