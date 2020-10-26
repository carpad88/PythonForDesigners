grupos = {'public.kern1.A': ('A', 'Agrave', 'Aacute')}
kerning = {('public.kern1.A', 'V'): -80}

flat = {}
for par, correccion in kerning.items():
    primero, segundo = par

    for nombreGlifo in grupos[primero]:
        flat[(nombreGlifo, segundo)] = correccion

# result
# >>> flat = {
# >>>     ('A', 'V'): -80,
# >>>     ('Agrave', 'V'): -80,
# >>>     ('Aacute', 'V'): -80
# >>> }
