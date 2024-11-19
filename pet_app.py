import streamlit as st
import requests

st.set_page_config(page_title="Pet app", page_icon="🐝")

st.header("Welcome to my Pet app!",
         divider="violet")

def get_bee_image():
    url= "https://cataas.com//cat"
    contents= requests.get(url)

    return contents.content

def get_dog_image_url():
    url="https://random.dog/woof.json"
    contents= requests.get(url).json()
    dog_image_url= contents["url"]

    return dog_image_url

c1, c2=st.columns(2)

with c1:
    bee_button = st.button("Click here for a bee image.")
    if bee_button:
        bee_image= get_bee_image()
        st.image(bee_image, width=300, caption= "My bee image")
with c2:
    dog_button = st.button("Click here for a dog image.")
    if dog_button:
        dog_image_url = get_dog_image_url()
        while dog_image_url[-4] == ".mp4":
            dog_image_url=get_dog_image_url()
        st.image(dog_image_url, width=300, caption="My dog image")