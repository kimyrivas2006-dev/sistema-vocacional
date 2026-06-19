import random
from base_datos import actualizar_usuario_en_db

# --- BANCO DE PREGUNTAS OFICIAL COMPLETO (60 REACTIVOS) ---
PREGUNTAS_HOLLAND = [
    # --- REALISTA (R) ---
    {"id": "R1", "categoria": "R", "texto": "Reparar fallas eléctricas o de iluminación en una casa o taller."},
    {"id": "R2", "categoria": "R", "texto": "Armar, desarmar o hacer mantenimiento a componentes de hardware de computadoras."},
    {"id": "R3", "categoria": "R", "texto": "Operar herramientas mecánicas, maquinaria de construcción o equipos de precisión."},
    {"id": "R4", "categoria": "R", "texto": "Construir estructuras utilizando materiales como madera, metal o cemento."},
    {"id": "R5", "categoria": "R", "texto": "Hacer mantenimiento preventivo o reparar motores de vehículos (carros, motos, etc.)."},
    {"id": "R6", "categoria": "R", "texto": "Instalar o configurar redes de cableado estructurado para sistemas informáticos."},
    {"id": "R7", "categoria": "R", "texto": "Trabajar al aire libre operando sistemas de riego o maquinaria agrícola."},
    {"id": "R8", "categoria": "R", "texto": "Utilizar herramientas de medición técnica como voltímetros, calibradores o niveles."},
    {"id": "R9", "categoria": "R", "texto": "Armar maquetas físicas, prototipos mecánicos o muebles modulares."},
    {"id": "R10", "categoria": "R", "texto": "Montar o reparar sistemas de tuberías, griferías o redes de gas."},

    # --- INVESTIGADOR (I) ---
    {"id": "I1", "categoria": "I", "texto": "Resolver acertijos lógicos, problemas matemáticos o analizar algoritmos complejos."},
    {"id": "I2", "categoria": "I", "texto": "Investigar las causas de un problema técnico o el origen oculto de una falla de software."},
    {"id": "I3", "categoria": "I", "texto": "Hacer experimentos científicos, estudiar biología, química o física a nivel profundo."},
    {"id": "I4", "categoria": "I", "texto": "Analizar grandes volúmenes de datos para descubrir patrones, estadísticas o tendencias."},
    {"id": "I5", "categoria": "I", "texto": "Leer artículos científicos o técnicos para entender cómo funcionan las nuevas tecnologías."},
    {"id": "I6", "categoria": "I", "texto": "Desarrollar modelos teóricos o fórmulas matemáticas para explicar un fenómeno."},
    {"id": "I7", "categoria": "I", "texto": "Estudiar la estructura de los lenguajes de programación o la arquitectura de sistemas."},
    {"id": "I8", "categoria": "I", "texto": "Realizar auditorías de sistemas informáticos para encontrar vulnerabilidades de seguridad."},
    {"id": "I9", "categoria": "I", "texto": "Investigar el comportamiento humano, la psicología o fenómenos sociológicos."},
    {"id": "I10", "categoria": "I", "texto": "Utilizar microscopios, simuladores de software o herramientas de diagnóstico avanzado."},

    # --- ARTÍSTICO (A) ---
    {"id": "A1", "categoria": "A", "texto": "Diseñar identidades visuales, logotipos, interfaces digitales o material gráfico interactivo."},
    {"id": "A2", "categoria": "A", "texto": "Escribir historias, novelas, guiones, artículos de blog o contenido creativo para redes."},
    {"id": "A3", "categoria": "A", "texto": "Crear composiciones musicales, editar pistas de audio o diseñar efectos sonoros."},
    {"id": "A4", "categoria": "A", "texto": "Pintar, dibujar, esculpir o realizar ilustraciones digitales utilizando tabletas gráficas."},
    {"id": "A5", "categoria": "A", "texto": "Idear y planificar la decoración de espacios, escenarios o interfaces de usuario (UX)."},
    {"id": "A6", "categoria": "A", "texto": "Actuar en obras de teatro, filmar videos creativos o dirigir producciones audiovisuales."},
    {"id": "A7", "categoria": "A", "texto": "Diseñar ropa, accesorios, empaques de productos o elementos de moda innovadores."},
    {"id": "A8", "categoria": "A", "texto": "Crear animaciones en 2D/3D, efectos visuales o videojuegos con enfoque artístico."},
    {"id": "A9", "categoria": "A", "texto": "Participar en sesiones de lluvia de ideas (brainstorming) para resolver problemas con enfoques fuera de lo común."},
    {"id": "A10", "categoria": "A", "texto": "Fotografiar paisajes, personas o productos buscando composiciones estéticas y expresivas."},

    # --- SOCIAL (S) ---
    {"id": "S1", "categoria": "S", "texto": "Explicar conceptos técnicos, científicos o académicos de forma sencilla para que otros aprendan."},
    {"id": "S2", "categoria": "S", "texto": "Prestar ayuda, orientar, escuchar o asesorar a personas que están pasando por problemas personales."},
    {"id": "S3", "categoria": "S", "texto": "Coordinar actividades de voluntariado, apoyo social o dinámicas para el bienestar comunitario."},
    {"id": "S4", "categoria": "S", "texto": "Enseñar a niños, jóvenes o adultos a desarrollar nuevas habilidades o el uso de herramientas."},
    {"id": "S5", "categoria": "S", "texto": "Cuidar, asistir o hacer terapia para mejorar la salud física o emocional de las personas."},
    {"id": "S6", "categoria": "S", "texto": "Mediar en conflictos familiares, laborales o comunitarios para lograr acuerdos pacíficos."},
    {"id": "S7", "categoria": "S", "texto": "Organizar clubes de estudio, foros de discusión o actividades recreativas grupales."},
    {"id": "S8", "categoria": "S", "texto": "Guiar a nuevos integrantes de un equipo de trabajo para que se adapten rápidamente."},
    {"id": "S9", "categoria": "S", "texto": "Atender llamadas o solicitudes brindando soluciones con mucha empatía y paciencia."},
    {"id": "S10", "categoria": "S", "texto": "Dictar conferencias, talleres o charlas motivacionales y formativas ante un público."},

    # --- EMPRENDEDOR (E) ---
    {"id": "E1", "categoria": "E", "texto": "Liderar, motivar y coordinar un equipo de personas para alcanzar las metas de un proyecto o negocio."},
    {"id": "E2", "categoria": "E", "texto": "Negociar contratos con proveedores, vender una idea tecnológica o convencer a clientes difíciles."},
    {"id": "E3", "categoria": "E", "texto": "Planificar estrategias comerciales, analizar la competencia o lanzar marcas al mercado."},
    {"id": "E4", "categoria": "E", "texto": "Asumir la responsabilidad financiera y legal de emprender una empresa o negocio propio."},
    {"id": "E5", "categoria": "E", "texto": "Organizar eventos corporativos, campañas publicitarias o ferias de negocios."},
    {"id": "E6", "categoria": "E", "texto": "Tomar decisiones rápidas e importantes bajo presión para resolver crisis operativas."},
    {"id": "E7", "categoria": "E", "texto": "Presentar proyectos o propuestas comerciales frente a inversionistas para conseguir financiamiento."},
    {"id": "E8", "categoria": "E", "texto": "Supervisar el rendimiento del personal y delegar tareas según las fortalezas de cada quien."},
    {"id": "E9", "categoria": "E", "texto": "Diseñar planes de expansión para llevar un producto o servicio a nuevas ciudades o países."},
    {"id": "E10", "categoria": "E", "texto": "Promover innovaciones tecnológicas argumentando sus beneficios económicos y de productividad."},

    # --- CONVENCIONAL (C) ---
    {"id": "C1", "categoria": "C", "texto": "Organizar, clasificar y mantener perfectamente estructuradas bases de datos o archivos digitales."},
    {"id": "C2", "categoria": "C", "texto": "Llevar el control riguroso de presupuestos, facturas, cuentas por pagar o reportes contables."},
    {"id": "C3", "categoria": "C", "texto": "Establecer manuales de procedimientos paso a paso y normas claras para evitar errores operativos."},
    {"id": "C4", "categoria": "C", "texto": "Verificar minuciosamente que un documento, contrato o código no tenga faltas ni errores de transcripción."},
    {"id": "C5", "categoria": "C", "texto": "Administrar inventarios detallados de mercancía, herramientas o licencias de software."},
    {"id": "C6", "categoria": "C", "texto": "Planificar agendas de trabajo, cronogramas de entregas y calendarios de reuniones."},
    {"id": "C7", "categoria": "C", "texto": "Procesar formularios, registros de inscripción o expedientes siguiendo leyes o reglamentos."},
    {"id": "C8", "categoria": "C", "texto": "Monitorear que los procesos de una empresa cumplan estrictamente con las auditorías de calidad."},
    {"id": "C9", "categoria": "C", "texto": "Generar reportes diarios, semanales o mensuales con métricas de rendimiento muy precisas."},
    {"id": "C10", "categoria": "C", "texto": "Transcribir y organizar datos estructurados en hojas de cálculo usando fórmulas o tablas dinámicas."}
]

def ejecutar_test_holland(usuario):
    print("\n=======================================")
    print("      INICIANDO TEST DE HOLLAND        ")
    print("  Escala: 1(Disgusto) a 5(Me gusta mucho)")
    print("  👉 Escribe 'salir' para pausar y guardar")
    print("=======================================\n")
    
    progreso = usuario["progreso_holland"]
    
    # 1. GENERACIÓN DEL MUESTREO ALEATORIO (5 por categoría de forma fija)
    if not progreso["preguntas_orden"]:
        print("🎲 Generando un test personalizado y balanceado (30 preguntas al azar)...")
        
        # Agrupamos los IDs por categoría
        categorias = {"R": [], "I": [], "A": [], "S": [], "E": [], "C": []}
        for p in PREGUNTAS_HOLLAND:
            categorias[p["categoria"]].append(p["id"])
            
        muestreo_final = []
        CANTIDAD_POR_CATEGORIA = 5
        
        for cat, lista_ids in categorias.items():
            seleccion_aleatoria = random.sample(lista_ids, CANTIDAD_POR_CATEGORIA)
            muestreo_final.extend(seleccion_aleatoria)
            
        random.shuffle(muestreo_final)
        progreso["preguntas_orden"] = muestreo_final
        actualizar_usuario_en_db(usuario)

    # Reconstruimos la lista en base a la muestra
    mapa_preguntas = {p["id"]: p for p in PREGUNTAS_HOLLAND}
    preguntas_del_test = [mapa_preguntas[pid] for pid in progreso["preguntas_orden"]]

    # 2. EJECUCIÓN CON CONTROL DE RESPUESTAS EN TIEMPO REAL
    for numero, p in enumerate(preguntas_del_test, start=1):
        if p["id"] in progreso["respuestas"]:
            continue
            
        print(f"{numero}. 👉 {p['texto']}")
        
        while True:
            respuesta = input("Tu respuesta (1-5) o 'salir': ").strip().lower()
            
            if respuesta == "salir":
                print("\n💾 Progreso guardado con éxito. ¡Vuelve cuando quieras!")
                actualizar_usuario_en_db(usuario)
                return "pausado"
                
            if respuesta in ["1", "2", "3", "4", "5"]:
                progreso["respuestas"][p["id"]] = int(respuesta)
                actualizar_usuario_en_db(usuario)
                break
            else:
                print("❌ Opción inválida. Ingresa un número del 1 al 5 o escribe 'salir'.")
        print("-" * 40)

    # 3. PROCESAMIENTO DE PUNTAJES FINALES
    puntajes = {"R": 0, "I": 0, "A": 0, "S": 0, "E": 0, "C": 0}
    for pid, valor in progreso["respuestas"].items():
        cat = mapa_preguntas[pid]["categoria"]
        puntajes[cat] += valor
        
    categorias_ordenadas = sorted(puntajes.items(), key=lambda x: x[1], reverse=True)
    codigo_resultado = categorias_ordenadas[0][0] + categorias_ordenadas[1][0] + categorias_ordenadas[2][0]
    
    print(f"\n¡Test finalizado con éxito! Tu Código RIASEC es: {codigo_resultado}")
    return codigo_resultado