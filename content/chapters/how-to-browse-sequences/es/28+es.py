sombras = 10
newPage(100, 100)

anchoSombra = width() / sombras

for indexSombra in range(sombras):
    valorDeGris = 1 - (1 / (sombras - 1) * indexSombra)
    fill(valorDeGris)
    rect(indexSombra * anchoSombra, 0, anchoSombra, height())
