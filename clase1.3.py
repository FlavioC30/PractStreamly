# agregar texto

	st.header("This is a header")
	st.subheader("This is a subheader")
	st.text("This is a simple text")
	st.write("This is a write dimension")

# hipervinculos
	“st.markdown("[Streamlit](https://www.streamlit.io)")”


	st.markdown("https://www.streamlit.io")

	“html_page = """
	<div style="background-color:blue;padding:50px">
	<p style="color:yellow;font-size:50px">Enjoy Streamlit!</p>
	</div>
	"""
	st.markdown(html_page, unsafe_allow_html=True)”

#Colored textboxes

	“st.success("Success!")
	st.info("Information")
	st.warning("This is a warning!")
	st.error("This is an error!")”

# “Images, audio, and video”

	“from PIL import Image
	img = Image.open("packt.jpeg")
	st.image(img, width=300, caption="Packt Logo")”

	“video_file = open("SampleVideo_1280x720_1mb.mp4","rb")
	video_bytes = video_file.read()
	st.video(video_bytes)”


# streamlit Widgets

“if st.button("Play"):
	st.text("Hello world!")”

“if st.checkbox("Checkbox"):
	st.text("Checkbox selected")”

“radio_but = st.radio("Your Selection", ["A", "B"])
if radio_but == "A":
	st.info("You selected A")
else:
	st.info("You selected B")”

“city = st.selectbox("Your City", ["Napoli", "Palermo", "Catania"])”

# multiselect
“occupation = st.multiselect("Your Occupation", ["Programmer", "Data Scientist", "IT Consultant", "DBA"])”


“Inputting text and numbers”

“Name = st.text_input("Your Name", "Write something…")
st.text(name)”

“Age = st.number_input("Input a number")”


“message = st.text_area("Your Message", "Write something...")”

# Slider

“select_val = st.slider("Select a Value", 1, 10)”

# Balloons
“if st.button("Balloons"):
	st.balloons()”

# “Date, time, and more”

“import datetime
today = st.date_input("Today is",datetime.datetime.now())”
“import time
hour = st.time_input("The time is",datetime.time(12,30))”

“data = {"name":"John","surname":"Wick"}
st.json(data)”


























