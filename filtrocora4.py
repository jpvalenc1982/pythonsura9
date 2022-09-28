import pandas as pd
tablaSiembras=pd.read_csv('./Siembras.csv')
'''
Usando pandas lea el archivo siembras csv y exporte un documento html con los siguientes filtros de información
4. Los datos de Santa Fe de Antioquia donde se tengan siembras de 250 arboles
'''
tablaFiltro4=(tablaSiembras[(tablaSiembras["Arboles"]>250)&(tablaSiembras["Ciudad"]=="Santa Fe de Antioquia")])
#print(tablaFiltro4)
archivoHTML=tablaFiltro4.to_html()
archivoTEXTO=open("datosfiltrocora4.html","w",encoding="utf-8") #utf-8 para exportar los caracteres
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()