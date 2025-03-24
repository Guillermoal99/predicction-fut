
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
        "FC Barcelona": 2.68,
        "Real Madrid": 2.11,
        "Villarreal": 1.75,
        "Athletic": 1.57,
        "Girona": 1.50,
        "Real Sociedad": 1.46,
        "Valencia": 1.39,
        "Betis": 1.36,
        "Rayo Vallecano": 1.32,
        "Sevilla": 1.29,
        "Osasuna": 1.21,
        "Celta": 1.18,
        "Espanyol": 1.14,
        "Getafe": 1.11,
        "Alavés": 1.07,
        "Mallorca": 1.04,
        "Las Palmas": 1.00,
        "Leganés": 0.96,
        "Valladolid": 0.93,
        "Atlético de Madrid": 0.89
    },
    "Tarjetas": {
        "FC Barcelona": 19 / 28,
        "Real Madrid": 20 / 28,
        "Villarreal": 23 / 28,
        "Athletic": 22 / 28,
        "Girona": 24 / 28,
        "Real Sociedad": 22 / 28,
        "Valencia": 26 / 28,
        "Betis": 23 / 28,
        "Rayo Vallecano": 27 / 28,
        "Sevilla": 25 / 28,
        "Osasuna": 27 / 28,
        "Celta": 25 / 28,
        "Espanyol": 26 / 28,
        "Getafe": 28 / 28,
        "Alavés": 28 / 28,
        "Mallorca": 24 / 28,
        "Las Palmas": 28 / 28,
        "Leganés": 21 / 28,
        "Valladolid": 28 / 28,
        "Atlético de Madrid": 20 / 28
    },
    "Córners": {
        "FC Barcelona": 175 / 28,
        "Real Madrid": 154 / 28,
        "Villarreal": 136 / 28,
        "Athletic": 153 / 28,
        "Girona": 145 / 28,
        "Real Sociedad": 155 / 28,
        "Valencia": 150 / 28,
        "Betis": 147 / 28,
        "Rayo Vallecano": 142 / 28,
        "Sevilla": 142 / 28,
        "Osasuna": 114 / 28,
        "Celta": 110 / 28,
        "Espanyol": 109 / 28,
        "Getafe": 109 / 28,
        "Alavés": 127 / 28,
        "Mallorca": 116 / 28,
        "Las Palmas": 110 / 28,
        "Leganés": 108 / 28,
        "Valladolid": 108 / 28,
        "Atlético de Madrid": 137 / 28
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
