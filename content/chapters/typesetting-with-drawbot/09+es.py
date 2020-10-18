texto = """Considerar la existencia de un conjunto de herramientas convencionales para la organización e interpretación del espacio concatenado, que de alguna manera interactúa con el lenguaje hablado, es útil porque es conveniente desde el punto de vista del diseño: colocar el texto en oposición a la imagen solo es útil replicar un modelo de edición de libros que se consagró a finales del siglo XV, ligado a las técnicas de producción existentes en ese momento (tipografía móvil y xilografía) y básicamente aplicable principalmente a la edición de libros ligada a la ficción, que es solo una pequeña parte de la producción escrita."""

cajaTexto = (20, 30, 150, 150)
while texto:
    newPage(200, 200)

    fill(.9)
    rect(*cajaTexto)

    fill(0)
    texto = textBox(texto, cajaTexto, align='left')