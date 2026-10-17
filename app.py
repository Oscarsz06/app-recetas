import unicodedata
import json

def singular(palabra):
    if len(palabra) > 3 and palabra.endswith("s"):
        return palabra[:-1]
    return palabra

def limpiar(texto):
    texto = texto.strip().lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return " ".join(singular(p) for p in texto.split())

basicos = ["aceite", "sal"]

with open("recetas.json", encoding="utf-8") as archivo:
    recetas_por_region = json.load(archivo)

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
tengo = [limpiar(i) for i in entrada.split(",")]

completas = []
casi = []

for nombre, datos in recetas.items():
    faltan = [i for i in datos["ingredientes"] if limpiar(i) not in tengo and limpiar(i) not in basicos]
    if not faltan:
        completas.append((nombre, datos))
    elif len(faltan) == 1:
        casi.append((nombre, faltan[0]))

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