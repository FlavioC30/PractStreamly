import streamlit as st
import pandas as pd
import numpy as np

st.title('Reportes')

# cargar datos desde un csv
ventas_df = pd.read_csv('datos/Ventas_minoristas.csv')
# ventas_df

st.write(ventas_df.describe())

st.write(ventas_df.dtypes)

# numero de ventas
num_ventas = ventas_df['Cantidad'].count()
#st.write(f'Numero de ventas: {num_ventas}')

#metrics
st.metric(label="Ventas", value="num_ventas", delta="5 %")

# total de ventas
total_ventas = ventas_df['Cantidad'].sum()
#st.write(f'Total de ventas: {total_ventas}')

st.metric(label="Total Ventas", value="total_ventas", delta="$us")

#promedio de ventas
promedio_ventas = ventas_df['Cantidad'].mean()

#numero de productos
num_productos = ventas_df['Producto'].nunique()

#numero de secciones
num_secciones = ventas_df['Seccion'].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("Promedio Ventas", promedio_ventas, "$us.")
col2.metric("", num_productos, "Num. Productos ")
col3.metric("", num_secciones, "Secciones")


# lista de productos unicos
productos = ventas_df['Producto'].unique()
st.write(productos)


# lista de secciones unicas
secciones = ventas_df['Seccion'].unique()
st.write(secciones)

# lista de marca_id unicas
marca_id = ventas_df['Marca_ID'].unique()
st.write(marca_id)


# promedio de ventas
promedio_ventas = ventas_df['Cantidad'].mean()

# top 10 de ventas
top_10_ventas = ventas_df.nlargest(10, 'Cantidad')

st.write(top_10_ventas)




# Ventas por mes
ventas_df['Fecha'] = pd.to_datetime(ventas_df['Fecha'])

ventas_df['Año'] = ventas_df['Fecha'].dt.year

ventas_df['Mes'] = ventas_df['Fecha'].dt.month

# crear un campo con el mes en texto
ventas_df['Mes_texto'] = ventas_df['Mes'].replace({1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio', 7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'})

ventas_df['Mes_texto_3'] = ventas_df['Mes'].replace({1:'Ene', 2:'Feb', 3:'Mar', 4:'Abr', 5:'May', 6:'Jun', 7:'Jul', 8:'Ago', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dic'})


st.write(ventas_df)





# rango de cantidad
rango_cantidad = ventas_df['Cantidad'].max() - ventas_df['Cantidad'].min()

# rango de fecha
rango_fecha = ventas_df['Fecha'].max() - ventas_df['Fecha'].min()


# total ventas por mes
total_ventas_mes = ventas_df.groupby('Mes_texto')['Cantidad'].sum()
st.write(total_ventas_mes)

# total ventas por producto y mes
total_ventas_producto_mes = ventas_df.groupby(['Producto', 'Mes_texto'])['Cantidad'].sum()

st.write(total_ventas_producto_mes)

