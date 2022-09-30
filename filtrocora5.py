import pandas as pd
tablaSiembras=pd.read_csv('./Siembras.csv')
'''
Usando pandas lea el archivo siembras csv y exporte un documento html con los siguientes filtros de información
5. Los datos de las veredas Rio Arriba y la Salazar de Belmira
'''
tablaFiltro5=tablaSiembras[(tablaSiembras["Vereda"].isin(['Rio Arriba','La Salazar']))&(tablaSiembras["Ciudad"]=="Belmira")]
# print(tablaFiltro5)
archivoHTML=tablaFiltro5.to_html()
archivoTEXTO=open("datosfiltrocora5.html","w",encoding="utf-8") #utf-8 para exportar los caracteres
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()