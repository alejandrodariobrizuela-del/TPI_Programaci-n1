def buscar_indice_por_nombre_exacto(paises, nombre):
    """Devuelve la posición del país cuyo nombre coincide exactamente."""
    for indice, pais in enumerate(paises):
        if pais["nombre"].lower() == nombre.lower():
            return indice
    return None


def obtener_resultados_busqueda(paises, texto):
    """Filtra países que contengan el texto de manera parcial."""
    return [p for p in paises if texto.lower() in p["nombre"].lower()]


def obtener_por_continente(paises, continente):
    """Devuelve los países pertenecientes a un continente."""
    return [p for p in paises if p["continente"].lower() == continente.lower()]


def obtener_por_rango(paises, campo, minimo, maximo):
    """Filtra países dentro de un rango numérico de un campo específico."""
    if minimo > maximo:
        minimo, maximo = maximo, minimo
    return [p for p in paises if minimo <= p[campo] <= maximo]


def ordenar_paises(paises, campo, descendente=False):
    """Devuelve una NUEVA lista ordenada por el campo indicado."""
    return sorted(paises, key=lambda p: p[campo], reverse=descendente)


def pais_extremo(paises, campo, buscar_mayor=True):
    """Devuelve el diccionario del país con el valor mayor o menor."""
    if not paises:
        return None
    if buscar_mayor:
        return max(paises, key=lambda p: p[campo])
    return min(paises, key=lambda p: p[campo])


def promedio_campo(paises, campo):
    """Calcula el promedio de un campo numérico."""
    if not paises:
        return 0
    return sum(p[campo] for p in paises) / len(paises)


def cantidad_por_continente(paises):
    """Devuelve un diccionario {continente: cantidad_de_países}."""
    conteo = {}
    for p in paises:
        continente = p["continente"]
        conteo[continente] = conteo.get(continente, 0) + 1
    return conteo