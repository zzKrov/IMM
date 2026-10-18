import streamlit as st
import base64

# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================
st.set_page_config(
    page_title="Interfaces Multimodales // Krov Industries",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# ESTILOS VISUALES: MINIMALISMO BRONCE Y FLUIDOS SIN LAG
# =========================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=Montserrat:wght@300;400;500;600&display=swap');

html, body, [data-testid="stAppViewContainer"], .stApp {
    background-color: #070609 !important;
    color: #d8d3dc !important;
    font-family: 'Montserrat', sans-serif !important;
    overflow-x: hidden;
}

[data-testid="stHeader"] { background: transparent !important; }

/* Fondo líquido acelerado por GPU */
.stApp {
    background:
        radial-gradient(circle at 15% 20%, rgba(197, 160, 89, 0.14) 0%, transparent 40%),
        radial-gradient(circle at 85% 30%, rgba(120, 100, 150, 0.12) 0%, transparent 45%),
        linear-gradient(135deg, #070609 0%, #14111a 50%, #070609 100%) !important;
    background-size: 200% 200% !important;
    animation: bronzeLava 14s ease infinite alternate !important;
}

@keyframes bronzeLava {
    0% { background-position: 0% 0%; }
    50% { background-position: 100% 100%; }
    100% { background-position: 0% 100%; }
}

.brand-signature {
    text-align: center;
    font-family: 'Cinzel', serif;
    font-size: 0.75rem;
    letter-spacing: 0.2em;
    color: #c5a059;
    text-transform: uppercase;
}

h1, h2, h3 {
    font-family: 'Cinzel', serif !important;
    letter-spacing: 0.06em;
}

.main-title {
    font-size: 2rem;
    font-weight: 600;
    text-align: center;
    color: #f3eff6;
    margin-bottom: 0.2rem;
}

.sub-lead {
    text-align: center;
    color: #948f98;
    font-size: 0.95rem;
    margin-bottom: 1.5rem;
}

.greeting-card {
    background: rgba(18, 15, 24, 0.82);
    border: 1px solid rgba(197, 160, 89, 0.35);
    border-radius: 8px;
    padding: 24px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.6);
    margin-bottom: 1.5rem;
}

div.stButton > button {
    border-radius: 4px !important;
    font-family: 'Cinzel', serif !important;
    font-size: 0.85rem !important;
    letter-spacing: 0.08em !important;
    background: linear-gradient(135deg, #1f1a26, #0e0c12) !important;
    color: #e4dfe8 !important;
    border: 1px solid rgba(197, 160, 89, 0.4) !important;
    padding: 0.75rem 1.6rem !important;
    transition: all 0.25s ease !important;
}

div.stButton > button:hover {
    border-color: #c5a059 !important;
    box-shadow: 0 0 25px rgba(197, 160, 89, 0.45) !important;
    transform: translateY(-2px);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="brand-signature">Krov Industries · Sistemas Sensoriales</div>', unsafe_allow_html=True)
st.markdown('<div class="main-title">Interfaces Multimodales</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-lead">Integración de canales táctiles, visuales y sonoros</div>', unsafe_allow_html=True)

# Tarjeta de bienvenida original ("HOLA Mi nombre es Juan")
st.markdown(
    """
    <div class="greeting-card">
        <h2 style="color:#ffffff; margin:0 0 4px 0; font-size:1.8rem;">HOLA</h2>
        <div style="font-size:1.15rem; color:#e2d9cc; margin-bottom:12px;">Mi nombre es Juan</div>
        <div style="font-size:0.8rem; letter-spacing:0.25em; color:#c5a059; text-transform:uppercase;">
            Interfaces multimodales en acción
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

texto = st.text_input("Texto de entrada:", value="Exploración multimodal básica")

col1, col2 = st.columns(2, gap="medium")

with col1:
    st.subheader("Experiencia")
    st.write("Las interfaces multimodales mejoran la interacción natural con sistemas informáticos.")
    resp = st.checkbox("Estoy de acuerdo", value=True)
    if resp:
        st.success("Interacción confirmada.")

with col2:
    st.subheader("Modalidad")
    modo = st.radio("Canal principal:", ["Visual", "Auditiva", "Táctil"], horizontal=True)
    if modo == "Visual":
        st.write("Canal óptico dominante.")
    elif modo == "Auditiva":
        st.write("Canal acústico dominante.")
    else:
        st.write("Canal háptico dominante.")

st.write("")
st.subheader("Salida y Ejecución")
in_mod = st.selectbox("Acción deseada:", ["Audio", "Visual", "Háptico"])

if st.button("Ejecutar acción", use_container_width=True):
    salidas = {
        "Audio": "Reproduciendo respuesta acústica...",
        "Visual": "Desplegando elementos ópticos...",
        "Háptico": "Canal de vibración activado."
    }
    st.info(salidas.get(in_mod, "Acción completada."))

with st.sidebar:
    st.subheader("Configuración")
    st.radio("Modalidad preferente:", ["Visual", "Auditiva", "Háptica"])
