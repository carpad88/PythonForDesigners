from itertools import product
from collections import defaultdict

kerning = defaultdict(int)
kerning.setdefault(0)

kerning[('A', 'V')] = -80
kerning[('V', 'A')] = -80
kerning[('L', 'A')] = 20
kerning[('A', 'W')] = -60
kerning[('P', 'a')] = -120

nombresGlifos = 'ALVPW'

correcciones = [kerning[nn] for nn in product(nombresGlifos, repeat=2)]
correcciones.sort()
print(correcciones)
# >>> [-80, -80, -60, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20]
# 120 fue descartado, nombresGlifos no contiene 'a'

minCorr, maxCorr = correcciones[0], correcciones[-1]
# >>> -80 20

referencia = abs(maxCorr) if abs(minCorr) < abs(maxCorr) else abs(minCorr)
# >>> 80
