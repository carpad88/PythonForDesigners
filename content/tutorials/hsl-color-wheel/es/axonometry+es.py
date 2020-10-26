#!/usr/bin/env python3
# coding: utf-8

# ---------- #
# Axonometry #
# ---------- #

### Módulos
# dependencias
from drawBot import newPage, width, height, translate
from drawBot import save, restore, scale, saveImage
from drawBot import newDrawing, endDrawing, savedState

# de la carpeta del proyecto
from HSLdonut import hslDonut

### Variables
discos = 16
anillos = 22
grosorAnillo = 5
radioAgujero = 45

### Instrucciones
if __name__ == '__main__':
    newDrawing()
    newPage(952, 488)

    translate(width()*.27, height()*.25)
    save()
    for cadaDisco in range(discos):
        with savedState():
            scale(1, .65)
            hslDonut(anillos,
                     grosorAnillo,
                     radioAgujero,
                     valorFijo=cadaDisco / (discos - 1),
                     esLuminosidadConst=True,
                     subtitulos=False)
        translate(0, 16)
    restore()

    translate(width()*.44, 0)
    save()
    for cadaDisco in range(discos):
        with savedState():
            scale(1, .65)
            hslDonut(anillos,
                     grosorAnillo,
                     radioAgujero,
                     valorFijo=cadaDisco / (discos - 1),
                     esLuminosidadConst=True,
                     subtitulos=False)
        translate(0, 16)
    restore()

    saveImage('cd-roms.pdf')
    endDrawing()
