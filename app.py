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
# SÍNTESIS DE SEÑALES MULTIMODALES REALES (AUDIO Y HÁPTICA)
# =========================================================
def generar_tono_acustico(frecuencia=587.33, duracion=0.6, tasa_muestreo=22050):
    """Genera en memoria una muestra acústica armónica pura (sin dependencias externas)."""
    n_muestras = int(tasa_muestreo * duracion)
    buffer = io.BytesIO()
    with wave.open(buffer, 'wb') as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(tasa_muestreo)
        trama = bytearray()
        for i in range(n_muestras):
            t = i / tasa_muestreo
            envolvente = math.exp(-4.2 * t)
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
# ESTILOS VISUALES: FONDO LÍQUIDO, BLOOM INTERACTIVO Y FLASH NEÓN
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=Montserrat:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

/* 1. Transparencia total de contenedores para permitir el paso de la luz */
html, body {
    background-color: #07060a !important;
    margin: 0;
    padding: 0;
}

[data-testid="stAppViewContainer"], .stApp, section.main, .block-container, [data-testid="stHeader"] {
    background: transparent !important;
    background-color: transparent !important;
    color: #ded9e2 !important;
    font-family: 'Montserrat', sans-serif !important;
    overflow-x: hidden;
}

[data-testid="stSidebar"], section[data-testid="stSidebar"] { display: none !important; }

/* 2. Base líquida con orbes en movimiento continuo en GPU */
.stApp {
    background: radial-gradient(circle at 50% 25%, #15111d 0%, #07060a 100%) !important;
}

.stApp::after {
    content: '';
    position: fixed;
    width: 600px;
    height: 600px;
    top: 15%;
    left: 20%;
    background: radial-gradient(circle, rgba(197, 160, 89, 0.14) 0%, rgba(120, 80, 160, 0.06) 50%, transparent 75%);
    border-radius: 50%;
    filter: blur(80px);
    pointer-events: none;
    z-index: 0;
    animation: orbLavaDrift 20s ease-in-out infinite alternate;
}

@keyframes orbLavaDrift {
    0% { transform: translate3d(0, 0, 0) scale(1); }
    50% { transform: translate3d(140px, 80px, 0) scale(1.15); }
    100% { transform: translate3d(-80px, 160px, 0) scale(0.92); }
}

/* 3. BLOOM INTERACTIVO REAL: Sigue al cursor con resplandor en pantalla completa */
.stApp::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: radial-gradient(circle 420px at var(--mx, 50vw) var(--my, 40vh), rgba(197, 160, 89, 0.22) 0%, rgba(140, 95, 175, 0.08) 45%, transparent 75%);
    pointer-events: none;
    z-index: 1;
    mix-blend-mode: screen;
    will-change: background;
}

/* 4. DESTELLO NEÓN SUAVE EN TODA LA PANTALLA (PULSO ÓPTICO) */
@keyframes fullScreenNeonPulse {
    0% {
        opacity: 0;
        transform: scale(0.98);
    }
    25% {
        opacity: 0.85;
        transform: scale(1);
    }
    100% {
        opacity: 0;
        transform: scale(1.02);
    }
}

.screen-neon-flash {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: radial-gradient(
        circle at center,
        rgba(212, 175, 55, 0.45) 0%,
        rgba(168, 85, 247, 0.32) 45%,
        rgba(0, 240, 255, 0.2) 75%,
        rgba(7, 6, 10, 0.75) 100%
    );
    mix-blend-mode: screen;
    box-shadow: inset 0 0 140px rgba(197, 160, 89, 0.8), 0 0 90px rgba(0, 240, 255, 0.5);
    pointer-events: none;
    z-index: 9999999;
    animation: fullScreenNeonPulse 1.1s cubic-bezier(0.1, 0.9, 0.2, 1) forwards;
}

/* 5. Contenedor principal y proporciones UX */
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

/* 6. Contenedores nativos con cristalización */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(18, 15, 24, 0.86) !important;
    border: 1px solid rgba(197, 160, 89, 0.28) !important;
    border-radius: 8px !important;
    padding: 1.2rem 1.4rem !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.55), inset 0 1px 0 rgba(255, 255, 255, 0.06) !important;
    backdrop-filter: blur(14px) !important;
    transition: border-color 0.25s ease, transform 0.2s ease, box-shadow 0.25s ease !important;
    margin-bottom: 0.8rem !important;
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    border-color: rgba(197, 160, 89, 0.55) !important;
    transform: translateY(-2px);
    box-shadow: 0 14px 40px rgba(0, 0, 0, 0.7), 0 0 20px rgba(197, 160, 89, 0.15) !important;
}

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
# SENSOR DE RATÓN: ACTUALIZA EL BLOOM SIN CONSUMIR CPU
# =========================================================
components.html(
    """
    <script>
    (function() {
        const pWin = window.parent;
        const pDoc = pWin.document;

        function updateBloom(e) {
            pDoc.documentElement.style.setProperty('--mx', e.clientX + 'px');
            pDoc.documentElement.style.setProperty('--my', e.clientY + 'px');
        }

        pWin.removeEventListener('mousemove', pWin.__KROV_BLOOM_HANDLER__);
        pWin.__KROV_BLOOM_HANDLER__ = updateBloom;
        pWin.addEventListener('mousemove', updateBloom, { passive: true });

        // Coordenadas iniciales centradas
        pDoc.documentElement.style.setProperty('--mx', (pWin.innerWidth / 2) + 'px');
        pDoc.documentElement.style.setProperty('--my', (pWin.innerHeight / 3) + 'px');
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
# CONTENIDO Y FLUJO MULTIMODAL
# =========================================================
st.markdown('<div class="brand-signature">Krov Industries · Sistemas Sensoriales</div>', unsafe_allow_html=True)
st.title("Interfaces multimodales")
st.markdown('<div class="sub-lead">Backend + frontend en una sola interfaz.<br>Explorando diferentes modalidades de interacción.</div>', unsafe_allow_html=True)

# Entrada de texto en contenedor sólido
with st.container(border=True):
    texto = st.text_input("Texto de entrada", "Este es mi texto")
    st.caption(f"Valor en memoria: {texto}")

st.write("")

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

# Acciones con ejecución real (Audio armónico, Pulso óptico con flash y Háptica física)
c_act, c_out = st.columns(2, gap="medium")

with c_act:
    with st.container(border=True):
        st.subheader("Acción")
        st.write("Ejecución manual de señal integral:")
        presionado = st.button("Presiona", use_container_width=True)
        if presionado:
            st.success("Señal multimodal emitida (Audio + Háptica + Flash óptico).")
            # Dispara destello neón en toda la pantalla
            st.markdown('<div class="screen-neon-flash"></div>', unsafe_allow_html=True)
            # Tono armónico
            st.audio(generar_tono_acustico(frecuencia=587.33, duracion=0.5), format="audio/wav", autoplay=True)
            # Vibración háptica
            disparar_vibracion_haptica()
        else:
            st.info("Sin acción ejecutada.")

with c_out:
    with st.container(border=True):
        st.subheader("Salida")
        in_mod = st.selectbox("Modalidad activa:", ["Audio", "Visual", "Háptico"])

        if in_mod == "Audio":
            set_mod = "Reproducir audio"
            st.write("Acción:", set_mod)
            if st.button("Ejecutar señal de audio", use_container_width=True):
                st.audio(generar_tono_acustico(frecuencia=523.25, duracion=0.8), format="audio/wav", autoplay=True)
                st.success("Tono armónico reproducido.")
        elif in_mod == "Visual":
            set_mod = "Reproducir video"
            st.write("Acción:", set_mod)
            if st.button("Ejecutar pulso óptico", use_container_width=True):
                # Destello neón suave en toda la pantalla
                st.markdown('<div class="screen-neon-flash"></div>', unsafe_allow_html=True)
                st.success("Pulso óptico emitido: Destello neón activo en toda la pantalla.")
        else:
            set_mod = "Activar vibración"
            st.write("Acción:", set_mod)
            if st.button("Ejecutar vibración física", use_container_width=True):
                disparar_vibracion_haptica()
                st.success("Señal háptica enviada al dispositivo (180ms - 80ms - 180ms).")
