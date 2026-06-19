import streamlit as stop
import streamlit as st

# 1. CONFIGURACIÓN DE LA PÁGINA (Debe ser siempre la primera línea de Streamlit)
st.set_page_config(
    page_title="Sistema Vocacional",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. BLOQUE COMPLETO DE ESTILOS CSS (Todo el diseño va estrictamente AQUÍ adentro)
st.markdown(
    """
    <style>
    /* Ocultar barra superior nativa de Streamlit */
    [data-testid="stHeader"] {
        display: none !important;
    }
    
    /* Título principal responsivo (No se corta en teléfonos) */
    .titulo-central {
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-size: min(9vw, 55px); 
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 15px;
        letter-spacing: -1px;
        line-height: 1.2;
        text-align: center;
    }

    /* Estilos de la barra de navegación superior */
    .navbar-superior {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 20px;
        background-color: transparent;
    }
    
    .logo-vocation {
        font-weight: bold;
        font-size: 20px;
        color: #ffffff;
    }

    /* 🎯 SOLUCIÓN A LOS BOTONES OSCUROS: Texto siempre blanco y legible */
    div.stButton > button {
        color: #ffffff !important;
        background-color: #262730 !important;
        border: 1px solid #4a4b57 !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        padding: 10px 24px !important;
        width: 100%;
    }
    
    div.stButton > button:hover {
        color: #ffffff !important;
        border-color: #7d3cff !important;
        background-color: #31323c !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 3. INTERFAZ Y CONTENIDO DE LA PORTADA
st.markdown('<h1 class="titulo-central">Sistema Vocacional</h1>', unsafe_allow_html=True)
st.write("<p style='text-align: center; color: #a3a8b4; font-size: 18px;'>Conecta tus talentos con las carreras del mañana.</p>", unsafe_allow_html=True)

# Espacio estético
st.markdown("<br>", unsafe_allow_html=True)

# Columnas centrales para los botones de acción principales
col_izq, col_centro, col_der = st.columns([1, 2, 1])

with col_centro:
    if st.button("Iniciar Sesión"):
        st.info("Formulario de inicio de sesión en desarrollo...")
    
    if st.button("Registrarse"):
        st.info("Formulario de registro en desarrollo...")

# Espacio antes del pie de página
st.markdown("<br><br><br>", unsafe_allow_html=True)

# 4. 🎯 SOLUCIÓN AL PIE DE PÁGINA RESPONSIVO (Sin columnas comprimidas)
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; padding: 10px; line-height: 2.0;">
        <a href="#" style="color: #ffffff; text-decoration: none; margin: 0 12px; font-size: 14px; display: inline-block;">Términos y Condiciones</a>
        <span style="color: #4a4b57; margin: 0 4px; hidden-mobile: true;">|</span>
        <a href="#" style="color: #ffffff; text-decoration: none; margin: 0 12px; font-size: 14px; display: inline-block;">Políticas de Privacidad</a>
        <span style="color: #4a4b57; margin: 0 4px;">|</span>
        <a href="#" style="color: #ffffff; text-decoration: none; margin: 0 12px; font-size: 14px; display: inline-block;">Contacto</a>
    </div>
    """,
    unsafe_allow_html=True
)
