import streamlit as st

if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1
st.session_state.nombre = 'Flavio'

st.header(f"This page has run {st.session_state.counter} times.")
st.write(st.session_state)
st.button("Run it again")

