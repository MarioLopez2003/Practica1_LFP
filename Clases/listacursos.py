from tkinter import *
from tkinter.ttk import Treeview
from cursos import Cursos
from registrocursos import registrocursos
class listacursos(Tk):
    def __init__(self):
        super().__init__()
        self.title("Listar Cursos")
        self.geometry("900x500")
        self.config(bg = "skyblue")
        self.resizable(False, False)
        tabla = Treeview(self)
        tabla['columns'] = ('Codigo', 'Nombre', 'Pre_requisitos', 'Opcionalidad', 'Semestre', 'Creditos', 'Estado')
        tabla.column("#0", width = 0, stretch= NO)
        tabla.column("Codigo", anchor = CENTER, width = 80)
        tabla.column("Nombre", anchor = CENTER, width = 260)
        tabla.column("Pre_requisitos", anchor = CENTER, width = 120)
        tabla.column("Opcionalidad", anchor = CENTER, width = 80)
        tabla.column("Semestre", anchor = CENTER, width = 80)
        tabla.column("Creditos", anchor = CENTER, width = 80)
        tabla.column("Estado", anchor = CENTER, width = 160)
        tabla.heading("#0", text = "", anchor = CENTER)
        tabla.heading("Codigo", text = "Codigo", anchor = CENTER)
        tabla.heading("Nombre", text = "Nombre", anchor = CENTER)
        tabla.heading("Pre_requisitos", text = "Pre requisitos", anchor = CENTER)
        tabla.heading("Opcionalidad", text = "Opcionalidad", anchor = CENTER)
        tabla.heading("Semestre", text = "Semestre", anchor = CENTER)
        tabla.heading("Creditos", text = "Creditos", anchor = CENTER)
        tabla.heading("Estado", text = "Estado", anchor = CENTER)
        #tabla.insert(parent = "", index = "end", values = (Cursos.listadoCursos[0], Cursos.listadoCursos[1], Cursos.listadoCursos[2], Cursos.get_obligatorio_status(int(Cursos.listadoCursos[3])), Cursos.listadoCursos[4], Cursos.listadoCursos[5], Cursos.set_estado_inf(int(Cursos.listadoCursos[6]))))
        def ingreso_registro():
            for listas in Cursos.listadoCursos:
                tabla.insert(parent = "", index = "end", values = (listas[0], listas[1], listas[2], Cursos.get_obligatorio_status(int(listas[3])), listas[4], listas[5], Cursos.set_estado_inf(int(listas[6]))))
        ingreso_registro()
        tabla.place(x=10, y= 20)
        def regresar():
            self.destroy()
        btnRegresar = Button(self, text = "Regresar", command = regresar)
        btnRegresar.place( x = 400, y = 400)