from tkinter import *
from tkinter import messagebox
from cursos import Cursos

class registrocursos(Tk):
    def __init__(self):
        super().__init__()
        self.title("Agregar Cursos")
        self.geometry("400x500")
        self.config(bg = "skyblue")
        self.resizable(False, False)
        LCodigo = Label(self, text="Codigo")
        LCodigo.place(x = 50, y = 20)
        Codigo = Entry(self, width = "30")
        Codigo.place(x = 180, y = 20)
        LNombre = Label(self, text = "Nombre")
        LNombre.place(x = 50, y = 80)
        Nombre = Entry(self, width = "30")
        Nombre.place(x = 180, y = 80)
        Lpre = Label(self, text = "Pre Requisito")
        Lpre.place(x = 50, y = 140)
        Prerequisito = Entry(self, width = "30")
        Prerequisito.place(x = 180, y = 140)
        LSemestre = Label(self, text = "Semestre")
        LSemestre.place(x = 50, y = 200)
        Semestre = Entry(self, width ="30")
        Semestre.place(x = 180, y = 200)
        LOpcion = Label(self, text = "Opcionalidad")
        LOpcion.place(x = 50, y = 260)
        Opcion = Entry(self, width = "30")
        Opcion.place(x = 180, y = 260)
        LCreditos = Label(self, text = "Creditos")
        LCreditos.place(x = 50, y = 320)
        Creditos = Entry(self, width = "30")
        Creditos.place(x = 180, y = 320)
        LEstado = Label(self, text = "Estado")
        LEstado.place(x = 50, y = 380)
        Estado = Entry(self, width = "30")
        Estado.place(x = 180, y = 380)
        def regresar():
            self.destroy()
        def agregar_curso():
            cod = Codigo.get()
            nombre = Nombre.get()
            requisito = Prerequisito.get()
            opcion = Opcion.get()
            semestre = Semestre.get()
            creditos = Creditos.get()
            estado = Estado.get()
            lista = []
            
            for curso in Cursos.listadoCursos:
                if cod.strip() == curso[0].strip():
                     return messagebox.showerror("Error", "El curso ya existe")
                if int(opcion.strip()) != 0 and int(opcion.strip()) !=1:
                    return messagebox.showerror("Error", "Dato Invalido para la opcion" +"\n" + "(Solo 0 y 1 son validos)")
                if int(estado.strip()) !=-1 and int(estado.strip()) != 0 and int(estado.strip()) != 1:
                    return messagebox.showerror("Error", "Dato Invalido para el estado"+ "\n" + "(Solo -1, 0 y 1 son validos)")
            limpiar()
            lista.append(cod)
            lista.append(nombre)
            lista.append(requisito)
            lista.append(opcion)
            lista.append(semestre)
            lista.append(creditos)
            lista.append(estado)
            Cursos.listadoCursos.append(lista)
            messagebox.showinfo("Registro Cursos", "Curso Agregado Correctamente")
            limpiar()

        def limpiar():
            Codigo.delete(0, 'end')
            Nombre.delete(0, 'end')
            Prerequisito.delete(0, 'end')
            Opcion.delete(0, 'end')
            Semestre.delete(0, 'end')
            Creditos.delete(0, 'end')
            Estado.delete(0, 'end')

        btnAgregar = Button(self, text = "Agregar", command = agregar_curso)
        btnAgregar.place( x = 200, y = 450)
        btnRegresar = Button(self, text = "Regresar", command = regresar)
        btnRegresar.place( x = 300, y = 450)