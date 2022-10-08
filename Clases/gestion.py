from tkinter import*
from listacursos import listacursos
from registrocursos import registrocursos
from editarcursos import editarcursos
from eliminarcursos import eliminarcursos
class gestion(Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestionar Cursos")
        self.geometry("500x250")
        self.config(bg = "skyblue")
        self.resizable(False, False)

        def ventanaListar():
            lista = listacursos()
            lista.attributes("-topmost", True)
            lista.mainloop()
        ListarCursos = Button(self, text = "Listar Cursos", command= ventanaListar)
        ListarCursos.place(x = 205, y = 20)

        def ventanaAgregar():
            registro = registrocursos()
            registro.attributes("-topmost", True)
            registro.mainloop()
        RegistrarCursos = Button(self, text = "Agregar Cursos", command = ventanaAgregar)
        RegistrarCursos.place(x = 200, y = 60)

        def ventanaEditar():
            editar = editarcursos()
            editar.attributes("-topmost", True)
            editar.mainloop()

        EditarCursos = Button(self, text = "Editar Curso", command = ventanaEditar)
        EditarCursos.place(x = 210, y = 100)

        def ventanaEliminar():
            eliminar = eliminarcursos()
            eliminar.attributes("-topmost", True)
            eliminar.mainloop()

        EliminarCursos = Button(self, text = "Eliminar Curso", command = ventanaEliminar)
        EliminarCursos.place(x = 205, y = 140)

        def cerrarGestion():
            self.destroy()

        Salir = Button(self, text ="Regresar", command = cerrarGestion)
        Salir.place(x = 220, y = 180)