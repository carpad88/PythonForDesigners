texto = """Considerar la existencia de un conjunto de herramientas convencionales para la organización e interpretación del espacio concatenado, que de alguna manera interactúa con el lenguaje hablado, es útil porque es conveniente desde el punto de vista del diseño."""

newPage(200, 200)
cajaTexto = (20, 30, 150, 150)

fill(.8)
rect(*cajaTexto)

fill(0)
textBox(texto, cajaTexto, align='left')