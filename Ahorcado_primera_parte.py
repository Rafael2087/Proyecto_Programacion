import random
import time
import keyboard 
import os
lista_español = [
    "casa", "perro", "gato", "libro", "mesa", "silla", "niño", "niña",
    "hombre", "mujer", "coche", "escuela", "trabajo", "amigo", "amiga",
    "agua", "comida", "ciudad", "calle", "sol", "luna", "mar", "árbol",
    "flor", "ropa", "zapato", "ventana", "puerta", "computadora", "teléfono",
    "dinero", "familia", "madre", "padre", "hermano", "hermana", "abuela",
    "abuelo", "maestra", "estudiante", "fiesta", "juego", "pelota", "música",
    "canción", "tiempo", "día", "noche", "amor", "salud", "paradigma", 
    "metafísico", "epistemología", "juxtapuesto", "transcendental", "ecléctico", 
    "inconmensurable", "iridiscente", "cognitivo", "hermenéutica", "diligente", 
    "austero", "procrastinación", "exacerbar", "subterfugio", "magnánimo", 
    "nebuloso", "desoxirribonucleico", "epifanía", "sinergia", "empático"
]
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
def ListaFacil(lista : list):
    listaFacil = []
    for i in lista:
        if facil(i):
            listaFacil.append(i)
    return listaFacil
def ListaMedio(lista : list):
    listaMedio = []
    for i in lista:
        if medio(i):
            listaMedio.append(i)
    return listaMedio
def ListaDificil(lista : list):
    listaDificil = []
    for i in lista:
        if dificil(i):
            listaDificil.append(i)
    return listaDificil
if __name__ == "__main__":
    while True:
        lista = ListaFacil(lista_español)
        palabra : str = random.choice(lista)
        ahorcado : str = "_" * len(palabra)
        errores : int = 0
        inicio : float = time.time()
        while errores < 7 :
            print(ahorcado)
            letra : str = str(input("Dijite un letra: "))
            if letra in palabra:
                for i in range(len(palabra)):
                    if palabra[i] == letra:
                        ahorcado = ahorcado[:i] + letra + ahorcado[i+1:]
                os.system('cls')
                if ahorcado == palabra:
                    print(ahorcado)
                    print(f'Felicidades ganaste')
                    time.sleep(1)
                    break
            else:
                errores += 1
                if errores == 1:
                    os.system('cls')
                    print(f'Tienes {errores} error.')
                else:
                    os.system('cls')
                    print(f'Tienes {errores} errores.')
        if errores == 7:  
            print(f'Mejor Suerte la proxima, la palabra es [{palabra}]')
        fin : float = time.time()
        print(f'Gracias por jugar')
        print(f'Tiempo de juego: {int(fin - inicio)} segundos')
        print(f'Presiona Enter para jugar de nuevo o Esc para salir')
        time.sleep(1)
        while True:
            if keyboard.is_pressed('enter'):
                break
            if keyboard.is_pressed('esc'):
                exit()
        
        
