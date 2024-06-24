import os

# Crear el directorio 'streamlit_hello'
os.makedirs('streamlit_hello', exist_ok=True)

# Cambiar al directorio 'streamlit_hello'
os.chdir('streamlit_hello')

## 3
with open('hello_demo.py', 'w') as f:
    f.write("""
import streamlit as st
st.write('Hello World')
""")

## 4

import streamlit as st
st.write('Hello World')
