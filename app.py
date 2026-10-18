import os
import base64
import streamlit as st
import streamlit.components.v1 as components

# =========================================================
# CONFIGURACIÓN GENERAL (SIN SIDEBAR)
# =========================================================
st.set_page_config(
    page_title="Interfaces Multimodales",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# ESTILOS VISUALES ERGONÓMICOS Y PROPORCIONES UX/UI
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700&family=Montserrat:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

/* 1. Transparencia total para dejar visible el fondo interactivo con bloom */
html, body, [data-testid="stAppViewContainer"], .stApp, section.main, .block-container {
    background: transparent !important;
    background-color: transparent !important;
    color: #e2dce6 !important;
    font-family: 'Montserrat', sans-serif !important;
    overflow-x: hidden;
}

body {
    background-color: #08070d !important;
}

[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stSidebar"], section[data-testid="stSidebar"] { display: none !important; }

/* 2. Contenedor principal con proporciones áureas de lectura (max 960px) */
.block-container {
    max-width: 960px !important;
    padding-top: 2rem !important;
    padding-bottom: 4rem !important;
    margin: 0 auto !important;
    position: relative;
    z-index: 10;
}

/* 3. Tipografía refinada */
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
    color: #f4eff8 !important;
}

h1 {
    font-size: 2.1rem !important;
    font-weight: 600 !important;
    text-align: center;
    margin-bottom: 0.2rem !important;
    text-shadow: 0 0 30px rgba(197, 160, 89, 0.35);
}

.sub-lead {
    text-align: center;
    font-size: 0.95rem;
    color: #a59fa9;
    margin-bottom: 1.8rem;
    line-height: 1.6;
}

/* 4. Tarjetas táctiles ergonómicas */
.interactive-panel {
    background: rgba(18, 16, 24, 0.82);
    border: 1px solid rgba(197, 160, 89, 0.25);
    border-radius: 8px;
    padding: 1.4rem 1.6rem;
    backdrop-filter: blur(14px);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6), inset 0 1px 0 rgba(255, 255, 255, 0.08);
    transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
    margin-bottom: 1rem;
}

.interactive-panel:hover {
    transform: translateY(-2px);
    border-color: rgba(197, 160, 89, 0.55);
    box-shadow: 0 14px 40px rgba(0, 0, 0, 0.7), 0 0 25px rgba(197, 160, 89, 0.15);
}

/* 5. Inputs y selectores pulidos */
.stTextInput input {
    background: rgba(12, 11, 16, 0.9) !important;
    color: #f3eff6 !important;
    border: 1px solid rgba(197, 160, 89, 0.3) !important;
    border-radius: 6px !important;
    font-family: 'Montserrat', sans-serif !important;
    padding: 10px 14px !important;
    transition: all 0.25s ease !important;
}

.stTextInput input:focus {
    border-color: #c5a059 !important;
    box-shadow: 0 0 20px rgba(197, 160, 89, 0.3) !important;
}

/* 6. Botones con respuesta háptica visual */
div.stButton > button {
    background: linear-gradient(135deg, #221c2c 0%, #120f18 100%) !important;
    color: #f3eff6 !important;
    border: 1px solid rgba(197, 160, 89, 0.45) !important;
    border-radius: 6px !important;
    font-family: 'Cinzel', serif !important;
    font-size: 0.88rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.08em !important;
    padding: 0.75rem 1.6rem !important;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.5) !important;
    transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

div.stButton > button:hover {
    transform: translateY(-2px) scale(1.02);
    border-color: #c5a059 !important;
    color: #ffffff !important;
    box-shadow: 0 10px 30px rgba(197, 160, 89, 0.35) !important;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# FONDO INTERACTIVO REAL: BLOOM Y RESPUESTA AL CURSOR (GPU)
# =========================================================
components.html(
    """
    <script>
    (function() {
        const pWin = window.parent;
        const pDoc = pWin.document;

        if (pWin.__KROV_MULTIMODAL_BG__) return;
        pWin.__KROV_MULTIMODAL_BG__ = true;

        let canvas = pDoc.getElementById('interactive-bloom-canvas');
        if (!canvas) {
            canvas = pDoc.createElement('canvas');
            canvas.id = 'interactive-bloom-canvas';
            canvas.style.cssText = 'position:fixed;top:0;left:0;width:100vw;height:100vh;pointer-events:none;z-index:0;background:#08070d;';
            pDoc.body.prepend(canvas);
        }

        const ctx = canvas.getContext('2d');
        let w = canvas.width = pWin.innerWidth;
        let h = canvas.height = pWin.innerHeight;

        pWin.addEventListener('resize', () => {
            w = canvas.width = pWin.innerWidth;
            h = canvas.height = pWin.innerHeight;
        });

        // Posición real y suavizada del cursor para el Bloom
        let mouse = { x: w * 0.5, y: h * 0.35 };
        let smoothMouse = { x: w * 0.5, y: h * 0.35 };

        pWin.addEventListener('mousemove', (e) => {
            mouse.x = e.clientX;
            mouse.y = e.clientY;
        });

        // Partículas motas ambientales en suspensión suave
        const particles = [];
        for (let i = 0; i < 35; i++) {
            particles.push({
                x: Math.random() * w,
                y: Math.random() * h,
                r: Math.random() * 2 + 1,
                vx: (Math.random() - 0.5) * 0.4,
                vy: (Math.random() - 0.5) * 0.4,
                baseAlpha: Math.random() * 0.4 + 0.2
            });
        }

        function render() {
            // Suavizado cinemático del cursor (lerp)
            smoothMouse.x += (mouse.x - smoothMouse.x) * 0.08;
            smoothMouse.y += (mouse.y - smoothMouse.y) * 0.08;

            ctx.clearRect(0, 0, w, h);
            ctx.fillStyle = '#08070d';
            ctx.fillRect(0, 0, w, h);

            // 1. BLOOM INTERACTIVO: Luz suave que sigue el puntero
            ctx.globalCompositeOperation = 'screen';
            const bloomGrad = ctx.createRadialGradient(
                smoothMouse.x, smoothMouse.y, 10,
                smoothMouse.x, smoothMouse.y, 340
            );
            bloomGrad.addColorStop(0, 'rgba(197, 160, 89, 0.22)');
            bloomGrad.addColorStop(0.4, 'rgba(125, 90, 160, 0.10)');
            bloomGrad.addColorStop(1, 'transparent');

            ctx.fillStyle = bloomGrad;
            ctx.beginPath();
            ctx.arc(smoothMouse.x, smoothMouse.y, 340, 0, Math.PI * 2);
            ctx.fill();

            // 2. Halo de fondo secundario con respiración suave
            const ambientGrad = ctx.createRadialGradient(w * 0.5, h * 0.2, 50, w * 0.5, h * 0.2, 600);
            ambientGrad.addColorStop(0, 'rgba(30, 24, 38, 0.8)');
            ambientGrad.addColorStop(1, 'transparent');
            ctx.fillStyle = ambientGrad;
            ctx.fillRect(0, 0, w, h);

            // 3. Motes de polvo dorado interactivos
            for (let p of particles) {
                p.x += p.vx;
                p.y += p.vy;

                if (p.x < 0) p.x = w;
                if (p.x > w) p.x = 0;
                if (p.y < 0) p.y = h;
                if (p.y > h) p.y = 0;

                // Reacción al pasar cerca del cursor
                const d = Math.hypot(p.x - smoothMouse.x, p.y - smoothMouse.y);
                let alpha = p.baseAlpha;
                if (d < 160) {
                    alpha = Math.min(1.0, p.baseAlpha + (1 - d / 160) * 0.6);
                    p.x += (p.x - smoothMouse.x) * 0.02;
                    p.y += (p.y - smoothMouse.y) * 0.02;
                }

                ctx.beginPath();
                ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
                ctx.fillStyle = `rgba(215, 195, 155, ${alpha})`;
                ctx.shadowBlur = 8;
                ctx.shadowColor = '#c5a059';
                ctx.fill();
            }

            ctx.globalCompositeOperation = 'source-over';
            requestAnimationFrame(render);
        }
        render();
    })();
    </script>
    """,
    height=0,
    width=0
)

# =========================================================
# CARGA SEGURA DE LA IMAGEN ORIGINAL
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

# Si la imagen existe la embebemos; de lo contrario desplegamos insignia geométrica limpia
if image_data:
    img_tag = f'<img class="image" src="data:image/png;base64,{image_data}">'
else:
    img_tag = '<div style="margin-top:16px; font-size:2.2rem; color:#c5a059;">✦</div>'

# =========================================================
# LIENZO DE BIENVENIDA MULTIMODAL CON INTERACCIÓN TÁCTIL
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
    position: relative; width: 100%; height: 380px;
    background: radial-gradient(circle at 50% 50%, rgba(25, 20, 32, 0.88), rgba(10, 8, 14, 0.96));
    border: 1px solid rgba(197, 160, 89, 0.35); border-radius: 8px;
    box-shadow: 0 15px 45px rgba(0, 0, 0, 0.7), inset 0 0 50px rgba(197, 160, 89, 0.05);
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    overflow: hidden;
}}

#interface::before {{
    content: ""; position: absolute; inset: 0;
    background-image:
        linear-gradient(rgba(197,160,89,0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(197,160,89,0.04) 1px, transparent 1px);
    background-size: 28px 28px; pointer-events: none;
}}

canvas {{ position: absolute; inset: 0; pointer-events: none; }}

.content {{
    position: relative; z-index: 2; text-align: center; padding: 20px;
}}

.title {{
    font-size: clamp(24px, 4.5vw, 42px); letter-spacing: 0.16em;
    color: #f3eff6; line-height: 1.25;
    text-shadow: 0 0 20px rgba(197, 160, 89, 0.35);
}}

.subtitle {{
    margin-top: 6px; font-family: 'Montserrat', sans-serif;
    font-size: 11px; letter-spacing: 0.3em;
    text-transform: uppercase; color: #c5a059;
}}

.image {{
    display: block; width: 140px; height: 140px;
    object-fit: contain; margin: 16px auto 0 auto;
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
    for (let i = 0; i < 2; i++) {{
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
        p.x += p.vx; p.y += p.vy; p.life -= 0.025;
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

components.html(html_canvas_box, height=400)

# =========================================================
# CONTENIDO Y FLUJO MULTIMODAL PRINCIPAL
# =========================================================
st.markdown('<div class="brand-signature">Krov Industries · Interacción Sensorial</div>', unsafe_allow_html=True)
st.title("Interfaces multimodales")
st.markdown('<div class="sub-lead">Backend + frontend en una sola interfaz.<br>Explorando diferentes modalidades de interacción.</div>', unsafe_allow_html=True)

# Entrada de texto
texto = st.text_input("Texto", "Este es mi texto")
st.caption(f"Registro en tiempo real: {texto}")

st.write("")

# Columnas de modalidades con proporciones ergonómicas
col1, col2 = st.columns(2, gap="medium")

with col1:
    st.markdown('<div class="interactive-panel">', unsafe_allow_html=True)
    st.subheader("Experiencia")
    st.write("Las interfaces multimodales mejoran la interacción natural entre personas y sistemas.")
    resp = st.checkbox("Estoy de acuerdo", value=True)
    if resp:
        st.success("Respuesta registrada: Correcto.")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="interactive-panel">', unsafe_allow_html=True)
    st.subheader("Modalidad")
    modo = st.radio("Canal principal preferente:", ["Visual", "Auditiva", "Táctil"], horizontal=True)

    if modo == "Visual":
        st.write("La vista domina la interacción.")
    elif modo == "Auditiva":
        st.write("El audio domina la interacción.")
    else:
        st.write("El tacto domina la interacción.")
    st.markdown('</div>', unsafe_allow_html=True)

# Sección de Acción y Salida
c_act, c_out = st.columns([1, 1], gap="medium")

with c_act:
    st.markdown('<div class="interactive-panel">', unsafe_allow_html=True)
    st.subheader("Acción")
    st.write("Comprobación de respuesta activa:")
    if st.button("Presiona", use_container_width=True):
        st.success("Gracias.")
    else:
        st.info("Sin acción ejecutada.")
    st.markdown('</div>', unsafe_allow_html=True)

with c_out:
    st.markdown('<div class="interactive-panel">', unsafe_allow_html=True)
    st.subheader("Salida")
    in_mod = st.selectbox("Modalidad de respuesta:", ["Audio", "Visual", "Háptico"])

    if in_mod == "Audio":
        set_mod = "Reproducir audio"
    elif in_mod == "Visual":
        set_mod = "Reproducir video"
    else:
        set_mod = "Activar vibración"

    st.write("Acción en cola:", set_mod)
    st.markdown('</div>', unsafe_allow_html=True)
