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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initCatalog():
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    loadObras(catalog)
    loadArtistas(catalog)

def loadObras(catalog):
    ObrasFile = cf.data_dir + 'MoMA/Artworks-utf8-large.csv'
    input_file = csv.DictReader(open(ObrasFile, encoding='utf-8'))
    for obra in input_file:
        model.addObra(catalog, obra)

def loadArtistas(catalog):
    artistasFile = cf.data_dir + 'MoMA/Artists-utf8-large.csv'
    input_file = csv.DictReader(open(artistasFile, encoding='utf-8'))
    for artista in input_file:
        model.addArtist(catalog, artista)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def listarCronologicamente(catalog, añoInicial, añoFinal):
    listaEnRango = model.listarCronologicamente(catalog, añoInicial, añoFinal)
    return listaEnRango
  
def listarAdquisiciones(catalog, fechaInicial, fechaFinal):
    resultado = model.listarAdquisiciones(catalog, fechaInicial, fechaFinal)
    return resultado

def clasificar_tecnicas(catalog,nombre):
    catalog_id = model.catalog_id(catalog,nombre)
    clasificar_tecnica= model.clasificar_tecnica(catalog,catalog_id)
    return clasificar_tecnica


def obrasAntiguas(catalog, medio, n):
    return model.obrasAntiguas(catalog, medio, n)

def numeroObras(catalog,nacion):
    return model.numeroObras(catalog,nacion)
 
def transportar_obras(catalog,departamento):
    Obras_transportar,count,peso, Precio, Precio_Total, Precio_Obras = model.transportar_obras(catalog,departamento)
    Obras_Antiguas, Precio_Antiguas= model.obras_mas_antiguas(Obras_transportar,Precio_Obras)
    Obras_Caras, IdMasCara= model.obras_mas_Caras(Precio_Obras)
    return Obras_Antiguas, count, peso, Precio, Precio_Total, Obras_Caras,IdMasCara, Precio_Antiguas

def nacionalidadCreadores(catalog):
    dictnacionalidades,info = model.nacionalidadCreadores(catalog)
    clasificacion = model.sortpaises(dictnacionalidades) 
    obras = model.obrasPais(catalog,info,clasificacion)
    return clasificacion, obras





