import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Scanner Barcode", page_icon="📷")

st.title("📷 Lector de Códigos de Barras")
st.success("Compatible con Streamlit Cloud")

html("""
<!DOCTYPE html>
<html>
<head>
  <script src="https://unpkg.com/@zxing/library@latest"></script>
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>

<video id="video" autoplay muted playsinline></video>
<p id="result">Esperando código...</p>

<script>
const codeReader = new ZXing.BrowserMultiFormatReader();

navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } })
  .then(stream => {
    const video = document.getElementById('video');
    video.srcObject = stream;
    video.play();

    codeReader.decodeFromVideoElement(video, (result, err) => {
      if (result) {
        document.getElementById('result').innerHTML =
          "<b>Tipo:</b> " + result.format + "<br>" +
          "<b>Código:</b> " + result.text;
      }
    });
  })
  .catch(err => {
    document.getElementById('result').innerText =
      "Error cámara: " + err;
  });
</script>

</body>
</html>
""", height=420)
