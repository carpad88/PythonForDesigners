from string import ascii_lowercase, ascii_uppercase

# convertir desde cadenas de texto a listas usando el constructor list()
minusculasLatinas = list(ascii_lowercase)
mayusculasLatinas = list(ascii_uppercase)

# crear una lista vacía para completar el alfabeto an empty list for the complete alphabet
alfabetoLatino = []

# extender la lista vacía con las mayúsculas y minúsculas
alfabetoLatino.extend(mayusculasLatinas)
alfabetoLatino.extend(minusculasLatinas)

# resultado: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']