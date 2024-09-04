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
    C--SI-->D(Seleccionar una palabra aleatoria con una cantidad menor o igual a 5 letras)-->Da[Intentos = 2*N° Letras]
    C--NO-->E{¿Medio?}
    E--SI-->F(Seleccionar una palabra aleatoria con una cantidad 5 < letras <= 10)-->Fa[Intentos = N° Letras + 5]
    E--NO-->G(Nivel Dificil)
    G-->H(Seleccionar una palabra aleatoria con una cantidad de letras mayor a 10)-->Ha[Intentos = N° Letras +2]
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
### Código Base



