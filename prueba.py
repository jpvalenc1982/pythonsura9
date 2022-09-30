import pandas as pd
tabla=pd.read_csv('./Siembras.csv')

#tabla de estadísticas
tablaEstadisticas=tabla.describe()
print(tablaEstadisticas)

#solo obtener medias de la tabla estadística (solo 1 fila)

tablaMedias=tablaEstadisticas.loc[['mean']]
print(tablaMedias)

#solo obtener los datos de una columna
tablaMediaArboles=tablaMedias["Arboles"].to_frame