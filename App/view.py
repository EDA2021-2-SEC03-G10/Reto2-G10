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
from DISClib.ADT import map as mp
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print(chr(27)+"[1;32m")
    print("Bienvenido")
    print(chr(27)+"[0;37m")
    print(chr(27)+"[4;32m"+"1" + chr(27)+ "[0;37m" + "- Cargar información en el catálogo")

    # Funciones de los laboratorios
    print(chr(27)+"[4;32m"+"2" + chr(27)+ "[0;37m" + "- las n obras más antiguas para un medio específico")
    print(chr(27)+"[4;32m"+"3" + chr(27)+ "[0;37m" + "- número total de obras de una nacionalidad")

    # Requisitos
    print(chr(27)+"[4;32m"+ "4" + chr(27)+ "[0;37m" + "- Listar cronológicamente los artistas (Requisito 1)")
    print(chr(27)+"[4;32m"+ "5" + chr(27)+ "[0;37m" + "- Listar cronologicamente las adquisiciones (Requisito 2)")
    print(chr(27)+"[4;32m"+ "6" + chr(27)+ "[0;37m" + "- Clasificar las obras de un artista por tecnica (Requisito 3)")
    print(chr(27)+"[4;32m"+ "7" + chr(27)+ "[0;37m" + "- Clasificar las obras por la nacionalidad de sus creadores (Requisito 4)")
    print(chr(27)+"[4;32m"+ "8" + chr(27)+ "[0;37m" + "- Transportar obras de un departamento (Requisito 5)")

def initCatalog():
    return controller.initCatalog()

def loadData(catalog):
    controller.loadData(catalog)

def obrasAntiguas(catalog, medio, n):
    return controller.obrasAntiguas(catalog, medio, n)

def numeroObras(catalog,nacion):
    return controller.numeroObras(catalog,nacion)

# Requisito 1
def listarCronologicamente(catalog, añoInicial, añoFinal):
    return controller.listarCronologicamente(catalog, añoInicial, añoFinal)

# Requisito 2
def listarAdquisiciones(catalog, fechaInicial, fechaFinal):
    pass

# Requisito 4
def nacionalidadCreadores(catalog):
    return controller.nacionalidadCreadores(catalog)

# Requisito 5
def transportar_obras(catalog,departamento):
    pass

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Obras cargadas: ' + str(lt.size(catalog['obras'])))
        print('Artistas cargados: ' + str(lt.size(catalog['artistas'])))

    elif int(inputs[0]) == 2:
        medio = input("Escriba el medio: ")
        n = int(input("Escriba el numero de obras mas antiguas que se desea obtener: "))
        print("Calculando obras mas antiguas por medio ....")
        print("\n")
        listaObras = obrasAntiguas(catalog, medio, n)
        for obra in lt.iterator(listaObras):
            print(obra)
            print("\n")

    elif int(inputs[0]) == 3:
        nacion = input("Escriba la nacionalidad: ")
        cantidad = numeroObras(catalog,nacion)["value"]
        print("La cantidad de obras de la nacionalidad dada es: " + str(cantidad))

    elif int(inputs[0]) == 4:
        añoInicial = int(input("Ingrese el año inicial(yyyy): ")) 
        añoFinal = int(input("Ingrese el año final(yyyy): "))
        print("Listando los artistas de manera cronologica ....")
        
        mapEnRango = listarCronologicamente(catalog, añoInicial, añoFinal)
        tamaño = mp.size(mapEnRango)
        print("\n")
        print("Numero de artistas dentro del rango: " + str(tamaño)+"\n")

        artista1 = mp.get(mapEnRango,0)
        artista2 = mp.get(mapEnRango,1)
        artista3 = mp.get(mapEnRango,2)
        artista4 = mp.get(mapEnRango,tamaño-3)
        artista5 = mp.get(mapEnRango,tamaño-2)
        artista6 = mp.get(mapEnRango,tamaño-1)

        artistas = artista1,artista2,artista3,artista4,artista5,artista6

        for artista in artistas:
            info = artista['value']
            print(chr(27)+"[1;34m"+ "Nombre: " + chr(27)+"[0;37m"+ info["DisplayName"],
                    chr(27)+"[1;34m"+ ", Nacimiento: "+ chr(27)+"[0;37m"+ info["BeginDate"], 
                    chr(27)+"[1;34m"+ ", Fallecimmiento: " + chr(27)+"[0;37m"+ info["EndDate"],
                    chr(27)+"[1;34m"+ ", Nacionalidad: " + chr(27)+"[0;37m"+ info["Nationality"],
                    chr(27)+"[1;34m"+ ", Genero: " + chr(27)+"[0;37m"+ info["Gender"])

    elif int(inputs[0]) == 5:
        pass

    elif int(inputs[0]) == 6:
        pass

    elif int(inputs[0]) == 7:
       clasificacion,obras = nacionalidadCreadores(catalog)
       print(chr(27)+"[1;44m"+"NACIONALIDADES CON EL MAYOR NUMERO DE OBRAS"+chr(27)+"[0;37m")
       print("\n")

       for pais in lt.iterator(clasificacion): 
           for llave in pais.keys():
               print(chr(27)+"[1;34m"+llave+"   "+chr(27)+"[0;37m"+str(pais[llave]))
               print("\n")

       print(chr(27)+"[1;44m"+"INFORMACION DE LAS 3 PRIMERAS Y DE LAS 3 ULTIMAS OBRAS DE LA NACIONALIDAD CON EL MAYOR NUMERO DE OBRAS"+chr(27)+"[0;37m")
       tamaño = lt.size(obras)

       obra1 = lt.getElement(obras, 1)
       obra2 = lt.getElement(obras, 2)
       obra3 = lt.getElement(obras, 3)
       obra4 = lt.getElement(obras, tamaño-2)
       obra5 = lt.getElement(obras, tamaño-1)
       obra6 = lt.getElement(obras, tamaño)

       obrasFinales = obra1,obra2,obra3,obra4,obra5,obra6

       for obra in obrasFinales: 
           print("\n")
           for llave2 in obra.keys():
               print(chr(27)+"[1;34m"+llave2+": "+chr(27)+"[0;37m"+obra[llave2])


    elif int(inputs[0]) == 8:
        pass

    else:
        sys.exit(0)
sys.exit(0)
