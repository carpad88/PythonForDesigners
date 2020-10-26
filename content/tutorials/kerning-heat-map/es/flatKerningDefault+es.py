### Modules
from collections import defaultdict

### Constantes
PRIMER_PREFIJO = 'public.kern1.'
SEGUNDO_PREFIJO = 'public.kern2.'

### Funciones
def aplanarKerning(unaFuente):
    flatK = defaultdict(int)
    flatK.setdefault(0)

    for par, correccion in unaFuente.kerning.items():
        primero, segundo = par

        # ambos grupos
        if primero.startswith(PRIMER_PREFIJO) and segundo.startswith(SEGUNDO_PREFIJO):
            for primerGlifo in unaFuente.groups[primero]:
                for segundoGlifo in unaFuente.groups[segundo]:
                    flatK[(primerGlifo, segundoGlifo)] = correccion

        # primer grupo, segundo glifo
        elif primero.startswith(PRIMER_PREFIJO):
            for primerGlifo in unaFuente.groups[primero]:
                flatK[(primerGlifo, segundo)] = correccion

        # primer glifo, segundo grupo
        elif segundo.startswith(SEGUNDO_PREFIJO):
            for segundoGlifo in unaFuente.groups[segundo]:
                flatK[(primero, segundoGlifo)] = correccion

        # primer glifo, segundo glifo
        else:
            flatK[(primero, segundo)] = correccion

    return flatK

