#Diccionarios y python y JSON
# Un diccionario es una colección de pares clave-valor
# Cada clave es única y se utiliza para acceder a su valor asociado
# Los diccionarios son mutables, lo que significa que se pueden modificar después de su creación

# Definición de un diccionario

persona = { 
           "nombre": "Pepe", 
           "edad": 25, 
           "Hobbies": ["Leer", "Cocinar"] 
        };    

print("Nombre:", persona["nombre"]);  # Acceso al valor asociado a la clave "nombre"
print("Edad:", persona["edad"]);      # Acceso al valor asociado a la clave "edad"
print("Hobbies:", persona["Hobbies"][0]);# Acceso al valor asociado a la lista

print(f"A {persona["nombre"]} le gusta {persona["Hobbies"][0]} y tiene {persona["edad"]} años.");