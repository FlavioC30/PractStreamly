import streamlit as st
import pandas as pd

import numpy as np 
st.title('Reportes')
ventas_df = pd.read_csv('Ventas_minoristas.csv')
ventas_df

st.write(ventas_df.describe())
st.write(ventas_df.dtypes)
st.write(ventas_df.info())

#numero de ventas 
num_ventas = ventas_df['Cantidad'].count()
st.write(f'Numero de ventas: {num_ventas}')

#total de ventas 
total_ventas = ventas_df['Cantidad'].sum()
st.write(f'Total de ventas:{total_ventas}')

#promedio de ventas 
promedio_ventas = ventas_df['Cantidad'].mean()

#top 10 de ventas 
top_ventas = ventas_df.nlargest(10, 'Cantidad')
st.write(top_ventas)

#total de ventas por mes
ventas_df['Fecha'] = pd.to_datetime(ventas_df['Fecha'])

ventas_df['Año'] = ventas_df['Fecha'].dt.year

ventas_df['Mes'] = ventas_df['Fecha'].dt.month

st.write(ventas_df)

#crear un campo con el mes en txt
ventas_df['Mes_texto'] = ventas_df['Mes'].replace({1:'Enero', 2:'Febrero', 3:'Marzo', 4:'Abril', 5:'Mayo', 6:'Junio', 7:'Julio', 8:'Agosto', 9:'Septiembre', 10:'Octubre', 11:'Noviembre', 12:'Diciembre'})
st.write(ventas_df)

ventas_df['Mes_texto_3'] = ventas_df['Mes'].replace({1:'Ene', 2:'Feb', 3:'Mar', 4:'Abr', 5:'May', 6:'Jun', 7:'Jul', 8:'Ago', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dic'})
st.write(ventas_df)
 
#lista de productos unicos 
produtos = ventas_df['Producto'].unique()
st.write(ventas_df)

#lista de secciones unicas
secciones = ventas_df['Seccion'].unique()
st.write(secciones)

#lista marca_id unicas
marca_id = ventas_df['Marca_ID'].unique()
st.write(marca_id) 

#rango de cantidad
rango_cantidad = ventas_df['Cantidad'].max()- ventas_df['Cantidad'].min()
st.write(rango_cantidad)

#rango fecha 
rango_fecha = ventas_df['Fecha'].max()- ventas_df['Fecha'].min()
st.write(rango_fecha)


#total ventas por mes
total_ventas_mes = ventas_df.groupby('Mes_texto')['Cantidad'].sum()
st.write(total_ventas_mes)

#cantidad de ventas de producto por mes 
total_ventas_productos_mes = ventas_df.groupby

