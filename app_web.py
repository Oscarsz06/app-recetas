import re

import streamlit as st

from logica import (
    buscar_en_regiones,
    catalogo_ingredientes,
    cargar_recetas,
    coincide_nombre,
    limpiar,
    platos_filtrados,
)

st.set_page_config(page_title="RecetApp", page_icon="🍳")


@st.cache_data
def datos_recetas():
    return cargar_recetas()


def pasos_en_lista(texto):
    partes = re.split(r"\s*(?=\d+\.\s)", texto)
    return [p.strip() for p in partes if p.strip()]


def mostrar_pasos(datos):
    for paso in pasos_en_lista(datos["pasos"]):
        st.write(paso)


recetas_por_region = datos_recetas()
regiones = list(recetas_por_region.keys())
catalogo = catalogo_ingredientes(recetas_por_region)
opciones = sorted(catalogo.values(), key=limpiar)

st.title("🍳 RecetApp")
st.write("Elige una región para ver sus platos y agrega ingredientes para ir reduciendo la lista.")

busqueda = st.text_input(
    "Buscar plato por nombre",
    placeholder="Ej. pollo, arepa, ceviche...",
    help="Escribe parte del nombre y presiona Enter. No importan las tildes ni las mayúsculas.",
).strip()

region = st.pills(
    "Región (opcional)",
    regiones,
    selection_mode="single",
    help="Elige una región para ver sus platos. Haz clic otra vez para quitar el filtro y ver todas.",
)

seleccion = st.multiselect(
    "Ingredientes que tienes",
    opciones,
    placeholder="Escribe para buscar y elige un ingrediente...",
    help="Elige un ingrediente para agregarlo. Haz clic en la x de uno para quitarlo.",
)
st.caption("Aceite y sal se dan por sentados, no hace falta agregarlos.")

solo_preparables = st.toggle(
    "Mostrar solo lo que ya puedo preparar",
    help="Muestra los platos que puedes hacer con tus ingredientes y los que te falta uno solo.",
)

tengo = [limpiar(i) for i in seleccion]
buscar_en = [region] if region else regiones
donde = f" de {region}" if region else " de todas las regiones"

if solo_preparables:
    if not seleccion:
        st.info("Agrega al menos un ingrediente para ver lo que puedes preparar.")
    else:
        completas, casi = buscar_en_regiones(recetas_por_region, buscar_en, tengo)
        completas = [c for c in completas if coincide_nombre(c[1], busqueda)]
        casi = [c for c in casi if coincide_nombre(c[1], busqueda)]

        st.subheader("Puedes preparar" + donde + (" (filtrado por nombre)" if busqueda else ""))
        if completas:
            for reg, nombre, datos in completas:
                titulo = f"{nombre} · {reg}" if not region else nombre
                with st.expander(titulo, expanded=len(completas) <= 3):
                    st.markdown("**Ingredientes:** " + ", ".join(datos["ingredientes"]))
                    mostrar_pasos(datos)
        elif busqueda:
            st.info("Ninguna receta completa coincide con tu búsqueda.")
        else:
            st.info("Ninguna receta completa todavía. Prueba agregando más ingredientes.")

        if casi:
            st.subheader("Te falta solo 1 ingrediente para")
            for reg, nombre, falta in casi:
                etiqueta = f" ({reg})" if not region else ""
                st.write(f"- **{nombre}**{etiqueta} (te falta: {falta})")
else:
    if not region and not seleccion and not busqueda:
        st.info("Elige una región, agrega ingredientes o busca un plato por nombre.")
    else:
        platos = platos_filtrados(recetas_por_region, buscar_en, tengo)
        platos = [p for p in platos if coincide_nombre(p[1], busqueda)]
        cantidad = len(platos)
        palabra = "plato" if cantidad == 1 else "platos"
        detalle = " con tus ingredientes" if seleccion else ""
        if busqueda:
            detalle += " (filtrado por nombre)"
        st.subheader(f"{cantidad} {palabra}{donde}{detalle}")

        if not platos:
            if busqueda:
                st.info("Ningún plato coincide con esa búsqueda. Prueba con otra palabra o cambia los filtros.")
            else:
                st.info("Ningún plato usa todos esos ingredientes. Quita alguno de la lista.")

        for reg, nombre, datos, faltan in platos:
            titulo = nombre if region else f"{nombre} · {reg}"
            if seleccion and not faltan:
                titulo = "✅ " + titulo
            with st.expander(titulo, expanded=cantidad <= 3):
                st.markdown("**Ingredientes:** " + ", ".join(datos["ingredientes"]))
                if seleccion:
                    if faltan:
                        st.markdown("**Te faltan:** " + ", ".join(faltan))
                    else:
                        st.markdown("**Tienes todo lo necesario.**")
                mostrar_pasos(datos)
