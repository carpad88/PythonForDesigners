limiteSeguro = 200    # ste valor es arbitrario
paracaidas = 0

while True:          # esto se repetirá sin fin
    paracaidas += 1
    if paracaidas == limiteSeguro:
        print("¡es tiempo de abrir el paracaídas!")
        break