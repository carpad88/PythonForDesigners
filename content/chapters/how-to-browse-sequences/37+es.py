miRuta = [(10.2, 22.3, (7, 51, 43)),
          (12.6, 19.8, (7, 52, 2)),
          (14.5, 18.2, (7, 52, 54))
          ]

interlinea = 18
anchoCelda = 50

newPage(200, 200)
font('InputMono-Regular')
fontSize(14)

for indeXFila, cadaFila in enumerate(miRuta):
    for indexCelda, contenidoCelda in enumerate(cadaFila):
        x = indexCelda * anchoCelda
        y = height() - (indeXFila + 1) * interlinea

        if indexCelda == 2:
            hora, minuto, segundo = contenidoCelda
            text(f'{hora:0>2}:{minuto:0>2}:{segundo:0>2}', (x, y))
        else:
            text(f'{contenidoCelda}', (x, y))
