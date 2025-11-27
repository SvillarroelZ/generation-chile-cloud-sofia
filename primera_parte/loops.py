
frutas = [
    {"nombre" : "manzana", "precio" : 10.99, "cantidad" : 3}, 
    {"nombre" : "banana", "precio" : 5.00, "cantidad" : 10}, 
    {"nombre" : "cereza", "precio" : .99, "cantidad" : 9}
]

total_venta = 0.0

#print(frutas[0], "-> Accedido por elemento")  # Acceso al primer elemento

# for fruta in frutas:
#     print(fruta["nombre"])  # Acceso al valor asociado a la clave "nombre" en cada diccionario

#Calcular total de la venta

# for fruta in frutas:
#     total_venta += fruta["precio"] * fruta["cantidad"]

# print(f"Tu total de venta es: {total_venta}")

# # While
# contador = 0
# while contador < len(frutas):
#     fruta = frutas[contador]
#     total_venta += fruta["precio"] * fruta["cantidad"]
#     contador += 1
#     if(contador != len(frutas)):
#         print(f"Llevas acumulado: {total_venta}")
#         print(f"llevas un total de {contador} frutas procesadas")
# print(f"Tu total de venta es: {total_venta}")

frutas = []
while True:
    nombre = input("Ingresa el nombre de la fruta que deseas agregar: ")
    
    if nombre.lower() == "salir":
        print("Saliendo del programa de registro de frutas.")
        break
    
    precio = float(input(f"Ingresa el precio de {nombre}: "))
 
    fruta = {
        "nombre" :nombre,
        "precio" : precio
    }
    frutas.append(fruta)
    #print(f"Ingresando la fruta: {nombre} con el precio de {precio}")
    print(f"Fruta {nombre} agregada con éxito.\n")

print

#Tarea imprimir el ticket de compra


total = 0
for fruta in frutas:
    print(f"- Producto agregado: {fruta['nombre'].capitalize()} Precio: ${fruta['precio']}")
    total += fruta["precio"]

print("--------------------------------------")
print(f"TOTAL A PAGAR:               ${total}")
print("======================================")


