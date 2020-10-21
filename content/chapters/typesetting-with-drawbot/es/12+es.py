texto = """Considerar la existencia de un conjunto de herramientas convencionales para la organización e interpretación del espacio concatenado, que de alguna manera interactúa con el lenguaje hablado, es útil porque es conveniente desde el punto de vista del diseño: colocar el texto en oposición a la imagen solo es útil replicar un modelo de edición de libros que se consagró a finales del siglo XV, ligado a las técnicas de producción existentes en ese momento (tipografía móvil y xilografía) y básicamente aplicable principalmente a la edición de libros ligada a la ficción, que es solo una pequeña parte de la producción escrita."""

cajaTexto = (10, 30, 180, 150)

# La alineación justificada sin separación de palabras no tiene sentido
newPage(200, 200)
hyphenation(False)
textBox(texto, cajaTexto, align='justified')

# la separación de sílabas ayuda, pero aún está lejos de ser óptima
newPage(200, 200)
hyphenation(True)
textBox(texto, cajaTexto, align='justified')

# elegir el idioma adecuado mejora la composición
newPage(200, 200)
hyphenation(True)
language('Spanish')
textBox(texto, cajaTexto, align='justified')

# en este caso solo alinearía a la izquierda
# no veo problemas en un borde derecho ligeramente irregular
# los diseñadores que se quejan de ello solo consideran
# el marco y no el contenido
newPage(200, 200)
hyphenation(True)
textBox(texto, cajaTexto, align='left')

