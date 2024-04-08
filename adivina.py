import pygame
import sys
import random

# Inicializar pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)

# Obtener el tamaño de la pantalla
ANCHO = pygame.display.Info().current_w
ALTO = pygame.display.Info().current_h

# Configurar la pantalla en modo de pantalla completa
pantalla = pygame.display.set_mode((ANCHO, ALTO), pygame.FULLSCREEN)
pygame.display.set_caption("Adivina Quién")

# Cargar imágenes
fondo = pygame.image.load("adivinaquienportada.png")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))  # Redimensionar al tamaño de la pantalla
boton_jugar_img = pygame.image.load("adivinaquienjugar.png")
boton_jugar_img = pygame.transform.scale(boton_jugar_img, (ANCHO // 10, ALTO // 10))  # Redimensionar
boton_salir_img = pygame.image.load("adivinaquiensalir.png")
boton_salir_img = pygame.transform.scale(boton_salir_img, (ANCHO // 15, ALTO // 15))  # Redimensionar
personaje_img = pygame.image.load("adivinaquien.png")
personaje_img = pygame.transform.scale(personaje_img, (ANCHO // 1.5, ALTO))
fondo_juego = pygame.image.load("adivinaquienfondo.png")
fondo_juego = pygame.transform.scale(fondo_juego, (ANCHO, ALTO))  # Redimensionar al tamaño de la pantalla
boton_si_img = pygame.image.load("si.png")
boton_si_img = pygame.transform.scale(boton_si_img, (ANCHO // 8, ALTO // 12))  # Redimensionar
boton_no_img = pygame.image.load("no.png")
boton_no_img = pygame.transform.scale(boton_no_img, (ANCHO // 8, ALTO // 12))  # Redimensionar
marco_img = pygame.image.load("adivinaquienmarcoverde.png")
marco_img = pygame.transform.scale(marco_img, (ANCHO//9.5, ALTO //6.2))
boton_rnc_img = pygame.image.load("adivinaquienreiniciar.png")
boton_rnc_img = pygame.transform.scale(boton_rnc_img, (ANCHO // 10, ALTO // 10))  # Redimensionar
mono_img = pygame.image.load("mono.png")
mono_img = pygame.transform.scale(mono_img, (ANCHO // 5, ALTO // 5))  # Redimensionar
sorpresa_img = pygame.image.load("sorpresa.png")
sorpresa_img = pygame.transform.scale(sorpresa_img, (ANCHO // 5, ALTO // 5))  # Redimensionar
pat_img = pygame.image.load("patricio.png")
pat_img = pygame.transform.scale(pat_img, (ANCHO // 5, ALTO // 5))  # Redimensionar
falle_img = pygame.image.load("falle.png")
falle_img = pygame.transform.scale(falle_img, (ANCHO // 5, ALTO // 5))  # Redimensionar

# Imagen para rellenar cuando se necesite cambiar de pregunta
prellenar_img = pygame.image.load("prellenar.png")
prellenar_img = pygame.transform.scale(prellenar_img, (ANCHO // 5, ALTO // 5))  # Redimensionar

# Imagenes de las posibles preguntas
ptieneojos_img = pygame.image.load("ptieneojos.png")
ptieneojos_img = pygame.transform.scale(ptieneojos_img, (ANCHO // 5, ALTO // 5))  # Redimensionar
pojosnegros_img = pygame.image.load("pojosnegros.png")
pojosnegros_img = pygame.transform.scale(pojosnegros_img, (ANCHO // 5, ALTO // 5))  # Redimensionar
pojosverdes_img = pygame.image.load("pojosverdes.png")
pojosverdes_img = pygame.transform.scale(pojosverdes_img, (ANCHO // 5, ALTO // 5))  # Redimensionar
pojosazules_img = pygame.image.load("pojosazules.png")
pojosazules_img = pygame.transform.scale(pojosazules_img, (ANCHO // 5, ALTO // 5))  # Redimensionar
ptienecabello_img = pygame.image.load("ptienecabello.png")
ptienecabello_img = pygame.transform.scale(ptienecabello_img, (ANCHO // 5, ALTO // 5))  # Redimensionar
ptienebarba_img = pygame.image.load("ptienebarba.png")
ptienebarba_img = pygame.transform.scale(ptienebarba_img,(ANCHO // 5, ALTO // 5))  # Redimensionar
ppelonegro_img = pygame.image.load("ppelonegro.png")
ppelonegro_img = pygame.transform.scale(ppelonegro_img, (ANCHO // 5, ALTO // 5))  # Redimensionar
ppelorubio_img = pygame.image.load("ppelorubio.png")
ppelorubio_img = pygame.transform.scale(ppelorubio_img, (ANCHO // 5, ALTO // 5))  # Redimensionar
ppelocafe_img = pygame.image.load("ppelocafe.png")
ppelocafe_img = pygame.transform.scale(ppelocafe_img, (ANCHO // 5, ALTO // 5))  # Redimensionar
ppelorojo_img = pygame.image.load("ppelorojo.png")
ppelorojo_img = pygame.transform.scale(ppelorojo_img, (ANCHO // 5, ALTO // 5))  # Redimensionar
ppelogris_img = pygame.image.load("ppelogris.png")
ppelogris_img = pygame.transform.scale(ppelogris_img, (ANCHO // 5, ALTO // 5))  # Redimensionar
ptienesombrero_img = pygame.image.load("ptienesombrero.png")
ptienesombrero_img = pygame.transform.scale(ptienesombrero_img, (ANCHO // 5, ALTO // 5))  # Redimensionar
ptienelentes_img = pygame.image.load("ptienelentes.png")
ptienelentes_img = pygame.transform.scale(ptienelentes_img, (ANCHO // 5, ALTO // 5))  # Redimensionar
phombre_img = pygame.image.load("phombre.png")
phombre_img = pygame.transform.scale(phombre_img, (ANCHO // 5, ALTO // 5))  # Redimensionar
ppiel_clara_img = pygame.image.load("ppielclara.png")
ppiel_clara_img = pygame.transform.scale(ppiel_clara_img, (ANCHO // 5, ALTO // 5))  # Redimensionar
ppiel_naranja_img = pygame.image.load("ppielrojamarilla.png")
ppiel_naranja_img = pygame.transform.scale(ppiel_naranja_img, (ANCHO // 5, ALTO // 5))  # Redimensionar
ppiel_morena_img = pygame.image.load("ppielmorena.png")
ppiel_morena_img = pygame.transform.scale(ppiel_morena_img, (ANCHO // 5, ALTO // 5))  # Redimensionar
ppiel_oscura_img = pygame.image.load("ppieloscura.png")
ppiel_oscura_img = pygame.transform.scale(ppiel_oscura_img, (ANCHO // 5, ALTO // 5))  # Redimensionar
pfallo_img = pygame.image.load("fallo.png")
pfallo_img = pygame.transform.scale(pfallo_img, (ANCHO // 5, ALTO // 5))  # Redimensionar
pexito_img = pygame.image.load("exito.png")
pexito_img = pygame.transform.scale(pexito_img, (ANCHO // 5, ALTO // 5))  # Redimensionar
pno_img = pygame.image.load("pnoencontro.png")
pno_img = pygame.transform.scale(pno_img, (ANCHO // 5, ALTO // 5))  # Redimensionar

# Imagen de la pregunta final
presultado_img = pygame.image.load("presultado.png")
presultado_img = pygame.transform.scale(presultado_img, (ANCHO // 5, ALTO // 5))  # Redimensionar

# Mantener una lista de las preguntas restantes
preguntas_restantes = [ptieneojos_img, ptienecabello_img, ptienebarba_img, ptienesombrero_img, ptienelentes_img, phombre_img, ppiel_clara_img, ppiel_naranja_img, ppiel_morena_img, ppiel_oscura_img]

# Definir la posición de los botones
boton_jugar_rect = boton_jugar_img.get_rect()
boton_jugar_rect.center = (ANCHO // 2, ALTO // 1.2)
boton_salir_rect = boton_salir_img.get_rect()
boton_salir_rect.center = (ANCHO // 20, ALTO // 18)
boton_si_rect = boton_si_img.get_rect()
boton_si_rect.center = (ANCHO // 10, ALTO // 1.5)
boton_no_rect = boton_no_img.get_rect()
boton_no_rect.center = (ANCHO // 3.7, ALTO // 1.5)
boton_rnc_rect = boton_rnc_img.get_rect()
boton_rnc_rect.center = (ANCHO // 5.5, ALTO //1.2)

# Definir la base de datos de personajes
personajes = [
    {"nombre": "Moises",    "ojos_visibles": True,  "ojos": "negros", "tiene_cabello": True,  "tiene_barba": True,  "pelo": "gris",  "sombrero": True,  "gafas": False, "hombre": True,  "piel": "oscura"},
    {"nombre": "Zuhra",     "ojos_visibles": True,  "ojos": "verdes", "tiene_cabello": True,  "tiene_barba": False, "pelo": "negro", "sombrero": True,  "gafas": False, "hombre": False, "piel": "morena"},
    {"nombre": "Roberto",   "ojos_visibles": True,  "ojos": "negros", "tiene_cabello": False, "tiene_barba": True,  "pelo": "rojo",  "sombrero": False, "gafas": False, "hombre": True,  "piel": "clara"},
    {"nombre": "Carolina",  "ojos_visibles": True,  "ojos": "negros", "tiene_cabello": True,  "tiene_barba": False, "pelo": "cafe",  "sombrero": True,  "gafas": False, "hombre": False, "piel": "clara"},
    {"nombre": "Rolando",   "ojos_visibles": True,  "ojos": "negros", "tiene_cabello": True,  "tiene_barba": False, "pelo": "negro", "sombrero": True,  "gafas": False, "hombre": True,  "piel": "morena"},
    {"nombre": "Anastasia", "ojos_visibles": True,  "ojos": "negros", "tiene_cabello": True,  "tiene_barba": False, "pelo": "rojo",  "sombrero": False, "gafas": False, "hombre": False, "piel": "clara"},
    {"nombre": "Ankit",     "ojos_visibles": True,  "ojos": "negros", "tiene_cabello": True,  "tiene_barba": True,  "pelo": "gris",  "sombrero": False, "gafas": True,  "hombre": True,  "piel": "morena"},
    {"nombre": "Vinita",    "ojos_visibles": True,  "ojos": "negros", "tiene_cabello": True,  "tiene_barba": False, "pelo": "negro", "sombrero": False, "gafas": False, "hombre": False, "piel": "morena"},
    {"nombre": "Joshua",    "ojos_visibles": True,  "ojos": "negros", "tiene_cabello": True,  "tiene_barba": True,  "pelo": "negro", "sombrero": True,  "gafas": False, "hombre": True,  "piel": "naranja"},
    {"nombre": "Alima",     "ojos_visibles": True,  "ojos": "negros", "tiene_cabello": False, "tiene_barba": False, "pelo": "no",    "sombrero": True,  "gafas": False, "hombre": False, "piel": "oscura"},
    {"nombre": "Carlos",    "ojos_visibles": True,  "ojos": "negros", "tiene_cabello": False, "tiene_barba": True,  "pelo": "gris",  "sombrero": True,  "gafas": False, "hombre": True,  "piel": "naranja"},
    {"nombre": "Carmen",    "ojos_visibles": True,  "ojos": "negros", "tiene_cabello": True,  "tiene_barba": False, "pelo": "negro", "sombrero": True,  "gafas": False, "hombre": False, "piel": "naranja"},
    {"nombre": "Paul",      "ojos_visibles": True,  "ojos": "negros", "tiene_cabello": True,  "tiene_barba": True,  "pelo": "negro", "sombrero": True,  "gafas": False, "hombre": True,  "piel": "oscura"},
    {"nombre": "Elsa",      "ojos_visibles": True,  "ojos": "azules", "tiene_cabello": True,  "tiene_barba": False, "pelo": "rubio", "sombrero": False, "gafas": False, "hombre": False, "piel": "clara"},
    {"nombre": "John",      "ojos_visibles": False, "ojos": "no",     "tiene_cabello": True,  "tiene_barba": True,  "pelo": "negro", "sombrero": False, "gafas": True,  "hombre": True,  "piel": "clara"},
    {"nombre": "Hermela",   "ojos_visibles": True,  "ojos": "azules", "tiene_cabello": False, "tiene_barba": False, "pelo": "no",    "sombrero": True,  "gafas": False, "hombre": False, "piel": "oscura"},
    {"nombre": "Arnold",    "ojos_visibles": True,  "ojos": "negros", "tiene_cabello": True,  "tiene_barba": False, "pelo": "cafe",  "sombrero": False, "gafas": False, "hombre": True,  "piel": "clara"},
    {"nombre": "Li",        "ojos_visibles": True,  "ojos": "negros", "tiene_cabello": True,  "tiene_barba": False, "pelo": "negro", "sombrero": False, "gafas": False, "hombre": False, "piel": "clara"},
    {"nombre": "Yonas",     "ojos_visibles": True,  "ojos": "negros", "tiene_cabello": True,  "tiene_barba": True,  "pelo": "negro", "sombrero": False, "gafas": False, "hombre": True,  "piel": "oscura"},
    {"nombre": "Rosa",      "ojos_visibles": True,  "ojos": "negros", "tiene_cabello": True,  "tiene_barba": False, "pelo": "negro", "sombrero": False, "gafas": False, "hombre": False, "piel": "naranja"},
    {"nombre": "Edward",    "ojos_visibles": True,  "ojos": "azules", "tiene_cabello": True,  "tiene_barba": True,  "pelo": "cafe",  "sombrero": True,  "gafas": False, "hombre": True,  "piel": "clara"},
    {"nombre": "Natalia",   "ojos_visibles": True,  "ojos": "negros", "tiene_cabello": True,  "tiene_barba": False, "pelo": "negro", "sombrero": False, "gafas": True,  "hombre": False, "piel": "morena"},
    {"nombre": "Hector",    "ojos_visibles": True,  "ojos": "negros", "tiene_cabello": True,  "tiene_barba": False, "pelo": "negro", "sombrero": True,  "gafas": True,  "hombre": True,  "piel": "morena"},
    {"nombre": "Elizabeth", "ojos_visibles": True,  "ojos": "negros", "tiene_cabello": True,  "tiene_barba": False, "pelo": "negro", "sombrero": False, "gafas": False, "hombre": False, "piel": "oscura"},
    {"nombre": "Mustafa",   "ojos_visibles": True,  "ojos": "verdes", "tiene_cabello": True,  "tiene_barba": True,  "pelo": "negro", "sombrero": True,  "gafas": False, "hombre": True,  "piel": "morena"}
]

personajes_elegibles = personajes

# Asociar cada imagen de pregunta con su nombre
preguntas_nombres = {
    ptieneojos_img: "o",
    pojosnegros_img: "on",
    pojosverdes_img: "ov",
    pojosazules_img: "oa",
    ptienecabello_img: "c",
    ptienebarba_img: "b",
    ppelonegro_img: "pn",
    ppelorubio_img: "pru",
    ppelocafe_img: "pc",
    ppelorojo_img: "pro",
    ppelogris_img: "pg",
    ptienesombrero_img: "ps",
    ptienelentes_img: "pl",
    phombre_img: "h",
    ppiel_clara_img: "pcl",
    ppiel_naranja_img: "pna",
    ppiel_morena_img: "pmo",
    ppiel_oscura_img: "pos"
}

# Función para dibujar la pantalla
def dibujar_pantalla():
    pantalla.blit(fondo, (0, 0))
    pantalla.blit(boton_jugar_img, boton_jugar_rect)
    pygame.display.update()

# Función para mostrar la pantalla de juego con una pregunta aleatoria
def mostrar_pantalla_juego(preguntas_restantes):
    pantalla.blit(fondo_juego, (0, 0))
    pantalla.blit(personaje_img, (ANCHO // 3, 0))
    pantalla.blit(mono_img, (ANCHO //8, ALTO//10))
    pantalla.blit(boton_salir_img, boton_salir_rect)
    pantalla.blit(boton_si_img, boton_si_rect)
    pantalla.blit(boton_no_img, boton_no_rect)
    pantalla.blit(boton_rnc_img, boton_rnc_rect)
    if preguntas_restantes:
        pregunta_aleatoria = random.choice(preguntas_restantes)
        pantalla.blit(pregunta_aleatoria, (ANCHO // 12, ALTO // 3))  # Mostrar la pregunta aleatoria
    else:
        pantalla.blit(presultado_img, (ANCHO // 12, ALTO // 3))  # Mostrar la imagen de resultado
        pygame.display.update()
        return None  # Retorna None para indicar que no hay pregunta
    pygame.display.update()
    return pregunta_aleatoria

# Definir el personaje de prueba
personaje_prueba = {
    "nombre": "Prueba",
    "ojos_visibles": "",
    "ojos": "",
    "tiene_cabello": "",
    "tiene_barba": "",
    "pelo": "",
    "sombrero": "",
    "gafas": "",
    "hombre":"",
    "piel": ""
}

# Función para encontrar coincidencias con el personaje de prueba
def encontrar_coincidencias(personaje_prueba, personajes_elegibles):
    coincidencias = []
    for personaje in personajes_elegibles:
        # Compara todas las características excepto el nombre
        if (personaje["ojos_visibles"] == personaje_prueba["ojos_visibles"] and
            personaje["ojos"] == personaje_prueba["ojos"] and
            personaje["tiene_cabello"] == personaje_prueba["tiene_cabello"] and
            personaje["tiene_barba"] == personaje_prueba["tiene_barba"] and
            personaje["pelo"] == personaje_prueba["pelo"] and
            personaje["sombrero"] == personaje_prueba["sombrero"] and
            personaje["gafas"] == personaje_prueba["gafas"] and
            personaje["hombre"] == personaje_prueba["hombre"] and
            personaje["piel"] == personaje_prueba["piel"]):
            
            coincidencias.append(personaje)
    return coincidencias

# Llama a la función para encontrar coincidencias y muestra los resultados
def mostrar_coincidencias():
    nombree = ""
    coincidencias = encontrar_coincidencias(personaje_prueba, personajes_elegibles)
    for personaje in coincidencias:
        nombree = personaje["nombre"]
        if personaje["nombre"]=="Moises":
            pantalla.blit(marco_img, (ANCHO // 2.7, ALTO // 17)) #Moises
        elif personaje["nombre"]=="Zuhra":
            pantalla.blit(marco_img, (ANCHO // 2.03, ALTO // 17)) #Zuhra
        elif personaje["nombre"]=="Roberto":
            pantalla.blit(marco_img, (ANCHO // 1.63, ALTO // 17)) #Roberto
        elif personaje["nombre"]=="Carolina":
            pantalla.blit(marco_img, (ANCHO // 1.365, ALTO // 17)) #Carolina
        elif personaje["nombre"]=="Rolando":
            pantalla.blit(marco_img, (ANCHO // 1.17, ALTO // 17)) #Rolando
        elif personaje["nombre"]=="Anastasia":
            pantalla.blit(marco_img, (ANCHO // 2.7, ALTO // 4.26)) #Anastasia
        elif personaje["nombre"]=="Ankit":
            pantalla.blit(marco_img, (ANCHO // 2.03, ALTO // 4.26)) #Ankit
        elif personaje["nombre"]=="Vinita":
            pantalla.blit(marco_img, (ANCHO // 1.63, ALTO // 4.26)) #Vinita
        elif personaje["nombre"]=="Joshua":
            pantalla.blit(marco_img, (ANCHO // 1.365, ALTO // 4.26)) #Joshua
        elif personaje["nombre"]=="Alima":
            pantalla.blit(marco_img, (ANCHO // 1.17, ALTO // 4.26)) #Alima
        elif personaje["nombre"]=="Carlos":
            pantalla.blit(marco_img, (ANCHO // 2.7, ALTO // 2.4)) #Carlos
        elif personaje["nombre"]=="Carmen":
            pantalla.blit(marco_img, (ANCHO // 2.03, ALTO // 2.4)) #Carmen
        elif personaje["nombre"]=="Paul":
            pantalla.blit(marco_img, (ANCHO // 1.63, ALTO // 2.4)) #Paul
        elif personaje["nombre"]=="Elsa":
            pantalla.blit(marco_img, (ANCHO // 1.365, ALTO // 2.4)) #Elsa
        elif personaje["nombre"]=="John":
            pantalla.blit(marco_img, (ANCHO // 1.17, ALTO // 2.4)) #John
        elif personaje["nombre"]=="Hermela":
            pantalla.blit(marco_img, (ANCHO // 2.7, ALTO // 1.66)) #Hermela
        elif personaje["nombre"]=="Arnold":
            pantalla.blit(marco_img, (ANCHO // 2.03, ALTO // 1.66)) #Arnold
        elif personaje["nombre"]=="Li":
            pantalla.blit(marco_img, (ANCHO // 1.63, ALTO // 1.66)) #Li
        elif personaje["nombre"]=="Yonas":
            pantalla.blit(marco_img, (ANCHO // 1.365, ALTO // 1.66)) #Yonas
        elif personaje["nombre"]=="Rosa":
            pantalla.blit(marco_img, (ANCHO // 1.17, ALTO // 1.66)) #Rosa
        elif personaje["nombre"]=="Edward":
            pantalla.blit(marco_img, (ANCHO // 2.7, ALTO // 1.27)) #Edward
        elif personaje["nombre"]=="Natalia":
            pantalla.blit(marco_img, (ANCHO // 2.03, ALTO // 1.27)) #Natalia
        elif personaje["nombre"]=="Hector":
            pantalla.blit(marco_img, (ANCHO // 1.63, ALTO // 1.27)) #Hector
        elif personaje["nombre"]=="Elizabeth":
            pantalla.blit(marco_img, (ANCHO // 1.365, ALTO // 1.27)) #Elizabeth
        elif personaje["nombre"]=="Mustafa":
            pantalla.blit(marco_img, (ANCHO // 1.17, ALTO // 1.27)) #Mustafa
        
    pygame.display.update()
    return nombree

# Función principal del juego
def jugar():
    dibujar_pantalla()
    preguntaspelo = 0
    peloya = 0
    yamostre = 0
    # Bucle principal del juego
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Verificar si se ha hecho clic en el botón "Jugar"
                if boton_jugar_rect.collidepoint(event.pos):
                    pregunta_actual = mostrar_pantalla_juego(preguntas_restantes)
                # Verificar si se ha hecho clic en el botón "Salir"
                elif boton_salir_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                # Verificar si se ha hecho clic en el botón "Reiniciar"
                elif boton_rnc_rect.collidepoint(event.pos):
                    preguntaspelo = 0
                    peloya = 0
                    yamostre = 0
                    personaje_prueba["ojos_visibles"] = ""
                    personaje_prueba["ojos"] = ""
                    personaje_prueba["tiene_cabello"] = ""
                    personaje_prueba["tiene_barba"] = ""
                    personaje_prueba["pelo"] = ""
                    personaje_prueba["sombrero"] = ""
                    personaje_prueba["gafas"] = ""
                    personaje_prueba["hombre"] = ""
                    personaje_prueba["piel"] = ""
                    preguntas_restantes.clear()
                    preguntas_restantes.append(ptieneojos_img)
                    preguntas_restantes.append(ptienecabello_img)
                    preguntas_restantes.append(ptienebarba_img)
                    preguntas_restantes.append(ptienesombrero_img)
                    preguntas_restantes.append(ptienelentes_img)
                    preguntas_restantes.append(phombre_img)
                    preguntas_restantes.append(ppiel_clara_img)
                    preguntas_restantes.append(ppiel_naranja_img)
                    preguntas_restantes.append(ppiel_morena_img)
                    preguntas_restantes.append(ppiel_oscura_img)
                    pantalla.blit(prellenar_img, (ANCHO // 12, ALTO // 3))  # Borrar la pantalla
                    pregunta_actual = mostrar_pantalla_juego(preguntas_restantes)
                    pygame.display.update()
                # Verificar si se ha hecho clic en el botón "Sí"
                elif boton_si_rect.collidepoint(event.pos):
                    if yamostre == 1:
                        pantalla.blit(prellenar_img, (ANCHO // 12, ALTO // 3))  # Borrar la pantalla
                        pantalla.blit(pexito_img, (ANCHO // 12, ALTO // 3))  # Mostrar la imagen de exito
                        pantalla.blit(pat_img, (ANCHO //8, ALTO//10))
                        pygame.display.update()
                        yamostre = 2
                    elif yamostre == 0:
                        if preguntas_restantes:
                            pantalla.blit(prellenar_img, (ANCHO // 12, ALTO // 3))  # Borrar la pregunta actual
                            pygame.display.update()
                            if preguntas_nombres.get(pregunta_actual) == "o":
                                personaje_prueba["ojos_visibles"] = True
                                preguntas_restantes.append(pojosnegros_img)
                                preguntas_restantes.append(pojosverdes_img)
                                preguntas_restantes.append(pojosazules_img)
                            if preguntas_nombres.get(pregunta_actual) == "on":
                                personaje_prueba["ojos"] = "negros"
                                if preguntas_restantes.count(pojosverdes_img) == 1:
                                    preguntas_restantes.remove(pojosverdes_img)
                                if preguntas_restantes.count(pojosazules_img) == 1:
                                    preguntas_restantes.remove(pojosazules_img)
                            if preguntas_nombres.get(pregunta_actual) == "ov":
                                personaje_prueba["ojos"] = "verdes"
                                if preguntas_restantes.count(pojosnegros_img) == 1:
                                    preguntas_restantes.remove(pojosnegros_img)
                                if preguntas_restantes.count(pojosazules_img) == 1:
                                    preguntas_restantes.remove(pojosazules_img)
                            if preguntas_nombres.get(pregunta_actual) == "oa":
                                personaje_prueba["ojos"] = "azules"
                                if preguntas_restantes.count(pojosnegros_img) == 1:
                                    preguntas_restantes.remove(pojosnegros_img)
                                if preguntas_restantes.count(pojosverdes_img) == 1:
                                    preguntas_restantes.remove(pojosverdes_img)
                            if preguntas_nombres.get(pregunta_actual) == "c":
                                personaje_prueba["tiene_cabello"] = True
                                preguntaspelo = preguntaspelo + 1
                                if preguntaspelo >=0 and preguntaspelo <=1:
                                    if peloya == 0:
                                        preguntas_restantes.append(ppelonegro_img)
                                        preguntas_restantes.append(ppelorubio_img)
                                        preguntas_restantes.append(ppelocafe_img)
                                        preguntas_restantes.append(ppelorojo_img)
                                        preguntas_restantes.append(ppelogris_img)
                                        peloya = 1
                            if preguntas_nombres.get(pregunta_actual) == "b":
                                personaje_prueba["tiene_barba"] = True
                                preguntaspelo = preguntaspelo +1
                                if preguntaspelo >=0 and preguntaspelo <=1:
                                    if peloya == 0:
                                        preguntas_restantes.append(ppelonegro_img)
                                        preguntas_restantes.append(ppelorubio_img)
                                        preguntas_restantes.append(ppelocafe_img)
                                        preguntas_restantes.append(ppelorojo_img)
                                        preguntas_restantes.append(ppelogris_img)
                                        peloya = 1
                            if preguntas_nombres.get(pregunta_actual) == "pn":
                                personaje_prueba["pelo"] = "negro"
                                if preguntas_restantes.count(ppelorubio_img) == 1:
                                    preguntas_restantes.remove(ppelorubio_img)
                                if preguntas_restantes.count(ppelocafe_img) == 1:
                                    preguntas_restantes.remove(ppelocafe_img)
                                if preguntas_restantes.count(ppelorojo_img) == 1:
                                    preguntas_restantes.remove(ppelorojo_img)
                                if preguntas_restantes.count(ppelogris_img) == 1:
                                    preguntas_restantes.remove(ppelogris_img)
                            if preguntas_nombres.get(pregunta_actual) == "pru":
                                personaje_prueba["pelo"] = "rubio"
                                if preguntas_restantes.count(ppelonegro_img) == 1:
                                    preguntas_restantes.remove(ppelonegro_img)
                                if preguntas_restantes.count(ppelocafe_img) == 1:
                                    preguntas_restantes.remove(ppelocafe_img)
                                if preguntas_restantes.count(ppelorojo_img) == 1:
                                    preguntas_restantes.remove(ppelorojo_img)
                                if preguntas_restantes.count(ppelogris_img) == 1:
                                    preguntas_restantes.remove(ppelogris_img)
                            if preguntas_nombres.get(pregunta_actual) == "pc":
                                personaje_prueba["pelo"] = "cafe"
                                if preguntas_restantes.count(ppelonegro_img) == 1:
                                    preguntas_restantes.remove(ppelonegro_img)
                                if preguntas_restantes.count(ppelorubio_img) == 1:
                                    preguntas_restantes.remove(ppelorubio_img)
                                if preguntas_restantes.count(ppelorojo_img) == 1:
                                    preguntas_restantes.remove(ppelorojo_img)
                                if preguntas_restantes.count(ppelogris_img) == 1:
                                    preguntas_restantes.remove(ppelogris_img)
                            if preguntas_nombres.get(pregunta_actual) == "pro":
                                personaje_prueba["pelo"] = "rojo"
                                if preguntas_restantes.count(ppelonegro_img) == 1:
                                    preguntas_restantes.remove(ppelonegro_img)
                                if preguntas_restantes.count(ppelorubio_img) == 1:
                                    preguntas_restantes.remove(ppelorubio_img)
                                if preguntas_restantes.count(ppelocafe_img) == 1:
                                    preguntas_restantes.remove(ppelocafe_img)
                                if preguntas_restantes.count(ppelogris_img) == 1:
                                    preguntas_restantes.remove(ppelogris_img)
                            if preguntas_nombres.get(pregunta_actual) == "pg":
                                personaje_prueba["pelo"] = "gris"
                                if preguntas_restantes.count(ppelonegro_img) == 1:
                                    preguntas_restantes.remove(ppelonegro_img)
                                if preguntas_restantes.count(ppelorubio_img) == 1:
                                    preguntas_restantes.remove(ppelorubio_img)
                                if preguntas_restantes.count(ppelocafe_img) == 1:
                                    preguntas_restantes.remove(ppelocafe_img)
                                if preguntas_restantes.count(ppelorojo_img) == 1:
                                    preguntas_restantes.remove(ppelorojo_img)
                            if preguntas_nombres.get(pregunta_actual) == "ps":
                                personaje_prueba["sombrero"] = True
                            if preguntas_nombres.get(pregunta_actual) == "pl":
                                personaje_prueba["gafas"] = True
                            if preguntas_nombres.get(pregunta_actual) == "h":
                                personaje_prueba["hombre"] = True
                            if preguntas_nombres.get(pregunta_actual) == "pcl":
                                personaje_prueba["piel"] = "clara"
                                if preguntas_restantes.count(ppiel_naranja_img) == 1:
                                    preguntas_restantes.remove(ppiel_naranja_img)
                                if preguntas_restantes.count(ppiel_morena_img) == 1:
                                    preguntas_restantes.remove(ppiel_morena_img)
                                if preguntas_restantes.count(ppiel_oscura_img) == 1:
                                    preguntas_restantes.remove(ppiel_oscura_img)
                            if preguntas_nombres.get(pregunta_actual) == "pna":
                                personaje_prueba["piel"] = "naranja"
                                if preguntas_restantes.count(ppiel_clara_img) == 1:
                                    preguntas_restantes.remove(ppiel_clara_img)
                                if preguntas_restantes.count(ppiel_morena_img) == 1:
                                    preguntas_restantes.remove(ppiel_morena_img)
                                if preguntas_restantes.count(ppiel_oscura_img) == 1:
                                    preguntas_restantes.remove(ppiel_oscura_img)
                            if preguntas_nombres.get(pregunta_actual) == "pmo":
                                personaje_prueba["piel"] = "morena"
                                if preguntas_restantes.count(ppiel_clara_img) == 1:
                                    preguntas_restantes.remove(ppiel_clara_img)
                                if preguntas_restantes.count(ppiel_naranja_img) == 1:
                                    preguntas_restantes.remove(ppiel_naranja_img)
                                if preguntas_restantes.count(ppiel_oscura_img) == 1:
                                    preguntas_restantes.remove(ppiel_oscura_img)
                            if preguntas_nombres.get(pregunta_actual) == "pos":
                                personaje_prueba["piel"] = "oscura"
                                if preguntas_restantes.count(ppiel_clara_img) == 1:
                                    preguntas_restantes.remove(ppiel_clara_img)
                                if preguntas_restantes.count(ppiel_naranja_img) == 1:
                                    preguntas_restantes.remove(ppiel_naranja_img)
                                if preguntas_restantes.count(ppiel_morena_img) == 1:
                                    preguntas_restantes.remove(ppiel_morena_img)
                            preguntas_restantes.remove(pregunta_actual)  # Eliminar la pregunta actual de la lista de preguntas restantes
                            if preguntas_restantes:  # Verificar si hay más preguntas restantes
                                pregunta_actual = mostrar_pantalla_juego(preguntas_restantes)  # Mostrar una nueva pregunta aleatoria
                            else:
                                resnom = mostrar_coincidencias()
                                if resnom == "":
                                    pantalla.blit(prellenar_img, (ANCHO // 12, ALTO // 3))  # Borrar la pregunta actual
                                    pantalla.blit(pno_img, (ANCHO // 12, ALTO // 3))
                                    pantalla.blit(falle_img, (ANCHO //8, ALTO//10))
                                    yamostre=4
                                else:
                                    yamostre = 1
                                pygame.display.update()
                        
                # Verificar si se ha hecho clic en el botón "No"
                elif boton_no_rect.collidepoint(event.pos):
                    if yamostre == 1:
                        pantalla.blit(prellenar_img, (ANCHO // 12, ALTO // 3))  # Borrar la pantalla
                        pantalla.blit(pfallo_img, (ANCHO // 12, ALTO // 3))  # Mostrar la imagen de exito
                        pantalla.blit(sorpresa_img, (ANCHO //8, ALTO//10))
                        pygame.display.update()
                        yamostre = 2
                    elif yamostre == 0:
                        if preguntas_restantes:
                            pantalla.blit(prellenar_img, (ANCHO // 12, ALTO // 3))  # Borrar la pregunta actual
                            pygame.display.update()
                            if preguntas_nombres.get(pregunta_actual) == "o":
                                personaje_prueba["ojos_visibles"] = False
                                personaje_prueba["ojos"] = "no"
                            if preguntas_nombres.get(pregunta_actual) == "on":
                                pruebavar = 0
                            if preguntas_nombres.get(pregunta_actual) == "ov":
                                pruebavar = 0
                            if preguntas_nombres.get(pregunta_actual) == "oa":
                                pruebavar = 0
                            if preguntas_nombres.get(pregunta_actual) == "c":
                                personaje_prueba["tiene_cabello"] = False
                                preguntaspelo = preguntaspelo - 1
                                if preguntaspelo == -2:
                                    personaje_prueba["pelo"] = "no"
                            if preguntas_nombres.get(pregunta_actual) == "b":
                                personaje_prueba["tiene_barba"] = False
                                preguntaspelo = preguntaspelo - 1
                                if preguntaspelo == -2:
                                    personaje_prueba["pelo"] = "no"
                                pruebavar = 0
                            if preguntas_nombres.get(pregunta_actual) == "pn":
                                pruebavar = 0
                            if preguntas_nombres.get(pregunta_actual) == "pru":
                                pruebavar = 0
                            if preguntas_nombres.get(pregunta_actual) == "pc":
                                pruebavar = 0
                            if preguntas_nombres.get(pregunta_actual) == "pro":
                                pruebavar = 0
                            if preguntas_nombres.get(pregunta_actual) == "pg":
                                pruebavar = 0
                            if preguntas_nombres.get(pregunta_actual) == "ps":
                                personaje_prueba["sombrero"] = False
                            if preguntas_nombres.get(pregunta_actual) == "pl":
                                personaje_prueba["gafas"] = False
                            if preguntas_nombres.get(pregunta_actual) == "h":
                                personaje_prueba["hombre"] = False
                            if preguntas_nombres.get(pregunta_actual) == "pcl":
                                pruebavar = 0
                            if preguntas_nombres.get(pregunta_actual) == "pna":
                                pruebavar = 0
                            if preguntas_nombres.get(pregunta_actual) == "pmo":
                                pruebavar = 0
                            if preguntas_nombres.get(pregunta_actual) == "pos":
                                pruebavar = 0
                            preguntas_restantes.remove(pregunta_actual)  # Eliminar la pregunta actual de la lista de preguntas restantes
                            if preguntas_restantes:  # Verificar si hay más preguntas restantes
                                pregunta_actual = mostrar_pantalla_juego(preguntas_restantes)  # Mostrar una nueva pregunta aleatoria
                            else:
                                pantalla.blit(presultado_img, (ANCHO // 12, ALTO // 3))  # Mostrar la imagen de resultado
                                resnom = mostrar_coincidencias()
                                if resnom == "":
                                    pantalla.blit(prellenar_img, (ANCHO // 12, ALTO // 3))  # Borrar la pregunta actual
                                    pantalla.blit(pno_img, (ANCHO // 12, ALTO // 3))
                                    pantalla.blit(falle_img, (ANCHO //8, ALTO//10))
                                    yamostre=4
                                else:
                                    yamostre = 1
                                pygame.display.update()
                                
                        
                        

# Iniciar el juego
if __name__ == "__main__":
    
    jugar()