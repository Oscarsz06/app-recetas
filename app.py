import unicodedata
import json

def limpiar(texto):
    texto = texto.strip().lower()
    texto = unicodedata.normalize("NFD", texto)
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")

basicos = ["aceite", "sal"]

with open("recetas.json", encoding="utf-8") as archivo:
    recetas = json.load(archivo)

print("Escribe los ingredientes que compraste, separados por coma.")
entrada = input("Ingredientes: ")
tengo = [limpiar(i) for i in entrada.split(",")]

completas = []
casi = []

for nombre, datos in recetas.items():
    faltan = [i for i in datos["ingredientes"] if i not in tengo and i not in basicos]
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