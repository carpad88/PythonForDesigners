def interpolarValor(a, b, factor):
    valor = a + (b - a) * factor

miValor = interpolarValor(10, 20, .5)
print(miValor)
