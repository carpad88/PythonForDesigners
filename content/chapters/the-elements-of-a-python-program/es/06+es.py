def caminar(distancia, longitudDePaso):
    distanciaCaminada = 0
    while distancia > distanciaCaminada:
        oneStepForward(longitudDePaso)
        distanciaCaminada += longitudDePaso

caminar(100, 5)