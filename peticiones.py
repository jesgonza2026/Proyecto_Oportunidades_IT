import requests

resp = requests.get('https://servicios.ine.es/wstempus/jsCache/es/DATOS_TABLA/71007?tip=AM')

# resp.status_code  int         200, 404, 500
# resp.text         str         cuerpo de la respuesta en texto plano
# resp.json()       dict/list   Parsea el cuerpo como JSON

#print(resp.json())

# Definir una lista con los id y nombres de los endpoints con la finalidad de hacer la lectura
# de todos en una sola funcion pasando el id de la tabla a leer y el nombre del archivo a guardar

tablas = [
    {"id": "71007", "nombre": "empresas_tic"},
    {"id": "67903", "nombre": "cifra_negocios"}
    {"id": "67904", "nombre": "valor_añadido"}
    {"id": "67901", "nombre": "num_ocupados"}
    {"id": "75360", "nombre": "coste_trabajador"}
    {"id": "71018", "nombre": "ia"}
    {"id": "76386", "nombre": "cloud_computing"}
    {"id": "76403", "nombre": "analitica_datos"}

]
#La tabla del INE cuyo ID es 71007 la vamos a guardar con el nombre empresas_tic etc



# Definir constantes de la url
base_url = 'https://servicios.ine.es/wstempus/jsCache/es/DATOS_TABLA'

#parametro de la url
final_url = '?tip=AM'

# funcion que sera invocada para hacer la lectura a la api para cada id de tabla que se le pase
# y creara un archivo json con la infromacion leida

def descargar_info(id_tabla, nombre_archivo):
    url = f"{base_url}/{id_tabla}{final_url}"

    try:
        resp = requests.get(url) #Hacemos la petición

        #AQUI
        #falta verificar status antes de comusir la data

        datos = resp.json() #"Coge la respuesta del INE y conviértela en datos que Python pueda manejar."
        print(datos)

        #AQUI
        #falta crear un archivo json para guardarlo en data/raw

        return True #Todo bien → True

    except requests.RequestException as e: #"Si ocurre un error relacionado con la petición, haz lo siguiente."
        print(f"Error: {e}")
        return False #Error → False

#ejemplo de llamado a la funcion

print("Iniciando descarga de las 8 tablas del INE...")
print("-" * 50) #Repite el símbolo - 50 veces.esto es solo estético, para que la salida quede ordenada
    
exitos = 0

#recorremos la lista de tablas una por una
for tabla in tablas:#"Ve recorriendo la lista tablas, elemento por elemento."Para cada elemento en la lista tablas..El for va a coger un diccionario cada vez.
    #accedemos a los valores del diccionario con la "clave"
    id_tabla = tabla["id"]#Python busca la clave id y nos devuelve su valor
    nombre = tabla["nombre"]#Python busca la clave nombre y nos devuelve su valor
    
    #llamamos a la funcion de descarga
    if descargar_info(id_tabla, nombre):
        exitos += 1
#Así que el for es el que hace posible que no tengas que llamar manualmente 8 veces a descargar_info().
# Resumen final.
print("-" * 50)
print(f"Descarga completada: {exitos} de {len(tablas)} tablas")