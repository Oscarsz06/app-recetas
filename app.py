from logica import cargar_recetas, ingredientes_del_usuario, buscar_recetas

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
        print(f"\n- {nombre}")
        print(datos["pasos"])
else:
    print("Ninguna receta completa todavía.")

if casi:
    print("\nTe falta solo 1 ingrediente para:")
    for nombre, falta in casi:
        print(f"- {nombre} (te falta: {falta})")
