import json
import re
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
        tiene_alguno = any(
            limpiar(i) in tengo and limpiar(i) not in BASICOS
            for i in datos["ingredientes"]
        )
        if not faltan:
            completas.append((nombre, datos))
        elif len(faltan) == 1 and tiene_alguno:
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


def buscar_en_regiones(recetas_por_region, regiones, tengo):
    """Busca en las regiones indicadas y marca de qué región es cada plato."""
    completas = []
    casi = []
    for region in regiones:
        comp, parcial = buscar_recetas(recetas_por_region[region], tengo)
        completas += [(region, nombre, datos) for nombre, datos in comp]
        casi += [(region, nombre, falta) for nombre, falta in parcial]
    return completas, casi


def platos_filtrados(recetas_por_region, regiones, tengo):
    """Platos que usan TODOS los ingredientes elegidos.

    Si no se eligió ningún ingrediente, devuelve todos los platos de las regiones.
    Cada elemento es (region, nombre, datos, faltan), ordenado de menos a más
    ingredientes faltantes.
    """
    resultado = []
    for region in regiones:
        for nombre, datos in recetas_por_region[region].items():
            claves = [limpiar(i) for i in datos["ingredientes"]]
            if not all(ing in claves for ing in tengo):
                continue
            faltan = [
                i for i in datos["ingredientes"]
                if limpiar(i) not in tengo and limpiar(i) not in BASICOS
            ]
            resultado.append((region, nombre, datos, faltan))
    resultado.sort(key=lambda plato: (len(plato[3]), plato[1]))
    return resultado


def coincide_nombre(nombre, consulta):
    """True si todas las palabras de la búsqueda aparecen en el nombre del plato.

    No distingue mayúsculas, tildes ni plurales. Sin búsqueda, todo coincide.
    """
    palabras = limpiar(consulta).split()
    nombre_limpio = limpiar(nombre)
    return all(palabra in nombre_limpio for palabra in palabras)


def pasos_de(datos):
    """Pasos como lista de textos.

    Acepta el formato nuevo (lista de pasos) y el viejo (un texto '1. ... 2. ...').
    """
    pasos = datos.get("pasos", [])
    if isinstance(pasos, str):
        partes = re.split(r"\s*(?=\d+\.\s)", pasos)
        return [re.sub(r"^\d+\.\s*", "", p).strip() for p in partes if p.strip()]
    return list(pasos)


def tiempo_legible(minutos):
    horas, mins = divmod(int(minutos), 60)
    if horas and mins:
        return f"{horas} h {mins} min"
    if horas:
        return f"{horas} h"
    return f"{mins} min"
