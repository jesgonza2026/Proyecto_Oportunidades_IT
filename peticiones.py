import requests
import json
from pathlib import Path

# resp.status_code  int         200, 404, 500
# resp.text         str         cuerpo de la respuesta en texto plano
# resp.json()       dict/list   Parsea el cuerpo como JSON

# Definir una lista con los id y nombres de los endpoints con la finalidad de hacer la lectura
# de todos en una sola funcion pasando el id de la tabla a leer y el nombre del archivo a guardar
#La tabla del INE cuyo ID es 71007 la vamos a guardar con el nombre empresas_tic etc
tablas = [
    {"id": "71007", "nombre": "empresas_tic"},
    {"id": "67903", "nombre": "cifra_negocios"},
    {"id": "67904", "nombre": "valor_anadido"},
    {"id": "67901", "nombre": "num_ocupados"},
    {"id": "75360", "nombre": "coste_trabajador"},
    {"id": "71018", "nombre": "ia"},
    {"id": "76386", "nombre": "cloud_computing"},
    {"id": "76403", "nombre": "analitica_datos"}
]

# Definir constantes de la url
base_url = 'https://servicios.ine.es/wstempus/jsCache/es/DATOS_TABLA'

#parametro de la url
final_url = '?tip=AM'

# funcion que sera invocada para hacer la lectura a la api para cada id de tabla que se le pase
# y creara un archivo json con la infromacion leida
def descargar_info(id_tabla, nombre_archivo):

    url = f"{base_url}/{id_tabla}{final_url}"
    raw_dir = Path("data/raw")

    try:
        resp = requests.get(url) #Hacemos la petición

        resp.raise_for_status()

        datos = resp.json() #Coge la respuesta del INE y conviértela en datos que Python pueda manejar.

        raw_dir.mkdir(parents=True, exist_ok=True)
        ruta = raw_dir / f"{nombre_archivo}_{id_tabla}.json";   #Nombre del archivo creado

        with open(ruta, "w", encoding="utf-8") as archivo:    #archivo es la variable donde se guarda la conexion al archivo donde se vacia la data
            json.dump(datos, archivo, ensure_ascii=False, indent=2)

        print(f"{nombre_archivo} ({id_tabla}) - {len(datos)} objetos descargada")
        return True 

    except requests.RequestException as e: #Si ocurre un error relacionado con la petición, haz lo siguiente.
        print(f"Error: {e}")
        return False 

#ejemplo de llamado a la funcion
print("Iniciando descarga de las 8 tablas del INE...")
print("-" * 50) 
    
exitos = 0

#recorremos la lista de tablas una por una
for tabla in tablas:
    #accedemos a los valores del diccionario con la "clave"
    id_tabla = tabla["id"]
    nombre = tabla["nombre"]
    
    #llamamos a la funcion de descarga
    if descargar_info(id_tabla, nombre):
        exitos += 1

print("-" * 50)
print(f"Descarga completada: {exitos} de {len(tablas)} tablas")