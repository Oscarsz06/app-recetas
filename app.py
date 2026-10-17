from logica import (
    buscar_recetas,
    cargar_recetas,
    ingredientes_del_usuario,
    pasos_de,
    tiempo_legible,
)


def imprimir_receta(nombre, datos):
    print(f"\n- {nombre}")
    partes = []
    if "tiempo" in datos:
        partes.append(tiempo_legible(datos["tiempo"]))
    if "porciones" in datos:
        partes.append(f"{datos['porciones']} porciones")
    if "dificultad" in datos:
        partes.append(datos["dificultad"])
    if partes:
        print("  " + " | ".join(partes))
    if datos.get("utensilios"):
        print("  Utensilios: " + ", ".join(datos["utensilios"]))
    print("  Ingredientes:")
    cantidades = datos.get("cantidades", {})
    for ingrediente in datos["ingredientes"]:
        cantidad = cantidades.get(ingrediente)
        print(f"    - {ingrediente}" + (f": {cantidad}" if cantidad else ""))
    print("  Preparación:")
    for numero, paso in enumerate(pasos_de(datos), start=1):
        print(f"    {numero}. {paso}")
    for consejo in datos.get("consejos", []):
        print(f"  Consejo: {consejo}")

recetas_por_region = cargar_recetas()
regiones = list(recetas_por_region.keys())

print("¿De qué región quieres cocinar?")
for numero, nombre_region in enumerate(regiones, start=1):
    print(f"{numero}. {nombre_region}")

while True:
    eleccion = input("Elige el número de la región: ").strip()
    if eleccion.isdigit() and 1 <= int(eleccion) <= len(regiones):
        region = regiones[int(eleccion) - 1]
        break
    print("Opción no válida, intenta de nuevo.")

recetas = recetas_por_region[region]

print(f"\nRegión elegida: {region}")
print("Escribe los ingredientes que compraste, separados por coma.")
entrada = input("Ingredientes: ")
tengo = ingredientes_del_usuario(entrada)

completas, casi = buscar_recetas(recetas, tengo)

print("\nPuedes preparar:")
if completas:
    for nombre, datos in completas:
        imprimir_receta(nombre, datos)
else:
    print("Ninguna receta completa todavía.")

if casi:
    print("\nTe falta solo 1 ingrediente para:")
    for nombre, falta in casi:
        print(f"- {nombre} (te falta: {falta})")
