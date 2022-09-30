import pandas as pd
tablaSiembras=pd.read_csv('./Siembras.csv')
'''
Usando pandas lea el archivo siembras csv y exporte un documento html con los siguientes filtros de información
6. Los datos de la veredas Quitasol de BELLO ordenados de menor a mayor y el promedio de arboles sembrados en esta vereda
'''
# quitasol=tablaSiembras[(tablaSiembras["Ciudad"]=="Bello")&(tablaSiembras["Vereda"]=="Quitasol")].sort_values('Arboles',ascending=True)
# tablaEstadisticas=quitasol.describe()
# tablaMedias=tablaEstadisticas.loc[['mean']]
# tablaMediaArboles=tablaMedias["Arboles"]
# # tablaMediaArboles=tablaMedias["Arboles"].to_frame
# print(tablaMediaArboles)
# archivoHTML=tablaMediaArboles.to_html()
# archivoTEXTO=open("datosfiltrocora6.html","w",encoding="utf-8") #utf-8 para exportar los caracteres
# archivoTEXTO.write(archivoHTML)
# archivoTEXTO.close()

DatosQuitasol = tablaSiembras[(tablaSiembras["Ciudad"] == "Bello") & (tablaSiembras["Vereda"] == "Quitasol")]
DatosQuitasol = DatosQuitasol.sort_values('Arboles', ascending=True)
DatosQuitasol = DatosQuitasol.assign(Promedio=DatosQuitasol['Arboles'].mean())
# Exportar tabla
archivoHTML = DatosQuitasol.to_html()
# abrir archivo
ArchivoTEXTO = open("datosfiltrocora6.html", "w", encoding="UTF-8")
# escribir en el archivo
ArchivoTEXTO.write(archivoHTML)
# cerrar archivo
ArchivoTEXTO.close()