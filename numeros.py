entero = 10;                     # int
decimal = 3.14;                  # float
texto = "Hola mundo";            # str
booleano = True;                 # bool
lista = [1, 2, 3];               # list
tupla = (4, 5, 6);               # tuple

# La diferencia de lista y tupla está en su mutabilidad
#
# lista[0] = 99      # Esto SÍ se puede
# tupla[0] = 99      # Esto NO se puede → error

diccionario = {"nombre": "Sofia", "edad": 30};  # dict
conjunto = {7, 8, 9};            # set

modulo = entero % 2;             # Residuo de la división.
suma = entero + 5;

print("La suma es:", suma);
print("División:", ( (entero /3)+2) );
print(f"{decimal} éste es un ejemplo de decimal");
print("Potencia:", (entero**2) );
print("Módulo:", modulo);