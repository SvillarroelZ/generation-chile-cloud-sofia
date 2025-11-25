# def suma_de_enteros(a, b) :
#     resultado = a + b
#     return resultado

# def suma_de_numeros_imaginarios(a, b) :
#     resultado = a + b
#     return resultado

# def calculo_descuento_aplicado(nombre_producto, precio_original, porcentaje_descuento) :
#     descuento = (porcentaje_descuento / 100) * precio_original
#     precio_final = precio_original - descuento
#     return f"El precio final de {nombre_producto} después de un descuento del {porcentaje_descuento}% es: {precio_final}"

#Las funciones sirven para organizar el código en bloques reutilizables y manejables.
# Se crean utilizando la palabra clave 'def', seguida del nombre de la función y paréntesis que pueden incluir parámetros.
# El bloque de código dentro de la función está indentado y se ejecuta cuando la función es llamada.
# Las funciones pueden devolver valores utilizando la palabra clave 'return'.   

#Ejemplo de uso de funcion que no recibe parametros y no devuelve valor
def mensaje_bienvenida():
    print("¡Bienvenido a nuestro programa!")

#Continua la ejecucion del programa
#mensaje_bienvenida()

def saludo(nombre):
    print(f"Hola, {nombre}! ¿Cómo estás?")

# mensaje_bienvenida()
# saludo("Sofia")

# Resultados esperados:
# ¡Bienvenido a nuestro programa!
# Hola, Sofia! ¿Cómo estás?

#Mejora
#saludo(input("Dime tu nombre:" ))

# def saludos_contabiliza_dias_con_edad(nombre, edad):
#     print(f"Hola, {nombre}! Tienes {edad} años, lo que equivale a {edad * 365} días.")
# saludos_contabiliza_dias_con_edad("Ana", 30)    

def saludo_contabiliza_dias_con_edad(nombre, edad):
    dias_anio = 365
    dias_totales = dias_anio * edad
    print(f"Hola, {nombre}! que bueno tenerte de regreso, han pasado {dias_totales} desde que naciste")
 
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))  

def calculo_de_años_por_edad(edad):
    return f"Tienes {edad} años."



def funcion_padre():
        funcion_hijo()
        print("Esto es la función padre.")
        
def funcion_hijo():
    print("Esto es la función hijo.")

funcion_padre