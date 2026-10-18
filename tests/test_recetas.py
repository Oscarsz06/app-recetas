"""Validación del archivo recetas.json: que todas las recetas tengan el formato correcto."""
from logica import cargar_recetas, limpiar

DIFICULTADES = {"Fácil", "Intermedio", "Desafiante"}
PROHIBIDOS = set("*_[]`$~")  # rompen el formato de Streamlit

RECETAS = cargar_recetas()
TODAS = [(region, nombre, datos) for region, platos in RECETAS.items() for nombre, datos in platos.items()]


def test_hay_50_platos_por_region():
    for region, platos in RECETAS.items():
        assert len(platos) == 50, f"{region} tiene {len(platos)} platos"


def test_hay_10_regiones():
    assert len(RECETAS) == 10


def test_cantidades_coinciden_con_ingredientes():
    for region, nombre, datos in TODAS:
        assert set(datos["cantidades"]) == set(datos["ingredientes"]), f"{region}: {nombre}"


def test_ingredientes_sin_repetir_dentro_de_una_receta():
    for region, nombre, datos in TODAS:
        claves = [limpiar(i) for i in datos["ingredientes"]]
        assert len(claves) == len(set(claves)), f"{region}: {nombre}"


def test_tiempo_y_porciones_en_rango():
    for region, nombre, datos in TODAS:
        assert 5 <= datos["tiempo"] <= 360, f"{region}: {nombre}"
        assert 1 <= datos["porciones"] <= 12, f"{region}: {nombre}"


def test_dificultad_valida():
    for region, nombre, datos in TODAS:
        assert datos["dificultad"] in DIFICULTADES, f"{region}: {nombre}"


def test_pasos_y_consejos_completos():
    for region, nombre, datos in TODAS:
        assert 4 <= len(datos["pasos"]) <= 8, f"{region}: {nombre}"
        assert all(len(p) >= 15 for p in datos["pasos"]), f"{region}: {nombre}"
        assert len(datos["consejos"]) >= 2, f"{region}: {nombre}"


def test_utensilios_presentes():
    for region, nombre, datos in TODAS:
        assert datos["utensilios"], f"{region}: {nombre}"


def test_sin_caracteres_que_rompan_el_formato():
    for region, nombre, datos in TODAS:
        textos = [nombre, *datos["pasos"], *datos["consejos"], *datos["utensilios"], *datos["cantidades"].values()]
        for texto in textos:
            assert not (PROHIBIDOS & set(texto)), f"{region}: {nombre}: {texto!r}"
