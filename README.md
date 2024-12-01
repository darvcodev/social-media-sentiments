[![Logo]('resources/logo.png')]

# Dashboard de Análisis de Sentimientos 📊

Este proyecto es un **dashboard interactivo** desarrollado en **Streamlit** para analizar y visualizar datos relacionados con el análisis de sentimientos. Permite cargar datasets personalizados, generar visualizaciones dinámicas y obtener estadísticas descriptivas de forma sencilla y profesional.

## Características 🌟

- **Cargar datasets personalizados**: Compatible con archivos CSV.
- **Visualizaciones interactivas**: Incluye gráficos de dispersión, histogramas, gráficos de líneas y gráficos de barras.
- **Estadísticas básicas**: Presenta un resumen descriptivo de las columnas numéricas.
- **Análisis categórico**: Muestra frecuencias de categorías en gráficos de barras.
- **Personalización**: Logo y estilos para una experiencia de usuario profesional.

## Tecnologías Utilizadas 🛠️

- **Python 3.9**
- [Streamlit](https://streamlit.io/) - Framework para aplicaciones interactivas.
- [Pandas](https://pandas.pydata.org/) - Manipulación y análisis de datos.
- [Plotly](https://plotly.com/) - Visualización de gráficos interactivos.

## Instalación y Uso 🚀

Sigue los pasos para configurar y ejecutar el proyecto localmente:

### 1. Clonar el repositorio

```bash
git clone https://github.com/darvcodev/social-media-sentiments.git
cd tu_repositorio

2. Crear un entorno virtual

Usa Conda o cualquier gestor de entornos virtuales:

conda create --name dashboard_env python=3.9
conda activate dashboard_env

3. Instalar dependencias

pip install -r requirements.txt

4. Ejecutar la aplicación

Ejecuta el siguiente comando en la terminal:

streamlit run app.py

5. Acceder al Dashboard

Abre tu navegador y ve a http://localhost:8501.

Estructura del Proyecto 📂

dashboard_project/
├── app.py          # Archivo principal de Streamlit
├── data/           # Carpeta con datasets (incluye sentimentdataset.csv)
├── resources/      # Carpeta con recursos (como logo.png)
├── requirements.txt # Lista de dependencias
└── README.md       # Documentación del proyecto

Visualizaciones Disponibles 📈

	1.	Gráfico de Dispersión: Analiza relaciones entre dos variables.
	2.	Histograma: Visualiza la distribución de una columna específica.
	3.	Gráfico de Líneas: Observa tendencias a lo largo de un eje.
	4.	Gráfico de Barras: Compara valores de categorías o rangos.

Despliegue en Streamlit Cloud 🌐

El proyecto está desplegado en Streamlit Cloud. Puedes acceder a la versión en vivo aquí:

🔗 Enlace al Dashboard

Contribuciones 🤝

¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, sigue estos pasos:
	1.	Haz un fork del repositorio.
	2.	Crea una rama para tu característica (git checkout -b feature/nueva-caracteristica).
	3.	Haz commit de tus cambios (git commit -m "Añadir nueva característica").
	4.	Haz push a la rama (git push origin feature/nueva-caracteristica).
	5.	Abre un Pull Request.

Licencia 📜

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.
```
