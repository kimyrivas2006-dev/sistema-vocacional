import json
import os

ARCHIVO_DB = "usuarios_db.json"

def cargar_datos():
    if not os.path.exists(ARCHIVO_DB):
        return {}
    with open(ARCHIVO_DB, "r", encoding="utf-8") as archivo:
        try:
            return json.load(archivo)
        except json.JSONDecodeError:
            return {}

def guardar_datos(datos):
    with open(ARCHIVO_DB, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

def buscar_o_crear_usuario(identidad, nombre_completo=None, edad=None):
    """
    Busca al usuario utilizando su número de identidad como clave única.
    Si no existe, utiliza los datos proporcionados para crear un nuevo perfil.
    """
    datos = cargar_datos()
    
    # Limpiamos espacios y caracteres raros de la identidad para usarla como llave única
    id_clave = str(identidad).strip().replace(".", "").replace("-", "")
    
    if id_clave in datos:
        print(f"\n¡Bienvenido de nuevo, {datos[id_clave]['nombre']}! Hemos recuperado tu progreso con tu cédula/ID.")
        return datos[id_clave]
    else:
        # Si es un usuario nuevo, la estructura ahora guarda la identidad formalmente
        nuevo_usuario = {
            "identidad": id_clave,
            "nombre": nombre_completo.strip(),
            "edad": edad,
            "resultados_holland": None,
            "resultados_gardner": None,
            "progreso_holland": {
                "respuestas": {},
                "preguntas_orden": []
            },
            "progreso_gardner": {
                "respuestas": {},
                "preguntas_orden": []
            }
        }
        datos[id_clave] = nuevo_usuario
        guardar_datos(datos)
        print(f"\n¡Mucho gusto, {nuevo_usuario['nombre']}! Tu perfil permanente ha sido creado con éxito.")
        return nuevo_usuario

def actualizar_usuario_en_db(usuario):
    datos = cargar_datos()
    # Usamos la identidad del usuario para sobrescribir sus datos actualizados
    id_clave = str(usuario["identidad"])
    datos[id_clave] = usuario
    guardar_datos(datos)