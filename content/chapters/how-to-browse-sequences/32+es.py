columnas = 4
newPage(200, 200)

tamañoCelda = height() / columnas

stroke(0)
fill(None)
for indexColumna in range(columnas):
    rect(colIndex * tamañoCelda, 0 * tamañoCelda, tamañoCelda, tamañoCelda)
