# Crear el diccionario con información personal ficticia
informacion_personal = {
    "Nombre": "Jorge Dominguez",
    "Edad": 25,
    "Ciudad": "Sucúa",
    "Profesion": "Ingeniero",
    "Estado_civil" : "Casado",
    "Telefono":"02740-001",
    "Genero": "masculinmo",

}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["Ciudad"]="Loja"

# Agregar una nueva clave-valor para la "Estado civil"
informacion_personal["Estado_civil"]= "casado"

# Verificar si la clave "Telefono" existe y agregarla si no existe
if "Telefono" not in informacion_personal:
    informacion_personal["elefono"] ="220"

# Eliminar la clave "genero"
if "Genero" in informacion_personal:
    del informacion_personal["Genero"]

# Imprimir el diccionario actualizado
print(informacion_personal)