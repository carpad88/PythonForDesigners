#!/usr/bin/env python3
# coding: utf-8

# ------------------------------- #
# Make multiple Kerning Heat Maps #
# ------------------------------- #

### Modules
# de la carpeta del proyecto
from flatKerningDefault import flatKerning
from withCaptions import kerningHeatMap, CELL_SIZE

# dependencias
from fontParts.world import OpenFont
from drawBot import newDrawing, endDrawing, newPage, saveImage, translate

# librería estándar
from string import ascii_uppercase, ascii_lowercase
from os import listdir, mkdir
from os.path import join, exists
from shutil import rmtree


### Objetos, funciones, procedimientos
def capturarArchivos(carpeta, extension):
    return [join(carpeta, nn) for nn in listdir(carpeta)
            if nn.endswith(extension)]


def limpiar(folder):
    if exists(folder):
        rmtree(folder)
    mkdir(folder)


### Instrucciones
if __name__ == '__main__':
    folderSalida = 'output'
    limpiar(folderSalida)

    rutasFuentes = capturarArchivos('fonts', '.ufo')
    conjuntoGlifos = {'uppercase': ascii_uppercase,
                      'lowercase': ascii_lowercase}

    for cadaRuta in rutasFuentes:
        estaFuente = OpenFont(cadaRuta)

        for nombreConjunto, cadaConjunto in conjuntoGlifos.items():
            flat = flatKerning(estaFuente, cadaConjunto)
            tamanoLienzo = TAMANO_CELDA * (len(cadaConjunto) + 4)
            newDrawing()
            newPage(tamanoLienzo, tamanoLienzo)
            translate(TAMANO_CELDA * 2, TAMANO_CELDA * 2)
            kerningHeatMap(flat, cadaConjunto, isFirstVertical=True)

            nombreFuente = f'{estaFuente.info.familyName} {estaFuente.info.styleName}'
            saveImage(join(folderSalida, f'{nombreFuente} - {nombreConjunto}.pdf'))
            endDrawing()

