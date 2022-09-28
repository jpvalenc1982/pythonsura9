import pandas as pd
tablaSiembras=pd.read_csv('./Siembras.csv')
'''
Usando pandas lea el archivo siembras csv y exporte un documento html con los siguientes filtros de información
3. Los datos de CAUCASIA incluyendo el número de hectáreas sembradas
'''
tablaFiltro3=tablaSiembras[tablaSiembras["Ciudad"]=="Caucasia"].filter(like='Hectareas')
#print(tablaFiltro3)
archivoHTML=tablaFiltro3.to_html()
archivoTEXTO=open("datosfiltrocora3.html","w",encoding="utf-8") #utf-8 para exportar los caracteres
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()