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
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    catalog = {'obras': None,
               'artistas': None,
               "Medium": None}

    catalog['obras'] = lt.newList()
    catalog['artistas'] = lt.newList()

    catalog['Medium'] = mp.newMap(120,
    maptype='PROBING',
    loadfactor=0.20,)

    catalog['Nationality'] = mp.newMap(160,
    maptype='PROBING',
    loadfactor=0.20)

    return catalog


# Funciones para agregar informacion al catalogo

def addObra(catalog, obra):
    lt.addLast(catalog['obras'], obra)
    mp.put(catalog["Medium"],obra["ObjectID"],obra["Medium"])

def addArtist(catalog, artista):
    lt.addLast(catalog['artistas'], artista)



# Funciones para creacion de datos

# Funciones de consulta

def obrasAntiguas(catalog, medio, n):
    masAntigua = 9999
    obraAntigua = None
    idMasAntiguas = lt.newList()
    obrasMasAntiguas = lt.newList()
    for i in range(0,n):
        for obra in lt.iterator(catalog['obras']):
            valor = mp.get(catalog["Medium"],obra["ObjectID"])["value"]
            if obra["Date"] != "":
                if valor == medio and int(obra["Date"]) < masAntigua and not(lt.isPresent(idMasAntiguas,obra["ObjectID"])):
                    masAntigua = int(obra["Date"])
                    obraAntigua = obra
        lt.addLast(obrasMasAntiguas,obraAntigua)
        lt.addLast(idMasAntiguas,obra["ObjectID"])

    return obrasMasAntiguas

def numeroObras(catalog, nacion):
    info = mp.newMap(4000, maptype='CHAINING', loadfactor=0.5,)
    for artista in lt.iterator(catalog["artistas"]):
        if not (mp.contains(catalog['Nationality'],artista["Nationality"])):
            mp.put(catalog['Nationality'],artista["Nationality"],0)
        mp.put(info,artista["ConstituentID"], artista["Nationality"])

    for obra in lt.iterator(catalog["obras"]):
        for id in obra["ConstituentID"].split(", "):
            id = id.replace("[","")
            id = id.replace("]","")
            if mp.get(info,id) != None:
                pais = (mp.get(info,id))["value"]
                nuevoValor = int((mp.get(catalog['Nationality'],pais))["value"]) + 1
                mp.put(catalog['Nationality'],pais,nuevoValor)
    return mp.get(catalog['Nationality'],nacion)

def listarCronologicamente(catalog, añoInicial, añoFinal):
    mapEnRango = mp.newMap(900, maptype='CHAINING',loadfactor=1)
    for artista in lt.iterator(catalog["artistas"]):
        if int(artista["BeginDate"]) >= añoInicial and int(artista["BeginDate"]) <= añoFinal:
            mp.put(mapEnRango,artista["DisplayName"],artista)

    mapFinal = mp.newMap(900, maptype='CHAINING',loadfactor=1)
    indice = 0

    for i in range(añoInicial,añoFinal+1):
        for elemento in lt.iterator(mp.valueSet(mapEnRango)):
            if int(elemento["BeginDate"]) == i:
              mp.put(mapFinal,indice,elemento)
              indice += 1

    return mapFinal

def nacionalidadCreadores(catalog):
    info = mp.newMap(4000, maptype='CHAINING', loadfactor=0.5,)
    for artista in lt.iterator(catalog["artistas"]):
        if not (mp.contains(catalog['Nationality'],artista["Nationality"])):
            mp.put(catalog['Nationality'],artista["Nationality"],0)
        mp.put(info,artista["ConstituentID"], [artista["Nationality"],artista["DisplayName"]])

    for obra in lt.iterator(catalog["obras"]):
        for id in obra["ConstituentID"].split(", "):
            id = id.replace("[","")
            id = id.replace("]","")
            if mp.get(info,id) != None:
                pais = (mp.get(info,id))["value"][0]
                nuevoValor = int((mp.get(catalog['Nationality'],pais))["value"]) + 1
                mp.put(catalog['Nationality'],pais,nuevoValor)

    paisSinNombre = (mp.get(catalog['Nationality'], ""))["value"]
    paisDesconocido = (mp.get(catalog['Nationality'],"Nationality unknown"))["value"]
    mp.put(catalog['Nationality'],"Nationality unknown",paisSinNombre + paisDesconocido)
    mp.remove(catalog['Nationality'],"")

    return catalog['Nationality'],info
# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def sortpaises(dict):
    map = mp.newMap(10, maptype='CHAINING',loadfactor=1)
    for i in range(0,10):
        mayor = -1
        llaveMayor = ""
        for llave in lt.iterator(mp.keySet(dict)):
           if mp.get(dict,llave) != None:
                valor = mp.get(dict,llave)["value"]
                if valor > mayor:
                    mayor = valor
                    llaveMayor = llave 
        mp.put(map,i,[llaveMayor,mayor])
        mp.remove(dict,llaveMayor)
    return map


def obrasPais(catalog,info,map):
    pais = (mp.get(map,0))["value"][0]
    mapFinal = mp.newMap(900, maptype='CHAINING',loadfactor=1)
    contador = 0
    for obra in lt.iterator(catalog["obras"]):
        condicion = False
        for id in obra["ConstituentID"].split(", "):
            id = id.replace("[","")
            id = id.replace("]","")
            if pais == (mp.get(info,id))["value"][0]:
                condicion = True
        if condicion: 
            formatoObra =  {"Titulo":obra["Title"] ,"Artistas":(mp.get(info,id))["value"][1],
            "Fecha":obra["Date"],"Medio":obra["Medium"],
            "Dimensiones":obra["Dimensions"]} 
            mp.put(mapFinal,contador,formatoObra)
            contador += 1   
    return mapFinal