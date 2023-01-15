import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)

# st.write("# Open Programme Deliverables! 👋")

st.sidebar.success("Select an app above.")


image = Image.open('image.png')

st.image(image)
