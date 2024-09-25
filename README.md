# Proyecto_Programacion
> - Rafael David Martínez Ovallos
> - Dania Lorena Pérez Moreno

[![logo-grupo.png](https://i.postimg.cc/T1KTDnfG/logo-grupo.png)](https://postimg.cc/vxdRRg4S)
### Amplia tu léxico jugando
A continuación te presentaremos un poco acerca del desarrollo de un juego que te puede teletransportar a tu infancia, aquella epoca en la que jugabas con tus amigos y compañeros del colegio. Esos juegos como serpiente, congelados, Stop, sopa de letras ... **Ahorcado**.
## ¿En que consiste el juego de Ahorcado?
| AHORCADO|
| ----------- |
| **Ahorcado** o Hangman es una juego que consiste en adivinar una palabra al azar, la manera en la cual se desarrolla es una determinado numero de rayas al piso **_** de acuerdo a la cantidad de letras de la plaabra, posterior el jugador sugiere una letra, si esta letra está dentro de la palabra se sustiye el guión en la posicion de la letra por la misma, esto se repite hasta que se adivine por completo la palabra o se acaben la cantidad de intentos |



## Diagrama de Flujo
A continuación se muestra el diagrama que se va a seguir para el desarrollo e implementación de los diferentes procesos que se deben de tener en cuenta para cumplir con el objetivo planteado.
```mermaid
graph TD;
    A("Inicio de Partida") --> B("¿Nivel de dificultad?")
    B-->C{¿Facíl?}
    C--SI-->D(Seleccionar una palabra aleatoria con una cantidad menor o igual a 5 letras)-->Da[Intentos = Letras+3]
    C--NO-->E{¿Medio?}
    E--SI-->F(Seleccionar una palabra aleatoria con una cantidad 5 < letras <= 10)-->Fa[Intentos = N° Letras + 2]
    E--NO-->G(Nivel Dificil)
    G-->H(Seleccionar una palabra aleatoria con una cantidad de letras mayor a 10)-->Ha[Intentos = N° Letras]
    Da-->J
    Fa-->J
    Ha-->J[Inicializar Variables]
    J-->K[Mostrar ""_"" de acuerdo a la cantidad de letras que contiene la palabra]
    K-->L(El usuario ingresa una letra)
    L-->M{¿Se introdujo solo una letra?}
    M--Si-->P
    M--NO-->O[Se muestra el mensaje: **Se debe introducir una sola letra**]-->M
    P[Se recorre cada posicion de la palabra]-->Q{¿Se encuentra la letra en la palabra?}
    Q--Si-->R(Se identifica cuantas veces aparece la letra en la palabra)
    R-->S(Se reemplaza el _ por la letra en la posición en la que esta se encuentra)-->U
    Q--NO-->T(Aparece una nueva parte de **Hangman**)-->U[Intentos= -1]
    U-->V{¿Se adivino la palabra}
    V--Si-->W(Se muestra **Felicidades**)-->Aa
    V--NO-->X{¿Intentos == 0?}--NO-->L
    X--Si-->Y(**PERDISTE**)
    Y-->Z(Se muestra en Hangman completo)
    Z-->Aa{¿Desea Jugar de nuevo?}--Si-->A
    Aa--NO-->Fin

```


### Librerías a utilizar
| RANDOM|
| ----------- |
|Ofrece generadores de números pseudo-aleatorios para varias distribuciones.Un generador de números aleatorios es un objeto que crea una secuencia de valores seudoaleatorios. Un generador que crea valores distribuidos uniformemente en un rango especificado es un generador de números aleatorios uniformes (URNG). |

| TIME|
| ----------- |
|Proporciona un conjunto de funciones para trabajar con fechas y/o horas. Además de estás funciones hay otras relacionadas en los módulos datetime y calendar que conviene conocer|

| THINKER|
| ----------- |
|Es una librería del lenguaje de programación Python y funciona para la creación y el desarrollo de aplicaciones de escritorio. Esta librería facilita el posicionamiento y desarrollo de una interfaz gráfica de escritorio con Python.|

| PIL|
| ----------- |
|Python Imaging Library (PIL) es una librería gratuita que permite la edición de imágenes directamente desde Python|

| TKINTER.MESSAGEBOX|
| ----------- |
|Proporciona una clase base de plantilla, así como una variedad de métodos convenientes para configuraciones de uso común. Los cuadros de mensaje son modales y devolverán un subconjunto de (Verdadero, Falso, OK, Ninguno, Sí, No) según la selección del usuario|

| OS|
| ----------- |
|Permite realizar operaciones dependiente del Sistema Operativo como crear una carpeta, listar contenidos de una carpeta, conocer acerca de un proceso, finalizar un proceso, etc.|

| UNICODE |
| ----------- |
|Representar caracteres, lo que permite a los programas de Python trabajar con todos estos caracteres posibles diferentes.|

| MSVCRT |
| ----------- |
|Desbloquea los bytes especificados que han sido previamente bloqueados. Establece el modo traducción del final de línea del descriptor de un archivo fd.|


### Código Base

EL codigo base para que funcione el ahorcado es el siguiente
```python
import random
import time
if __name__ == "__main__":
    while True:
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
        print(f'Tiempo de juego: {int(fin - inicio)} segundos')

```
Este codigo es el que permite que el ahorcado funcione con lo que solamente sería agregarle las opciones de dificultad y otras alternativas extras para jugar.

### Funciones que se tendrán en cuenta
#### Def generar palabra
----------------------
De utiliza la libreria **random.choice**, la cual devuelve un valor aleatorio extraído de la secuencia pasada como argumento, es decir, permite el ingreso a la  lista que contiene las palabras y retorna un elemento (palabra) aleatoria.
```python
def ListaFacil(lista: list): # Función para crear una lista de palabras fáciles
    return [eliminar_acentos(i) for i in lista if facil(i)]

def ListaMedio(lista: list): # Función para crear una lista de palabras de dificultad media
    return [eliminar_acentos(i) for i in lista if medio(i)]

def ListaDificil(lista: list): # Función para crear una lista de palabras difíciles
    return [eliminar_acentos(i) for i in lista if dificil(i)]

def dificil_interfaz():
    vidas: int = 11
    lista: list = ListaDificil(palabras_español)
    palabra: str = random.choice(lista)
    palabra = eliminar_acentos(palabra)
    print(f"Palabra seleccionada: {palabra}")
    return palabra
```
#### Def num_intentos
----------------------
```python
def num_intentos (nivel : int, palabra : str):
    num_intentos : int = 0
    if nivel == 1:
        num_intentos = len(palabra) + 3
    elif nivel == 2:
        num_intentos = len(palabra)+2
    elif nivel == 3:
        num_intentos = len(palabra)
    return num_intentos        
```
#### Inicio de Interfaz gráfica
----------------------
Se utilizaron 3 interfaces con el fin de crear un ambiente más interactivo con el usuario
```python
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
```
#### Cambio de la interfaz
----------------------
Debido a que se estaba utilizando imagenes en el canvas de la interfaces, en el momento de abrir otra interfaz generaba error debido a que las imegenes quedaban guardas en la memoria del canvas, haciendo dificil ejecutar el codigo de la manera correcta, por ello se utiliza *.destroy()* La cual elimina la interfaz para poder abrir la nueva
```python
#Funcion para cambiar de ventana, pasar de ventana 1 a ventana 2
    def mostrar_interfaz_2(nombre):
        global interfaz_inicio
        interfaz_inicio.destroy() #Elimina la interfaz
        interfaz_2_nivel(nombre)
```
#### Cambio en los botones de la interfaz
----------------------
Se busco un forma optima de que un boton pudieron ejecutar con dos o mas funciones a la vez, de la manera en la cual se crea funciones dentro de funciones.
```python
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
```

#### Cambio en los botones de la interfaz
----------------------
Se creo una secuencia de imagenes que se mostrarian secuencialmente en cada fallo que se tenga. Cabe aclarar que para que las imagen funciones deben estan en el mismo folden el codigo general.  
[![Captura-de-pantalla-2024-09-25-104134.png](https://i.postimg.cc/Gp785yC2/Captura-de-pantalla-2024-09-25-104134.png)](https://postimg.cc/Tyb3yhhM)
```python
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

```
#### Proceso de descarga del programa
----------------------
- Entra al repositorio en Githug, posterior entra al readme y seleccion el documento que se muestra a continuación.
[![a.png](https://i.postimg.cc/NfSdWKQd/a.png)](https://postimg.cc/4mvvcN7c)
- Ingresas en el archivo .rar
[![b.png](https://i.postimg.cc/NFVxqnvK/b.png)](https://postimg.cc/4H6cpBdG)
- En la parte superior derecha le das en los tres puntitos y se despliega un menú, le debes dar clic en descargar o *ctr+shif+s*
 [![c.png](https://i.postimg.cc/J4fQpSQg/c.png)](https://postimg.cc/zVkWBt6S)
- Se hace la descarga y se descomprime en la carpeta que se desea
