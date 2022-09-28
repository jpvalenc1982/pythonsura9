import pandas as pd
tablaSiembras=pd.read_csv('./Siembras.csv')
'''
Usando pandas lea el archivo siembras csv y exporte un documento html con los siguientes filtros de información
2. Los datos de MEDELLIN ordenados de mayor a menor número de arboles
'''
tablaFiltro2=tablaSiembras[tablaSiembras["Ciudad"]=="Medellín"].sort_values('Arboles',ascending=False)
#print(tablaFiltro2)
archivoHTML=tablaFiltro2.to_html()
archivoTEXTO=open("datosfiltrocora2.html","w",encoding="utf-8") #utf-8 para exportar los caracteres
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()