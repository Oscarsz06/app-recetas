import unicodedata

def limpiar(texto):
    texto = texto.strip().lower()
    texto = unicodedata.normalize("NFD", texto)
    return "".join(c for c in texto if unicodedata.category(c) != "Mn")

basicos = ["aceite", "sal"]

recetas = {
    "Arroz con huevo": {
        "ingredientes": ["arroz", "huevo", "aceite", "sal"],
        "pasos": "1. Cocina el arroz. 2. Fríe los huevos en aceite. 3. Sirve juntos con sal.",
    },
    "Huevos pericos": {
        "ingredientes": ["huevo", "tomate", "cebolla", "aceite", "sal"],
        "pasos": "1. Pica tomate y cebolla. 2. Sofríelos en aceite. 3. Agrega los huevos batidos y revuelve hasta que cuajen.",
    },
    "Yuca frita": {
        "ingredientes": ["yuca", "aceite", "sal"],
        "pasos": "1. Cocinaa yuca en agua con sal. 2. Córtala en tiras. 3. Fríela hasta que dore.",
    },
    "Patacones": {
        "ingredientes": ["platano verde", "aceite", "sal"],
        "pasos": "1. Corta el plátano en rodajas gruesas. 2. Fríe. 3. Aplasta, fríe de nuevo y sala.",
    },
}

print("Escribe los ingredientes que compraste, separados por coma.")
entrada = input("Ingredientes: ")
tengo = [limpiar(i) for i in entrada.split(",")]

print("\nPuedes preparar:")
encontrado = False
for nombre, datos in recetas.items():
    faltan = [i for i in datos["ingredientes"] if i not in tengo and i not in basicos]
    if not faltan:
        print(f"\n- {nombre}")
        print(datos["pasos"])
        encontrado = True

if not encontrado:
    print("Ninguna receta con esos ingredientes todavía.")