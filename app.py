import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Barcode Scanner", page_icon="📷")

st.title("📷 Lector de Códigos de Barras")
st.write("Permite la cámara cuando el navegador lo solicite")

html(
"""
<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <script src="https://unpkg.com/@zxing/library@0.20.0"></script>

  <style>
    video {
      width: 100%;
      border-radius: 12px;
      border: 3px solid #4CAF50;
    }
    #status {
      margin-top: 10px;
      font-size: 18px;
      font-weight: bold;
    }
  </style>
</head>

<body>

<video id="video" autoplay muted playsinline></video>
<div id="status">📷 Esperando permiso de cámara…</div>

<script>
  const video = document.getElementById("video");
  const status = document.getElementById("status");

  const codeReader = new ZXing.BrowserMultiFormatReader();

  async function start() {
    try {
      status.innerText = "📷 Abriendo cámara…";

      await navigator.mediaDevices.getUserMedia({
        video: { facingMode: { exact: "environment" } }
      });

      codeReader.decodeFromVideoElement(video, (result, err) => {
        if (result) {
          if (navigator.vibrate) navigator.vibrate(200);

          status.innerHTML =
            "✅ <b>Tipo:</b> " + result.format + "<br>" +
            "🔢 <b>Código:</b> " + result.text;

          codeReader.reset();
        }
      });
    } catch (e) {
      status.innerText =
        "❌ No se pudo abrir la cámara. Usa Chrome y acepta permisos.";
    }
  }

  start();
</script>

</body>
</html>
""",
height=480
)
