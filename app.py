import streamlit as st
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from PIL import Image

st.set_page_config(
    page_title="Scanner con Cámara",
    page_icon="📷",
    layout="centered"
)

st.title("📷 Lector de Códigos de Barras")
st.caption("Escaneo usando cámara en Streamlit")

camera_image = st.camera_input("Escanear código")

if camera_image:
    # Convertir imagen
    image = Image.open(camera_image)
    image_np = np.array(image)
    image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    barcodes = decode(image_cv)

    st.image(image, caption="Imagen capturada", use_container_width=True)

    if barcodes:
        st.success("Código detectado ✔")

        for barcode in barcodes:
            data = barcode.data.decode("utf-8")
            code_type = barcode.type

            st.markdown("### 📊 Resultado")
            st.write(f"**Tipo:** {code_type}")
            st.write(f"**Contenido:** {data}")
    else:
        st.warning("No se detectó ningún código")
