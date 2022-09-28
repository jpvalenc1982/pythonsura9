import pandas as pd
tablaSiembras=pd.read_csv('./Siembras.csv')
'''
Usando pandas lea el archivo siembras csv y exporte un documento html con los siguientes filtros de información
1. Datos por municipio
- Andes
- Barbosa
- Caldas
- Támesis
- Yarumal
'''
#options = ['Andes','Barbosa','Caldas','Támesis','Yarumal']
tablaFiltro1=tablaSiembras[tablaSiembras["Ciudad"].isin(['Andes','Barbosa','Caldas','Támesis','Yarumal'])]
#tablaFiltro1=tablaSiembras[tablaSiembras["Ciudad"]=="Andes"].head(50)
# print(tablaFiltro1)
archivoHTML=tablaFiltro1.to_html()
archivoTEXTO=open("datosfiltrocora1.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()