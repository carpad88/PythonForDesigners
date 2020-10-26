from fontParts.world import OpenFont

miFuente = OpenFont('Source Serif Pro Regular.ufo')

for par, correccion in miFuente.kerning.items():
    primero, segundo = par
    print(f'{primero} vs {segundo} = {correccion}')

    # aquí una selección de los diferentes tipos de pares de kerning (con ejemplo)
    # grupo vs grupo
    # >>> public.kern1.periodcentered vs public.kern2.LAT_T = -40

    # grupo vs glifo
    # >>> public.kern1.zero.lf vs AE = -21

    # glifo vs grupo
    # >>> zeta vs public.kern2.GRK_alpha = -20

    # glifo vs glyph
    # >>> B vs AE = -50
