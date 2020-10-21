columnas = 4
filas = 4
newPage(200, 200)

anchoCelda = width() / columnas
altoCelda = height() / filas

for indexFila in range(filas):
    for indexColumna in range(columnas):
        x = indexColumna * anchoCelda
        y = indexFila * altoCelda

        stroke(None)
        fill(0)
        text(f'{indexColumna}, {indexFila}', (x + 5, y + 5))

        fill(None)
        stroke(0)
        rect(x, y, anchoCelda, altoCelda)
