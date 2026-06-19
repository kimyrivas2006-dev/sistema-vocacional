# --- TRADUCCIÓN INDIVIDUAL DE RASGOS RIASEC (HOLLAND) ---
DESCRIPCIONES_HOLLAND = {
    "R": "**Realista (R):** Posees una fuerte orientación hacia la práctica, el manejo de herramientas, hardware, objetos físicos o actividades al aire libre. Prefieres soluciones tangibles y directas antes que discusiones puramente teóricas.",
    "I": "**Investigador (I):** Tu enfoque es analítico, intelectual y científico. Te apasiona diagnosticar la raíz de los problemas, auditar sistemas, analizar datos y comprender cómo funcionan las cosas a nivel profundo.",
    "A": "**Artístico (A):** Destacas por tu pensamiento original, creativo e independiente. Prefieres entornos de trabajo libres, expresivos y dinámicos donde puedas innovar visual, lingüística o conceptualmente.",
    "S": "**Social (S):** Tu motor principal es el factor humano, el sentido pedagógico y el bienestar comunitario. Tienes una gran facilidad para comunicar, enseñar, guiar y facilitar el desarrollo de otras personas.",
    "E": "**Emprendedor (E):** Posees una mente gerencial, líder y orientada a los resultados. Te sientes cómodo tomando decisiones bajo presión, coordinando equipos, gestionando proyectos independientes y vendiendo ideas innovadoras.",
    "C": "**Convencional (C):** Tu fuerte es la estructura, la organización minuciosa, el control de procesos y la gestión de datos estructurados. Prefieres metodologías claras, orden lógico y flujos operativos eficientes."
}

# --- TRADUCCIÓN DE INTELIGENCIAS (GARDNER) ---
DESCRIPCIONES_GARDNER = {
    "LV": "Inteligencia Lingüístico-Verbal (Habilidad para evasión y estructurar ideas mediante la palabra y la oratoria).",
    "LM": "Inteligencia Lógico-Matemática (Capacidad analítica, pensamiento estructurado, razonamiento computacional y manejo de datos).",
    "VE": "Inteligencia Visual-Espacial (Destreza para el diseño gráfico, interfaces, mapas conceptuales y distribución espacial).",
    "KC": "Inteligencia Kinestésico-Corporal (Coordinación psicomotriz, precisión manual y experimentación física).",
    "MU": "Inteligencia Musical (Sensibilidad acústica, edición de audio, ritmo y composición estructural).",
    "ER": "Inteligencia Interpersonal (Empatía, liderazgo, lectura del entorno social y mediación de conflictos).",
    "RA": "Inteligencia Intrapersonal (Autodisciplina, introspección profunda, autogestión y claridad de metas).",
    "NA": "Inteligencia Naturalista (Reconocimiento de patrones orgánicos, sostenibilidad, agricultura urbana y gestión ambiental).",
    "E": "Perfil Emprendedor (Capacidad innata para identificar oportunidades, liderar iniciativas, gestionar recursos y materializar proyectos)."
}

# --- BANCO GENERAL DE CARRERAS CON SUS "ETIQUETAS" DE ENTRADA ---
BANCO_CARRERAS = [
    {
        "nombre": "Tecnología Educativa e Informática Aplicada (EdTech)",
        "descripcion": "Dirección y diseño de plataformas e-learning, sistemas de evaluación digital, entornos de aprendizaje virtual y docencia tecnológica en entornos de innovación.",
        "holland_requeridos": ["S", "E", "I", "C"],
        "gardner_requeridos": ["LM", "LV", "ER", "E"]
    },
    {
        "nombre": "Dirección y Gerencia de Proyectos Tecnológicos",
        "descripcion": "Liderazgo estratégico de equipos interdisciplinarios de desarrollo de software, optimización de infraestructura de hardware, planificación presupuestaria e implementación de soluciones lógicas.",
        "holland_requeridos": ["E", "I", "C", "R"],
        "gardner_requeridos": ["E", "ER", "LM"]
    },
    {
        "nombre": "Diseño de Experiencia de Usuario y Branding Digital (UX/UI)",
        "descripcion": "Modelado visual de aplicaciones, diseño de interfaces web interactivas, maquetación de flujos de usuario y gestión de identidad de marca corporativa.",
        "holland_requeridos": ["A", "R", "E"],
        "gardner_requeridos": ["VE", "LM", "KC", "E"]
    },
    {
        "nombre": "Ingeniería de Sistemas y Auditoría de Software",
        "descripcion": "Desarrollo de sistemas de gran escala, arquitectura de bases de datos, control de procesos lógicos y seguridad informática corporativa.",
        "holland_requeridos": ["I", "R", "C"],
        "gardner_requeridos": ["LM", "VE", "RA"]
    },
    {
        "nombre": "Gestión de Agronegocios Sostenibles y Bio-Ecosistemas",
        "descripcion": "Desarrollo empresarial e industrialización de productos artesanales fermentados, optimización de agricultura urbana, compostaje técnico y preservación ambiental basada en datos.",
        "holland_requeridos": ["I", "R", "S", "E"],
        "gardner_requeridos": ["NA", "E", "LM", "RA"]
    }
]