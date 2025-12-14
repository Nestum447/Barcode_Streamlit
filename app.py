import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Scanner Barcode", page_icon="📷")

st.title("📷 Lector de Códigos de Barras")
st.info("Apunta la cámara al código. Funciona mejor con buena luz.")

html(
"""
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://unpkg.com/@zxing/library@latest"></script>
  <style>
    video {
      width: 100%;
      border-radius: 10px;
      border: 2px solid #4CAF50;
    }
    #result {
      font-size: 18px;
      margin-top: 10px;
      color: green;
      font-weight: bold;
    }
  </style>
</head>
<body>

<video id="video" muted autoplay playsinline></video>
<div id="result">Esperando código...</div>

<script>
  const codeReader = new ZXing.BrowserMultiFormatReader();
  const videoElement = document.getElementById('video');
  const resultElement = document.getElementById('result');

  navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } })
    .then(stream => {
      videoElement.srcObject = stream;
      videoElement.play();

      codeReader.decodeFromVideoElement(videoElement, (result, err) => {
        if (result) {
          resultElement.innerHTML =
            "📦 Tipo: " + result.format + "<br>" +
            "🔢 Código: " + result.text;
        }
      });
    })
    .catch(err => {
      resultElement.innerHTML = "❌ Error de cámara: " + err;
    });
</script>

</body>
</html>
""",
height=450
)
