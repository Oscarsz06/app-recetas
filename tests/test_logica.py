"""Pruebas de la lógica de búsqueda (logica.py)."""
from logica import (
    BASICOS,
    buscar_en_regiones,
    catalogo_ingredientes,
    coincide_nombre,
    ingredientes_del_usuario,
    limpiar,
    pasos_de,
    platos_filtrados,
    tiempo_legible,
)

# Recetas pequeñas e inventadas, para que las pruebas no dependan de recetas.json
RECETAS = {
    "Pais A": {
        "Arroz con huevo": {"ingredientes": ["arroz", "huevo", "aceite", "sal"]},
        "Omelette": {"ingredientes": ["huevo", "queso", "sal"]},
        "Sopa de pollo": {"ingredientes": ["pollo", "papa", "zanahoria", "sal"]},
    },
    "Pais B": {
        "Pollo asado": {"ingredientes": ["pollo", "limón", "aceite", "sal"]},
    },
}


def nombres(resultado):
    return [plato[1] for plato in resultado]


# --- limpiar ---------------------------------------------------------------

def test_limpiar_quita_tildes_y_mayusculas():
    assert limpiar("LIMÓN") == "limon"


def test_limpiar_convierte_plural_en_singular():
    assert limpiar("Tomates") == "tomate"
    assert limpiar("huevos") == "huevo"


def test_limpiar_no_recorta_palabras_cortas():
    # "gas" mide 3 letras: no se le quita la "s"
    assert limpiar("gas") == "gas"


def test_limpiar_ignora_espacios_sobrantes():
    assert limpiar("  queso   fresco ") == "queso fresco"


def test_ingredientes_del_usuario_separa_por_comas():
    assert ingredientes_del_usuario("Arroz, Huevos, ,Limón") == ["arroz", "huevo", "limon"]


# --- catálogo --------------------------------------------------------------

def test_catalogo_no_incluye_basicos():
    catalogo = catalogo_ingredientes(RECETAS)
    for basico in BASICOS:
        assert basico not in catalogo


def test_catalogo_contiene_los_ingredientes_de_todas_las_regiones():
    catalogo = catalogo_ingredientes(RECETAS)
    assert {"arroz", "huevo", "queso", "pollo", "papa", "zanahoria", "limon"} == set(catalogo)


# --- platos_filtrados ------------------------------------------------------

def test_sin_ingredientes_devuelve_todos_los_platos():
    resultado = platos_filtrados(RECETAS, ["Pais A", "Pais B"], [])
    assert len(resultado) == 4


def test_solo_salen_platos_que_usan_todos_los_ingredientes_elegidos():
    resultado = platos_filtrados(RECETAS, ["Pais A", "Pais B"], ["pollo", "papa"])
    assert nombres(resultado) == ["Sopa de pollo"]


def test_respeta_las_regiones_elegidas():
    resultado = platos_filtrados(RECETAS, ["Pais B"], ["pollo"])
    assert nombres(resultado) == ["Pollo asado"]


def test_aceite_y_sal_se_asumen_siempre():
    # Con arroz y huevo no falta nada: el aceite y la sal ya se dan por tenidos
    resultado = platos_filtrados(RECETAS, ["Pais A"], ["arroz", "huevo"])
    assert resultado[0][1] == "Arroz con huevo"
    assert resultado[0][3] == []


def test_calcula_los_ingredientes_que_faltan():
    resultado = platos_filtrados(RECETAS, ["Pais A"], ["pollo"])
    assert resultado[0][3] == ["papa", "zanahoria"]


def test_ordena_de_menos_a_mas_faltantes():
    resultado = platos_filtrados(RECETAS, ["Pais A"], ["huevo"])
    faltantes = [len(plato[3]) for plato in resultado]
    assert faltantes == sorted(faltantes)
    assert nombres(resultado)[0] == "Arroz con huevo"


# --- buscar_en_regiones ----------------------------------------------------

def test_buscar_en_regiones_separa_completos_y_casi():
    completas, casi = buscar_en_regiones(RECETAS, ["Pais A"], ["huevo", "queso"])
    assert [c[1] for c in completas] == ["Omelette"]
    assert ("Pais A", "Arroz con huevo", "arroz") in casi


# --- coincide_nombre -------------------------------------------------------

def test_coincide_nombre_ignora_tildes_y_mayusculas():
    assert coincide_nombre("Pollo al limón", "LIMON")


def test_coincide_nombre_exige_todas_las_palabras():
    assert coincide_nombre("Arroz con pollo", "pollo arroz")
    assert not coincide_nombre("Arroz con pollo", "pollo frito")


def test_coincide_nombre_sin_busqueda_coincide_todo():
    assert coincide_nombre("Cualquier plato", "")


# --- pasos y tiempo --------------------------------------------------------

def test_pasos_de_acepta_lista():
    assert pasos_de({"pasos": ["Corta.", "Cocina."]}) == ["Corta.", "Cocina."]


def test_pasos_de_acepta_texto_numerado_antiguo():
    datos = {"pasos": "1. Corta la cebolla. 2. Fríela. 3. Sirve."}
    assert pasos_de(datos) == ["Corta la cebolla.", "Fríela.", "Sirve."]


def test_pasos_de_sin_pasos_devuelve_lista_vacia():
    assert pasos_de({}) == []


def test_tiempo_legible():
    assert tiempo_legible(25) == "25 min"
    assert tiempo_legible(60) == "1 h"
    assert tiempo_legible(95) == "1 h 35 min"
