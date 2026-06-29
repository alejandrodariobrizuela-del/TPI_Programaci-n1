import csv
import os

def obtener_ruta_absoluta(ruta_relativa):
    """Convierte una ruta relativa en absoluta basándose en la posición de este archivo."""
    directorio_actual = os.path.dirname(os.path.abspath(__file__))
    return os.path.normpath(os.path.join(directorio_actual, ruta_relativa))


def cargar_paises(ruta):
    """Lee el archivo CSV y devuelve una lista de diccionarios (países)."""
    paises = []
    ruta_real = obtener_ruta_absoluta(ruta)
    
    try:
        with open(ruta_real, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                try:
                    pais = {
                        "nombre": fila["nombre"].strip(),
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"].strip(),
                    }
                    paises.append(pais)
                except (ValueError, KeyError) as error:
                    print(f"Aviso: se ignoró una fila con formato inválido -> {fila} ({error})")
    except FileNotFoundError:
        print(f"No se encontró el archivo en '{ruta_real}'. Se iniciará con una lista vacía.")
    return paises


def guardar_paises(paises, ruta):
    """Escribe la lista de países en el archivo CSV (sobrescribe el contenido)."""
    campos = ["nombre", "poblacion", "superficie", "continente"]
    ruta_real = obtener_ruta_absoluta(ruta)
    
    # Asegura que la carpeta contenedora exista (por si acaso)
    os.makedirs(os.path.dirname(ruta_real), exist_ok=True)
    
    with open(ruta_real, mode="w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for pais in paises:
            escritor.writerow(pais)