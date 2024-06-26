import streamlit as st
import pandas as pd
import numpy as np

st.title('Reportes')

# cargar datos desde un csv
ventas_df = pd.read_csv('Ventas_minoristas.csv')
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

#
options = st.multiselect(
    "Seleccione uno o más productos",
    productos,
    )
st.write("You selected:", options)


# lista de secciones unicas
secciones = ventas_df['Seccion'].unique()
st.write(secciones)

#
option = st.selectbox(
   "Seleccione una seccion",
    secciones,)
st.write("You selected:", option)



# lista de marca_id unicas
marca_id = ventas_df['Marca_ID'].unique()
st.write(marca_id)

#s
genre = st.radio(
    "Seleccione una marca",
    marca_id,
    index=None,
)
st.write("You selected:", genre)

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
cantidad_max = ventas_df['Cantidad'].max() 
cantidad_min = ventas_df['Cantidad'].min()

rango_cantidad = st.slider("Seleccione Rango", 
                           cantidad_min, 
                           cantidad_max,
(cantidad_min, cantidad_max))
st.write("cantidad", rango_cantidad)


# rango de fecha
rango_fecha = ventas_df['Fecha'].max() - ventas_df['Fecha'].min()

#
r_fecha_max = ventas_df['Fecha'].max().date()
r_fecha_min = ventas_df['Fecha'].min().date()

rango_fechas = st.slider("Seleccione rango",
                         r_fecha_max,
                         r_fecha_min,
                         (r_fecha_max, r_fecha_max))
st.write("fechas ", rango_fechas)

# total ventas por mes
total_ventas_mes = ventas_df.groupby('Mes_texto')['Cantidad'].sum()
st.write(total_ventas_mes)

df_total_ventas_mes = pd.DataFrame(total_ventas_mes).reset_index()

st.write(df_total_ventas_mes.columns)

st.bar_chart(total_ventas_mes, x='Mes_texto', y= 'Cantidad')




# total ventas por producto y mes
total_ventas_producto_mes = ventas_df.groupby(['Producto', 'Mes_texto'])['Cantidad'].sum()

st.write(total_ventas_producto_mes)



