numerosAleatorios = [8, 6, 5, 5, 0, 1, 7, 7, 6, 7, 2, 5, 8, 6, 4, 7]

numeroA = numerosAleatorios.pop()
# numeroA: 7

# numerosAleatorios: [8, 6, 5, 5, 0, 1, 7, 7, 6, 7, 2, 5, 8, 6, 4]
numeroA = numerosAleatorios.pop(0)
# numeroA: 8

# numerosAleatorios: [6, 5, 5, 0, 1, 7, 7, 6, 7, 2, 5, 8, 6, 4]
numeroA = numerosAleatorios.pop(5)
# numeroA: 7

# numerosAleatorios: [6, 5, 5, 0, 1, 7, 6, 7, 2, 5, 8, 6, 4]
numeroA = numerosAleatorios.pop(24)
# resultado: IndexError: pop index out of range

# verifica el largo de la lista antes de usar pop
# con la función incorporada len()
