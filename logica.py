import json
import unicodedata
from pathlib import Path

BASICOS = ["aceite", "sal"]
RUTA_RECETAS = Path(__file__).with_name("recetas.json")


def singular(palabra):
    if len(palabra) > 3 and palabra.endswith("s"):
        return palabra[:-1]
    return palabra


def limpiar(texto):
    texto = texto.strip().lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return " ".join(singular(p) for p in texto.split())


def cargar_recetas():
    with open(RUTA_RECETAS, encoding="utf-8") as archivo:
        return json.load(archivo)


def ingredientes_del_usuario(entrada):
    return [limpiar(i) for i in entrada.split(",") if i.strip()]


def buscar_recetas(recetas, tengo):
    completas = []
    casi = []
    for nombre, datos in recetas.items():
        faltan = [
            i for i in datos["ingredientes"]
            if limpiar(i) not in tengo and limpiar(i) not in BASICOS
        ]
        if not faltan:
            completas.append((nombre, datos))
        elif len(faltan) == 1:
            casi.append((nombre, faltan[0]))
    return completas, casi


def catalogo_ingredientes(recetas_por_region):
    """Devuelve {clave: nombre para mostrar} con todos los ingredientes (sin los básicos)."""
    catalogo = {}
    for recetas in recetas_por_region.values():
        for datos in recetas.values():
            for ingrediente in datos["ingredientes"]:
                clave = limpiar(ingrediente)
                if clave not in BASICOS:
                    catalogo.setdefault(clave, ingrediente)
    return catalogo
