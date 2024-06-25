# hello_demo.py

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt
import seaborn as sns

# Sección 1: Hola Mundo
st.write('Hello World')

# Sección 2: Media de una distribución binomial
binom_dist = np.random.binomial(1, 0.5, 100)
st.write(np.mean(binom_dist))

# Sección 3: Histograma de medias
binom_dist = np.random.binomial(1, 0.5, 1000)
list_of_means = [np.random.choice(binom_dist, 100, replace=True).mean() for _ in range(1000)]
fig, ax = plt.subplots()
ax.hist(list_of_means)
st.pyplot(fig)

# Sección 4: Histograma con múltiples gráficos
fig1, ax1 = plt.subplots()
ax1.hist(list_of_means)
st.pyplot(fig1)

fig2, ax2 = plt.subplots()
ax2.hist([1, 1, 1, 1])
st.pyplot(fig2)

# Sección 5: Entrada del usuario para la probabilidad de cara en una moneda
perc_heads = st.number_input(label='Posibilidad de que las monedas caigan en cara', min_value=0.0, max_value=1.0, value=0.5, key='number_input_1')
binom_dist = np.random.binomial(1, perc_heads, 1000)
list_of_means = [np.random.choice(binom_dist, 100, replace=True).mean() for _ in range(1000)]
fig, ax = plt.subplots()
ax.hist(list_of_means, range=[0, 1])
st.pyplot(fig)

# Sección 6: Título y descripción de la aplicación
st.title('Ilustrando el teorema del límite central con Streamlit')
st.subheader('Una aplicación de Tyler Richards')
st.write('Esta aplicación simula mil lanzamientos de monedas utilizando la posibilidad de que salga cara ingresada a continuación, y luego toma muestras con reemplazo de esa población y traza el histograma de las medias de las muestras para ilustrar el teorema del límite central.!')

# Reutilizando entrada del usuario y cálculo anterior
fig, ax = plt.subplots()
ax.hist(list_of_means)
st.pyplot(fig)

# Sección 7: Palmer's Penguins
st.title("Palmer's Penguins")
penguins_df = pd.read_csv('penguins.csv')
st.write(penguins_df.head())

# Sección 8: Gráfico de dispersión personalizado
st.markdown('Use this Streamlit app to make your own scatterplot about penguins!')
selected_species = st.selectbox('What species would you like to visualize?', ['Adelie', 'Gentoo', 'Chinstrap'])
selected_x_var = st.selectbox('What do you want the x variable to be?', ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])
selected_y_var = st.selectbox('What about the y?', ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g'])

penguins_df = penguins_df[penguins_df['species'] == selected_species]
alt_chart = alt.Chart(penguins_df).mark_circle().encode(x=selected_x_var, y=selected_y_var)
st.altair_chart(alt_chart)
