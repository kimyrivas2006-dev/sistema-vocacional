import streamlit as st
from base_datos import buscar_o_crear_usuario, actualizar_usuario_en_db, cargar_datos
from test_holland import PREGUNTAS_HOLLAND
from test_gardner import PREGUNTAS_GARDNER
import random
import plotly.express as px

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="VocatiON - Sistema Vocacional", page_icon="🎓", layout="centered")

# --- INICIALIZACIÓN DE LA MEMORIA WEB (SESSION STATE) ---
if "usuario" not in st.session_state:
    st.session_state.usuario = None
if "pantalla" not in st.session_state:
    st.session_state.pantalla = "portada"

# --- FUNCIONES DE CONTROL DE FLUJO ---
def cerrar_sesion():
    st.session_state.usuario = None
    st.session_state.pantalla = "portada"
    st.rerun()

# =========================================================================
# 1. PASO A: PORTADA DE BIENVENIDA (CÓDIGO NATIVO RESPONSIVO)
# =========================================================================
if st.session_state.pantalla == "portada":
    st.markdown(
        """
        <style>
        /* Ocultar barra superior nativa de Streamlit */
        [data-testid="stHeader"] {
            display: none !important;
        }
        [data-testid="stAppViewContainer"] {
            padding-top: 0rem !important;
        }
        .block-container {
            padding-top: 2rem !important;
            padding-bottom: 2rem !important;
            max-width: 1200px !important;
        }
        
        /* Fondo con degradado líquido aurora profundo */
        .stApp {
            background: linear-gradient(135deg, #0d0b21 0%, #17123a 40%, #3a1c50 80%, #52184b 100%) !important;
            color: #ffffff !important;
        }
        
        /* Barra de Navegación Superior */
        .navbar-superior {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 40px;
            width: 100%;
        }
        .logo-vocation {
            font-family: 'Helvetica Neue', Arial, sans-serif;
            font-size: 26px;
            font-weight: bold;
            color: #ffffff;
            margin-top: 10px;
        }
        .logo-vocation span {
            color: #00bf63 !important;
        }
        .link-nosotros-limpio {
            font-family: 'Helvetica Neue', Arial, sans-serif;
            font-size: 20px !important;
            color: #ffffff !important;
            text-decoration: none !important;
            font-weight: 500;
            display: block;
            text-align: right;
            margin-top: 15px;
        }
        
        /* Cuerpo Central */
        .cuerpo-portada {
            text-align: center;
            margin-top: 80px;
            margin-bottom: 20px;
            padding: 0 15px;
        }
        
        /* SOLUCIÓN AL TÍTULO CORTADO: Se reduce de forma dinámica en teléfonos */
        .titulo-central {
            font-family: 'Helvetica Neue', Arial, sans-serif;
            font-size: min(9vw, 65px);
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 15px;
            letter-spacing: -1px;
            line-height: 1.2;
        }
        .subtitulo-frase {
            font-family: 'Helvetica Neue', Arial, sans-serif;
            font-style: italic;
            font-size: min(4.5vw, 22px);
            color: #ffffff;
            opacity: 0.9;
        }
        
        /* FORZAR CENTRADO DEL BOTÓN EN EL EJE CENTRAL */
        .stButton {
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            width: 100% !important;
            margin: 40px 0 !important;
        }
        
        /* Estilos de la Píldora Blanca Grande */
        .stButton button {
            background-color: #ffffff !important;
            color: #17123a !important;
            border-radius: 30px !important;
            border: none !important;
            padding: 14px 80px !important;
            box-shadow: 0 4px 25px rgba(0, 0, 0, 0.5) !important;
            transition: all 0.2s ease !important;
        }
        
        /* Texto interno del botón en Súper Negrita */
        .stButton button p {
            font-family: 'Helvetica Neue', Arial, sans-serif !important;
            font-size: 24px !important;
            font-weight: 800 !important;
            color: #17123a !important;
            margin: 0 !important;
        }
        
        .stButton button:hover {
            transform: scale(1.05) !important;
            background-color: #f8f9fa !important;
        }
        
        /* SOLUCIÓN AL PIE DE PÁGINA: Contenedor responsivo centrado */
        .footer-portada-limpio {
            margin-top: 100px;
            padding-bottom: 20px;
            text-align: center;
            font-family: 'Helvetica Neue', Arial, sans-serif;
            font-size: 18px;
            line-height: 2.0;
        }
        .footer-portada-limpio a {
            color: #ffffff !important;
            text-decoration: none !important;
            opacity: 0.9;
            margin: 0 15px;
            display: inline-block;
        }
        .footer-separador {
            color: rgba(255, 255, 255, 0.4);
        }

        /* Ajustes específicos para teléfonos */
        @media (max-width: 640px) {
            .cuerpo-portada {
                margin-top: 40px;
            }
            .stButton button {
                padding: 12px 50px !important; /* Reduce el ancho del botón para que quepa bien */
            }
            .footer-separador {
                display: none !important; /* Esconde las barras verticales en el celular */
            }
            .footer-portada-limpio a {
                display: block !important; /* Coloca los enlaces uno abajo del otro */
                margin: 10px 0 !important;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Barra Superior
    col_logo, col_vacio, col_nosotros = st.columns([2, 5, 2])
    with col_logo:
        st.markdown('<div class="logo-vocation">Vocati<span>ON</span></div>', unsafe_allow_html=True)
    with col_nosotros:
        st.markdown('<a href="#" class="link-nosotros-limpio">Nosotros</a>', unsafe_allow_html=True)
        
    # Cuerpo Central (Título y Frase)
    st.markdown(
        """
        <div class="cuerpo-portada">
            <div class="titulo-central">Sistema Vocacional</div>
            <div class="subtitulo-frase">Conecta tus talentos con las carreras del mañana</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    # Botón Nativo que responde al CSS de arriba
    if st.button("Iniciar"):
        st.session_state.pantalla = "login"
        st.rerun()
        
    # Pie de Página Integrado
    st.markdown(
        """
        <div class="footer-portada-limpio">
            <a href="#">Términos y Condiciones</a>
            <span class="footer-separador">|</span>
            <a href="#">Políticas de Privacidad</a>
            <span class="footer-separador">|</span>
            <a href="#">Contacto</a>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================================
# 2. PASO B: FORMULARIO DE INGRESO (FONDO CLARO, LIMPIO Y PROFESIONAL)
# =========================================================================
elif st.session_state.pantalla == "login":
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f8f9fa !important;
            color: #212529 !important;
        }
        .login-box {
            background-color: #ffffff;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            border-left: 5px solid #17123a;
            margin-top: 20px;
        }
        /* Asegurar legibilidad del texto en los botones del panel claro */
        div.stButton > button {
            color: #212529 !important;
        }
        div.stButton > button[kind="primary"] {
            color: #ffffff !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("## 🔑 Ingreso al Sistema Vocacional")
    st.markdown("Por favor, introduce tus datos para cargar o crear tu perfil de evaluación.")
    
    with st.container():
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        identidad_input = st.text_input("Documento de Identidad (Cédula):", key="id_login")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.write("")
    
    col_btn1, col_btn2 = st.columns([1, 2])
    with col_btn1:
        if st.button("⬅ Volver"):
            st.session_state.pantalla = "portada"
            st.rerun()
            
    with col_btn2:
        if st.button("Ingresar al Panel 🚀", type="primary", use_container_width=True):
            id_clave = identidad_input.strip().replace(".", "").replace("-", "")
            if id_clave:
                datos_db = cargar_datos()
                if id_clave in datos_db:
                    st.session_state.usuario = buscar_o_crear_usuario(id_clave)
                    st.session_state.pantalla = "menu"
                    st.rerun()
                else:
                    st.session_state.id_nuevo = id_clave
                    st.session_state.pantalla = "registro"
                    st.rerun()
            else:
                st.error("❌ Por favor, ingresa un número de documento válido.")

elif st.session_state.pantalla == "registro":
    st.markdown("<style>.stApp { background-color: #f8f9fa !important; color: #212529 !important; } div.stButton > button[kind=\"primary\"] { color: #ffffff !important; }</style>", unsafe_allow_html=True)
    st.markdown("## ✨ Crear Nuevo Perfil Escolar")
    st.warning(f"La cédula ID: {st.session_state.id_nuevo} no está registrada en el sistema.")
    
    nombre_nuevo = st.text_input("Nombre Completo del Estudiante:")
    edad_nueva = st.text_input("Edad (Años):")
    
    if st.button("Registrar and Entrar al Sistema", use_container_width=True, type="primary"):
        if nombre_nuevo and edad_nueva:
            st.session_state.usuario = buscar_o_crear_usuario(
                st.session_state.id_nuevo, nombre_nuevo, edad_nueva
            )
            st.success("¡Perfil estudiantil creado con éxito!")
            st.session_state.pantalla = "menu"
            st.rerun()
        else:
            st.error("❌ Todos los campos son obligatorios.")

# =========================================================================
# 3. MENÚ PRINCIPAL / PANEL DE RESULTADOS
# =========================================================================
elif st.session_state.pantalla == "menu":
    st.markdown("<style>.stApp { background-color: #f8f9fa !important; color: #212529 !important; } div.stButton > button { color: #212529 !important; }</style>", unsafe_allow_html=True)
    usuario = st.session_state.usuario
    st.title(f"👋 ¡Hola, {usuario['nombre']}!")
    st.markdown("#### Panel de Control de Evaluación Vocacional")
    
    st.divider()
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Módulo Holland")
        if usuario["resultados_holland"]:
            st.success(f"✅ ¡Completado! Código: **{usuario['resultados_holland']}**")
        else:
            respondidas_h = len(usuario["progreso_holland"]["respuestas"])
            if respondidas_h > 0:
                st.warning(f"⏳ En Progreso ({respondidas_h} de 30)")
            else:
                st.error("❌ Sin Iniciar (0 de 30)")
        
        if st.button("Ir al Test de Holland", key="btn_h", use_container_width=True):
            if not usuario["progreso_holland"]["preguntas_orden"]:
                categorias = {"R":[], "I":[], "A":[], "S":[], "E":[], "C":[]}
                for p in PREGUNTAS_HOLLAND:
                    categorias[p["categoria"]].append(p["id"])
                muestreo = []
                for cat, ids in categorias.items():
                    muestreo.extend(random.sample(ids, 5))
                random.shuffle(muestreo)
                usuario["progreso_holland"]["preguntas_orden"] = muestreo
                actualizar_usuario_en_db(usuario)
            st.session_state.pantalla = "holland"
            st.rerun()

    with col2:
        st.subheader("🧠 Módulo Gardner")
        if usuario["resultados_gardner"]:
            st.success("✅ ¡Completado! Perfil generado.")
        else:
            respondidas_g = len(usuario["progreso_gardner"]["respuestas"])
            if respondidas_g > 0:
                st.warning(f"⏳ En Progreso ({respondidas_g} de 45)")
            else:
                st.error("❌ Sin Iniciar (0 de 45)")
                
        if st.button("Ir al Test de Gardner", key="btn_g", use_container_width=True):
            if not usuario["progreso_gardner"]["preguntas_orden"]:
                categorias = {"LV":[], "LM":[], "VE":[], "KC":[], "MU":[], "ER":[], "RA":[], "NA":[], "E":[]}
                for p in PREGUNTAS_GARDNER:
                    categorias[p["categoria"]].append(p["id"])
                muestreo = []
                for cat, ids in categorias.items():
                    muestreo.extend(random.sample(ids, 5))
                random.shuffle(muestreo)
                usuario["progreso_gardner"]["preguntas_orden"] = muestreo
                actualizar_usuario_en_db(usuario)
            st.session_state.pantalla = "gardner"
            st.rerun()

    if usuario["resultados_holland"] or usuario["resultados_gardner"]:
        st.divider()
        st.markdown("## 📊 TU INFORME VOCACIONAL INTEGRADO")
        
        from diccionario_vocacional import DESCRIPCIONES_HOLLAND, DESCRIPCIONES_GARDNER, BANCO_CARRERAS
        
        if usuario["resultados_holland"]:
            codigo_riasec = usuario["resultados_holland"]
            st.markdown(f"### 🔹 Análisis de Personalidad RIASEC: **{codigo_riasec}**")
            
            mapa_p_h = {p["id"]: p for p in PREGUNTAS_HOLLAND}
            puntajes_h = {"Realista (R)":0, "Investigador (I)":0, "Artístico (A)":0, "Social (S)":0, "Emprendedor (E)":0, "Convencional (C)":0}
            cat_letras = {"R": "Realista (R)", "I": "Investigador (I)", "A": "Artístico (A)", "S": "Social (S)", "E": "Emprendedor (E)", "C": "Convencional (C)"}
            
            for pid, valor in usuario["progreso_holland"]["respuestas"].items():
                cat = mapa_p_h[pid]["categoria"]
                puntajes_h[cat_letras[cat]] += valor
                
            fig_h = px.bar(x=list(puntajes_h.keys()), y=list(puntajes_h.values()), labels={'x': 'Dimensiones', 'y': 'Pts'}, color=list(puntajes_h.values()), color_continuous_scale='Sunset')
            fig_h.update_layout(showlegend=False, height=350, margin=dict(l=20, r=20, t=20, b=20), coloraxis_showscale=False)
            st.plotly_chart(fig_h, use_container_width=True)
            
            for letra in codigo_riasec:
                if letra in DESCRIPCIONES_HOLLAND:
                    st.write(DESCRIPCIONES_HOLLAND[letra])
        
        if usuario["resultados_gardner"]:
            st.divider()
            st.markdown("### 🧠 Tus Inteligencias Potenciales (Top 3)")
            perfil_ordenado = usuario["resultados_gardner"]
            
            nombres_mapa = {"LV": "Lingüístico-Verbal", "LM": "Lógico-Matemática", "VE": "Visual-Espacial", "KC": "Kinestésico-Corporal", "MU": "Musical", "ER": "Interpersonal", "RA": "Intrapersonal", "NA": "Naturalista", "E": "Perfil Emprendedor"}
            categorias_grafico = [nombres_mapa.get(str(item[0]).strip().upper(), item[0]) for item in perfil_ordenado]
            puntajes_grafico = [item[1] for item in perfil_ordenado]
            
            fig_g = px.bar(x=puntajes_grafico, y=categorias_grafico, orientation='h', labels={'x': 'Pts', 'y': 'Inteligencia'}, color=puntajes_grafico, color_continuous_scale='Viridis')
            fig_g.update_layout(yaxis={'categoryorder': 'total ascending'}, showlegend=False, height=380, margin=dict(l=20, r=20, t=20, b=20), coloraxis_showscale=False)
            st.plotly_chart(fig_g, use_container_width=True)
            
            for item in perfil_ordenado[:3]:
                inte_id = str(item[0]).strip().upper()
                pts = item[1]
                if inte_id == "E":
                    st.write(f"⭐ **{pts} pts** -> Perfil Emprendedor.")
                elif inte_id in DESCRIPCIONES_GARDNER:
                    st.write(f"⭐ **{pts} pts** -> {DESCRIPCIONES_GARDNER[inte_id]}")

    st.divider()
    if st.button("Cerrar Sesión", type="secondary", use_container_width=True):
        cerrar_sesion()

# =========================================================================
# 4. INTERFAZ INTERACTIVA: TEST DE HOLLAND
# =========================================================================
elif st.session_state.pantalla == "holland":
    st.markdown("<style>.stApp { background-color: #f8f9fa !important; color: #212529 !important; } div.stButton > button { color: #212529 !important; } div.stButton > button[kind=\"primary\"] { color: #ffffff !important; }</style>", unsafe_allow_html=True)
    usuario = st.session_state.usuario
    progreso = usuario["progreso_holland"]
    st.title("📋 Cuestionario de Intereses de Holland")
    
    mapa_p = {p["id"]: p for p in PREGUNTAS_HOLLAND}
    ids_totales = progreso["preguntas_orden"]
    respondidas = progreso["respuestas"]
    
    id_actual = next((pid for pid in ids_totales if pid not in respondidas), None)
            
    if id_actual:
        st.markdown(f"#### Pregunta {len(respondidas) + 1} de 30")
        st.progress(len(respondidas) / 30)
        st.info(f"**{mapa_p[id_actual]['texto']}**")
        
        respuesta = st.radio("Tu valoración:", options=[1, 2, 3, 4, 5], format_func=lambda x: {1:"1 - Me disgusta mucho", 2:"2 - Me disgusta", 3:"3 - Me es indiferente", 4:"4 - Me gusta", 5:"5 - Me gusta mucho"}[x], horizontal=True)
        col_nav1, col_nav2, col_nav3 = st.columns(3)
        with col_nav1:
            if len(respondidas) > 0:
                if st.button("⬅ Anterior"):
                    ultimo_id = ids_totales[len(respondidas) - 1]
                    del progreso["respuestas"][ultimo_id]
                    actualizar_usuario_en_db(usuario)
                    st.rerun()
        with col_nav2:
            if st.button("Guardar y Siguiente ➡", type="primary", use_container_width=True):
                progreso["respuestas"][id_actual] = respuesta
                actualizar_usuario_en_db(usuario)
                st.rerun()
        with col_nav3:
            if st.button("Pausar y Menú"):
                st.session_state.pantalla = "menu"
                st.rerun()
    else:
        puntajes = {"R":0, "I":0, "A":0, "S":0, "E":0, "C":0}
        for pid, valor in respondidas.items():
            cat = mapa_p[pid]["categoria"]
            puntajes[cat] += valor
        ordenadas = sorted(puntajes.items(), key=lambda x: x[1], reverse=True)
        codigo = ordenadas[0][0] + ordenadas[1][0] + ordenadas[2][0]
        usuario["resultados_holland"] = codigo
        actualizar_usuario_en_db(usuario)
        st.balloons()
        st.session_state.pantalla = "menu"
        st.rerun()

# =========================================================================
# 5. INTERFAZ INTERACTIVA: TEST DE GARDNER
# =========================================================================
elif st.session_state.pantalla == "gardner":
    st.markdown("<style>.stApp { background-color: #f8f9fa !important; color: #212529 !important; } div.stButton > button { color: #212529 !important; } div.stButton > button[kind=\"primary\"] { color: #ffffff !important; }</style>", unsafe_allow_html=True)
    usuario = st.session_state.usuario
    progreso = usuario["progreso_gardner"]
    st.title("🧠 Cuestionario de Inteligencias Múltiples (Gardner)")
    
    mapa_p = {p["id"]: p for p in PREGUNTAS_GARDNER}
    ids_totales = progreso["preguntas_orden"]
    respondidas = progreso["respuestas"]
    
    id_actual = next((pid for pid in ids_totales if pid not in respondidas), None)
            
    if id_actual:
        st.markdown(f"#### Pregunta {len(respondidas) + 1} de 45")
        st.progress(len(respondidas) / 45)
        st.info(f"**{mapa_p[id_actual]['texto']}**")
        
        respuesta = st.radio("Tu valoración:", options=[1, 2, 3, 4, 5], format_func=lambda x: {1:"1 - Total desacuerdo", 2:"2 - En desacuerdo", 3:"3 - Neutro", 4:"4 - De acuerdo", 5:"5 - Total acuerdo"}[x], horizontal=True)
        col_nav1, col_nav2, col_nav3 = st.columns(3)
        with col_nav1:
            if len(respondidas) > 0:
                if st.button("⬅ Anterior"):
                    ultimo_id = ids_totales[len(respondidas) - 1]
                    del progreso["respuestas"][ultimo_id]
                    actualizar_usuario_en_db(usuario)
                    st.rerun()
        with col_nav2:
            if st.button("Guardar y Siguiente ➡", type="primary", use_container_width=True):
                progreso["respuestas"][id_actual] = respuesta
                actualizar_usuario_en_db(usuario)
                st.rerun()
        with col_nav3:
            if st.button("Pausar y Menú"):
                st.session_state.pantalla = "menu"
                st.rerun()
    else:
        puntajes = {"LV":0, "LM":0, "VE":0, "KC":0, "MU":0, "ER":0, "RA":0, "NA":0, "E":0}
        for pid, valor in respondidas.items():
            cat = mapa_p[pid]["categoria"]
            puntajes[cat] += valor
        perfil_ordenado = sorted(puntajes.items(), key=lambda x: x[1], reverse=True)
        usuario["resultados_gardner"] = perfil_ordenado
        actualizar_usuario_en_db(usuario)
        st.balloons()
        st.session_state.pantalla = "menu"
        st.rerun()
