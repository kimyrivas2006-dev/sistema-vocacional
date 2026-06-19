import random
from base_datos import actualizar_usuario_en_db

# --- BANCO DE PREGUNTAS OFICIAL COMPLETO (80 REACTIVOS) ---
PREGUNTAS_GARDNER = [
    # --- LINGÜÍSTICO-VERBAL (LV) ---
    {"id": "LV1", "categoria": "LV", "texto": "Disfrutar de la lectura de libros, artículos, novelas o essays de forma frecuente."},
    {"id": "LV2", "categoria": "LV", "texto": "Redactar textos, cartas, ensayos o historias con facilidad y buena ortografía."},
    {"id": "LV3", "categoria": "LV", "texto": "Aprender con facilidad el significado de palabras nuevas o hablar otros idiomas."},
    {"id": "LV4", "categoria": "LV", "texto": "Disfrutar de juegos de palabras, crucigramas, sopa de letras o el juego de Scrabble."},
    {"id": "LV5", "categoria": "LV", "texto": "Recordar con precisión frases, citas célebres, poemas o datos leídos previamente."},
    {"id": "LV6", "categoria": "LV", "texto": "Expresar ideas de forma clara, elocuente y convincente al hablar en público."},
    {"id": "LV7", "categoria": "LV", "texto": "Disfrutar de escuchar debates, audiolibros, podcasts informativos o discursos."},
    {"id": "LV8", "categoria": "LV", "texto": "Encontrar facilidad para explicar conceptos complejos utilizando metáforas o analogías verbales."},
    {"id": "LV9", "categoria": "LV", "texto": "Prestar mucha atención a la estructura gramatical y la correcta pronunciación al comunicarte."},
    {"id": "LV10", "categoria": "LV", "texto": "Escribir apuntes detallados, diarios personales o bitácoras de tus experiencias."},

    # --- LÓGICO-MATEMÁTICA (LM) ---
    {"id": "LM1", "categoria": "LM", "texto": "Resolver acertijos de lógica, sudokus, problemas matemáticos o ecuaciones por diversión."},
    {"id": "LM2", "categoria": "LM", "texto": "Encontrar patrones lógicos, secuencias numéricas o relaciones estadísticas en los datos."},
    {"id": "LM3", "categoria": "LM", "texto": "Interesarte por saber cómo funcionan los sistemas de computación, algoritmos o la programación."},
    {"id": "LM4", "categoria": "LM", "texto": "Utilizar hojas de cálculo (como Excel) para organizar finanzas, métricas o presupuestos detallados."},
    {"id": "LM5", "categoria": "LM", "texto": "Abordar los problemas cotidianos de forma estructurada, analítica y basada en datos."},
    {"id": "LM6", "categoria": "LM", "texto": "Disfrutar de juegos de estrategia pura como el ajedrez, las damas o videojuegos de estrategia."},
    {"id": "LM7", "categoria": "LM", "texto": "Interesarte por teorías científicas, demostraciones empíricas o la física detrás de los fenómenos."},
    {"id": "LM8", "categoria": "LM", "texto": "Establecer clasificaciones, categorías o jerarquías claras para organizar la información."},
    {"id": "LM9", "categoria": "LM", "texto": "Calcular estimaciones numéricas o presupuestos mentales con bastante rapidez."},
    {"id": "LM10", "categoria": "LM", "texto": "Cuestionar el porqué de las cosas buscando explicaciones racionales, lógicas y demostrables."},

    # --- VISUAL-ESPACIAL (VE) ---
    {"id": "VE1", "categoria": "VE", "texto": "Orientarte con extrema facilidad en ciudades o lugares nuevos utilizando mapas o puntos de referencia."},
    {"id": "VE2", "categoria": "VE", "texto": "Imaginar con claridad cómo se vería un objeto tridimensional si lo rotaras mentalmente."},
    {"id": "VE3", "categoria": "VE", "texto": "Tener facilidad para interpretar gráficos, diagramas de flujo, planos arquitectónicos o infografías."},
    {"id": "VE4", "categoria": "VE", "texto": "Disfrutar de actividades como el dibujo, la pintura, la fotografía o el diseño gráfico digital."},
    {"id": "VE5", "categoria": "VE", "texto": "Armar rompecabezas complejos o figuras tridimensionales (como Legos o maquetas) con rapidez."},
    {"id": "VE6", "categoria": "VE", "texto": "Prestar mucha atención a la combinación de colores, la armonía visual y la estética de los entornos."},
    {"id": "VE7", "categoria": "VE", "texto": "Recordar con facilidad las caras de las personas, logotipos o detalles visuales de lugares que visitaste."},
    {"id": "VE8", "categoria": "VE", "texto": "Tener facilidad para diseñar la distribución de muebles en una habitación para optimizar el espacio."},
    {"id": "VE9", "categoria": "VE", "texto": "Disfrutar de la creación de mapas mentales, bocetos o esquemas visuales para estudiar o planificar."},
    {"id": "VE10", "categoria": "VE", "texto": "Interesarte por el cine, la edición de video, la animación en 3D o las artes puramente visuales."},

    # --- KINESTÉSICO-CORPORAL (KC) ---
    {"id": "KC1", "categoria": "KC", "texto": "Aprender a hacer algo mucho mejor cuando lo ejecutas directamente con tus manos o cuerpo."},
    {"id": "KC2", "categoria": "KC", "texto": "Tener habilidad y precisión para realizar trabajos manuales (artesanías, costura, carpintería o reparaciones técnico-mecánicas)."},
    {"id": "KC3", "categoria": "KC", "texto": "Practicar deportes, danza, yoga o actividades físicas que requieran coordinación, equilibrio y agilidad."},
    {"id": "KC4", "categoria": "KC", "texto": "Gesticular mucho con las manos o el cuerpo al momento de expresarte o explicar una idea."},
    {"id": "KC5", "categoria": "KC", "texto": "Tener buena memoria muscular: recuerdas movimientos físicos específicos con facilidad (manejar, teclear, gestos)."},
    {"id": "KC6", "categoria": "KC", "texto": "Disfrutar del desarme y exploración física de objetos para entender cómo están construidos."},
    {"id": "KC7", "categoria": "KC", "texto": "Sentir incomodidad al pasar sentado períodos de tiempo excesivamente largos; necesitas moverte."},
    {"id": "KC8", "categoria": "KC", "texto": "Poseer destreza para actividades de precisión fina como usar pinzas, soldar circuitos o esculpir."},
    {"id": "KC9", "categoria": "KC", "texto": "Disfrutar de actividades al aire libre que involucren esfuerzo muscular o destreza física."},
    {"id": "KC10", "categoria": "KC", "texto": "Tener facilidad para imitar gestos, expresiones corporales o movimientos de otras personas."},

    # --- MUSICAL (MU) ---
    {"id": "MU1", "categoria": "MU", "texto": "Tocar un instrumento musical, cantar de forma afinada o producir pistas de audio digital."},
    {"id": "MU2", "categoria": "MU", "texto": "Detectar de inmediato cuando una note musical, un instrumento o una voz están desafinados."},
    {"id": "MU3", "categoria": "MU", "texto": "Seguir el ritmo de una canción con el pie, las manos o golpeando ligeramente una superficie de manera inconsciente."},
    {"id": "MU4", "categoria": "MU", "texto": "Recordar con facilidad melodías, tonos de canciones o jingles publicitarios con solo escucharlos una vez."},
    {"id": "MU5", "categoria": "MU", "texto": "Escuchar música de forma activa mientras trabajas, estudias o realizas labores diarias para concentrarte."},
    {"id": "MU6", "categoria": "MU", "texto": "Diferenciar con facilidad los distintos instrumentos que componen una canción compleja."},
    {"id": "MU7", "categoria": "MU", "texto": "Interesarte por aprender sobre géneros musicales, estructuras de composición o edición de sonido."},
    {"id": "MU8", "categoria": "MU", "texto": "Tener sensibilidad hacia los sonidos del entorno (el canto de aves, el sonido de la lluvia, texturas acústicas)."},
    {"id": "MU9", "categoria": "MU", "texto": "Asociar recuerdos, emociones profundas o ideas específicas a canciones o melodías concretas."},
    {"id": "MU10", "categoria": "MU", "texto": "Disfrutar de tararear, silbar o crear ritmos propios cuando estás a solas."},

    # --- INTERPERSONAL (ER) ---
    {"id": "ER1", "categoria": "ER", "texto": "Notar con facilidad el estado de ánimo, las emociones o las verdaderas intenciones de una persona aunque intente ocultarlo."},
    {"id": "ER2", "categoria": "ER", "texto": "Tener facilidad para hacer nuevos amigos y sentirte cómodo interactuando en grupos sociales diversos."},
    {"id": "ER3", "categoria": "ER", "texto": "Actuar con frecuencia como mediador o consejero cuando tus amigos, familiares o compañeros tienen disputas."},
    {"id": "ER4", "categoria": "ER", "texto": "Disfrutar de liderar proyectos grupales, delegar responsabilidades y motivar a equipos humanos."},
    {"id": "ER5", "categoria": "ER", "texto": "Practicar la escucha activa, mostrando una empatía profunda hacia los problemas de los demás."},
    {"id": "ER6", "categoria": "ER", "texto": "Tener facilidad para persuadir, vender una idea o convencer a personas con argumentos adaptados a ellos."},
    {"id": "ER7", "categoria": "ER", "texto": "Preferir trabajar en proyectos colaborativos en equipo antes que trabajar completamente solo de forma aislada."},
    {"id": "ER8", "categoria": "ER", "texto": "Comprender los códigos sociales de etiqueta y saber cómo comportarte de manera asertiva en entornos públicos variados."},
    {"id": "ER9", "categoria": "ER", "texto": "Disfrutar de organizar reuniones sociales, eventos, fiestas comunitarias o dinámicas grupales."},
    {"id": "ER10", "categoria": "ER", "texto": "Interesarte genuinamente por las culturas, la política, la historia de las sociedades o las relaciones humanas."},

    # --- INTRAPERSONAL (RA) ---
    {"id": "RA1", "categoria": "RA", "texto": "Pasar tiempo a solas reflexionando profundamente sobre tus propios pensamientos, aciertos y errores."},
    {"id": "RA2", "categoria": "RA", "texto": "Tener una comprensión muy clara de cuáles son tus mayores fortalezas y tus puntos débiles a nivel personal."},
    {"id": "RA3", "categoria": "RA", "texto": "Establecer metas personales muy claras y poseer la autodisciplina necesaria para trabajar de forma independiente por alcanzarlas."},
    {"id": "RA4", "categoria": "RA", "texto": "Conocer con precisión qué situaciones detonan tu estrés, tu enojo o tu alegría, logrando regular tus reacciones."},
    {"id": "RA5", "categoria": "RA", "texto": "Preferir actividades, pasatiempos o proyectos de desarrollo individual antes que dinámicas masivas."},
    {"id": "RA6", "categoria": "RA", "texto": "Guiarte firmemente por tus propios valores y convicciones, aunque estos vayan en contra de la opinión de la mayoría."},
    {"id": "RA7", "categoria": "RA", "texto": "Disfrutar de la introspección escribiendo un diario, leyendo filosofía o meditando sobre el propósito de tu vida."},
    {"id": "RA8", "categoria": "RA", "texto": "Ser capaz de motivarte a ti mismo para salir adelante tras un fracaso sin depender exclusivamente del reconocimiento externo."},
    {"id": "RA9", "categoria": "RA", "texto": "Analizar de forma independiente tus propios procesos de aprendizaje para descubrir cómo estudias o trabajas mejor."},
    {"id": "RA10", "categoria": "RA", "texto": "Mantener una alta independencia emocional; te sientes seguro con tus decisiones sin buscar la aprobación constante."},

    # --- NATURALISTA (NA) ---
    {"id": "NA1", "categoria": "NA", "texto": "Disfrutar plenamente del cuidado de plantas, la siembra, el control de la tierra o la jardinería urbana."},
    {"id": "NA2", "categoria": "NA", "texto": "Tener facilidad para clasificar, identificar y reconocer diferentes especies de flora, fauna o tipos de rocas."},
    {"id": "NA3", "categoria": "NA", "texto": "Sentir un profundo bienestar y relajación al hacer caminatas por la montaña, bosques, playas o entornos naturales."},
    {"id": "NA4", "categoria": "NA", "texto": "Interesarte de forma activa por temas ecológicos, reciclaje, compostaje y la sostenibilidad ambiental."},
    {"id": "NA5", "categoria": "NA", "texto": "Mostrar facilidad para el cuidado, entrenamiento, observación o asistencia médica de animales domésticos o silvestres."},
    {"id": "NA6", "categoria": "NA", "texto": "Prestar mucha atención a los cambios climáticos, las fases lunares o los ciclos naturales del entorno."},
    {"id": "NA7", "categoria": "NA", "texto": "Disfrutar de pasatiempos al aire libre como el campismo, el excursionismo o la exploración geográfica."},
    {"id": "NA8", "categoria": "NA", "texto": "Tener curiosidad científica por fenómenos naturales como la geología, la meteorología o la astronomía."},
    {"id": "NA9", "categoria": "NA", "texto": "Identificar con rapidez patrones en la naturaleza, comportamientos animales o alteraciones en un ecosistema."},
    {"id": "NA10", "categoria": "NA", "texto": "Preferir coleccionar, fotografiar o estudiar elementos biológicos u orgánicos reales antes que objetos puramente sintéticos."},

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
    {"id": "E10", "categoria": "E", "texto": "Promover innovaciones tecnológicas argumentando sus beneficios económicos y de productividad."}
]

def ejecutar_test_gardner(usuario):
    print("\n=======================================")
    print("      INICIANDO TEST DE GARDNER        ")
    print("  Escala: 1(Total desacuerdo) a 5(Total acuerdo)")
    print("  👉 Escribe 'salir' para pausar y guardar")
    print("=======================================\n")
    
    progreso = usuario["progreso_gardner"]
    
    # 1. GENERACIÓN DEL MUESTREO ALEATORIO (5 por cada una de las 8 inteligencias)
    if not progreso["preguntas_orden"]:
        print("🎲 Generando tu test de inteligencias personalizado (40 preguntas al azar)...")
        
        # Agrupamos los IDs por categoría
        categorias = {"LV": [], "LM": [], "VE": [], "KC": [], "MU": [], "ER": [], "RA": [], "NA": [], "E": []}
        for p in PREGUNTAS_GARDNER:
            categorias[p["categoria"]].append(p["id"])
            
        muestreo_final = []
        CANTIDAD_POR_CATEGORIA = 5
        
        # Recorremos todas las categorías para sacar las 5 preguntas al azar de cada una
        for cat, lista_ids in categorias.items():
            seleccion_aleatoria = random.sample(lista_ids, CANTIDAD_POR_CATEGORIA)
            muestreo_final.extend(seleccion_aleatoria)
            
        random.shuffle(muestreo_final)
        progreso["preguntas_orden"] = muestreo_final
        actualizar_usuario_en_db(usuario)

    # Reconstruimos la lista en base a la muestra
    mapa_preguntas = {p["id"]: p for p in PREGUNTAS_GARDNER}
    preguntas_del_test = [mapa_preguntas[pid] for pid in progreso["preguntas_orden"]]

    # 2. EJECUCIÓN CON CONTROL DE RESPUESTAS EN TIEMPO REAL
    for numero, p in enumerate(preguntas_del_test, start=1):
        if p["id"] in progreso["respuestas"]:
            continue
            
        print(f"{numero}. 👉 {p['texto']}")
        
        while True:
            respuesta = input("Tu respuesta (1-5) o 'salir': ").strip().lower()
            
            if respuesta == "salir":
                print("\n💾 Progreso de Gardner guardado con éxito. ¡Vuelve cuando quieras!")
                actualizar_usuario_en_db(usuario)
                return "pausado"
                
            if respuesta in ["1", "2", "3", "4", "5"]:
                progreso["respuestas"][p["id"]] = int(respuesta)
                actualizar_usuario_en_db(usuario)
                break
            else:
                print("❌ Opción inválida. Ingresa un número del 1 al 5 o escribe 'salir'.")
        print("-" * 40)

    # 3. PROCESAMIENTO DE RESULTADOS
    puntajes = {"LV": 0, "LM": 0, "VE": 0, "KC": 0, "MU": 0, "ER": 0, "RA": 0, "NA": 0, "E": 0}
    for pid, valor in progreso["respuestas"].items():
        cat = mapa_preguntas[pid]["categoria"]
        puntajes[cat] += valor
        
    perfil_ordenado = sorted(puntajes.items(), key=lambda x: x[1], reverse=True)
    
    print("\n¡Test de Gardner finalizado con éxito!")
    return perfil_ordenado