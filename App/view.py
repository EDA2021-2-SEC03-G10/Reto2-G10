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
    return controller.listarAdquisiciones(catalog, fechaInicial, fechaFinal)
 
# Requisito 3
def clasificar_tecnicas(catalog,nombre):
    return controller.clasificar_tecnicas(catalog,nombre)

# Requisito 4
def nacionalidadCreadores(catalog):
    return controller.nacionalidadCreadores(catalog)

# Requisito 5
def transportar_obras(catalog,departamento):
    return controller.transportar_obras(catalog,departamento)

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
        fechaInicial = (input("Ingrese la fecha inicial(yyyy-mm-dd): "))
        año, mes, día = map(int, fechaInicial.split('-'))
        fechaInicial= (año, mes, día)
        fechaFinal = (input("Ingrese el año final(yyyy-mm-dd): "))
        año2, mes2, día2 = map(int, fechaFinal.split('-'))
        fechaFinal= (año2, mes2, día2)
        print("Listando las adquisiciones de manera cronologica ....")
        mapFechas,compras = listarAdquisiciones(catalog, fechaInicial, fechaFinal)
        tamaño = mp.size(mapFechas)
        print("\n")
        print("Numero de obras dentro del rango: " + str(tamaño)+"\n")
        print("Número total de obras adquiridas por compra " + str(compras)+"\n")

        obra1 = mp.get(mapFechas, 0)
        obra2 = mp.get(mapFechas, 1)
        obra3 = mp.get(mapFechas, 2)
        obra4 = mp.get(mapFechas, tamaño-3)
        obra5 = mp.get(mapFechas, tamaño-2)
        obra6 = mp.get(mapFechas, tamaño-1)

        print(chr(27)+"[1;37m"+"Las primeras y las últimas 3 obras son: "+chr(27)+"[0;37m")
        print("\n")

        obras = obra1,obra2,obra3,obra4,obra5,obra6

        for obra in obras:
            datos = obra['value']
            print(chr(27)+"[1;34m"+"Título: " + chr(27)+"[0;37m"+ datos["Title"],
                    chr(27)+"[1;34m"+", Fecha: " + chr(27)+"[0;37m"+ datos["Date"],
                    chr(27)+"[1;34m"+", Medio: " + chr(27)+"[0;37m"+ datos["Medium"],
                    chr(27)+"[1;34m"+", Dimensiones: " + chr(27)+"[0;37m"+ datos["Dimensions"])
            print("\n")

    elif int(inputs[0]) == 6:
        nombre = str(input("Ingrese el nombre del artista: "))
        tecnicas = clasificar_tecnicas(catalog,nombre)
        tamaño = mp.size(tecnicas)
        print("Numero de obras dentro del rango: " + str(tamaño)+"\n")
        obra1 = mp.get(tecnicas, 0)
        obra2 = mp.get(tecnicas, 1)
        obra3 = mp.get(tecnicas, 2)
        obra4 = mp.get(tecnicas, tamaño-3)
        obra5 = mp.get(tecnicas, tamaño-2)
        obra6 = mp.get(tecnicas, tamaño-1)

        print(chr(27)+"[1;37m"+"Las primeras y las últimas 3 obras por técnica son: "+chr(27)+"[0;37m")
        print("\n")

        obras = obra1,obra2,obra3,obra4,obra5,obra6

        for obra in obras:
            datosObra = obra["value"]
            print(chr(27)+"[1;34m"+"Título: " + chr(27)+"[0;37m"+ datosObra["Title"],
                    chr(27)+"[1;34m"+", Fecha: " + chr(27)+"[0;37m"+ datosObra["Date"],
                    chr(27)+"[1;34m"+", Medio: " + chr(27)+"[0;37m"+ datosObra["Medium"],
                    chr(27)+"[1;34m"+", Dimensiones: " + chr(27)+"[0;37m"+ datosObra["Dimensions"])
            print("\n")

    elif int(inputs[0]) == 7:
       clasificacion,obras = nacionalidadCreadores(catalog)
       print(chr(27)+"[1;44m"+"NACIONALIDADES CON EL MAYOR NUMERO DE OBRAS"+chr(27)+"[0;37m")
       print("\n")

       for posicion in range(0,10):
            pais = (mp.get(clasificacion, posicion))["value"][0]
            conteo = (mp.get(clasificacion, posicion))["value"][1]
            print(chr(27)+"[1;34m"+pais+"   "+chr(27)+"[0;37m"+ str(conteo))
            print("\n")

       print(chr(27)+"[1;44m"+"INFORMACION DE LAS 3 PRIMERAS Y DE LAS 3 ULTIMAS OBRAS DE LA NACIONALIDAD CON EL MAYOR NUMERO DE OBRAS"+chr(27)+"[0;37m")
       tamaño = mp.size(obras)

       obra1 = mp.get(obras, 0)["value"]
       obra2 = mp.get(obras, 1)["value"]
       obra3 = mp.get(obras, 2)["value"]
       obra4 = mp.get(obras, tamaño-3)["value"]
       obra5 = mp.get(obras, tamaño-2)["value"]
       obra6 = mp.get(obras, tamaño-1)["value"]

       obrasFinales = obra1,obra2,obra3,obra4,obra5,obra6

       for obra in obrasFinales: 
           print("\n")
           for llave2 in obra:
               print(chr(27)+"[1;34m"+llave2+": "+chr(27)+"[0;37m"+obra[llave2])


    elif int(inputs[0]) == 8:
        departamento = (input("Ingrese el departamento a transportar las obras: "))
        obras_antigüedad,count,peso,precio,precio_total, obras_caras,Precio_caras, Precio_antiguas = transportar_obras(catalog,departamento)
        print("El número de obras a transportar es: " + str(count))
        print("Peso estimado de las obras: " + str(peso))
        print ("Estimado en USD del precio del servicio: " +str(precio_total)+ "USD")
        print( chr(27)+"[1;44m"+ "Las 5 obras más antiguas son: "+chr(27)+"[0;37m")
        print("\n")
        conteo1 = 1
        for obra_antigua in lt.iterator(obras_antigüedad):
            print(chr(27)+"[1;34m" + "Título: " + chr(27)+"[0;37m"+ str(obra_antigua["Title"]))
            print(chr(27)+"[1;34m" + "Artistas: " + chr(27)+"[0;37m"+ str(obra_antigua["ConstituentID"]))
            print(chr(27)+"[1;34m" + "Clasificación: " +chr(27)+"[0;37m"+ str(obra_antigua["Classification"]))
            print(chr(27)+"[1;34m" + "Fecha: " +chr(27)+"[0;37m"+ str(obra_antigua["Date"]))
            print(chr(27)+"[1;34m" + "Medio: " + chr(27)+"[0;37m"+ str(obra_antigua["Medium"]))
            print(chr(27)+"[1;34m" + "Dimensiones: " +chr(27)+"[0;37m"+ str(obra_antigua["Dimensions"]))
            print(chr(27)+"[1;34m" + "Precio: " +chr(27)+"[0;37m"+ str(lt.getElement(Precio_antiguas,conteo1)))
            conteo1 +=1
            print("\n")
        print( chr(27)+"[1;44m"+"Las 5 obras más costosas a transportar son: "+chr(27)+"[0;37m")
        print("\n")
        conteo2=1
        for obra_costosa in lt.iterator(obras_caras):
            print(chr(27)+"[1;34m" + "Título: " + chr(27)+"[0;37m"+ str(obra_costosa["Title"]))
            print(chr(27)+"[1;34m" + "Artistas: " + chr(27)+"[0;37m"+ str(obra_costosa["ConstituentID"]))
            print(chr(27)+"[1;34m" + "Clasificación: " + chr(27)+"[0;37m"+ str(obra_costosa["Classification"]))
            print(chr(27)+"[1;34m" + "Fecha: " +chr(27)+"[0;37m"+ str(obra_costosa["Date"]))
            print(chr(27)+"[1;34m" + "Medio: " + chr(27)+"[0;37m"+ str(obra_costosa["Medium"]))
            print(chr(27)+"[1;34m" + "Dimensiones: " + chr(27)+"[0;37m"+ str(obra_costosa["Dimensions"]))
            print(chr(27)+"[1;34m" + "Precio: " + chr(27)+"[0;37m"+ str(lt.getElement(Precio_caras,conteo2)))
            conteo2 +=1
            print("\n")

    else:
        sys.exit(0)
sys.exit(0)
