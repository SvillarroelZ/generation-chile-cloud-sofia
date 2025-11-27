# Ejemplos de excepciones comunes en Python

# Las excepciones son errores que ocurren durante la ejecución de un programa, 
# normalmente no los esperamos pero son errores lógicos que pueden ocurrir.

        # print(10 / 0) # ZeroDivisionError: division by zero

        # int("Hola") # ValueError: invalid literal for int() with base 10: 'Hola'

        # lista = [1,2,3] 
        # print(lista[10]) # IndexError: list index out of range

# Bloques try y except
# Podemos manejar las excepciones usando bloques try y except,
# de esta forma podemos evitar que el programa se detenga abruptamente.
# El código dentro del bloque try se ejecuta normalmente,
# pero si ocurre una excepción, se salta al bloque except.  
# El catch del error comienza a saltar por las funciones hasta que lo captura un try-except.
# Podemos tener múltiples bloques except para manejar diferentes tipos de excepciones.
# También podemos usar un bloque except genérico para capturar cualquier excepción no manejada específicamente. 

        # try:
        #     numero = int(input("Ingresa un número: ")) # ValueError si la entrada no es un número válido
        #     print("Número válido:", numero) # Si no hay error, se imprime el número
        # except: # Captura cualquier excepción 
        #     print("Error: no ingresaste un número válido.") # Mensaje de error genérico
            
# En lugar de mostrar detalles técnicos, como errores de disco, fallas de base de datos 
# o información interna del sistema, entregar mensajes claros y amigables que indiquen 
# qué puede hacer el usuario o a quién contactar según su contexto. No sobre exponer errores técnicos.

# Actividad
# Escribe un programa que solicite al usuario ingresar un número y divida ese número entre 5.

while True:
    try:
        numero = int(input("Ingresa un número entero distinto de 0 para dividir 5 entre ese valor: "))

        if numero == 0:
            print("Error: no se puede dividir entre cero. Intenta con otro número.")
            continue

        # Si el número es válido, hacemos la división normal
        resultado = 5 / numero

        # Si el resultado es un entero exacto (ej: 1.0, 5.0)
        if resultado.is_integer():
            print(f"El resultado de dividir 5 entre {numero} es: {int(resultado)}")
        else:
            # Resultado con parte decimal, lo mostramos con al menos un decimal
            print(f"El resultado de dividir 5 entre {numero} es: {resultado:.2f}")

        break  # salimos del bucle porque ya obtuvimos una operación válida

    except ValueError:
        print("Error: ingresa solo números enteros válidos (sin decimales ni letras).")

    except ZeroDivisionError:
        # Por seguridad. ya controla el 0 arriba
        print("Error: se produjo una división entre cero. Intenta con otro número.")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}. Intenta nuevamente.")
        
# Else y finally
# Podemos usar else para ejecutar código si no ocurre ninguna excepción en el bloque try.
# Finalmente, el bloque finally se ejecuta siempre, sin importar si ocurrió una excepción o no
