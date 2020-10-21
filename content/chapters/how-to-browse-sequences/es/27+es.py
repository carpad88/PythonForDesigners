cantidadDeLineas = 8
radio = 3
newPage(100, 100)

for indexCadaLinea in range(cantidadDeLineas):
    cuota = width() / (cantidadDeLineas + 1) * (indexCadaLinea + 1)
    fill(None)
    stroke(0)
    line((20, cuota), (80, cuota))

    stroke(None)
    fill(0)
    oval(20 - radio, cuota - radio, radio * 2, radio * 2)
    oval(80 - radio, cuota - radio, radio * 2, radio * 2)
