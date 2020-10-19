numerosAleatorios = [8, 6, 5, 5, 0, 1, 7, 7, 6, 7, 2, 5, 8, 6, 4, 7]

numerosAleatorios.remove(5) # recuerde: ¡item no es el índice de posición!
# resultado: [8, 6, 5, 0, 1, 7, 7, 6, 7, 2, 5, 8, 6, 4, 7]

numerosAleatorios.remove(5)
# resultado: [8, 6, 0, 1, 7, 7, 6, 7, 2, 5, 8, 6, 4, 7]

numerosAleatorios.remove(0)
# resultado: [8, 6, 1, 7, 7, 6, 7, 2, 5, 8, 6, 4, 7]

numerosAleatorios.remove(0)
# resultado: ValueError: list.remove(x): x not in list

# comprueba si la lista contiene el elemento que deseas eliminar
# con la palabra clave "in"
if 0 in numerosAleatorios:
    numerosAleatorios.remove(0)
# resultado: [8, 6, 1, 7, 7, 6, 7, 2, 5, 8, 6, 4, 7]
