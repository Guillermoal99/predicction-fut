
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Predicción de Partidos de Fútbol", layout="centered")

st.title("🏐 Predicción de Resultados de Fútbol")

st.markdown("Esta app calcula una predicción de goles, tarjetas y córners para un partido de La Liga basado en datos promedio.")

# Equipos disponibles
equipos = [
    "Real Madrid", "Barcelona", "Atlético de Madrid", "Sevilla", "Valencia",
    "Athletic", "Real Sociedad", "Villarreal", "Betis", "Osasuna",
    "Celta", "Espanyol", "Getafe", "Alavés", "Rayo Vallecano",
    "Mallorca", "Girona", "Las Palmas", "Leganés", "Valladolid"
]

# Selección de equipos
col1, col2 = st.columns(2)
with col1:
    equipo_local = st.selectbox("Equipo Local", equipos)
with col2:
    equipo_visitante = st.selectbox("Equipo Visitante", equipos)

if equipo_local == equipo_visitante:
    st.warning("Elige dos equipos diferentes.")
else:
    st.subheader(f"📊 Estadísticas simuladas")

    # Simulación de datos por equipo (normalmente usarías datos reales)
    datos = {
        "Goles": {
            equipo_local: 1.8,
            equipo_visitante: 1.2
        },
        "Goles_Encajados": {
            equipo_local: 1.0,
            equipo_visitante: 1.5
        },
        "Tarjetas": {
            equipo_local: 2.1,
            equipo_visitante: 2.5
        },
        "Córners": {
            equipo_local: 5.4,
            equipo_visitante: 4.3
        }
    }

    goles_local = (datos["Goles"][equipo_local] + datos["Goles_Encajados"][equipo_visitante]) / 2
    goles_visitante = (datos["Goles"][equipo_visitante] + datos["Goles_Encajados"][equipo_local]) / 2
    tarjetas = (datos["Tarjetas"][equipo_local] + datos["Tarjetas"][equipo_visitante]) / 2
    corners = (datos["Córners"][equipo_local] + datos["Córners"][equipo_visitante]) / 2

    st.markdown("### Predicción del Partido")
    st.write(f"🎯 Resultado estimado: **{equipo_local} {round(goles_local)} - {round(goles_visitante)} {equipo_visitante}**")
    st.write(f"🟨 Tarjetas amarillas estimadas: **{tarjetas:.1f}**")
    st.write(f"🎯 Córners totales estimados: **{corners:.1f}**")

    st.info("Estos valores son ejemplos. Puedes ajustar las estadísticas con datos reales más adelante.")
