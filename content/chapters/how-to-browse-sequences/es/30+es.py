rayas = 10
newPage(100, 100)

anchoDeRaya = width() / rayas

for indexDeRaya in range(rayas):
    if indexDeRaya % 2 == 0:
        fill(0)
    else:
        fill(1)
    rect(indexDeRaya * anchoDeRaya, 0, anchoDeRaya, height())
