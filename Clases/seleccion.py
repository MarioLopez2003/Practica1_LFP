from tkinter import*
from tkinter import filedialog
from tkinter import messagebox
from listacursos import listacursos
from cursos import Cursos
class seleccion(Tk):
    def __init__(self):
        super().__init__()
        self.title("Seleccionar Archivo")
        self.geometry("400x150")
        self.config(bg = "skyblue")
        self.resizable(False, False)
    
        LRuta = Label(self, text = "Ruta")
        LRuta.place(x = 50, y = 50)
        txtruta = StringVar()
        Ruta = Entry(self, textvariable = txtruta, width = "30")
        Ruta.place ( x = 150, y = 50)

        def regresar():
            self.destroy()
        def seleccion_archivo():
            archivo = filedialog.askopenfilename(title = "abrir", initialdir = "C:/", filetypes=(("Archivos csv", "*.csv"), ("Archivos LFP", "*.lfp")))
            f = open(archivo, 'r', encoding="utf-8", errors = "ignore")
            try:
                print ("Archivo Seleccionado Correctamente")
                for linea in f:
                    separacion = linea.split(",")
                    for curso in Cursos.listadoCursos:
                        if separacion[0].strip() == curso[0].strip():
                           Cursos.listadoCursos.remove(curso)
                    print(separacion)
                    Cursos.listadoCursos.append(separacion)
                messagebox.showinfo("Carga","Cursos Cargados Correctamente")
            except:
                print("Archivo no Encontrado")
            finally:
                f.close()
                regresar()
        btnSeleccionar = Button(self, text = "Seleccionar", command = seleccion_archivo)
        btnSeleccionar.place(x = 200, y = 100)
        btnRegresar = Button(self, text = "Regresar", command = regresar)
        btnRegresar.place( x = 300, y = 100)