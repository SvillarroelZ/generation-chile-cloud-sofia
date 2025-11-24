# # La diferencia de lista y tupla está en su mutabilidad
# #
# # lista[0] = 99      # Esto SÍ se puede
# # tupla[0] = 99      # Esto NO se puede → error

# fruta1 = manzana = "Manzana";
# fruta2 = pera = "Pera";
# fruta3 = banana = "Banana";
# lista_de_frutas = ["manzana", "banana", "pera"];

# print(lista_de_frutas[0]);
# print(lista_de_frutas[-1]);
# print(lista_de_frutas[1]);
# print(lista_de_frutas[2]);

# frutas = ["BANANA", "MANZANA", "PERA"];
# frutas.append("NARANJA");

# Sistema de gestion de alumnos usando listas de python
# Create read update delete (CRUD) de alumnos

alumnos = []
alumno1 = input("Ingresa el nombre del primer alumno: ");
alumno2 = input("Ingresa el nombre del segundo alumno: ");
alumno3 = input("Ingresa el nombre del tercer alumno: ");
alumno4 = input("Ingresa el nombre del cuarto alumno: ");
alumno5 = input("Ingresa el nombre del quinto alumno: ");

alumnos.append(alumno1);
alumnos.append(alumno2);
alumnos.append(alumno3);
alumnos.append(alumno4);
alumnos.append(alumno5);
print("Lista de alumnos:", alumnos);

# Actualizar el nombre del segundo alumno
nuevo_nombre = input("Ingresa el nuevo nombre para el segundo alumno: ");
alumnos[1] = nuevo_nombre;
print("Lista de alumnos actualizada:", alumnos);

# Eliminar el segundo alumno
alumnos.pop(1);

# Mostrar todos los alumnos
print("Lista final de alumnos:");
for alumno in alumnos:
    print(alumno);
    
print(alumnos.count(alumno));