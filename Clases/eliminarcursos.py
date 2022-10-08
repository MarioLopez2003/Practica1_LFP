from tkinter import *
from tkinter import messagebox
from cursos import Cursos
class eliminarcursos(Tk):
    def __init__(self):
        super().__init__()
        self.title("Eliminar Cursos")
        self.geometry("400x150")
        self.config(bg = "skyblue")
        self.resizable(False, False)
        LCod = Label(self, text = "Codigo de Curso")
        LCod.place(x = 50, y =30)
        txtcod = StringVar()
        Cod = Entry(self, textvariable =txtcod, width = "30")
        Cod.place(x = 180, y = 30)
        def regresar():
            self.destroy()
        def eliminar_curso():   
            cod = Cod.get()
            for curso in Cursos.listadoCursos:
                if cod.strip() == curso[0].strip():
                    Cursos.listadoCursos.remove(curso)
            messagebox.showinfo("Elimninacion Cursos", "Curso " + cod + " Eliminado Correctamente")
            limpiar()
        def limpiar():
            Cod.delete(0, 'end')
        btnEliminar = Button(self, text = "Eliminar", command = eliminar_curso)
        btnEliminar.place(x = 200, y = 100)
        btnRegresar = Button(self, text = "Regresar", command = regresar)
        btnRegresar.place( x = 300, y = 100)