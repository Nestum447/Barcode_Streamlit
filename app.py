import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Barcode Scanner", page_icon="📷")

st.title("📷 Lector de Códigos de Barras")
st.write("Al detectar un código, el teléfono vibrará 📳")

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
<div id="status">📷 Inicializando cámara…</div>

<script>
  const status = document.getElementById("status");
  const video = document.getElementById("video");

  const codeReader = new ZXing.BrowserMultiFormatReader();

  async function startScanner() {
    try {
      const devices = await ZXing.BrowserCodeReader.listVideoInputDevices();

      const backCamera = devices.find(d =>
        d.label.toLowerCase().includes("back") ||
        d.label.toLowerCase().includes("rear")
      ) || devices[0];

      status.innerText = "🔍 Escaneando…";

      codeReader.decodeFromVideoDevice(
        backCamera.deviceId,
        video,
        (result, err) => {
          if (result) {
            // 📳 VIBRAR
            if (navigator.vibrate) {
              navigator.vibrate([200, 100, 200]); // patrón
            }

            status.innerHTML =
              "✅ <b>Tipo:</b> " + result.format + "<br>" +
              "🔢 <b>Código:</b> " + result.text;

            codeReader.reset(); // detener escaneo
          }
        }
      );
    } catch (e) {
      status.innerText = "❌ Error cámara: " + e;
    }
  }

  startScanner();
</script>

</body>
</html>
""",
height=500
)
