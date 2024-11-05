import streamlit as st
import segno
import time

st.set_page_config(page_title= "Hi", page_icon="laughing")
st.image("images/IMG_1901.jpg")


st.title("QR Code Generator")

qr_url = st.text_input(label="Enter your link here:")

def generate_qrcode(qr_url):
    qrcode=segno.make_qr(qr_url)
    qrcode.save("images/qrcode_saved.png", scale=5)

if qr_url:
    with st.spinner("Generate QR Coe:"):
        time.sleep(2)
    generate_qrcode(qr_url)
    st.image("images/qrcode_saved.png", caption= qr_url)

st.markdown("MADE BY ALEXA")

#st.write(qr_url)