# Trabajar con condicionales if-else en Python

# if(condicion := True):
#     print("La condición es verdadera.");
# else:
#     print("La condición es falsa.");

MAYOR_EDAD = 18

edad = int(input("Por favor, ingresa tu edad: "))

if (edad) > MAYOR_EDAD:           # Comparar si la condicion mayor o igual a la constante.
    print("Eres mayor de edad")

elif (edad) == MAYOR_EDAD:        # Comparar si la condicion es igual a la constante.
    print("Eres mayor de edad, tienes exactamente 18 años")

elif (edad) == MAYOR_EDAD -1:     # Comparar si la condicion es igual a la constante menos uno.
    print("Estás a un año de ser mayor de edad")  

else :                            # Comparar si la condicion no se cumple.
    print("Eres menor de edad")

