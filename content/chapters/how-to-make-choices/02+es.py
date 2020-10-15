miPrimeraLista = [1, 'a', False]
miSegundaLista = miPrimeraLista
miTerceraLista = [1, 'a', False]

# dos alias refiriéndose al mismo objeto en memoria
miPrimeraLista is miSegundaLista
# Verdadero

# revisión adicional
id(miPrimeraLista) == id(miSegundaLista)
# Verdadero

# dos alias refiriéndose a dos objetos diferentes
# con el mismo contenido
miPrimeraLista is miTerceraLista
# Falso

# de hecho tienen el mismo contenido
myFirstList == myThirdList
# Verdadero

# pero diferente identidad
id(myFirstList) == id(myThirdList)
# Falso