import streamlit as st
from PIL import Image
import datetime
import time
import os

# Agregar texto
st.header("This is a header")
st.subheader("This is a subheader")
st.text("This is a simple text")
st.write("This is a write dimension")

# Hipervínculos
st.markdown("[Streamlit](https://www.streamlit.io)")
st.markdown("https://www.streamlit.io")

html_page = """
<div style="background-color:blue;padding:50px">
<p style="color:yellow;font-size:50px">Enjoy Streamlit!</p>
</div>
"""
st.markdown(html_page, unsafe_allow_html=True)

# Colores en textos
st.success("Success!")
st.info("Information")
st.warning("This is a warning!")
st.error("This is an error!")

# Imágenes, audio y video
image_path = "packt.jpeg"
if os.path.exists(image_path):
    img = Image.open(image_path)
    st.image(img, width=300, caption="Packt Logo")
else:
    st.error("Image file not found")

video_path = "SampleVideo_1280x720_1mb.mp4"
if os.path.exists(video_path):
    video_file = open(video_path, "rb")
    video_bytes = video_file.read()
    st.video(video_bytes)
else:
    st.error("Video file not found")

# Widgets de Streamlit
if st.button("Play"):
    st.text("Hello world!")

if st.checkbox("Checkbox"):
    st.text("Checkbox selected")

radio_but = st.radio("Your Selection", ["A", "B"])
if radio_but == "A":
    st.info("You selected A")
else:
    st.info("You selected B")

city = st.selectbox("Your City", ["Napoli", "Palermo", "Catania"])

# Multiselect
occupation = st.multiselect("Your Occupation", ["Programmer", "Data Scientist", "IT Consultant", "DBA"])

# Ingresando texto y números
name = st.text_input("Your Name", "Write something…")
st.text(name)

age = st.number_input("Input a number")

message = st.text_area("Your Message", "Write something...")

# Slider
select_val = st.slider("Select a Value", 1, 10)

# Globos
if st.button("Balloons"):
    st.balloons()

# Fecha, hora y más
today = st.date_input("Today is", datetime.datetime.now())
hour = st.time_input("The time is", datetime.time(12, 30))

data = {"name": "John", "surname": "Wick"}
st.json(data)
