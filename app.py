import streamlit as st
import pandas as pd
import plotly.express as px

# --- Cargar el dataset ---
# Asegúrate de que este archivo esté en la misma carpeta que este script
df = pd.read_csv("ai_job_market_insights.csv")

# --- Encabezado del dashboard ---
st.header("AI-Powered Job Market Insights Dashboard 💼")

st.markdown("""
This dashboard explores trends in the AI-driven job market, including salaries, industries, and automation risk.
""")

# --- Mostrar una vista previa del dataset ---
if st.checkbox("Show data preview"):
    st.dataframe(df.head())

# --- Selección de gráfico ---
option = st.selectbox(
    "Choose a visualization:",
    ("Salaries by Industry", "Automation Risk by AI Adoption", "Remote Work Distribution")
)

# --- Visualización dinámica ---
if option == "Salaries by Industry":
    fig = px.box(df, x="Industry", y="Salary_USD", color="Industry",
                 title="Salary Distribution by Industry")
    st.plotly_chart(fig)

elif option == "Automation Risk by AI Adoption":
    fig = px.histogram(df, x="Automation_Risk", color="AI_Adoption_Level",
                       title="Automation Risk by AI Adoption Level", barmode="group")
    st.plotly_chart(fig)

elif option == "Remote Work Distribution":
    fig = px.pie(df, names="Remote_Friendly", title="Remote-Friendly Jobs Share")
    st.plotly_chart(fig)

