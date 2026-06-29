import validaciones
import logica

def mostrar_paises(lista):
    """Muestra una lista de países formateada como tabla."""
    if not lista:
        print("\nNo hay países para mostrar.")
        return
    print(f"\n{'Nombre':<20}{'Población':>15}{'Superficie (km²)':>20}{'Continente':>15}")
    print("-" * 70)
    for p in lista:
        print(f"{p['nombre']:<20}{p['poblacion']:>15,}{p['superficie']:>20,}{p['continente']:>15}")
    print(f"\nTotal: {len(lista)} país(es)\n")


def agregar_pais(paises):
    print("\n--- Agregar nuevo país ---")
    nombre = validaciones.pedir_texto_no_vacio("Nombre del país: ")

    if logica.buscar_indice_por_nombre_exacto(paises, nombre) is not None:
        print(f"⚠ Ya existe un país llamado '{nombre}'. No se agregó (use 'Actualizar').")
        return

    poblacion = validaciones.pedir_entero_positivo("Población: ")
    superficie = validaciones.pedir_entero_positivo("Superficie en km²: ")
    continente = validaciones.pedir_texto_no_vacio("Continente: ")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente,
    }
    paises.append(nuevo_pais)
    print(f"✅ País '{nombre}' agregado correctamente.")


def actualizar_pais(paises):
    print("\n--- Actualizar país ---")
    nombre = validaciones.pedir_texto_no_vacio("Nombre exacto del país a actualizar: ")
    indice = logica.buscar_indice_por_nombre_exacto(paises, nombre)

    if indice is None:
        print(f"⚠ No se encontró ningún país llamado '{nombre}'.")
        return

    print(f"País encontrado -> {paises[indice]}")
    nueva_poblacion = validaciones.pedir_entero_positivo("Nueva población: ")
    nueva_superficie = validaciones.pedir_entero_positivo("Nueva superficie en km²: ")

    paises[indice]["poblacion"] = nueva_poblacion
    paises[indice]["superficie"] = nueva_superficie
    print(f"✅ Datos de '{paises[indice]['nombre']}' actualizados correctamente.")


def buscar_pais(paises):
    print("\n--- Buscar país ---")
    texto = validaciones.pedir_texto_no_vacio("Nombre o parte del nombre a buscar: ")
    resultados = logica.obtener_resultados_busqueda(paises, texto)
    mostrar_paises(resultados)


def menu_filtrar(paises):
    print("\n--- Filtrar países ---")
    print("1. Por continente")
    print("2. Por rango de población")
    print("3. Por rango de superficie")
    opcion = input("Elegí una opción: ").strip()

    if opcion == "1":
        continente = validaciones.pedir_texto_no_vacio("Continente a filtrar: ")
        resultados = logica.obtener_por_continente(paises, continente)
        mostrar_paises(resultados)
    elif opcion in ("2", "3"):
        campo = "poblacion" if opcion == "2" else "superficie"
        nombre_campo = "población" if campo == "poblacion" else "superficie"
        minimo = validaciones.pedir_entero_positivo(f"Valor mínimo de {nombre_campo}: ")
        maximo = validaciones.pedir_entero_positivo(f"Valor máximo de {nombre_campo}: ")
        resultados = logica.obtener_por_rango(paises, campo, minimo, maximo)
        mostrar_paises(resultados)
    else:
        print("⚠ Opción inválida.")


def menu_ordenar(paises):
    print("\n--- Ordenar países ---")
    print("1. Por nombre")
    print("2. Por población")
    print("3. Por superficie")
    opcion = input("Elegí una opción: ").strip()

    campos = {"1": "nombre", "2": "poblacion", "3": "superficie"}
    if opcion not in campos:
        print("⚠ Opción inválida.")
        return

    orden = input("¿Ascendente (A) o Descendente (D)?: ").strip().lower()
    descendente = (orden == "d")

    resultado = logica.ordenar_paises(paises, campos[opcion], descendente)
    mostrar_paises(resultado)


def mostrar_estadisticas(paises):
    if not paises:
        print("⚠ No hay países cargados para calcular estadísticas.")
        return

    mayor = logica.pais_extremo(paises, "poblacion", True)
    menor = logica.pais_extremo(paises, "poblacion", False)
    prom_pob = logica.promedio_campo(paises, "poblacion")
    prom_sup = logica.promedio_campo(paises, "superficie")
    conteo = logica.cantidad_por_continente(paises)

    print("\n--- Estadísticas generales ---")
    print(f"País con mayor población: {mayor['nombre']} ({mayor['poblacion']:,})")
    print(f"País con menor población: {menor['nombre']} ({menor['poblacion']:,})")
    print(f"Promedio de población: {prom_pob:,.2f}")
    print(f"Promedio de superficie: {prom_sup:,.2f} km²")
    print("\nCantidad de países por continente:")
    for continente, cantidad in conteo.items():
        print(f"  {continente}: {cantidad}")
    print()


def mostrar_menu_principal():
    print("\n============================")
    print(" GESTIÓN DE DATOS DE PAÍSES")
    print("============================")
    print("1. Agregar país")
    print("2. Actualizar país (población y superficie)")
    print("3. Buscar país por nombre")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Mostrar todos los países")
    print("8. Guardar cambios en el CSV")
    print("9. Salir")