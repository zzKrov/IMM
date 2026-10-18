import streamlit as st
import streamlit.components.v1 as components
import base64


# =========================================================
# CONFIG
# =========================================================

st.set_page_config(
    page_title="Interfaces Multimodales",
    page_icon="✦",
    layout="wide"
)


# =========================================================
# GLOBAL STYLE
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600&family=Montserrat:wght@300;400;500&display=swap');

.stApp {
    background:
        radial-gradient(
            circle at 50% 0%,
            #1c1920,
            #0a090c 55%,
            #050507 100%
        );

    color: #d8d3dc;
}

.block-container {
    max-width: 1100px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    font-family: 'Cinzel', Georgia, serif !important;
    font-weight: 500 !important;
    letter-spacing: 0.06em;
}

h1 {
    font-size: 1.65rem !important;
}

h2 {
    font-size: 1.15rem !important;
}

h3 {
    font-size: 0.95rem !important;
}

p, label {
    font-family: 'Montserrat', sans-serif !important;
    font-size: 0.82rem !important;
    color: #aaa4ae;
}

.stTextInput input {
    background: #0e0d11 !important;
    color: #ddd9e0 !important;
    border: 1px solid #302c35 !important;
    border-radius: 3px !important;
    font-family: 'Montserrat', sans-serif !important;
}

.stButton > button {
    background: linear-gradient(180deg, #18151c, #0e0d11);
    color: #dcd6df;
    border: 1px solid #39333f;
    border-radius: 3px;
    font-family: 'Cinzel', serif;
    letter-spacing: 0.08em;
}

.stButton > button:hover {
    border-color: #80738b;
    background: #211c25;
}

[data-testid="column"] {
    background: rgba(255,255,255,0.018);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 3px;
    padding: 1rem 1.1rem;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #09080c, #100e14);
    border-right: 1px solid #27232c;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# IMAGE
# =========================================================

with open("Interfaces Mult2.png", "rb") as file:
    image_data = base64.b64encode(file.read()).decode()


# =========================================================
# CANVAS
# =========================================================

html = """
<!DOCTYPE html>

<html>

<head>

<style>

html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    background: transparent;
}

#interface {
    position: relative;
    width: 100%;
    height: 390px;

    overflow: hidden;

    background:
        linear-gradient(
            135deg,
            #111015,
            #08070a
        );

    border: 1px solid #29242e;
    border-radius: 3px;
}


/* GRID */

#interface::before {
    content: "";
    position: absolute;
    inset: 0;

    background-image:
        linear-gradient(
            rgba(150,140,160,0.035) 1px,
            transparent 1px
        ),
        linear-gradient(
            90deg,
            rgba(150,140,160,0.035) 1px,
            transparent 1px
        );

    background-size: 30px 30px;
}


/* PARTICLES */

#particles {
    position: absolute;
    inset: 0;

    width: 100%;
    height: 100%;

    pointer-events: none;
}


/* CONTENT */

.content {
    position: absolute;

    left: 50%;
    top: 50%;

    transform: translate(-50%, -50%);

    width: 100%;

    text-align: center;

    z-index: 2;
}


.title {
    font-family: Cinzel, Georgia, serif;

    font-size: clamp(28px, 5vw, 52px);

    letter-spacing: 0.18em;

    color: #ddd7e1;
}


.subtitle {
    margin-top: 6px;

    font-family: Montserrat, sans-serif;

    font-size: 10px;

    letter-spacing: 0.3em;

    text-transform: uppercase;

    color: #77707d;
}


.image {
    display: block;

    width: 150px;
    height: 150px;

    object-fit: contain;

    margin: 18px auto 0;

    border: 1px solid rgba(255,255,255,0.10);
}


/* CORNERS */

.corner {
    position: absolute;

    width: 18px;
    height: 18px;

    border: 1px solid #62596a;

    z-index: 3;
}

.top-left {
    top: 7px;
    left: 7px;

    border-right: none;
    border-bottom: none;
}

.top-right {
    top: 7px;
    right: 7px;

    border-left: none;
    border-bottom: none;
}

.bottom-left {
    bottom: 7px;
    left: 7px;

    border-right: none;
    border-top: none;
}

.bottom-right {
    bottom: 7px;
    right: 7px;

    border-left: none;
    border-top: none;
}

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

        <div class="title">
            HOLA<br>Mi nombre es Juan
        </div>

        <div class="subtitle">
            Interfaces multimodales
        </div>

        <img
            class="image"
            src="data:image/png;base64,IMAGE_DATA"
        >

    </div>

</div>


<script>

const canvas = document.getElementById("particles");
const ctx = canvas.getContext("2d");

const interfaceBox = document.getElementById("interface");

let particles = [];


function resize() {

    canvas.width = interfaceBox.clientWidth;
    canvas.height = interfaceBox.clientHeight;

}


resize();

window.addEventListener("resize", resize);


interfaceBox.addEventListener("mousemove", function(event) {

    const rect = interfaceBox.getBoundingClientRect();

    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;


    for (let i = 0; i < 3; i++) {

        particles.push({

            x: x,
            y: y,

            vx: (Math.random() - 0.5) * 0.8,
            vy: (Math.random() - 0.5) * 0.8,

            life: 1,

            size: Math.random() * 1.5 + 0.5

        });

    }

});


function animate() {

    ctx.clearRect(
        0,
        0,
        canvas.width,
        canvas.height
    );


    for (
        let i = particles.length - 1;
        i >= 0;
        i--
    ) {

        const p = particles[i];


        p.x += p.vx;
        p.y += p.vy;

        p.life -= 0.025;


        ctx.beginPath();

        ctx.arc(
            p.x,
            p.y,
            p.size,
            0,
            Math.PI * 2
        );


        ctx.fillStyle =
            "rgba(190,175,205," +
            (p.life * 0.5) +
            ")";


        ctx.fill();


        if (p.life <= 0) {

            particles.splice(i, 1);

        }

    }


    requestAnimationFrame(animate);

}


animate();

</script>

</body>

</html>
"""


# Insert image AFTER the HTML string has been completely defined
html = html.replace(
    "IMAGE_DATA",
    image_data
)


components.html(
    html,
    height=410
)


# =========================================================
# MAIN PAGE
# =========================================================

st.title(
    "Interfaces multimodales"
)

st.header(
    "Backend + frontend en una sola interfaz."
)

st.write(
    "Explorando diferentes modalidades de interacción."
)


# =========================================================
# TEXT
# =========================================================

texto = st.text_input(
    "Texto",
    "Este es mi texto"
)

st.write(
    "Texto:",
    texto
)


# =========================================================
# MODALIDADES
# =========================================================

st.subheader(
    "Modalidades"
)


col1, col2 = st.columns(2)


with col1:

    st.subheader(
        "Experiencia"
    )

    st.write(
        "Las interfaces multimodales "
        "mejoran la interacción."
    )

    resp = st.checkbox(
        "Estoy de acuerdo"
    )

    if resp:
        st.write(
            "Correcto."
        )


with col2:

    st.subheader(
        "Modalidad"
    )

    modo = st.radio(
        "Principal",
        [
            "Visual",
            "Auditiva",
            "Táctil"
        ]
    )

    if modo == "Visual":

        st.write(
            "La vista domina."
        )

    elif modo == "Auditiva":

        st.write(
            "El audio domina."
        )

    else:

        st.write(
            "El tacto domina."
        )


# =========================================================
# BUTTON
# =========================================================

st.subheader(
    "Acción"
)


if st.button("Presiona"):

    st.write(
        "Gracias."
    )

else:

    st.write(
        "Sin acción."
    )


# =========================================================
# SELECTBOX
# =========================================================

st.subheader(
    "Salida"
)


in_mod = st.selectbox(
    "Modalidad",
    [
        "Audio",
        "Visual",
        "Háptico"
    ]
)


if in_mod == "Audio":

    set_mod = "Reproducir audio"

elif in_mod == "Visual":

    set_mod = "Reproducir video"

else:

    set_mod = "Activar vibración"


st.write(
    "Acción:",
    set_mod
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.subheader(
        "Configuración"
    )

    mod_radio = st.radio(
        "Modalidad",
        [
            "Visual",
            "Auditiva",
            "Háptica"
        ]
    )
