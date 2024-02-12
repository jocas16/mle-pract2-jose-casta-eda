import streamlit as st
from utils import generate_image, classify_image

# Inicializar Streamlit
st.title('Generación y Clasificación de Imágenes')

# Dividir la pantalla en dos columnas
col1, col2 = st.columns([1, 1])

# Sección de Generación de Imágenes (col1)
with col1:
    st.title('Generación de Imágenes')
    input_text_generation = st.text_input('Ingrese la solicitud de generación de imágenes')

    if st.button('Mostrar Imagen'):
        image_link = generate_image(input_text_generation)
        st.image(image_link, caption='Imagen Mostrada')

# Sección de Clasificación de Imágenes (col2)
with col2:
    st.title('Clasificación de Imágenes')
    uploaded_file = st.file_uploader('Cargar imagen para clasificación')

    if uploaded_file is not None:
        predicted_class = classify_image(uploaded_file)
        st.write('Imagen clasificada como:', predicted_class)
        
