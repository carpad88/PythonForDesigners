columnas = 4
filas = 4
newPage(200, 200)

anchoCelda = width() / columnas
altoCelda = height() / filas

for indexFila in range(filas):
    for indexColumna in range(columnas):
        valorDeGris = (indexFila + indexColumna) / (filas + columnas - 2)
        fill(valorDeGris)
        rect(indexColumna * anchoCelda, indexFila * altoCelda, anchoCelda, altoCelda)
