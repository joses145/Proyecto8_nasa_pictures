import requests
from getting_image import generate_image
import streamlit as st

API_key = "WpWBbXUsx77uCRYv3ferWvQIqQYKCvXgjMdLj9dK"

url = f"https://api.nasa.gov/planetary/apod?api_key={API_key}"

req = requests.get(url)
content = req.json()

print(content)

explanation = content["explanation"]
title = content["title"]
date = content["date"]
image_URL = content["url"]

generate_image(image_URL)

#st.set_page_config(layout="wide")

st.title(title)
st.subheader(date)
st.image("image.jpg", width=200)
st.write(explanation)
