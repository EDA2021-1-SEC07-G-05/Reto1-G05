﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(est_datos):
    if est_datos == 1:
        x = 'ARRAY_LIST'
    else:
        x = 'SINGLE_LINKED'
    catalog = {'videos': None,   
               'category': None}
    
    catalog['videos'] = lt.newList(x)
    catalog['category'] = lt.newList('ARRAY_LIST')
    return catalog
# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)
    return None

def addCategory(catalog, category):
    cat = newCategory(category['name'], category['id'])
    lt.addLast(catalog['category'], cat)
    return None

# Funciones para creacion de datos

def newCategory(name, ide):
    category = {'cat_name': name,
                'cat_id': ide}
    return category

# Funciones de consulta
def getFirstVideo(catalog):
    return lt.firstElement(catalog['videos'])


# Funciones utilizadas para comparar elementos dentro de una lista
def cmpVideosByViews(video_1, video_2):
    if video_1['views']<video_2['views']:
        valor = True
    else:
        valor = False
    return valor

# Funciones de ordenamiento