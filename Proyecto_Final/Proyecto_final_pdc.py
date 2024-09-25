#Liberias a utilizar
from tkinter import *
from random import choice
from tkinter.messagebox import showwarning
from PIL import ImageTk, Image
import random
import time
import os
from unidecode import unidecode
import msvcrt

#declara variables globales
letras_usadas :list = []
vidas : int= 9
letras_acertadas : int = 0
juego_terminado : bool= False
opcion_nivel : int = 0

#Listas de palabras 
palabras_español : list =["abajo", "abierto", "abogado", "abrir", "abuelo", "acabar", "aceptar", "acerca", "acuerdo",
    "adelante", "además", "adiós", "admitir", "afectar", "agosto", "ahí", "ahora", "aire", "al",
    "alcanzar", "alegría", "algo", "alguien", "algún", "alrededor", "alto", "amable", "amar", "amigo",
    "amor", "análisis", "ancho", "andar", "animal", "anoche", "ante", "anterior", "antes", "antiguo",
    "anunciar", "año", "aparecer", "apenas", "aprender", "aprovechar", "aquí", "árbol", "arte", "asegurar",
    "así", "asunto", "atención", "atrás", "aumentar", "aún", "aunque", "autor", "autoridad", "avanzar",
    "ayer", "ayuda", "bajo", "banco", "bastante", "bien", "blanco", "boca", "boda", "bolsa",
    "bonito", "brazo", "bueno", "buscar", "cabeza", "cada", "caer", "calle", "cama", "cambio",
    "caminar", "campo", "cansado", "cantar", "capaz", "capital", "cara", "carácter", "carne", "carta",
    "casa", "casi", "caso", "cátedra", "causa", "celebrar", "centro", "cerca", "cerrar", "chico",
    "cielo", "ciencia", "cierto", "cinco", "cita", "ciudad", "claro", "clase", "coche", "coger",
    "comer", "comida", "compañero", "comprar", "común", "con", "conocer", "conseguir", "construir", "contar",
    "contra", "corazón", "correr", "cosa", "crear", "crecer", "creer", "crisis", "cruzar", "cuadro",
    "cuando", "cuanto", "cuatro", "cubrir", "cuerpo", "culpa", "cumplir", "curioso", "dar", "de",
    "deber", "decidir", "decir", "dedo", "defender", "dejar", "delante", "demasiado", "dentro", "derecho",
    "desarrollar", "desde", "después", "destino", "día", "diferente", "difícil", "dinero", "dios", "dirección",
    "director", "disculpa", "disfrutar", "divertido", "doble", "doctor", "dolor", "domingo", "donde", "dormir",
    "dos", "duda", "dueño", "durante", "echar", "edad", "educación", "efecto", "ejemplo", "ejercicio",
    "el", "ella", "ellos", "empezar", "empresa", "en", "encima", "encontrar", "energía", "enfermo",
    "enseñar", "entender", "entrar", "entregar", "enviar", "época", "equipo", "error", "escapar", "escuela",
    "ese", "esfuerzo", "espacio", "esperar", "espíritu", "esposa", "estar", "este", "estilo", "estoy",
    "estudio", "etapa", "evidente", "examen", "exigir", "existir", "éxito", "experiencia", "explicar", "expresión",
    "extender", "extraño", "fácil", "familia", "famoso", "fantástico", "favor", "feliz", "fenómeno", "fiesta",
    "figura", "final", "financiero", "flor", "fondo", "forma", "fortuna", "foto", "frase", "frente",
    "frío", "fuego", "fuente", "fuerte", "futuro", "ganar", "gente", "gesto", "girar", "gobierno",
    "golpe", "gracias", "grande", "gritar", "grupo", "guardar", "guerra", "gustar", "haber", "hablar",
    "hacer", "hacia", "hallar", "hermano", "héroe", "hija", "hijo", "historia", "hogar", "hombre",
    "hora", "hoy", "huir", "humano", "idea", "igual", "imagen", "imitar", "importante", "imposible",
    "incluir", "indicar", "información", "iniciar", "inmenso", "insistir", "instante", "intentar", "interés", "interior",
    "invierno", "ir", "izquierda", "jefe", "joven", "juego", "jugar", "juntos", "justo", "largo",
    "leer", "lejos", "lengua", "levantar", "libertad", "libro", "límite", "lindo", "línea", "llegar",
    "lleno", "llevar", "llorar", "luz", "madre", "malo", "mano", "mantener", "mar", "maravilloso",
    "margen", "más", "matar", "material", "mayo", "mejor", "memoria", "menor", "mensaje", "mente",
    "mercado", "mes", "meter", "mi", "miedo", "mientras", "mismo", "mitad", "modelo", "momento",
    "mover", "mucho", "mujer", "mundo", "música", "nacer", "nada", "nadie", "natural", "necesario",
    "necesitar", "negro", "ni", "ninguno", "niño", "nivel", "no", "noche", "nombre", "nosotros",
    "notar", "nueva", "nuevo", "nunca", "objetivo", "obligar", "obra", "observar", "obtener", "ocasión",
    "ocupar", "ocurrir", "oír", "olvidar", "operación", "opinar", "oponer", "origen", "otro", "pagar",
    "país", "palabra", "papel", "parecer", "parte", "pasar", "paso", "paz", "pedir", "pelear",
    "peligro", "pena", "pensar", "peor", "pequeño", "perder", "perfecto", "permitir", "pero", "persona",
    "pertenecer", "placer", "planta", "plaza", "pobre", "poder", "policía", "político", "poner", "por",
    "porque", "poseer", "posible", "práctica", "precio", "preciso", "preferir", "pregunta", "preparar", "presente",
    "presidente", "prestar", "primero", "principal", "problema", "proceso", "producir", "producto", "profesor", "profundo",
    "programa", "progreso", "prometer", "propio", "proteger", "proyecto", "prueba", "publicar", "pueblo", "puerta",
    "pues", "puesto", "punto", "puro", "quedar", "querer", "quien", "quitar", "rápido", "raro",
    "razón", "real", "realidad", "realizar", "recibir", "reciente", "reconocer", "recordar", "recorrer", "reducir",
    "referir", "región", "regresar", "relación", "repetir", "responder", "resto", "resultado", "retirar", "reunir",
    "revelar", "rico", "riesgo", "río", "rojo", "romper", "ropa", "rostro", "saber", "sacar",
    "sala", "salir", "salud", "salvar", "sangre", "santo", "se", "secreto", "sector", "seguir",
    "segundo", "seguro", "seis", "semana", "sentar", "sentido", "sentir"]

palabras_ingles : list= [
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "I",
    "it", "for", "not", "on", "with", "he", "as", "you", "do", "at", "this", "but", "his", "by", "from", "they", "we", "say", "her", "she",
    "or", "an", "will", "my", "one", "all", "would", "there", "their", "what","so", "up", "out", "if", "about", "who", "get", "which", "go", "me",
    "when", "make", "can", "like", "time", "no", "just", "him", "know", "take","people", "into", "year", "your", "good", "some", "could", "them", "see", "other",
    "than", "then", "now", "look", "only", "come", "its", "over", "think", "also","back", "after", "use", "two", "how", "our", "work", "first", "well", "way",
    "even", "new", "want", "because", "any", "these", "give", "day", "most", "us", "is", "are", "was", "were", "am", "been", "has", "had", "were", "become",
    "more", "such", "must", "shall", "should", "might", "ask", "much", "find", "many","right", "left", "need", "put", "last", "long", "never", "always", "next", "while",
    "few", "both", "same", "feel", "great", "part", "little", "every", "another", "place","over", "under", "home", "still", "high", "something", "too", "nothing", "call", "show",
    "try", "move", "keep", "let", "stop", "begin", "talk", "run", "walk", "play","live", "help", "read", "write", "sit", "stand", "close", "open", "hear", "watch",
    "listen", "talk", "love", "hate", "believe", "wait", "carry", "give", "hold", "bring","tell", "ask", "follow", "remember", "meet", "leave", "reach", "start", "end", "stay",
    "pay", "teach", "learn", "buy", "sell", "fall", "cut", "grow", "break", "draw","fight", "kill", "save", "lose", "win", "jump", "hit", "throw", "catch", "build",
    "push", "pull", "drive", "fly", "ride", "swim", "climb", "turn", "pick", "drop","change", "cook", "eat", "drink", "wash", "clean", "dry", "cut", "fix", "repair",
    "paint", "fold", "plant", "hide", "find", "wish", "hope", "plan", "choose", "share","join", "send", "show", "print", "draw", "write", "give", "receive", "borrow", "lend",
    "steal", "cheat", "break", "burn", "dig", "fall", "climb", "drive", "ride", "sail","swim", "fly", "travel", "rest", "sleep", "dream", "smile", "laugh", "cry", "shout",
    "whisper", "sing", "dance", "read", "write", "play", "paint", "draw", "run", "walk","jump", "sit", "stand", "lie", "turn", "stop", "start", "wait", "go", "come",
    "take", "give", "get", "put", "find", "lose", "open", "close", "begin", "finish","eat", "drink", "cook", "clean", "fix", "repair", "wash", "dry", "fold", "cut",
    "drive", "ride", "fly", "sail", "swim", "climb", "walk", "run", "jump", "skip", "rest", "sleep", "wake", "dream", "smile", "laugh", "cry", "shout", "talk", "speak",
    "listen", "hear", "see", "watch", "look", "show", "tell", "ask", "answer", "teach","learn", "study", "think", "know", "understand", "remember", "forget", "believe", "hope", "wish",
    "need", "want", "like", "love", "hate", "enjoy", "prefer", "choose", "decide", "plan","try", "fail", "win", "lose", "start", "stop", "continue", "begin", "finish", "work",
    "play", "rest", "help", "care", "ask", "answer", "give", "receive", "send", "bring","take", "buy", "sell", "pay", "borrow", "lend", "keep", "lose", "find", "break"
]
palabras_frances : list = [
    "le", "de", "un", "être", "et", "à", "en", "avoir", "que", "pour",
    "dans", "ce", "il", "qui", "ne", "sur", "se", "pas", "plus", "pouvoir","par", "je", "avec", "tout", "faire", "son", "mettre", "autre", "on", "mais",
    "nous", "comme", "ou", "si", "leur", "y", "dire", "elle", "devoir", "avant","deux", "même", "prendre", "aussi", "celui", "donner", "bien", "où", "fois", "vous",
    "encore", "nouveau", "aller", "entre", "premier", "vouloir", "déjà", "grand", "mon", "me","moins", "aucun", "lui", "temps", "savoir", "falloir", "voir", "quelque", "sans", "raison",
    "notre", "dont", "non", "an", "monde", "jour", "monsieur", "demander", "alors", "après","trouver", "personne", "rendre", "part", "dernier", "venir", "pendant", "passer", "peu", "lequel",
    "suite", "bon", "comprendre", "depuis", "point", "ainsi", "heure", "rester", "toujours", "tenir","porte", "parler", "fort", "montrer", "continuer", "penser", "entendre", "travailler", "commencer", "marcher",
    "garder", "aimer", "attendre", "arriver", "chercher", "sortir", "revenir", "appeler", "recevoir", "écrire","répondre", "vivre", "ouvrir", "changer", "arrêter", "perdre", "expliquer", "considérer", "gagner", "exister",
    "refuser", "lire", "réussir", "traverser", "décider", "produire", "utiliser", "préparer", "apprendre", "choisir","développer", "reconnaître", "permettre", "aider", "jouer", "apporter", "élever", "former", "créer", "offrir",
    "suivre", "réaliser", "accepter", "agir", "ajouter", "apparaître", "atteindre", "avancer", "changer", "chercher","compter", "conduire", "connaître", "construire", "courir", "couvrir", "croire", "découvrir", "défendre", "décrire",
    "décider", "développer", "dire", "disparaître", "dormir", "écouter", "écrire", "empêcher", "entendre", "entrer","envoyer", "espérer", "essayer", "établir", "éviter", "expliquer", "faire", "falloir", "fermer", "finir",
    "gagner", "garder", "habiter", "ignorer", "imaginer", "importer", "informer", "installer", "intéresser", "inviter","jouer", "laisser", "lire", "maintenir", "manger", "marcher", "montrer", "mourir", "naître", "obtenir",
    "offrir", "ouvrir", "parler", "partir", "passer", "penser", "perdre", "permettre", "plaire", "porter","poser", "pouvoir", "prendre", "préparer", "présenter", "prévenir", "produire", "proposer", "protéger", "quitter",
    "raconter", "recevoir", "reconnaître", "réduire", "refuser", "regarder", "rejoindre", "remarquer", "remettre", "remplacer","rencontrer", "rendre", "répondre", "reposer", "rester", "retenir", "retirer", "retourner", "réussir", "revenir",
    "rire", "savoir", "sembler", "sentir", "servir", "sortir", "souffrir", "souhaiter", "suivre", "tenir","terminer", "tirer", "tomber", "tourner", "travailler", "trouver", "utiliser", "venir", "vivre", "voir",
    "vouloir"
]
palabras_aleman : list = [
    "der", "die", "und", "sein", "in", "ein", "zu", "haben", "ich", "werden",
    "sie", "von", "nicht", "mit", "es", "sich", "auch", "auf", "für", "an", "er", "so", "dass", "können", "dies", "als", "ihr", "ja", "wie", "bei",
    "oder", "wir", "aber", "dann", "man", "da", "sein", "noch", "nach", "was", "wenn", "nur", "müssen", "sagen", "um", "über", "machen", "kein", "mein", "schon",
    "vor", "durch", "geben", "mehr", "andere", "viel", "kommen", "jetzt", "sollen", "mir","wollen", "gehen", "wissen", "sehen", "lassen", "uns", "unter", "weil", "stehen", "jed",
    "immer", "denn", "warum", "ganz", "neu", "gut", "finden", "bleiben", "arbeiten", "leben",
    "nehmen", "brauchen", "wieder", "sehen", "sagen", "spielen", "laufen", "lesen", "schreiben", "lernen","essen", "trinken", "fahren", "fliegen", "schlafen", "wachen", "denken", "glauben", "hoffen", "lieben",
    "hassen", "fühlen", "hören", "sprechen", "fragen", "antworten", "beginnen", "enden", "öffnen", "schließen","kaufen", "verkaufen", "gewinnen", "verlieren", "suchen", "finden", "treffen", "verstehen", "erklären", "entscheiden",
    "vergessen", "erinnern", "erreichen", "verlassen", "bleiben", "reisen", "fahren", "laufen", "springen", "fallen", "steigen", "sitzen", "stehen", "liegen", "halten", "tragen", "ziehen", "drücken", "werfen", "fangen",
    "schlagen", "treten", "beißen", "lecken", "riechen", "sehen", "hören", "fühlen", "schmecken", "denken","glauben", "wissen", "verstehen", "lernen", "lehren", "arbeiten", "spielen", "kämpfen", "lieben", "hassen",
    "hoffen", "fürchten", "freuen", "ärgern", "weinen", "lachen", "singen", "tanzen", "malen", "schreiben","lesen", "rechnen", "zählen", "messen", "wiegen", "schneiden", "kleben", "nähen", "stricken", "häkeln",
    "bauen", "zerstören", "pflanzen", "ernten", "kochen", "backen", "braten", "dünsten", "grillen", "schälen","schneiden", "reiben", "mischen", "rühren", "gießen", "trinken", "essen", "schlafen", "wachen", "träumen",
    "denken", "glauben", "wissen", "verstehen", "lernen", "lehren", "arbeiten", "spielen", "kämpfen", "lieben", "hassen", "hoffen", "fürchten", "freuen", "ärgern", "weinen", "lachen", "singen", "tanzen", "malen",
    "schreiben", "lesen", "rechnen", "zählen", "messen", "wiegen", "schneiden", "kleben", "nähen", "stricken", "häkeln", "bauen", "zerstören", "pflanzen", "ernten", "kochen", "backen", "braten", "dünsten", "grillen"
]

# Se utiliza para eliminar los acentos presentes en algunas palabras para que en el momento de la ejecucion no se presente ningun inconveniente
def eliminar_acentos(texto):
    return unidecode(texto) # convierte los caracteres especiales en sus equivalentes ASCII.

texto_con_acentos : str= "áéíóú ÁÉÍÓÚ ñ Ñ ü Ü"
texto_sin_acentos = eliminar_acentos(texto_con_acentos)

#Funciones que recorre la lista en español y seleccion todas las palabras que cumplan con la condicion de acuerdo a la longitud de cada palabra
def facil (palabra : str):
        if len(palabra) < 5:
            return True  
        
def medio(palabra : str):
    if len(palabra) >= 5 and len(palabra) <= 8:
        for i in palabra:
            if palabra.count(i) <= 3:
                return True
            else:
                return False
    else:
        return False
    
def dificil(palabra : str):
    if len(palabra) > 8:
        for i in palabra:
            if palabra.count(i) <= 2:
                return True
            else:
                return False
    else:
        return False    
    
# Se crean listas de acuerdo a la longitud de cada palabra, ademas de utilizar la funcion para quitar los acentos de las letras
def ListaFacil(lista: list): # Función para crear una lista de palabras fáciles
    return [eliminar_acentos(i) for i in lista if facil(i)]

def ListaMedio(lista: list): # Función para crear una lista de palabras de dificultad media
    return [eliminar_acentos(i) for i in lista if medio(i)]

def ListaDificil(lista: list): # Función para crear una lista de palabras difíciles
    return [eliminar_acentos(i) for i in lista if dificil(i)]

#Se le pregunta al usuario que nivel de dificultar desea utilizar y de acuerdo a esto de ingresa a una determinada lista de palabras
def nivel():
    print("¿Cómo deseas manejar el programa?")
    print("1. fácil")
    print("2. medio")
    print("3. difícil")

    opcion_nivel = int(input("Ingrese el nivel que desea: "))
    if opcion_nivel == 1:
        vidas: int = 7
        lista = ListaFacil(palabras_español)
        palabra: str = random.choice(lista) #de la lista se escoge una palabra al asar
        return palabra #Retorna la palabra que mas adelante se va a utilizar
    
    elif opcion_nivel == 2:
        vidas: int = 9
        lista = ListaMedio(palabras_español)
        palabra: str = random.choice(lista)
        return palabra
    
    elif opcion_nivel == 3:
        vidas: int = 11
        lista = ListaDificil(palabras_español)
        palabra: str = random.choice(lista)
        return palabra
    else: #Si se introduce algo diferetne a 1,2 o 3 se vuelve a pedir el dato
        print("Opción no válida.")
        nivel() 
'''
def puntaje(tiempo_transcurrido): # Calcular puntaje del jugador dependiendo de la dificultad
    letras : int = len(palabra)
    if dificultad == 1:
        puntaje_total : int = letras * 10 + (40 - tiempo_transcurrido) * 10 
    elif dificultad == 2:
        puntaje_total : int = letras * 20 + (50 - tiempo_transcurrido) * 10
    elif dificultad == 3:
        puntaje_total : int = letras * 30 + (60 - tiempo_transcurrido) * 10
    else:
        return print("Selecciona una opción válida")
    return puntaje_total
'''
def facil_interfaz():
    vidas: int = 7
    lista: list = ListaFacil(palabras_español)
    palabra: str = random.choice(lista)
    palabra = eliminar_acentos(palabra)
    print(f"Palabra seleccionada: {palabra}")
    # Aquí puedes añadir el código para iniciar el juego con la palabra seleccionada
    return palabra
    
# Se crea una funcion para que retorne el puntaje de acuerdo a la dificultad elegida por el usuario
def puntaje_facil():
    vidas: int = 7
    lista: list = ListaFacil(palabras_español)
    palabra: str = random.choice(lista)
    palabra = eliminar_acentos(palabra)
    print(f"Palabra seleccionada: {palabra}")
    def puntaje(tiempo_transcurrido): # Calcular puntaje del jugador dependiendo de la dificultad
        letras : int = len(palabra)
        puntaje_total : int = letras * 10 + (40 - tiempo_transcurrido) * 10 
        return puntaje_total
    return palabra


def medio_interfaz():
    vidas: int = 9 #Se da una nuevo de vidas de acuerdo a la dificultad del juego
    lista: list = ListaMedio(palabras_español) #Se ingresa a la funcion que utiliza la lista parta obtener la lista de palabras que cumple con esa condicion
    palabra: str = random.choice(lista) #Se escoge una palabra al asar de la lista
    palabra = eliminar_acentos(palabra)
    print(f"Palabra seleccionada: {palabra}")
    # Aquí puedes añadir el código para iniciar el juego con la palabra seleccionada
    return palabra

def dificil_interfaz():
    vidas: int = 11
    lista: list = ListaDificil(palabras_español)
    palabra: str = random.choice(lista)
    palabra = eliminar_acentos(palabra)
    print(f"Palabra seleccionada: {palabra}")
    return palabra

#Se crea una funcion que ingrese a la lista de otros idiomas, en este caso el idioma aleman
def aleman():
    vidas: int = 10 #Se da un numero de vidas de acuerdo al idioma seleccionado
    lista = palabras_aleman
    palabra: str = random.choice(lista) #Se ingresa a la lista de las palabras del idioma y se retorna una al asar
    palabra = eliminar_acentos(palabra)
    print(f"Palabra seleccionada: {palabra}")

    return palabra

def frances():
    vidas: int = 10
    lista = palabras_frances
    palabra: str = random.choice(lista)
    palabra = eliminar_acentos(palabra)
    print(f"Palabra seleccionada: {palabra}")
    return palabra

def ingles():
    vidas: int = 10
    lista = palabras_ingles
    palabra: str = random.choice(lista)
    palabra = eliminar_acentos(palabra)
    print(f"Palabra seleccionada: {palabra}")

    return palabra

#Funcion que se va a manejar desde consola, en ella se va a preguntar al usuario de que manera desea jugar
def idioma():
    print("¿Desea jugar con una palabra en otro idioma?")
    print("1. Sí")
    print("2. No")
    #Pregunta si desea jugar en otro idioma
    opcion_idioma = int(input())
    if opcion_idioma == 1:
        print("Elija en cuál de estos idiomas desea jugar")
        print("1. Alemán")
        print("2. Español")
        print("3. Inglés")
        print("4. Francés")
        idioma_opc = int(input("¿Qué idioma desea jugar? "))
        if idioma_opc == 1:
            vidas: int = 10
            lista = palabras_aleman #Ingresa a la lista de palabras en Aleman
            palabra: str = random.choice(lista) #Elige una palabra al asar
            return palabra
        elif idioma_opc == 2:
            return nivel()
        elif idioma_opc == 3:
            vidas: int = 10 #Se da un numnero determinado de vidas
            lista = palabras_ingles
            palabra: str = random.choice(lista)
            return palabra
        elif idioma_opc == 4:
            vidas: int = 10
            lista = palabras_frances
            palabra: str = random.choice(lista)
            return palabra
    elif opcion_idioma == 2:
        print("Por defecto se iniciará a jugar en el idioma Español")
        return nivel()
    else:
        print("Opción no válida")
        return idioma()

#Se le pregunta al usuario si dese manejar el programa desde consola o interfas
def forma_ejecucion():
    print("¿Cómo deseas manejar el programa?")
    print("1. Consola")
    print("2. Interfaz Gráfica")
    opcion : int= input("Elige una opción (1 o 2): ")
    #De acuerdo a la opcion elegida se ingresa a la funcion que maneja el programa ya sea desde consola o por la interfaz
    if opcion == "1":
        ejecutar_consola()
    elif opcion == "2":
        ejecutar_interfaz_grafica()
    else:
        print("Opción no válida. Por favor, elige 1 o 2.")
        forma_ejecucion()  # Vuelve a preguntar si la opción es inválida

#Funcion que se utiliza en la consola para dibujar el ahorcado de acuerdo a los errores que se tengan
def dibujo_ahorcado(vidas, opcion_nivel): # Función para dibujar el ahorcado
    if opcion_nivel == 1:
        dibujo = [
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """,  # Estado 5 (horca vacía)
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,  # Estado 4 (solo la cabeza)
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,  # Estado 3 (cabeza y cuerpo)
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,  # Estado 2 (un brazo)
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        """,  # Estado 1 (ambos brazos)
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """,  # Estado 0 (ahorcado completo)
    ]
        return dibujo[vidas]
    if opcion_nivel == 2:
        dibujo = [
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """,  # Estado 7 (horca vacía)
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,  # Estado 6 (solo la cabeza)
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,  # Estado 5 (cabeza y cuerpo)
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,  # Estado 4 (un brazo)
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        """,  # Estado 3 (ambos brazos)
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        """,  # Estado 2 (un pie)
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """,  # Estado 1 (ambos pies)
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """,  # Estado 0 (ahorcado completo)
    ]
        return dibujo[vidas]
    if opcion_nivel == 3:
        dibujo = [
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """,  # Estado 9 (horca vacía)
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,  # Estado 8 (solo la cabeza)
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,  # Estado 7 (cabeza y cuerpo)
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,  # Estado 6 (un brazo)
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        ---------
        """,  # Estado 5 (ambos brazos)
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        ---------
        """,  # Estado 4 (un pie)
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """,  # Estado 3 (ambos pies)
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ---------
        """,  # Estado 2 (ahorcado completo)
    ]
        return dibujo[vidas]

#Funcion que controla el juego desde consola
def ejecutar_consola():
    print("Has elegido manejar el programa por consola.")
    time.sleep(2)
    os.system('cls')
    palabra = idioma()
    ahorcado : str = "_" * len(palabra) # Crear el ahorcado
    intento : int = 0
    inicio : float = time.time() # Iniciar el cronómetro
    while intento < vidas : # Mientras el jugador tenga intentos
            print(ahorcado)
            print(dibujo_ahorcado(intento,opcion_nivel))
            print(f'Dijiete una letra: ')
            letra = msvcrt.getch().lower()
            if letra == b'\x1b':
                print("Muchas gracias por jugar.")
                time.sleep(1)
                exit()
            else:
                letra = letra.decode('utf-8') # Convertir la letra a string
            if letra in letras_usadas:
                os.system('cls')
                print(f'Ya usaste la letra {letra}') # Si el jugador ya usó la letra
                intento += 1
                if intento == 1:
                    os.system('cls')
                    print(f'Tienes {intento} error.')
                else:
                    os.system('cls')
                    print(f'Tienes {intento} errores.')
            else:
                letras_usadas.append(letra) # Agregar la letra a la lista de letras usadas
            if letra in palabra:
                for i in range(len(palabra)):
                    if palabra[i] == letra:
                        ahorcado = ahorcado[:i] + letra + ahorcado[i+1:] # Reemplazar el guión bajo por la letra
                os.system('cls')
                if ahorcado == palabra: # Si el jugador adivina la palabra
                    print(ahorcado)
                    print(f'Felicidades ganaste')
                    time.sleep(2)
                    break
            else:
                intento += 1
                if intento == 1:
                    os.system('cls')
                    print(f'Tienes {intento} error.')
                else:
                    os.system('cls')
                    print(f'Tienes {intento} errores.')
            print(f'Letras usadas: {letras_usadas}')
    if vidas == intento:  # Si el jugador pierde
            print(f'Mejor Suerte la proxima, la palabra es [{palabra}]')
    fin : float = time.time()
    tiempo : int = int(fin - inicio)
    print(f'Gracias por jugar')
    print(f'Tiempo de juego: {tiempo} segundos')
    if palabra == ahorcado:
          print(f'Puntaje: {puntaje(palabra,opcion_nivel,tiempo)}')
    print(f'Presiona Enter para jugar de nuevo o Esc para salir')
    time.sleep(1)

    while True:
            alternativa = msvcrt.getch() # Leer la alternativa del jugador
            if alternativa == b'\x1b': # Si el jugador presiona la tecla Esc, el juego se cierra
                print("Muchas gracias por jugar.")
                time.sleep(1)
                exit()
            elif alternativa == b'\r': # Si el jugador presiona Enter, el juego se reinicia
                os.system('cls')
                break
            else:
                print('Presiona Enter para jugar de nuevo o Esc para salir')
                continue
            
    
#Funcion que controla el juego desde interfaz grafica
def ejecutar_interfaz_grafica():
    print("Has elegido manejar el programa por interfaz gráfica.")
    #Variables globales que se deben utilizar
    global interfaz_juego, hangman, primer_imagen, imagenes, palabra, letra_obtenida, letras_faltantes, guiones, imagenes, tiempo_transcurrido
    

    #UInterfaz 1
    def interfaz_1():
        global interfaz_inicio #Se declara global ya que se elimina en un punto y se necesitan algunos datos que se encuentran en la misma
        # Ventana 1
        #Se utiliza la libreria Tk
        interfaz_inicio = Tk()
        interfaz_inicio.config(width=600, height=600, bg="blue", relief="groove", bd=10)
        interfaz_inicio.geometry("800x400") #Dimension de la interfaz
        #Se utiliza canvas para poder trabajar sobre imagenes 
        inicio = Canvas(interfaz_inicio, width=600, height=600)
        inicio.pack(expand=True, fill="both") #Permite que se mantenda las dimensiones de la interfaz

        #Se crean label o widgets  para mostrar y permitir el ingreso de informacion
        label_1 = Label(inicio, text="Bienvenidos a HANGMAN \n un juego extraordinario \n Hecho por los mejores", font=("Terminal", 18))
        label_1.grid(column=0, padx=0, pady=0) #Permite ubicar los label en la posicion que se quiera

        # Etiqueta para el nombre del jugador
        nombre_jugador_label = Label(inicio, text="Introduce tu nombre Jugador", font=("Courier", 18))
        nombre_jugador_label.grid(padx=30, pady=20)
        
        # Entrada para el nombre del jugador
        nombre_entry = Entry(inicio, width=20, font=("Verdana", 24))
        nombre_entry.grid(padx=30, pady=20)

        # Botón para seleccionar el nivel de dificultad
        nivel_dificultad = Button(inicio, text="Siguiente", command=lambda: mostrar_interfaz_2(nombre_entry.get())) #Permite cambiar de ventana
        nivel_dificultad.grid(padx=30, pady=0)
        
        #Funcion para poner imagenes en la interfaz
        imagen_logo = PhotoImage(file="logo_mecaprores.png")
        logo = inicio.create_image(600, 190, image=imagen_logo)
        
        interfaz_inicio.mainloop() # mantiene la ventana activa hasta que se hace clic en el botón cerrar

    #Funcion para cambiar de ventana, pasar de ventana 1 a ventana 2
    def mostrar_interfaz_2(nombre):
        global interfaz_inicio
        interfaz_inicio.destroy() #Elimina la interfaz
        interfaz_2_nivel(nombre)

    #Funcion para mostrar botones de los idiomas disponibles en la interfaz dependiendo de otro boton
    def mostrar_botones_idioma():
        global palabra_seleccionada
        # Mostrar botones de idioma
        idioma_label = Label(inicio_2, text="Elige el idioma", font=("Courier", 10))
        idioma_label.grid(column=8, padx=200, pady=20)

        #funcion para que un boton pueda cumplir con 2 o mas funciones
        def iniciar_aleman():
            global palabra_seleccionada
            palabra_seleccionada = aleman()
            mostrar_juego_hangman("nombre")
            return palabra_seleccionada #Retorna la palabra seleccionada

        idioma_aleman = Button(inicio_2, text="Alemán", command=iniciar_aleman) #Boton que realiza la funcion de ingresar a la lista y elegir una palabra al azar
        idioma_aleman.grid(column=8, padx=200, pady=0)


        def iniciar_ingles():
            global palabra_seleccionada
            palabra_seleccionada = ingles()
            mostrar_juego_hangman("nombre")
            return palabra_seleccionada


        idioma_ingles = Button(inicio_2, text="Inglés", command=iniciar_ingles) #Comando que cumple el boton en el momento de oprimirlo
        idioma_ingles.grid(column=8, padx=200, pady=0) # Posicion del boton

        def iniciar_frances():
            global palabra_seleccionada
            palabra_seleccionada = frances()
            mostrar_juego_hangman("nombre")
            return palabra_seleccionada

        idioma_frances = Button(inicio_2, text="Francés", command=iniciar_frances)
        idioma_frances.grid(column=8, padx=200, pady=0)

    #Funcion para mostrar botones de los niveles en español en la interfaz dependiendo de otro boton
    def mostrar_niveles():
        global palabra_seleccionada
        # Mostrar botones de idioma
        idioma_label = Label(inicio_2, text="Elige el Nivel del Juego", font=("Courier", 10))
        idioma_label.grid(column=8, padx=200, pady=20)


        #funcion para que un boton pueda cumplir con 2 o mas funciones
        def iniciar_facil():
            global palabra_seleccionada
            palabra_seleccionada = facil_interfaz() 
            mostrar_juego_hangman("nombre")
            return palabra_seleccionada

        nivel_facil = Button(inicio_2, text="Fácil", command=iniciar_facil)
        nivel_facil.grid(column=8, padx=200, pady=0) #posicion del boton


        def iniciar_medio():
            global palabra_seleccionada #Se declara global para poderla utilizar fuera de la funcion
            palabra_seleccionada = medio_interfaz()
            mostrar_juego_hangman("nombre")
            return palabra_seleccionada
        nivel_medio = Button(inicio_2, text="Medio", command=iniciar_medio)
        nivel_medio.grid(column=8, padx=200, pady=0)


        def iniciar_dificil():
            global palabra_seleccionada
            palabra_seleccionada =dificil_interfaz()
            mostrar_juego_hangman("nombre")
            return palabra_seleccionada
        nivel_dificil = Button(inicio_2, text="Difícil", command=dificil_interfaz)
        nivel_dificil.grid(column=8, padx=200, pady=0)


    #Ingreso de la interfaz 2
    def interfaz_2_nivel(nombre):
        global interfaz_2, inicio_2
        #Creacion de la interfaz 2
        interfaz_2 = Tk() 
        interfaz_2.config(width=600, height=600, bg="blue", relief="groove", bd=10)
        interfaz_2.geometry("800x400") 
        inicio_2 = Canvas(interfaz_2, width=600, height=600)
        inicio_2.pack(expand=True, fill="both")

        label_1 = Label(inicio_2, text=f"Hola {nombre} \n ¿Osas retar? \n No creo que puedas con este juego", font=("Terminal", 18))
        label_1.grid(column=8, padx=200, pady=0)

        # Etiqueta para el idioma
        idioma_label = Label(inicio_2, text="¿Deseas jugar en otros idiomas diferente al español?", font=("Courier", 10))
        idioma_label.grid(column=8, padx=200, pady=20)

        # Botón para seleccionar el idioma
        idioma_si = Button(inicio_2, text="Sí", command=mostrar_botones_idioma)
        idioma_si.grid(column=8, padx=200, pady=0)

        #Boton para ingresar a los niveles disponibles
        idioma_no = Button(inicio_2, text="No", command=mostrar_niveles)
        idioma_no.grid(column=8, padx=200, pady=0)
        
        #imagenes utilizadas en la interfz
        imagen_1 = PhotoImage(file="in_2.png")
        cap = inicio_2.create_image(100, 210, image=imagen_1) #Posicion de la imagven
        imagen_2 = PhotoImage(file="cap_1.png")
        cap_2 = inicio_2.create_image(700, 190, image=imagen_2)
        
        interfaz_2.mainloop()

    #Funcion cerrar la interfaz 2 y abrir la interfaz final
    def mostrar_juego_hangman(nombre):
        global palabra_seleccionada
        global interfaz_2
        interfaz_2.destroy()
        interfaz_juego_hangman()

    def interfaz_juego_hangman():
        global interfaz_juego, hangman, primer_imagen, imagenes, palabra, letra_obtenida, letras_faltantes, guiones, imagenes
        
        #funciones de algunos botones
        def cerrar_interfaz():
            interfaz_juego.destroy()

        def volver_jugar():
            interfaz_juego.destroy()
            forma_ejecucion()

        def colocar_letra():
            x = 50
            y = 150
            contador = 0
            Label(hangman, text="Letras sin usar").place(x=50, y=100)
            for i in range(26):
                contador += 1
                letras_faltantes[i].place(x=x, y=y)
                x += 30
                if contador == 5:
                    y += 35
                    contador = 0
                    x = 50

        #
        def probar_letra():
            global vidas, letras_acertadas, juego_terminado #variables globales

            letra = letra_obtenida.get().lower()#obtene la palabra y la convierte toda en minuscula

            # Verificar si la letra ingresada es válida
            if not letra.isalpha() or len(letra) != 1:
                showwarning(title="Letra inválida", message="Por favor, ingrese una letra válida.") #Se muestra una caja de texto si el ingreso esta mal
                return

            if letra in letras_usadas:
                showwarning(title="Letra repetida", message="Ya has usado esta letra. Intenta con otra.")
                return

            #Cada letra que se va utilizando se va agregando a una lista
            letras_usadas.append(letra)
            letras_faltantes[ord(letra) - 97].config(text="")

            #Verifica si la letra ingresada esta dentro de la palabra
            if letra in palabra:
                if palabra.count(letra) > 1:
                    letras_acertadas += palabra.count(letra)#Si la letra esta cuenta cuantas veces se repite
                    for i in range(len(palabra)):
                        if palabra[i] == letra:
                            guiones[i].config(text=letra) #Reemplaza en guion por la letra que se encuentra dentro de la palabra
                else:
                    letras_acertadas += palabra.count(letra)
                    guiones[palabra.index(letra)].config(text=letra)
                if letras_acertadas == len(palabra):
                    showwarning(title="Victoria", message="¡Felicitaciones!")
                    juego_terminado = True
            else:
                vidas -= 1
                hangman.itemconfig(primer_imagen, image=imagenes[vidas - 1])#Por cada error se va restando una vida
                if vidas == 0:
                    showwarning(title="Perdiste", message=f"Se te han acabado las vidas. La palabra era: {palabra}")
                    juego_terminado = True #Verifica que el juego haya terminado

        #funcion para mostrar el tiempo del juego
        def actualizar_tiempo():
            global tiempo_transcurrido
            if not juego_terminado:
                tiempo_transcurrido = time.time() - inicio_tiempo
                tiempo_label.config(text=f"Tiempo transcurrido: {tiempo_transcurrido:.2f} segundos")
                interfaz_juego.after(1000, actualizar_tiempo)  # Actualiza cada segundo
            else:
                tiempo_label.config(text=f"Juego terminado, Tiempo transcurrido: {tiempo_transcurrido:.2f}")


        #Creacion de la interfaz del juego
        interfaz_juego = Tk()
        interfaz_juego.iconbitmap("logo.ico")

        palabra = palabra_seleccionada
        letra_obtenida = StringVar()
        interfaz_juego.config(width=1000, height=600, bg="blue", relief="groove", bd=10) #Caracteristicas
        interfaz_juego.geometry("1000x600")#dimensiones de la interfaz
        hangman = Canvas(interfaz_juego, width=1000, height=600)
        hangman.pack(expand=True, fill="both")
        #Imagenes a utilizar 
        imagenes = [
            PhotoImage(file="11.png"),
            PhotoImage(file="10.png"),
            PhotoImage(file="9.png"),
            PhotoImage(file="8.png"),
            PhotoImage(file="7.png"),
            PhotoImage(file="6.png"),
            PhotoImage(file="5.png"),
            PhotoImage(file="4.png"),
            PhotoImage(file="3.png"),
            PhotoImage(file="2.png"),

        ]
        primer_imagen = hangman.create_image(750, 330, image=imagenes[9])
        #widgets que pertenecen a la interfaz final
        Label(hangman, text="Introduce una letra", font=("verdana", 24)).grid(row=0, column=0, padx=10, pady=10)
        Entry(hangman, width=2, font=("verdana", 24), textvariable=letra_obtenida).grid(row=0, column=1, padx=10, pady=10)
        Button(hangman, text="Probar", bg="yellow", command=probar_letra).grid(row=1, column=0, pady=10)
        Button(hangman, text="Salir del juego", bg="red", command=cerrar_interfaz).grid(row=0, column=80, padx=450, pady=10)
        Button(hangman, text="Volver a Jugar", bg="blue", command=volver_jugar).grid(row=1, column=80, padx=450, pady=10)

        letras_faltantes = [Label(hangman, text=chr(a + 97), font=("verdana", 20)) for a in range(26)]
        colocar_letra()
        guiones = [Label(hangman, text="_", font=("verdana", 30)) for _ in palabra]
        inicialX = 200
        for i in range(len(palabra)):
            guiones[i].place(x=inicialX, y=400)
            inicialX += 50

        # Agregar la etiqueta para mostrar el tiempo
        tiempo_label = Label(hangman, text="Tiempo transcurrido: 0.00 segundos", font=("Arial", 14))
        tiempo_label.grid(row=2, column=0, pady=400)


        # Iniciar el tiempo
        inicio_tiempo = time.time()
        actualizar_tiempo()

        interfaz_juego.mainloop() 
    interfaz_1()



if __name__ == "__main__":
    #Ejecucion del codigo 
    forma_ejecucion()