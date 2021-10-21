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
   
 def listarAdquisiciones(catalog, fechaInical, fechaFinal):
    mapFecha = mp.newMap(900, maptype='CHAINING',loadfactor=1)
    compra=0
    for obra in lt.iterator(catalog['obras']):
        if (obra["CreditLine"])=="Purchase":
            compra+=1
        if (obra["DateAcquired"]) != "":
            año3,mes3,dia3 =map(int, (obra['DateAcquired']).split('-'))
            fechaA=(año3,mes3,dia3)
            if fechaA >= fechaInical and fechaA<= fechaFinal:
                mp.put(mapFecha,obra["Title"],obra)
    adquisiciones = mp.newMap(900, maptype='CHAINING',loadfactor=1)
    indice = 0
    for i in range(fechaInical[0],fechaFinal[0]):
        for eso in lt.iterator(mp.valueSet(mapFecha)):
            if fechaA[0]== i:
                mp.put(adquisiciones,indice,eso)
                indice += 1 

    return adquisiciones,compra
   
def catalog_id(catalog,nombre):
    for artista in lt.iterator(catalog["artistas"]):
        if nombre in artista["DisplayName"]:
            return artista["ConstituentID"]

def clasificar_tecnica(catalog,map):
    datos = mp.newMap(4000, maptype='CHAINING', loadfactor=0.5)
    todo = mp.newMap(4000, maptype='CHAINING', loadfactor=0.5)
    for obra in lt.iterator(catalog["obras"]):
        mp.put(datos,obra["ObjectID"],obra)
        for id in obra["ConstituentID"].split(", "):
            id = id.replace("[","")
            id = id.replace("]","")
            if mp.get(datos,id) != None:
                if id in map:
                    mp.put(todo,obra["ObjectID"],obra)
    return todo

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
   
   def transportar_obras(catalog,departamento):
    count = 0
    peso = 0
    Precio_total= 0
    Precio= 0
    Fechas_obras= mp.newMap(5000, maptype= "PROBING", loadfactor=0.5)
    Precio_obras = mp.newMap(5000, maptype='PROBING',loadfactor=0.5)
    for obra in lt.iterator(catalog["obras"]):
        Dimension = 1
        if departamento == (obra["Department"]):
            mp.put(Fechas_obras,obra["ObjectID"],obra)
            count += 1
            
            if obra["Weight (kg)"] != "":
                peso += float(obra["Weight (kg)"])
            if obra["Height (cm)"] != "" and obra["Height (cm)"] != "0":
                Dimension *= (float(obra["Height (cm)"])/100)         
            if obra["Width (cm)"] != "" and obra["Width (cm)"] != "0":
                Dimension *= (float(obra["Width (cm)"])/100)
            if obra["Depth (cm)"] != "" and obra["Depth (cm)"] != "0":
                Dimension *= (float(obra["Depth (cm)"])/100) 
            if  Dimension != 1:
                Precio= 72*(Dimension)
            else:
                Precio= 48
            Precio_total += Precio
            mp.put(Precio_obras,obra["ObjectID"],[Precio,obra])
    return Fechas_obras,count, peso,Precio,Precio_total,Precio_obras

def obras_mas_antiguas(map,map_precios):
    obraAntigua = None
    idMasAntiguas = lt.newList()
    obrasMasAntiguas = lt.newList()
    Precios_obras= lt.newList("ARRAY_LIST")
    for i in range(0,5):
        masAntigua=9999
        for id in lt.iterator(mp.keySet(map)):
            valor = mp.get(map,id)["value"]["Date"]
            if valor != "":
                if int(valor) < masAntigua and not(lt.isPresent(idMasAntiguas,id)):
                    masAntigua = int(valor)
                    obraAntigua = mp.get(map,id)["value"]
                    idObraAntigua = id
        lt.addLast(idMasAntiguas,idObraAntigua)
        lt.addLast(obrasMasAntiguas,obraAntigua)
        precio_antigua = mp.get(map_precios,idObraAntigua)["value"][0]
        lt.addLast(Precios_obras,precio_antigua)
    return obrasMasAntiguas,Precios_obras

def obras_mas_Caras(map):
    obraCara = None
    idMasCara = lt.newList("ARRAY_LIST")
    obrasMasCaras = lt.newList()
    for i in range(0,5):
        masCara=0
        for id in lt.iterator(mp.keySet(map)):
            valor = mp.get(map,id)["value"][0]
            if valor > masCara and not(lt.isPresent(idMasCara,valor)):
                masCara = valor
                idCara = id
        lt.addLast(idMasCara,masCara)
        obraCara = mp.get(map,idCara)["value"][1]
        lt.addLast(obrasMasCaras,obraCara)
    return obrasMasCaras,idMasCara
