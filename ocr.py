import streamlit as st
from PIL import Image
import easyocr as ocr

st.set_page_config(layout="wide")
st.markdown('**_Optical Recognition app_ **')


hide_menu_style = """
        <style>
        #MainMenu,footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


sunset_imgs = [
    'CNIC.jpg'
    # 'contrast.jpg'
]
# indices_on_page, images_on_page = map(list, zip(sunset_imgs))
# st.image(sunset_imgs, width=10,caption=['CNIC Sample','CNIC Sample'],use_column_width=True)

if sunset_imgs is not None:
    for i in range(len(sunset_imgs)):
        image = Image.open(sunset_imgs[i])
        new_image = image.resize((200, 100))
        st.image(new_image, caption="CNIC Sample Image")
    
title_alignment = """
<style>
.css-1kyxreq {
  justify-content: center;
}
</style>
"""
st.markdown(title_alignment, unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose a file", type=['jpg','jpeg'], accept_multiple_files=False)
if uploaded_file is not None:
    st.write('file has been uploaded')
    img = Image.open(uploaded_file)
    img = img.resize((200, 150))
    st.image(img)
    reader = ocr.Reader(['en'])
    splits = reader.readtext(img, detail = 0, paragraph=False)
    st.json(splits)