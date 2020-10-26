from collections import defaultdict

kerning = defaultdict(int)
kerning.setdefault(0)

# creemos un par falso
kerning[('A', 'V')] = -80

# Si la clave está en el diccionario, devuelve su valor
print(kerning[('A', 'V')])
# >>> -80

# Si no, se devuelve 0
print(kerning[('H', 'H')])
# >>> 0
