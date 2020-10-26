### Constantes
TAMANO_CELDA = 30

### Variables
nombresGlifos = 'ABCDE'

### Instrucciones
tamanoLienzo = (len(nombresGlifos) + 2) * TAMANO_CELDA
newPage(tamanoLienzo, tamanoLienzo)
font('.SFNS-Regular', 18)
translate(TAMANO_CELDA, TAMANO_CELDA)
for jj, glifoY in enumerate(nombresGlifos):
    for ii, glifoX in enumerate(nombresGlifos):
        with savedState():
            translate(ii * TAMANO_CELDA, jj * TAMANO_CELDA)
            text(f'{glifoX}{glifoY}', (0, TAMANO_CELDA * .3))
