import streamlit as st
import pandas as pd
import plotly.express as px

# --- Cargar el dataset ---
df = pd.read_csv("ai_job_market_insights.csv")

# --- Encabezado del dashboard ---
st.header("AI-Powered Job Market Insights Dashboard 💼")

st.markdown("""
This dashboard explores trends in the AI-driven job market, including **salaries**, **industries**, and **automation risk**.  
Use the menu below to explore different visualizations.
""")

# --- Mostrar una vista previa del dataset ---
if st.checkbox("Show data preview", key="preview"):
    st.dataframe(df.head())

# --- Menú de selección de gráficos ---
option = st.selectbox(
    "Choose a visualization:",
    (
        "Salaries by Industry",
        "Automation Risk by AI Adoption",
        "Remote Work Distribution"
    ),
    key="chart_selector"
)

# --- Visualización dinámica ---
if option == "Salaries by Industry":
    fig = px.box(
        df,
        x="Industry",
        y="Salary_USD",
        color="Industry",
        title="Salary Distribution by Industry",
        points="all"
    )
    st.plotly_chart(fig, use_container_width=True)

elif option == "Automation Risk by AI Adoption":
    fig = px.histogram(
        df,
        x="Automation_Risk",
        color="AI_Adoption_Level",
        title="Automation Risk by AI Adoption Level",
        barmode="group"
    )
    st.plotly_chart(fig, use_container_width=True)

elif option == "Remote Work Distribution":
    fig = px.pie(
        df,
        names="Remote_Friendly",
        title="Remote-Friendly Jobs Share"
    )
    st.plotly_chart(fig, use_container_width=True)
