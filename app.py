import streamlit as st
import streamlit.components.v1 as components

# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================
st.set_page_config(
    page_title="Interfaces Multimodales // Krov Industries",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# LÍNEA BASE VISUAL: BRONCE REAL Y FLUIDOS DE OBSIDIANA
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=Montserrat:wght@300;400;500;600&display=swap');

html, body, [data-testid="stAppViewContainer"], .stApp {
    background-color: #060508 !important;
    color: #d8d3dc !important;
    font-family: 'Montserrat', sans-serif !important;
    overflow-x: hidden;
}

[data-testid="stHeader"] { background: transparent !important; }

/* 1. Malla de gradiente suave */
.stApp {
    background: linear-gradient(135deg, #060508 0%, #15121c 30%, #201b2a 60%, #09080c 100%) !important;
    background-size: 300% 300% !important;
    animation: royalMesh 18s ease infinite alternate !important;
}

@keyframes royalMesh {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* 2. Fluidos orgánicos */
.fluid-bronze-1 {
    position: fixed;
    top: 15%;
    left: -120px;
    width: 500px;
    height: 500px;
    background: radial-gradient(circle, rgba(197, 160, 89, 0.12) 0%, transparent 70%);
    border-radius: 40% 60% 70% 30% / 50% 60% 40% 50%;
    filter: blur(85px);
    animation: bronzeDrift1 22s infinite alternate ease-in-out;
    pointer-events: none;
    z-index: 0;
}

.fluid-bronze-2 {
    position: fixed;
    bottom: 5%;
    right: -100px;
    width: 550px;
    height: 550px;
    background: radial-gradient(circle, rgba(140, 110, 170, 0.1) 0%, transparent 70%);
    border-radius: 60% 40% 50% 50% / 40% 50% 60% 50%;
    filter: blur(90px);
    animation: bronzeDrift2 25s infinite alternate ease-in-out;
    pointer-events: none;
    z-index: 0;
}

@keyframes bronzeDrift1 {
    0% { transform: translate(0, 0) scale(1); }
    50% { transform: translate(100px, 60px) scale(1.15); }
    100% { transform: translate(30px, 120px) scale(0.95); }
}

@keyframes bronzeDrift2 {
    0% { transform: translate(0, 0) scale(1); }
    50% { transform: translate(-90px, -70px) scale(1.2); }
    100% { transform: translate(-20px, -110px) scale(0.9); }
}

.brand-signature {
    text-align: center;
    font-family: 'Cinzel', serif;
    font-size: 0.75rem;
    letter-spacing: 0.2em;
    color: #c5a059;
    text-transform: uppercase;
    margin-bottom: 2px;
}

h1, h2, h3 {
    font-family: 'Cinzel', serif !important;
    letter-spacing: 0.06em;
}

.main-title {
    font-size: 2.1rem;
    font-weight: 600;
    text-align: center;
    color: #f3eff6;
    margin-bottom: 0.2rem;
    text-shadow: 0 0 25px rgba(197, 160, 89, 0.35);
}

.sub-lead {
    text-align: center;
    color: #948f98;
    font-size: 0.95rem;
    margin-bottom: 1.8rem;
}

.interface-frame {
    background: rgba(16, 14, 22, 0.85);
    border: 1px solid rgba(197, 160, 89, 0.3);
    border-radius: 8px;
    padding: 24px;
    backdrop-filter: blur(14px);
    box-shadow: 0 12px 35px rgba(0, 0, 0, 0.6);
    margin-bottom: 20px;
}

div.stButton > button {
    border-radius: 4px !important;
    font-family: 'Cinzel', serif !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.08em !important;
    background: linear-gradient(135deg, #1c1724, #0f0c14) !important;
    color: #e4dfe8 !important;
    border: 1px solid rgba(197, 160, 89, 0.4) !important;
    padding: 0.75rem 1.6rem !important;
    transition: all 0.25s ease !important;
}

div.stButton > button:hover {
    border-color: #c5a059 !important;
    box-shadow: 0 0 25px rgba(197, 160, 89, 0.35) !important;
    transform: translateY(-2px);
}
</style>

<div class="fluid-bronze-1"></div>
<div class="fluid-bronze-2"></div>
""", unsafe_allow_html=True)

st.markdown('<div class="brand-signature">Krov Industries · Sistemas Sensoriales</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">Interfaces Multimodales</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-lead">Exploración de canales táctiles, visuales y acústicos en una única superficie de interacción</div>', unsafe_allow_html=True)

# =========================================================
# LIENZO VISUAL CON PARTÍCULAS
# =========================================================
html_canvas = """
<!DOCTYPE html>
<html>
<head>
<style>
body { margin: 0; background: transparent; overflow: hidden; }
#box {
    position: relative; width: 100%; height: 260px;
    background: radial-gradient(circle at 50% 50%, rgba(32, 27, 42, 0.8), rgba(11, 9, 15, 0.95));
    border: 1px solid rgba(197, 160, 89, 0.35); border-radius: 8px;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
}
canvas { position: absolute; inset: 0; pointer-events: none; }
.title { font-family: 'Cinzel', Georgia, serif; font-size: 24px; color: #f3eff6; letter-spacing: 0.15em; z-index: 2; text-align: center; }
.sub { font-family: 'Montserrat', sans-serif; font-size: 11px; color: #c5a059; letter-spacing: 0.25em; text-transform: uppercase; margin-top: 6px; z-index: 2; }
</style>
</head>
<body>
<div id="box">
    <canvas id="c"></canvas>
    <div class="title">INTERACCIÓN INTEGRADA</div>
    <div class="sub">CANAL VISUAL · AUDITIVO · HÁPTICO</div>
</div>
<script>
const c = document.getElementById('c'), ctx = c.getContext('2d'), box = document.getElementById('box');
let w = c.width = box.clientWidth, h = c.height = box.clientHeight;
window.addEventListener('resize', () => { w = c.width = box.clientWidth; h = c.height = box.clientHeight; });
const pts = [];
box.addEventListener('mousemove', (e) => {
    const r = box.getBoundingClientRect();
    for(let i=0; i<2; i++) {
        pts.push({ x: e.clientX - r.left, y: e.clientY - r.top, vx: (Math.random()-0.5)*1.2, vy: (Math.random()-0.5)*1.2, a: 1 });
    }
});
function loop() {
    ctx.clearRect(0,0,w,h);
    for(let i=pts.length-1; i>=0; i--) {
        const p = pts[i]; p.x += p.vx; p.y += p.vy; p.a -= 0.025;
        if(p.a <= 0) { pts.splice(i,1); continue; }
        ctx.beginPath(); ctx.arc(p.x, p.y, 2, 0, Math.PI*2);
        ctx.fillStyle = `rgba(197, 160, 89, ${p.a})`; ctx.fill();
    }
    requestAnimationFrame(loop);
}
loop();
</script>
</body>
</html>
"""
components.html(html_canvas, height=280)

# =========================================================
# CONTROLES Y CANALES MULTIMODALES
# =========================================================
c_left, c_right = st.columns([1.1, 1], gap="large")

with c_left:
    st.markdown('<div class="interface-frame">', unsafe_allow_html=True)
    st.markdown("### 1. Parámetros de Entrada")
    texto = st.text_input("Mensaje contextual:", value="Exploración sensorial continua")
    st.caption(f"Valor registrado: {texto}")
    
    st.write("")
    acepta = st.checkbox("Habilitar canal háptico complementario", value=True)
    if acepta:
        st.info("Respuesta táctil y háptica habilitada para dispositivos compatibles.")
    st.markdown('</div>', unsafe_allow_html=True)

with c_right:
    st.markdown('<div class="interface-frame">', unsafe_allow_html=True)
    st.markdown("### 2. Modulación de Salida")
    modo = st.radio("Canal principal preferente:", ["Visual", "Auditiva", "Háptica"], horizontal=True)
    
    salida_tipo = st.selectbox("Modo de respuesta:", ["Reproducir audio ambiental", "Desplegar interfaz óptica", "Activar vibración táctil"])
    
    st.write("")
    if st.button("Ejecutar acción multimodal", use_container_width=True):
        st.success(f"Canal activo: {modo} // Salida: {salida_tipo}")
    st.markdown('</div>', unsafe_allow_html=True)
