import tkinter
raiz = tkinter.Tk()
raiz.title("Ahorcado")
#raiz.resizable(False, False)
raiz.iconbitmap("logo.ico")
#raiz.geometry("800x600")

miFrame = tkinter.Frame(raiz)
miFrame.pack(side="top", anchor="n")
miFrame.config(bg="black", width="800", height="600")


raiz.mainloop()