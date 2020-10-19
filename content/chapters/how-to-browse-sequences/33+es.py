columnas = 4
filas = 4
newPage(200, 200)

anchoCelda = width() / columnas
altoCelda = height() / filas

stroke(0)
fill(None)
for indexFila in range(filas):
    for indexColumna in range(columnas):
        rect(indexColumna * anchoCelda, indexFila * altoCelda, anchoCelda, altoCelda)
