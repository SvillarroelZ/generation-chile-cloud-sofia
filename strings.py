nombre = "Sofia";
apellido = "González";
nombre_completo = nombre + " " + apellido;
ciudad = "Santiago";

print(f"hola {nombre}, bienvenido a {ciudad}")

mensaje = "hola {nombre_completo}, bienvenido a {ciudad}"
print(mensaje.format(nombre_completo=nombre_completo, ciudad=ciudad).upper());
print(type(nombre));
print(nombre.upper());

nom=input("Hola, ¿Cuál es tu nombre?: ")
nom=nom.title()
ap=input(f"¡Encantado de conocerte, {nom}! ¿Cuál es tu apellido?: ")
ap=ap.title()
  