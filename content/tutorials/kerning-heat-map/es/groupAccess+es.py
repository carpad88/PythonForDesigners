from fontParts.world import OpenFont
miFuente = OpenFont('Source Serif Pro Regular.ufo')

conjuntoGlifos = miFuente.groups['public.kern1.zero.lf']
print(conjuntoGlifos)
# >>> ('zero.lf', 'zero.lfslash', 'zero.cap')
