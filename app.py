import os
import io
import math
import wave
import struct
import base64
import streamlit as st
import streamlit.components.v1 as components

# =========================================================
# CONFIGURACIÓN GENERAL (SIN BARRA LATERAL)
# =========================================================
st.set_page_config(
    page_title="Interfaces Multimodales",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# GENERADORES DE SEÑALES MULTIMODALES (AUDIO Y HÁPTICA)
# =========================================================
def generar_tono_armonico(frecuencia=523.25, duracion=0.7, tasa_muestreo=22050):
    """Genera una muestra acústica armónica en memoria con envolvente suave (sin librerías pesadas)."""
    n_muestras = int(tasa_muestreo * duracion)
    buffer = io.BytesIO()
    with wave.open(buffer, 'wb') as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(tasa_muestreo)
        trama = bytearray()
        for i in range(n_muestras):
            t = i / tasa_muestreo
            envolvente = math.exp(-4.5 * t)
            # Tono fundamental + armónico superior
            onda = (0.7 * math.sin(2 * math.pi * frecuencia * t) + 0.3 * math.sin(4 * math.pi * frecuencia * t)) * envolvente
            muestra = int(max(min(onda, 1.0), -1.0) * 32767)
            trama.extend(struct.pack('<h', muestra))
        wav.writeframes(trama)
    return buffer.getvalue()

def disparar_vibracion_haptica():
    """Ejecuta vibración física real mediante la API del navegador en dispositivos compatibles."""
    components.html(
        """
        <script>
        if (window.navigator && window.navigator.vibrate) {
            window.navigator.vibrate([180, 80, 180, 80, 240]);
        }
        </script>
        """,
        height=0,
        width=0
    )

# =========================================================
# ESTILOS VISUALES ERGONÓMICOS Y BLOOM REACTIVO (GPU)
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=Montserrat:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

/* 1. Base oscura y limpia con prevención de fatiga ocular */
html, body, [data-testid="stAppViewContainer"], .stApp, section.main, .block-container {
    background-color: #07060a !important;
    color: #ded9e2 !important;
    font-family: 'Montserrat', sans-serif !important;
    overflow-x: hidden;
}

[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stSidebar"], section[data-testid="stSidebar"] { display: none !important; }

/* 2. Bloom ambiental interactivo en GPU que sigue al cursor en tiempo real */
body::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: radial-gradient(circle 380px at var(--mouse-x, 50vw) var(--mouse-y, 35vh), rgba(197, 160, 89, 0.16) 0%, rgba(120, 85, 150, 0.05) 50%, transparent 75%);
    pointer-events: none;
    z-index: 0;
    will-change: background;
}

/* 3. Contenedor proporcionado de lectura ergonómica */
.block-container {
    max-width: 980px !important;
    padding-top: 1.8rem !important;
    padding-bottom: 4rem !important;
    margin: 0 auto !important;
    position: relative;
    z-index: 10;
}

.brand-signature {
    text-align: center;
    font-family: 'Cinzel', serif;
    font-size: 0.72rem;
    letter-spacing: 0.22em;
    color: #c5a059;
    text-transform: uppercase;
    margin-bottom: 2px;
}

h1, h2, h3 {
    font-family: 'Cinzel', Georgia, serif !important;
    letter-spacing: 0.05em;
    color: #f3edf6 !important;
}

h1 {
    font-size: 2.1rem !important;
    font-weight: 600 !important;
    text-align: center;
    margin-bottom: 0.2rem !important;
    text-shadow: 0 0 25px rgba(197, 160, 89, 0.35);
}

.sub-lead {
    text-align: center;
    font-size: 0.95rem;
    color: #9d96a2;
    margin-bottom: 1.6rem;
    line-height: 1.6;
}

/* 4. Contenedores con contenido real integrado (sin cajas vacías) */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(18, 15, 24, 0.85) !important;
    border: 1px solid rgba(197, 160, 89, 0.25) !important;
    border-radius: 8px !important;
    padding: 1.2rem 1.4rem !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.55), inset 0 1px 0 rgba(255, 255, 255, 0.06) !important;
    backdrop-filter: blur(12px) !important;
    transition: border-color 0.25s ease, transform 0.2s ease, box-shadow 0.25s ease !important;
    margin-bottom: 0.8rem !important;
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    border-color: rgba(197, 160, 89, 0.5) !important;
    transform: translateY(-2px);
    box-shadow: 0 14px 40px rgba(0, 0, 0, 0.7), 0 0 20px rgba(197, 160, 89, 0.12) !important;
}

/* 5. Inputs y selectores con foco suave */
.stTextInput input, div[data-baseweb="select"] > div {
    background: rgba(11, 9, 15, 0.9) !important;
    color: #f3edf6 !important;
    border: 1px solid rgba(197, 160, 89, 0.28) !important;
    border-radius: 6px !important;
    font-family: 'Montserrat', sans-serif !important;
    transition: all 0.25s ease !important;
}

.stTextInput input:focus, div[data-baseweb="select"] > div:hover {
    border-color: #c5a059 !important;
    box-shadow: 0 0 15px rgba(197, 160, 89, 0.3) !important;
}

/* 6. Botones con respuesta táctil */
div.stButton > button {
    background: linear-gradient(135deg, #221c2a 0%, #120e17 100%) !important;
    color: #f3eff6 !important;
    border: 1px solid rgba(197, 160, 89, 0.45) !important;
    border-radius: 6px !important;
    font-family: 'Cinzel', serif !important;
    font-size: 0.88rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.06em !important;
    padding: 0.75rem 1.6rem !important;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.5) !important;
    transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

div.stButton > button:hover {
    transform: translateY(-2px) scale(1.02);
    border-color: #c5a059 !important;
    color: #ffffff !important;
    box-shadow: 0 10px 30px rgba(197, 160, 89, 0.4) !important;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# SEGUIMIENTO DEL CURSOR PARA EL BLOOM (CERO CONSUMO DE CPU)
# =========================================================
components.html(
    """
    <script>
    (function() {
        const pWin = window.parent;
        const pDoc = pWin.document;

        if (pWin.__KROV_BLOOM_ACTIVE__) return;
        pWin.__KROV_BLOOM_ACTIVE__ = true;

        pWin.addEventListener('mousemove', (e) => {
            pDoc.documentElement.style.setProperty('--mouse-x', e.clientX + 'px');
            pDoc.documentElement.style.setProperty('--mouse-y', e.clientY + 'px');
        }, { passive: true });
    })();
    </script>
    """,
    height=0,
    width=0
)

# =========================================================
# CARGA SEGURA DE LA IMAGEN
# =========================================================
image_data = ""
for img_name in ["Interfaces Mult2.png", "Interfaces_Mult2.png", "InterfacesMult2.png"]:
    if os.path.exists(img_name):
        try:
            with open(img_name, "rb") as file:
                image_data = base64.b64encode(file.read()).decode()
            break
        except Exception:
            pass

img_tag = f'<img class="image" src="data:image/png;base64,{image_data}">' if image_data else '<div style="margin-top:14px; font-size:2rem; color:#c5a059;">✦</div>'

# =========================================================
# LIENZO VISUAL CENTRAL
# =========================================================
html_canvas_box = f"""
<!DOCTYPE html>
<html>
<head>
<style>
* {{ box-sizing: border-box; }}
html, body {{
    margin: 0; padding: 0; width: 100%; height: 100%;
    overflow: hidden; background: transparent;
    font-family: 'Cinzel', Georgia, serif;
}}
#interface {{
    position: relative; width: 100%; height: 360px;
    background: radial-gradient(circle at 50% 50%, rgba(26, 21, 32, 0.9), rgba(10, 8, 14, 0.98));
    border: 1px solid rgba(197, 160, 89, 0.35); border-radius: 8px;
    box-shadow: 0 14px 40px rgba(0, 0, 0, 0.7);
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    overflow: hidden;
}}
#interface::before {{
    content: ""; position: absolute; inset: 0;
    background-image:
        linear-gradient(rgba(197,160,89,0.035) 1px, transparent 1px),
        linear-gradient(90deg, rgba(197,160,89,0.035) 1px, transparent 1px);
    background-size: 26px 26px; pointer-events: none;
}}
canvas {{ position: absolute; inset: 0; pointer-events: none; }}
.content {{ position: relative; z-index: 2; text-align: center; padding: 18px; }}
.title {{
    font-size: clamp(22px, 4vw, 38px); letter-spacing: 0.16em;
    color: #f3eff6; line-height: 1.25;
    text-shadow: 0 0 20px rgba(197, 160, 89, 0.3);
}}
.subtitle {{
    margin-top: 6px; font-family: 'Montserrat', sans-serif;
    font-size: 11px; letter-spacing: 0.28em;
    text-transform: uppercase; color: #c5a059;
}}
.image {{
    display: block; width: 130px; height: 130px;
    object-fit: contain; margin: 14px auto 0 auto;
    border: 1px solid rgba(197, 160, 89, 0.25); border-radius: 6px;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.6);
}}
.corner {{
    position: absolute; width: 16px; height: 16px;
    border: 1px solid #c5a059; z-index: 3; pointer-events: none;
}}
.top-left {{ top: 8px; left: 8px; border-right: none; border-bottom: none; }}
.top-right {{ top: 8px; right: 8px; border-left: none; border-bottom: none; }}
.bottom-left {{ bottom: 8px; left: 8px; border-right: none; border-top: none; }}
.bottom-right {{ bottom: 8px; right: 8px; border-left: none; border-top: none; }}
</style>
</head>
<body>
<div id="interface">
    <canvas id="particles"></canvas>
    <div class="corner top-left"></div>
    <div class="corner top-right"></div>
    <div class="corner bottom-left"></div>
    <div class="corner bottom-right"></div>
    <div class="content">
        <div class="title">HOLA<br>Mi nombre es Juan</div>
        <div class="subtitle">Interfaces multimodales</div>
        {img_tag}
    </div>
</div>
<script>
const canvas = document.getElementById("particles"), ctx = canvas.getContext("2d");
const box = document.getElementById("interface");
let w = canvas.width = box.clientWidth, h = canvas.height = box.clientHeight;
window.addEventListener("resize", () => {{ w = canvas.width = box.clientWidth; h = canvas.height = box.clientHeight; }});

let localPts = [];
box.addEventListener("mousemove", (e) => {{
    const r = box.getBoundingClientRect();
    if (localPts.length < 20) {{
        localPts.push({{
            x: e.clientX - r.left, y: e.clientY - r.top,
            vx: (Math.random() - 0.5) * 0.8, vy: (Math.random() - 0.5) * 0.8,
            life: 1.0
        }});
    }}
}});

function animLocal() {{
    ctx.clearRect(0, 0, w, h);
    for (let i = localPts.length - 1; i >= 0; i--) {{
        const p = localPts[i];
        p.x += p.vx; p.y += p.vy; p.life -= 0.03;
        if (p.life <= 0) {{ localPts.splice(i, 1); continue; }}
        ctx.beginPath();
        ctx.arc(p.x, p.y, 1.8, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(197, 160, 89, ${{p.life * 0.7}})`;
        ctx.fill();
    }}
    requestAnimationFrame(animLocal);
}}
animLocal();
</script>
</body>
</html>
"""

components.html(html_canvas_box, height=380)

# =========================================================
# CONTENIDO Y FLUJO MULTIMODAL (CONTENEDORES INTEGRADOS)
# =========================================================
st.markdown('<div class="brand-signature">Krov Industries · Sistemas Sensoriales</div>', unsafe_allow_html=True)
st.title("Interfaces multimodales")
st.markdown('<div class="sub-lead">Backend + frontend en una sola interfaz.<br>Explorando diferentes modalidades de interacción.</div>', unsafe_allow_html=True)

# Entrada de texto en tarjeta unificada
with st.container(border=True):
    texto = st.text_input("Texto de entrada", "Este es mi texto")
    st.caption(f"Valor en memoria: {texto}")

st.write("")

# Columnas con contenido contenido real adentro
col1, col2 = st.columns(2, gap="medium")

with col1:
    with st.container(border=True):
        st.subheader("Experiencia")
        st.write("Las interfaces multimodales mejoran la interacción natural entre usuarios y sistemas.")
        resp = st.checkbox("Estoy de acuerdo", value=True)
        if resp:
            st.success("Correcto.")

with col2:
    with st.container(border=True):
        st.subheader("Modalidad")
        modo = st.radio("Canal principal preferente:", ["Visual", "Auditiva", "Táctil"], horizontal=True)
        if modo == "Visual":
            st.write("La vista domina.")
        elif modo == "Auditiva":
            st.write("El audio domina.")
        else:
            st.write("El tacto domina.")

st.write("")

# Acciones con ejecución real (Audio armónico y Háptica física)
c_act, c_out = st.columns(2, gap="medium")

with c_act:
    with st.container(border=True):
        st.subheader("Acción")
        st.write("Ejecución manual de señal:")
        presionado = st.button("Presiona", use_container_width=True)
        if presionado:
            st.success("Gracias.")
            # Dispara tono armónico y vibración física
            st.audio(generar_tono_armonico(frecuencia=587.33, duracion=0.5), format="audio/wav", autoplay=True)
            disparar_vibracion_haptica()
        else:
            st.info("Sin acción.")

with c_out:
    with st.container(border=True):
        st.subheader("Salida")
        in_mod = st.selectbox("Modalidad activa:", ["Audio", "Visual", "Háptico"])

        if in_mod == "Audio":
            set_mod = "Reproducir audio"
            st.write("Acción:", set_mod)
            if st.button("Ejecutar señal de audio", use_container_width=True):
                st.audio(generar_tono_armonico(frecuencia=523.25, duracion=0.8), format="audio/wav", autoplay=True)
                st.success("Tono armónico reproducido en altavoces.")
        elif in_mod == "Visual":
            set_mod = "Reproducir video"
            st.write("Acción:", set_mod)
            if st.button("Ejecutar pulso óptico", use_container_width=True):
                st.info("Canal óptico activo: Desplegando señal luminosa.")
        else:
            set_mod = "Activar vibración"
            st.write("Acción:", set_mod)
            if st.button("Ejecutar vibración física", use_container_width=True):
                disparar_vibracion_haptica()
                st.success("Señal háptica enviada al dispositivo (patrón: 180ms - 80ms - 180ms).")
