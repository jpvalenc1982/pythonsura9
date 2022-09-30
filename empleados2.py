import pandas as pd
tablaEmpleados=pd.read_csv('./empleados.csv')

#Filtro 2. Quiero obtener todos los datos de los analistas 2
tablaAnalistas2=tablaEmpleados[tablaEmpleados["cargo"]=="analista2"].head(50)
archivoHTML=tablaAnalistas2.to_html()
archivoTEXTO=open("datosanalistas2.html","w",encoding="utf-8")
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()