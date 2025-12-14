import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Barcode Scanner", page_icon="📷")

st.title("📷 Lector de Códigos de Barras")
st.write("Pulsa el botón y apunta al código")

# 🔒 Evita re-render del componente
if "scanner_started" not in st.session_state:
    st.session_state.scanner_started = False

if not st.session_state.scanner_started:
    if st.button("▶️ Iniciar escaneo"):
        st.session_state.scanner_started = True
        st.experimental_rerun()
else:
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
      <div id="status">🔍 Escaneando…</div>

      <script>
        let codeReader;
        const video = document.getElementById("video");
        const status = document.getElementById("status");

        async function startScanner() {
          try {
            codeReader = new ZXing.BrowserMultiFormatReader();

            const devices = await ZXing.BrowserCodeReader.listVideoInputDevices();
            const backCamera = devices.find(d =>
              d.label.toLowerCase().includes("back") ||
              d.label.toLowerCase().includes("rear")
            ) || devices[0];

            codeReader.decodeFromVideoDevice(
              backCamera.deviceId,
              video,
              (result, err) => {
                if (result) {
                  if (navigator.vibrate) navigator.vibrate(200);

                  status.innerHTML =
                    "✅ <b>Tipo:</b> " + result.format + "<br>" +
                    "🔢 <b>Código:</b> " + result.text;

                  codeReader.reset();
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
