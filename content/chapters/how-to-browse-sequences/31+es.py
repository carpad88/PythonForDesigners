filas = 4
newPage(200, 200)

tamañoCelda = height() / filas

stroke(0)
fill(None)
for indexFila in range(filas):
    rect(0 * tamañoCelda, indexFila * tamañoCelda, tamañoCelda, tamañoCelda)
