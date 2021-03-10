"""
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
import time 
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as slc
from DISClib.Algorithms.Sorting import mergesort as mg 
from DISClib.Algorithms.Sorting import quicksort as qc
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
    
    catalog['videos'] = lt.newList(x, cmpfunction = cmpVideos)
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

def getCategory_id(catalog, category):
    for i in lt.iterator(catalog['category']):
        if i['cat_name'] == ' ' + category:
            cat_id = int(i['cat_id'])
            break
    return cat_id

def get_all_elements(catalog):
    resultado = list()
    for i in lt.iterator(catalog):
        pos = 1
        resultado.append(lt.getElement(catalog, pos))
        pos += 1
    return resultado

def mostTrendingVideo(catalog, attribute, indicator):
    lista_trabajo = lt.newList('SINGLE_LINKED', cmpVideos)

    if indicator == 0:
        for video in lt.iterator(catalog['videos']):
            if lt.isPresent(lista_trabajo, video) != 0:
                pos = lt.isPresent(lista_trabajo, video)
                lt.getElement(lista_trabajo, pos)['trending_days'] += 1

            elif video['country'] == attribute:
                lt.addFirst(lista_trabajo, video)
                lt.firstElement(lista_trabajo)['trending_days'] = 1

    else: 
        for video in lt.iterator(catalog['videos']):
            if lt.isPresent(lista_trabajo, video) != 0:
                pos = lt.isPresent(lista_trabajo, video)
                lt.getElement(lista_trabajo, pos)['trending_days'] += 1

            elif video['category_id'] == attribute:
                lt.addFirst(lista_trabajo, video)
                lt.firstElement(lista_trabajo)['trending_days'] = 1

    sorted_list = mg.sort(lista_trabajo, cmpVideosByTrend)
       
    return  lt.firstElement(sorted_list)

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpVideosByViews(video_1, video_2):
    if int(video_1['views'])>int(video_2['views']):
        valor = True
    else:
        valor = False
    return valor

def cmpVideos(video_1, video_2):
    if video_1['video_id']>video_2['video_id']:
        return 1
    elif video_1['video_id'] == video_2['video_id']:
        return 0
    else:
        return -1

def cmpVideosByTrend(video_1, video_2):
    if video_1['trending_days'] > video_2['trending_days']:
        valor = True
    else:
        valor = False
    return valor
# Funciones de ordenamiento

def sort_sublist(catalog, numlen, category, country):

    lista_trabajo = lt.newList('ARRAY_LIST')

    for i in lt.iterator(catalog['videos']):
        if i['country'] == country and int(i['category_id']) == category:
            lt.addFirst(lista_trabajo, i)

    
    sorted_list = mg.sort(lista_trabajo, cmpVideosByViews)

    try:
        resultado = lt.subList(sorted_list,1,numlen)
    except:
        resultado = 'No existen tantos videos, intente con un número más pequeño...'
    return resultado
