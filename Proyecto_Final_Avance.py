import random, time, tkinter

palabras_español= [
    "abajo", "abierto", "abogado", "abrazo", "aceptar", "acerca", "aclamar", "acordar", "accion", "acero",
    "adivinar", "aereo", "afligir", "agregar", "alarma", "alegria", "aliento", "alineado", "almuerzo", "alquilar",
    "amigo", "amor", "amparo", "andar", "analisis", "animal", "anochecer", "anterior", "apagar", "apellido",
    "aplauso", "apostar", "aprender", "apreciar", "aquel", "arbol", "arena", "asistir", "atender", "aumentar",
    "bailar", "bajo", "banar", "barco", "baston", "bebida", "beisbol", "belleza", "becerro", "bicolor",
    "buscar", "cama", "camino", "cansado", "carro", "casa", "cerrar", "chico", "cielo", "clave",
    "comer", "comida", "corazon", "crear", "cruzar", "cuchara", "cuadro", "cuidado", "decidir", "dedo",
    "dejar", "demasiado", "dientes", "dificil", "dinero", "doctor", "dormir", "educacion", "empezar", "enviar",
    "escuchar", "escribir", "esperar", "estudio", "facil", "familia", "feliz", "fiesta", "florecer", "futbol",
    "ganar", "gato", "gente", "gracia", "grande", "gracias", "hablar", "hacer", "hijo", "hombre",
    "hora", "hotel", "jugar", "jardin", "joven", "juguete", "lampara", "lugar", "lluvia", "mano",
    "mesa", "mirar", "movil", "naranja", "nieve", "nino", "noche", "nube", "oficina", "oir",
    "ojo", "palabra", "pan", "papa", "parecer", "parte", "pequeno", "persona", "piso", "plaza",
    "poder", "poner", "pregunta", "puerta", "rapido", "ropa", "salir", "saber", "salud", "semana",
    "ser", "servicio", "silla", "sopa", "tarde", "te", "telefono", "tiempo", "toma", "trabajo"
]

if __name__ == "__main__":
    palabra : str = random.choice(palabras_español)
    ahorcado : str = "_" * len(palabra)
    errores : int = 0
    inicio : float = time.time()
    while errores < len(palabra) + 3 :
        letra : str = str(input("Dijite un letra: "))
        if letra in palabra:
            for i in range(len(palabra)):
                if palabra[i] == letra:
                    ahorcado = ahorcado[:i] + letra + ahorcado[i+1:]
            print(ahorcado)
            if ahorcado == palabra:
                print(f'Felicidades ganaste')
                break
        else:
            errores += 1
            if errores == 1:
                print(f'Tienes {errores} error.')
            else:
                print(f'Tienes {errores} errores.')
    if errores == len(palabra) + 3:  
        print(f'Mejor Suerte la proxima, la palabra es [{palabra}]')
    fin : float = time.time()
    print(f'Gracias por jugar')
    print(f'Tiempo de juego: {(fin - inicio)} segundos')
        
