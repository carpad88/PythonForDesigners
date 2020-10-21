newPage(100, 100)
miVariable = 10

# ¡expresiones de comparación encadenadas!
# es útil a la hora de buscar
# un valor incluido entre valores
if 20 < miVariable:
    fill(0)
elif 20 >= miVariable > 12:
    fill(.3)
elif 12 >= miVariable > 8:
    fill(.6)
else:
    fill(.9)
rect(10, 10, 50, 50)