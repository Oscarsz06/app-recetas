import re

import streamlit as st

from logica import cargar_recetas, ingredientes_del_usuario, buscar_recetas

st.set_page_config(page_title="App de Recetas", page_icon="🍳")

st.title("🍳 App de Recetas")
st.write("Elige una región, escribe lo que compraste y te digo qué puedes cocinar.")

recetas_por_region = cargar_recetas()


def pasos_en_lista(texto):
    partes = re.split(r"\s*(?=\d+\.\s)", texto)
    return [p.strip() for p in partes if p.strip()]


region = st.selectbox(
    "¿De qué región quieres cocinar?",
    list(recetas_por_region.keys()),
)

entrada = st.text_input(
    "Ingredientes que compraste (separados por coma)",
    placeholder="arroz, pollo, cebolla, tomate, papa",
)

if entrada.strip():
    tengo = ingredientes_del_usuario(entrada)
    completas, casi = buscar_recetas(recetas_por_region[region], tengo)

    st.subheader("Puedes preparar")
    if completas:
        for nombre, datos in completas:
            with st.expander(nombre, expanded=True):
                st.markdown("**Ingredientes:** " + ", ".join(datos["ingredientes"]))
                for paso in pasos_en_lista(datos["pasos"]):
                    st.write(paso)
    else:
        st.info("Ninguna receta completa todavía.")

    if casi:
        st.subheader("Te falta solo 1 ingrediente para")
        for nombre, falta in casi:
            st.write(f"- **{nombre}** (te falta: {falta})")
else:
    st.caption("Escribe tus ingredientes para ver las recetas.")
