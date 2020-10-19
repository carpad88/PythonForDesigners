cantidadDeLineas = 100
newPage(100, 100)
stroke(0)

factor = 1
for indexCadaLinea in range(cantidadDeLineas):
    x = width() / (cantidadDeLineas + 1) * (indexCadaLinea + 1) * factor
    line((x, 20), (x, 80))
    factor += 0.1
