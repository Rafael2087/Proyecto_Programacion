import random
import time
if __name__ == "__main__":
    lista = ["palabra","comida","carne","cerdo","juegos","arroz"]
    palabra : str = random.choice(lista)
    ahorcado : str = "_" * len(palabra)
    errores : int = 0
    inicio : float = time.time()
    while errores < 7 :
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
    if errores == 7:  
        print(f'Mejor Suerte la proxima, la palabra es [{palabra}]')
    fin : float = time.time()
    print(f'Gracias por jugar')
    print(f'Tiempo de juego: {(fin - inicio)} segundos')
        
        
