import re

import streamlit as st

from logica import (
    buscar_recetas,
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
catalogo = catalogo_ingredientes(recetas_por_region)
opciones = sorted(catalogo.values(), key=limpiar)

st.title("🍳 App de Recetas")
st.write("Elige una región, agrega los ingredientes que tienes y te digo qué puedes cocinar.")

region = st.selectbox(
    "¿De qué región quieres cocinar?",
    list(recetas_por_region.keys()),
)

seleccion = st.multiselect(
    "Ingredientes que tienes",
    opciones,
    placeholder="Escribe para buscar y elige un ingrediente...",
    help="Elige un ingrediente para agregarlo. Haz clic en la x de uno para quitarlo.",
)
st.caption("Aceite y sal se dan por sentados, no hace falta agregarlos.")

if seleccion:
    tengo = [limpiar(i) for i in seleccion]
    completas, casi = buscar_recetas(recetas_por_region[region], tengo)

    st.subheader("Puedes preparar")
    if completas:
        for nombre, datos in completas:
            with st.expander(nombre, expanded=len(completas) <= 3):
                st.markdown("**Ingredientes:** " + ", ".join(datos["ingredientes"]))
                for paso in pasos_en_lista(datos["pasos"]):
                    st.write(paso)
    else:
        st.info("Ninguna receta completa todavía. Prueba agregando más ingredientes.")

    if casi:
        st.subheader("Te falta solo 1 ingrediente para")
        for nombre, falta in casi:
            st.write(f"- **{nombre}** (te falta: {falta})")
else:
    st.info("Agrega al menos un ingrediente para ver las recetas.")
