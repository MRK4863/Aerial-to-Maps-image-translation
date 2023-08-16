import streamlit as st
import pickle
import streamlit as st
import pandas as pd
from PIL import Image

def generate_and_display_images(uploaded_file):
    if uploaded_file is not None:
        # st.image(uploaded_file)
        img = Image.open(uploaded_file)
        img = img.resize((256,256))
        col1, col2 = st.columns(2, gap = "small")
        with col1:
            st.image(img)
            st.markdown("Satellite Image")
        with col2:
            st.image(img)
            st.markdown("Mapview image")


if __name__ == "__main__":
    st.set_page_config(layout='centered',
                    page_title="Aerial to Map view translator")
    
    st.header("Map view Generator")

    st.markdown("#")
    uploaded_file = st.file_uploader("Upload your file here...", type=['png', 'jpg', 'jpeg'])
    print(type(uploaded_file))
    # StreamLit application
    
    if st.button("Generate..", use_container_width=True):
        generate_and_display_images(uploaded_file)

