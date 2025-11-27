# # Script interactivo para operaciones básicas con dos números
# # Paso 1: Definir una función para leer un número desde la terminal
# def leer_numero(mensaje):
# 	while True:  # Repetir hasta que el usuario ingrese un valor válido
# 		entrada = input(mensaje)  # Leer lo que el usuario escribe
# 		try:
# 			return float(entrada)  # Intentar convertir la entrada a número decimal
# 		except ValueError:
# 			print("Por favor, ingresa un número válido.")  # Mensaje si el usuario se equivoca

# # Paso 2: Pedir los dos números al usuario
# print("Bienvenido al programa de operaciones básicas!")
# num1 = leer_numero("Ingresa el primer número: ")
# num2 = leer_numero("Ingresa el segundo número: ")

# # Paso 3: Realizar las operaciones y mostrar los resultados
# print(f"\nResultados para los números {num1} y {num2}:")

# # Suma
# print(f"La suma es: {num1 + num2}")
# # Resta
# print(f"La resta es: {num1 - num2}")
# # Multiplicación
# print(f"La multiplicación es: {num1 * num2}")
# # División (verificar que el segundo número no sea cero)
# if num2 != 0:
# 	print(f"La división es: {num1 / num2}")
# 	# Módulo (resto de la división)
# 	print(f"El módulo es: {num1 % num2}")
# else:
# 	print("No se puede dividir ni calcular el módulo por cero.")

# # Paso 4: Comparar los números
# if num1 > num2:
# 	print(f"El primer número ({num1}) es mayor que el segundo ({num2}).")
# elif num1 < num2:
# 	print(f"El segundo número ({num2}) es mayor que el primero ({num1}).")
# else:
# 	print("Ambos números son iguales.")

numero1 = float(input("Ingresa el primer número: "));
numero2 = float(input("Ingresa el segundo número: "));

print(f"\nEl resultado de la suma es:", (numero1) + (numero2));
print(f"\nEl resultado de la resta es:", (numero1) - (numero2));
print(f"\nEl resultado de la multiplicación es:", (numero1) * (numero2));
print(f"\nEl resultado de la división es:", int((numero1) / (numero2)));
print(f"\nEl resultado del módulo es:", (numero1) % (numero2));


