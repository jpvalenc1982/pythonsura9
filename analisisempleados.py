import pandas as pd
tablaEmpleados=pd.read_csv('./empleados.csv')
#print(tablaEmpleados)
#print(tablaEmpleados.to_string())

#Filtro 1. Quiero obtener todos los datos de los analistas 1
# tablaAnalistas1=tablaEmpleados[tablaEmpleados["cargo"]=="analista1"].head(50)
# archivoHTML=tablaAnalistas1.to_html()
# archivoTEXTO=open("datosanalistas1.html","w",encoding="utf-8")
# archivoTEXTO.write(archivoHTML)
# archivoTEXTO.close()

#Filtro 2. Quiero obtener todos los datos de los analistas 2
# tablaAnalistas2=tablaEmpleados[tablaEmpleados["cargo"]=="analista2"].head(50)
# archivoHTML=tablaAnalistas2.to_html()
# archivoTEXTO=open("datosanalistas2.html","w",encoding="utf-8")
# archivoTEXTO.write(archivoHTML)
# archivoTEXTO.close()

#Filtro 3. Analistas menores de 30 años que ganen más de 6.000.000

tablaAnalistas=(tablaEmpleados[(tablaEmpleados["edad"]<30)&(tablaEmpleados["salario"]>5500000)])
archivoHTML=tablaAnalistas.to_html()
archivoTEXTO=open("analistas.html","w",encoding="utf-8") #utf-8 para exportar los caracteres
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()