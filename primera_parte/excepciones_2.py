# # Excepciones

# def validar_edad(edad):
#     if edad < 0:
#         raise ValueError("La edad no puede ser negativa.")
#     return edad

# validar_edad(int(input("Ingresa tu edad: ")))

def validar_email(email):
    if "@" not in email:
        raise ValueError("Email inválido, debe contener '@'.")
    return email
    
try:
    correo = input("Ingresa tu correo: ")
    correo_validado = validar_email(correo)
    print("Correo válido:", correo_validado)

except ValueError as error:
    print("Error:", error)