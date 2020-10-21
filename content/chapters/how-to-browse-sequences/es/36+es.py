columnas = 4
filas = 4
newPage(200, 200)

anchoCelda = width() / columnas
altoCelda = height() / filas

for indexFila in range(filas):
    for indexColumna in range(columnas):
        if (indexFila + indexColumna) % 2 == 0:
            fill(0)
        else:
            fill(1)
        rect(indexColumna * anchoCelda, indexFila * altoCelda, anchoCelda, altoCelda)
