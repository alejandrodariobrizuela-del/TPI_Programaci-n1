def pedir_texto_no_vacio(mensaje):
    """Pide un texto por teclado hasta que el usuario ingrese algo no vacío."""
    while True:
        valor = input(mensaje).strip()
        if valor != "":
            return valor
        print("⚠ El campo no puede estar vacío. Intentá de nuevo.")


def pedir_entero_positivo(mensaje):
    """Pide un número entero positivo, validando que sea numérico y mayor a 0."""
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = int(entrada)
            if valor <= 0:
                print("⚠ El valor debe ser un número entero positivo.")
                continue
            return valor
        except ValueError:
            print("⚠ Ingresá un número entero válido (sin letras ni decimales).")