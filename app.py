import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Scanner ZXing", page_icon="📷")

st.title("📷 Lector de Códigos de Barras")
st.caption("Compatible con Streamlit Cloud")

html("""
<!DOCTYPE html>
<html>
<head>
  <script src="https://unpkg.com/@zxing/library@latest"></script>
</head>
<body>
  <video id="video" width="300"></video>
  <p id="result"></p>

  <script>
    const codeReader = new ZXing.BrowserMultiFormatReader();
    const resultElem = document.getElementById('result');

    codeReader.decodeFromVideoDevice(null, 'video', (result, err) => {
      if (result) {
        resultElem.innerHTML = 
          "<b>Tipo:</b> " + result.format + "<br>" +
          "<b>Contenido:</b> " + result.text;
      }
    });
  </script>
</body>
</html>
""", height=400)
