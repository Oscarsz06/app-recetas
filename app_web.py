import re

import streamlit as st

from logica import (
    buscar_en_regiones,
    catalogo_ingredientes,
    cargar_recetas,
    limpiar,
)

st.set_page_config(page_title="App de Recetas", page_icon="🍳")


@st.cache_data
def datos_recetas():
    return cargar_recetas()


def pasos_en_lista(texto):
    partes = re.split(r"\s*(?=\d+\.\s)", texto)
    return [p.strip() for p in partes if p.strip()]


recetas_por_region = datos_recetas()
regiones = list(recetas_por_region.keys())
catalogo = catalogo_ingredientes(recetas_por_region)
opciones = sorted(catalogo.values(), key=limpiar)

st.title("🍳 App de Recetas")
st.write("Agrega los ingredientes que tienes y te digo qué puedes cocinar. Si quieres, filtra por región.")

seleccion = st.multiselect(
    "Ingredientes que tienes",
    opciones,
    placeholder="Escribe para buscar y elige un ingrediente...",
    help="Elige un ingrediente para agregarlo. Haz clic en la x de uno para quitarlo.",
)
st.caption("Aceite y sal se dan por sentados, no hace falta agregarlos.")

region = st.pills(
    "Región (opcional)",
    regiones,
    selection_mode="single",
    help="Elige una región para filtrar. Haz clic otra vez para quitar el filtro y ver todas.",
)

if seleccion:
    tengo = [limpiar(i) for i in seleccion]
    buscar_en = [region] if region else regiones
    completas, casi = buscar_en_regiones(recetas_por_region, buscar_en, tengo)

    st.subheader("Puedes preparar" + (f" ({region})" if region else " (todas las regiones)"))
    if completas:
        for reg, nombre, datos in completas:
            titulo = f"{nombre} · {reg}" if not region else nombre
            with st.expander(titulo, expanded=len(completas) <= 3):
                st.markdown("**Ingredientes:** " + ", ".join(datos["ingredientes"]))
                for paso in pasos_en_lista(datos["pasos"]):
                    st.write(paso)
    else:
        st.info("Ninguna receta completa todavía. Prueba agregando más ingredientes.")

    if casi:
        st.subheader("Te falta solo 1 ingrediente para")
        for reg, nombre, falta in casi:
            etiqueta = f" ({reg})" if not region else ""
            st.write(f"- **{nombre}**{etiqueta} (te falta: {falta})")
else:
    st.info("Agrega al menos un ingrediente para ver las recetas.")
