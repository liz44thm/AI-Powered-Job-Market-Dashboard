import streamlit as st
import pandas as pd
import plotly.express as px

# --- Cargar el dataset con manejo de errores ---
try:
    df = pd.read_csv("ai_job_market_insights.csv")
except FileNotFoundError:
    st.error("❌ El archivo CSV no se encontró. Verifica la ruta.")
    st.stop()
except Exception as e:
    st.error(f"⚠️ Error al cargar el archivo: {e}")
    st.stop()

# --- Encabezado del dashboard ---
st.set_page_config(page_title="Mercado Laboral IA", layout="wide")
st.title("Panel de análisis del mercado laboral impulsado por IA 💼")

st.markdown("""
Este panel explora tendencias en el mercado laboral impulsado por IA, incluyendo **salarios**, **industrias** y **riesgo de automatización**.  
Usa el menú lateral para explorar diferentes visualizaciones.
""")

# --- Barra lateral con controles ---
st.sidebar.header("Opciones de visualización")

# Vista previa del dataset
if st.sidebar.checkbox("Mostrar vista previa de datos"):
    st.subheader("Vista previa del conjunto de datos")
    st.dataframe(df.head())

# Filtro por industria
industries = st.sidebar.multiselect(
    "Filtrar por industria:",
    options=df["Industry"].dropna().unique()
)
filtered_df = df[df["Industry"].isin(industries)] if industries else df

# Menú de selección de gráficos
option = st.sidebar.selectbox(
    "Selecciona una visualización:",
    (
        "Distribución de salarios por industria",
        "Riesgo de automatización por nivel de adopción de IA",
        "Distribución de trabajos remotos"
    )
)

# --- Funciones de visualización ---
def show_salary_distribution(data):
    st.subheader("Distribución de salarios por industria")
    fig = px.box(
        data,
        x="Industry",
        y="Salary_USD",
        color="Industry",
        title="Distribución de salarios por industria",
        points="all"
    )
    st.plotly_chart(fig, use_container_width=True)

def show_automation_risk(data):
    st.subheader("Riesgo de automatización por nivel de adopción de IA")
    fig = px.histogram(
        data,
        x="Automation_Risk",
        color="AI_Adoption_Level",
        title="Riesgo de automatización según el nivel de adopción de IA",
        barmode="group"
    )
    st.plotly_chart(fig, use_container_width=True)

def show_remote_work_distribution(data):
    st.subheader("Distribución de trabajos remotos")
    fig = px.pie(
        data,
        names="Remote_Friendly",
        title="Proporción de trabajos compatibles con trabajo remoto"
    )
    st.plotly_chart(fig, use_container_width=True)

# --- Mostrar visualización seleccionada ---
if option == "Distribución de salarios por industria":
    show_salary_distribution(filtered_df)
elif option == "Riesgo de automatización por nivel de adopción de IA":
    show_automation_risk(filtered_df)
elif option == "Distribución de trabajos remotos":
    show_remote_work_distribution(filtered_df)

