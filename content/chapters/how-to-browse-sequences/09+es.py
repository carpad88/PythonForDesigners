algunasCoordenadas = [(11.2, 32.1),
                   (43.9, 14.8)]

primerPunto = (34.1, 76.4)
algunasCoordenadas.insert(0, primerPunto)
# resultado: [(34.1, 76.4), (11.2, 32.1), (43.9, 14.8)]

ultimoPunto = (63.1, 87.3)
algunasCoordenadas.insert(len(algunasCoordenadas), ultimoPunto)
# resultado: [(34.1, 76.4), (11.2, 32.1), (43.9, 14.8), (63.1, 87.3)]

puntoA = (87.4, 6.2)
algunasCoordenadas.insert(2, puntoA)
# resultado: [(34.1, 76.4), (11.2, 32.1), (87.4, 6.2), (43.9, 14.8), (63.1, 87.3)]

otroPunto = (45.9, 98.7)
algunasCoordenadas.insert(200, anotherPoint)
# resultado: [(34.1, 76.4), (11.2, 32.1), (87.4, 6.2), (43.9, 14.8), (63.1, 87.3), (45.9, 98.7)]

# insert no se queja si el índice es mucho más grande que la lista
# pondrá el elemento al final de la lista sin generar un IndexError
