import pandas as pd
tablaSiembras=pd.read_csv('./Siembras.csv')
'''
Usando pandas lea el archivo siembras csv y exporte un documento html con los siguientes filtros de información
7. Todos los datos de CARAMANTA
'''
tablaFiltro7=tablaSiembras[tablaSiembras["Ciudad"]=="Caramanta"]
# print(tablaFiltro7)
archivoHTML=tablaFiltro7.to_html()
archivoTEXTO=open("datosfiltrocora7.html","w",encoding="utf-8") #utf-8 para exportar los caracteres
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()