#importación de manejo de data frame y archivos

import pandas as pd
from pathlib import Path #Sirve para trabajar con rutas de archivos y carpetas de una forma más sencilla.

#1.leer el archivo excel:

ruta=Path(__file__).parent.parent /"data"/"excel"/"estructura_cnae2009.xls"


#construir la ruta fuera y guardarla en una variable
df = pd.read_excel(ruta, sheet_name="clasificacion")

#llamamos al método read excel y le tengo que dar la ruta, que la tengo arriba y el nombre de la hoja

#2.Ver columnas:

print("Columnas:",df.columns.tolist())#to list me lo da limpio, no me dice tb el tipo de objeto
#print("Columnas:",df.columns)#si quiero saber que objeto es

#3.Obtener columnas de interés 

df = df[["CODINTEGR","TITULO_CNAE2009"]]

#4.Renombrar las columnas

df = df.rename(columns={
    "CODINTEGR": "codigo",
    "TITULO_CNAE2009": "nombre"
})

#💡 Regla fácil para recordar:

#Una columna → df["columna"]
#Varias columnas → df[["columna1", "columna2"]]

print("Columnas:",df.columns.tolist())
