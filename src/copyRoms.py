#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################
# copyRoms.py
# copy roms
#
# Autor: César Augusto Martínez Franco
#        Lisset Noriega Domínguez
#
#        Jesús Arturo Vázquez Zaragoza
#
# License: MIT
#
# ## ###############################################

import os
import shutil
"""Copía roms desde una memoria usb

Parameters

sourceDir : String
    Dirección desde donde se copia los roms
    
destDir : String
    Dirección de destino de los roms
    
return
    void

"""
def copyFiles(sourceDir, destDir):
    fileExt = ".gbc"
    ROMS = []
    for file in os.listdir(sourceDir):
        if file.endswith(fileExt):
            ROMS.append(file)
    for rom in ROMS:
        src = "{}/{}".format(sourceDir,rom)
        dst = "{}/{}".format(destDir,rom)
        try:
            shutil.copy(src, dst)
        except shutil.SameFileError:
            print('Ya se encuentra el archivo')
        except PermissionError:
            print('Permiso denegado')
        except:
            print('Ocurrió un error al copiar los archivos')

#copyFiles("/home/pi/Desktop/proyectoFInalEmbebidos/ROMS/GBC","/home/pi/Desktop")
