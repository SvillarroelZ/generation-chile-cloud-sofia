def suma(a, b):
    # Validar que ambos valores sean numéricos (int o float)
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Los valores deben ser numéricos.")
    
    # Validar que no sean negativos
    if a < 0 or b < 0:
        raise ValueError("Los valores no pueden ser negativos.")

    return a + b