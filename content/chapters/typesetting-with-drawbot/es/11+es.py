texto = """Considerar la existencia de un conjunto de herramientas convencionales para la organización e interpretación del espacio concatenado, que de alguna manera interactúa con el lenguaje hablado, es útil porque es conveniente desde el punto de vista del diseño."""

newPage(200, 200)
hyphenation(True)
language('English')
textBox(texto, (20, 30, 150, 150), align='left')

newPage(200, 200)
hyphenation(True)
language('Spanish')
textBox(texto, (20, 30, 150, 150), align='left')