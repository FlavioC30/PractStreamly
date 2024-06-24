import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib as plt

st.title('App Dia2')

st.sidebar.title('Filtros')

add_selectbox = st.sidebar.selectbox(
    "seleccione Metrica??",
    ("top 10 vendedores", "Media de ventas", "Ventas por mes")
)

add_slider = st.sidebar.slider(
    'Total ventas',
    1000.0, 100000.0, (10000.0, 5000.0)
)

left_column, right_column = st.columns(2)
## left_column, center_column, right_column = st.columns(3)

left_column.button('Click me')

with right_column:
    add_selectbox = st.selectbox("seleccione otra Metrica?",
    ("top 10 vendedores", "Media de ventas", "Ventas por mes")
)

with right_column:
    chosen = st.radio(
        'starting hat',
        ("grifindon", "Revenclaw", "cristiano", "Styletherin"))
    st.write(f"you are in {chosen} house!")


st.write('You selections')
add_slider = st.slider('total ventas 2', 10000.0, 1000.0, 500000.0)


    

