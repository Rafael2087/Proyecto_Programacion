from tkinter import *

raiz = Tk()
raiz.config(width = 800, height = 600, bg ="blue", relief="groove", bd=10)
juego_ahorcado = Frame (raiz)
juego_ahorcado.config (width=800, height =600, relief ="sunken", bd =15)
juego_ahorcado.grid_propagate (False)

juego_ahorcado.pack()

Label (juego_ahorcado, tex = "Introduce una letra", font =("Verdana", 24)
    ).grid (row =0 , column = 0, padx = 10, pady = 10)

letra_ingresada = Entry (juego_ahorcado, width =1, pady = 10, font = ("Verdama", 24)
    ).grid(row = 0, column= 1, padx= 10, pady=10)

verificar_letra = Button (juego_ahorcado, text = "Verificar", bd ="orange", command= verificar_letra
                          ).grid(row=1, column=0, pady=10)


raiz.mainloop() 

