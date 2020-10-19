cantidadDeLineas = 8
newPage(100, 100)

stroke(0)
for indexCadaLinea in range(cantidadDeLineas):
    cuota = width() / (cantidadDeLineas + 1) * (indexCadaLinea + 1)
    line((20, cuota), (80, cuota))
