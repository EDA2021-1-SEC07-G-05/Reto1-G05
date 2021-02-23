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
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog(est_datos):
    #Los condicionales de aquí dictan que Est. de datos implementar de acuerdo a lo que el usario puso en el view y que luego pasó por el controller
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

#La función que ves aquí simplemente le entran dos videos y devuelve True si el segundo video tiene mas o igual views que el primero
def cmpVideosByViews(video_1, video_2):
    if video_1['views']<video_2['views']:
        valor = True
    else:
        valor = False
    return valor

# Funciones de ordenamiento

#Esta de aquí sería tu parte, con los datos que llegaron del view y pasaron por el controller, en estafunción debes
#crear y ordenar una sublista de tamaño numlen y con la función de ordenamiento type_sort. Recuerda que type_sort es un número, así que aquí
#tienes que usar condicionales tal que, 1 = insertion_sort 2 = selection_sort 3 = Shell_sort. Recuerda también imprimir el tiempo que se demora.
#No estaría de más basarte en el sort del ejemplo del lab04. Cualquier cosa escríbeme!!
"""Aqui está la función que me dijiste, espero que haya quedado bien :)"""
def sort_sublist(catalog, numlen, type_sort):

    sub_list= lt.subList(catalog['videos'],1,numlen)
    sub_list= sub_list.copy()
    start_time= time.process_time()

    if type_sort==1: 
        sorted_list =ins.sort(sub_list,cmpVideosByViews)
    
    elif type_sort ==2:
        sorted_list= slc.sort(sub_list,cmpVideosByViews)
     
    else: 
        sorted_list = sa.sort(sub_list,cmpVideosByViews)
    
    stop_time= time.process_time()
    elapsed_time_mseg = (stop_time-start_time)*1000 
    return elapsed_time_mseg, sorted_list