index = 0

while index <= 20:
    index += 1

    if index % 2 == 0:
        print('número par encontrado')
        continue
    print('número impar encontrado')

print('fuera del bucle while')