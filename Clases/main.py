from tkinter import *
from seleccion import seleccion
from gestion import gestion
from conteocreditos import conteocreditos

class menu(Tk):
    def __init__(self):
        super().__init__()
        self.title("Practica 1")
        self.geometry("500x250")
        self.resizable(False, False)
        self.configure(bg = "skyblue")

        
        curso = Label(text = "Nombre del curso: Lab. Lenguajes Formales y de Programacion")
        curso.config(font = ("Arial", 10 , "bold"))
        curso.place(x = 50, y = 5)
        nombre = Label(text = 'Nombre: Mario Aaron Lopez Joaquin')
        nombre.config(font = ("Arial", 10 , "bold"))
        nombre.place( x = 50, y = 30)
        carnet = Label(text = "Carnet: 202109554")
        carnet.config(font = ("Arial", 10 , "bold"))
        carnet.place(x = 50, y = 55)

        def cargar_archivo():
            ventana2 = seleccion()
            ventana2.mainloop()
        btnCarga = Button(self, text = "Cargar Archivo", command = cargar_archivo)
        btnCarga.place(x = 205, y = 80)

        def gestion_curso():
            ventana3 = gestion()
            ventana3.attributes("-top", True)
            ventana3.mainloop()

        btnGestion = Button(text = "Gestionar Cursos", command = gestion_curso)
        btnGestion.place(x = 200, y = 120)

        def conteo():
            ventana4 = conteocreditos()
            ventana4.attributes("-topmost", True)
            ventana4.mainloop()

        btnConteo = Button(text = "Conteo de Creditos", command = conteo)
        btnConteo.place(x = 195, y = 160)

        def salir():
            self.destroy()

        btnSalir = Button(text = "Salir", command = salir)
        btnSalir.place(x = 220, y = 200)
if __name__ == "__main__":
    app = menu()
    app.mainloop()