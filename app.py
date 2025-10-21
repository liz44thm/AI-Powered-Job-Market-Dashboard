import streamlit as st
import pandas as pd
import plotly.express as px

# --- Cargar el dataset ---

df = pd.read_csv("ai_job_market_insights.csv")

# --- Encabezado del dashboard ---
st.header("AI-Powered Job Market Insights Dashboard 💼")

st.markdown("""
This dashboard explores trends in the AI-driven job market, including salaries, industries, and automation risk.
""")

# --- Mostrar una vista previa del dataset ---
if st.checkbox("Show data preview"):
    st.dataframe(df.head())

# --- Selección de gráfico --
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

# --- Cargar el dataset ---
df = pd.read_csv("ai_job_market_insights.csv")

# --- Encabezado del dashboard ---
st.header("AI-Powered Job Market Insights Dashboard 💼")

st.markdown("""
Explore how Artificial Intelligence is shaping the job market.  
Use the checkboxes below to display different visualizations.
""")

# --- Mostrar una vista previa del dataset ---
if st.checkbox("Show data preview"):
    st.dataframe(df.head())

# --- Casilla para mostrar histograma ---
show_hist = st.checkbox("Show Salary Histogram by Industry")

if show_hist:
    st.write("### Salary Distribution by Industry")
    fig_hist = px.histogram(
        df,
        x="Industry",
        y="Salary_USD",
        color="Industry",
        title="Salary Distribution by Industry",
        nbins=20
    )
    st.plotly_chart(fig_hist)

# --- Casilla para mostrar gráfico de dispersión ---
show_scatter = st.checkbox("Show Scatter Plot: Salary vs. Automation Risk")

if show_scatter:
    st.write("### Scatter Plot of Salary vs. Automation Risk")
    fig_scatter = px.scatter(
        df,
        x="Automation_Risk",
        y="Salary_USD",
        color="AI_Adoption_Level",
        size="Salary_USD",
        hover_name="Job_Title",
        title="Salary vs. Automation Risk Colored by AI Adoption Level"
    )
    st.plotly_chart(fig_scatter)