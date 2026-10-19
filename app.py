import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Encabezado
st.header('Análisis de anuncios de venta de coches')

# Leer datos
car_data = pd.read_csv('vehicles_us.csv')

# Casilla de verificación 1: Histograma
build_histogram = st.checkbox('Construir un histograma')
if build_histogram:
    st.write('Construir un histograma para la columna odómetro')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación 2: Gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')
if build_scatter:
    st.write('Construir un gráfico de dispersión de Precio vs. Odómetro')
    fig_scatter = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
    fig_scatter.update_layout(title_text='Precio vs. Odómetro')
    st.plotly_chart(fig_scatter, use_container_width=True)