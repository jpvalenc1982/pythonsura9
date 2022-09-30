import pandas as pd
tablaEmpleados=pd.read_csv('./empleados.csv')

#Filtro 3. Analistas menores de 30 años que ganen más de 6.000.000

tablaAnalistas=(tablaEmpleados[(tablaEmpleados["edad"]<30)&(tablaEmpleados["salario"]>5500000)])
archivoHTML=tablaAnalistas.to_html()
archivoTEXTO=open("analistas.html","w",encoding="utf-8") #utf-8 para exportar los caracteres
archivoTEXTO.write(archivoHTML)
archivoTEXTO.close()