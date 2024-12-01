import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(
    page_title="Análisis de Sentimientos - Dashboard",
    page_icon="📊",
    layout="wide"
)

# Título del Dashboard
st.title("📊 Dashboard de Análisis de Sentimientos")

logo_path = "https://i.ibb.co/jg9vDRw/logo.png"
st.sidebar.markdown(
    f"""
    <div style="text-align: center;">
        <img src="{logo_path}" alt="Logo" style="width: 80%; margin-bottom: 10px;">
    </div>
    """,
    unsafe_allow_html=True
)

# Subir archivo o usar el predeterminado
uploaded_file = st.sidebar.file_uploader("Sube un archivo CSV", type=["csv"])

if uploaded_file:
    data_path = uploaded_file
else:
    data_path = "./data/sentimentdataset.csv"

# Cargar datos
try:
    df = pd.read_csv(data_path)
    
    # Eliminar columnas no deseadas automáticamente
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

    st.sidebar.success("Datos cargados correctamente.")
    
    # Mostrar vista previa de los datos
    st.subheader("Vista Previa del Conjunto de Datos")
    st.dataframe(df.head())

    # Verificar columnas
    st.sidebar.header("Opciones de Visualización")
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    all_columns = df.columns

    # Filtros de visualización
    visualization_type = st.sidebar.selectbox(
        "Selecciona el tipo de visualización",
        ["Gráfico de Dispersión", "Histograma", "Gráfico de Líneas", "Gráfico de Barras"]
    )

    st.sidebar.subheader("Opciones de Columnas")
    x_axis = st.sidebar.selectbox("Selecciona el eje X", options=all_columns)
    y_axis = st.sidebar.selectbox("Selecciona el eje Y", options=numeric_columns)
    
    # Generar visualización
    st.subheader(f"Visualización: {visualization_type}")
    if visualization_type == "Gráfico de Dispersión":
        fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{y_axis} vs {x_axis}")
    elif visualization_type == "Histograma":
        fig = px.histogram(df, x=x_axis, title=f"Distribución de {x_axis}")
    elif visualization_type == "Gráfico de Líneas":
        fig = px.line(df, x=x_axis, y=y_axis, title=f"{y_axis} a lo largo de {x_axis}")
    elif visualization_type == "Gráfico de Barras":
        fig = px.bar(df, x=x_axis, y=y_axis, title=f"{y_axis} por {x_axis}")

    st.plotly_chart(fig, use_container_width=True)

    # Añadir análisis adicional (estadísticas)
    st.subheader("📈 Estadísticas Básicas del Conjunto de Datos")
    st.write(df.describe())

    # Opcional: Selección dinámica de columna
    st.sidebar.header("Análisis por Categoría")
    category_column = st.sidebar.selectbox("Selecciona una columna categórica", options=all_columns)
    if category_column:
        st.subheader(f"Frecuencia de Categorías en {category_column}")
        category_count = df[category_column].value_counts()
        st.bar_chart(category_count)
    
except Exception as e:
    st.error(f"No se pudieron cargar los datos. Error: {e}")