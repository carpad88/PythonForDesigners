from fontParts.world import OpenFont
miFuente = OpenFont('Source Serif Pro Regular.ufo')
print(miFuente.info.familyName, miFuente.info.styleName)
# >>> Source Serif Pro Regular
print(miFuente.kerning)
# >>> <RKerning for font 'Source Serif Pro Regular' path='Source Serif Pro Regular.ufo' at 4412747344>
print(len(miFuente.kerning))
# >>> 7970
