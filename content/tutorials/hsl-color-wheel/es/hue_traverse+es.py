### Modules
from colorsys import hls_to_rgb

### Constantes
CIRCULO_COMPLETO = 360

### Instrucciones
newPage(400, 400)
# mover el punto de referencia al centro del lienzo
# facilita la rotación dentro del bucle for
translate(width() / 2, height() / 2)

# iteramos sobre 360 ° usando pasos de 10 °
for angulo in range(0, CIRCULO_COMPLETO, 10):
    # tanto la saturación como la luminosidad son parámetros fijos
    color_RGB = hls_to_rgb(angulo / CIRCULO_COMPLETO, .7, .7)

    # ¡contexto de estado gráfico!
    # más información aquí
    # https://www.drawbot.com/content/canvas/state.html#managing-the-graphics-state
    with savedState():
        rotate(angulo)
        translate(100, 0)
        fill(*color_RGB)
        oval(-4, -4, 8, 8)

