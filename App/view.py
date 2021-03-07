"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf

def funcion_boba():
    pass

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print('2- Requerimiento 1')
    print("0- Salir")


def initCatalog(est_datos):
    return controller.initCatalog(est_datos)

def loadData(catalog):
    controller.loadData(catalog)
    return None

def getFirstVideo(catalog):
    return controller.getFirstVideo(catalog)

def sort_sublist(catalog, numlen, type_sort, category, country):
    return controller.sort_sublist(catalog, numlen, type_sort, category, country)

def get_all_elements(catalog):
    return controller.get_all_elements(catalog)

def view_req1(diccionario):
    title = diccionario['title']
    cannel_title = diccionario['channel_title']
    publish_time = diccionario['publish_time']
    views = diccionario['views']
    likes = diccionario['likes']
    dislikes = diccionario['dislikes']
    tags = diccionario['tags']
    return title, cannel_title, publish_time, views, likes, dislikes, tags

def primerVideo(diccionario):
    title = diccionario['title']
    cannel_title = diccionario['channel_title']
    trending_date = diccionario['trending_date']
    country = diccionario['country']
    views = diccionario['views']
    likes = diccionario['likes']
    dislikes = diccionario['dislikes']

    return title, cannel_title, trending_date, country, views, likes, dislikes

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
       
        print('\nSelección de estructura:')
        print('1- Arreglo')
        print('2- Lista encadenada')
        est_datos = input('Seleccione que tipo de estructura desea implementar para el catálogo\n')
        print("Cargando información de los archivos ....")
        catalog = initCatalog(est_datos)
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('\nLista de categorías')
        print(catalog['category']['elements'])
        print('\nElementos del primer video')
        print(primerVideo(getFirstVideo(catalog)))
        
    elif int(inputs[0]) == 2:

        print('\nTipos de ordenamientos disponibles: ')
        print('1- Insertion Sort')
        print('2- Selection Sort')
        print('3- Shell Sort')
        print('4- Merge Sort')
        print('5- Quick Sort')
        type_sort = int(input('Seleccione el tipo de ordenamiento que desea ejecutar:\n'))
        numlen = int(input('Digite la cantidad de videos con más views que desea consultar:\n'))
        category = input('Digite la categoria que desea consultar:\n')
        country = input('Digite el país que desea consultar:\n')
        result = sort_sublist(catalog, numlen, type_sort, category, country)

        try:
            pos = 1
            for i in lt.iterator(result):
                print(f'Video número {pos}')
                print(view_req1(i))
                print('\n')
                pos += 1
        except:
            print(result)
        
    else:
        sys.exit(0)
sys.exit(0)
#hoaaa
