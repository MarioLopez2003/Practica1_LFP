from tkinter import *
from cursos import Cursos
class conteocreditos(Tk):
    def __init__(self):
        super().__init__()
        self.title("Conteo de Creditos")
        self.geometry("400x400")
        self.config(bg = "skyblue")
        self.resizable(False, False)

        def conteo_creditos_aprobados():
            print("Cursos Aprobados:")
            lista_aprobados = []
            suma = 0
            for curso in Cursos.listadoCursos:
             if int(curso[6]) == 0:
                  lista_aprobados.append(curso[1])
                  suma = suma + int(curso[5])
            print(lista_aprobados)
            print("\n")
            return suma

        def conteo_creditos_cursando():
            print("Cursos Cursando:")
            lista_cursando = []
            suma = 0
            for curso in Cursos.listadoCursos:
                if int(curso[6]) == 1:
                    lista_cursando.append(curso[1])
                    suma = suma + int(curso[5])
            print(lista_cursando)
            print("\n")
            return suma

        def conteo_creditos_pendientes():
            print("Cursos Pendientes: ")
            lista_pendientes = []
            suma = 0
            for curso in Cursos.listadoCursos:
                if int(curso[6]) == -1:
                    if int(curso[3]) == 1: 
                        lista_pendientes.append(curso[1])
                        suma = suma + int(curso[5])
            print(lista_pendientes)
            print("\n")
            return suma

        LCreditosA = Label(self, text = "Creditos Aprobados: " + str(conteo_creditos_aprobados()))
        LCreditosA.place( x = 50, y = 20)
        LCreditosC = Label(self, text = "Creditos Cursando: " + str(conteo_creditos_cursando()))
        LCreditosC.place(x = 50, y = 60)
        LCreditosP = Label(self, text = "Creditos Pendientes: " + str(conteo_creditos_pendientes()))
        LCreditosP.place(x = 50, y = 100)

        LObligatorios = Label(self, text = "Creditos Obligatorios hasta semestre N: ")
        LObligatorios.place(x = 50, y = 140)
        txtobligatorio = StringVar()
        Creditos_Obligatorios = Entry(self, textvariable =txtobligatorio, width = "15")
        Creditos_Obligatorios.place(x = 270, y = 140)

        LSemestre = Label(self, text = "Semestre")
        LSemestre.place( x= 50, y = 180)
        Semestre = Spinbox(self, from_ = 1, to = 10, width = "5")
        Semestre.place(x = 120, y = 180)

        def creditos_obligatorios():
            print("Cursos hasta el semestre " + Semestre.get())
            suma = 0
            listado = []
            for curso in Cursos.listadoCursos:
               if int(curso[4]) <= int(Semestre.get()):
                   if int(curso[3]) == 1:
                    listado.append(curso[1])
                    suma = suma + int(curso[5])
            print(listado)
            print("\n")
            Creditos_Obligatorios.insert(0, str(suma))
        
        def limpiar1():
            Creditos_Obligatorios.delete(0, 'end')

        btnContarObligatorios = Button(self, text = "Contar", command = creditos_obligatorios)
        btnContarObligatorios.place( x = 200, y = 175)
        btnLimpiar1 = Button(self, text = "Limpiar", command = limpiar1)
        btnLimpiar1.place(x = 250, y = 175)

        LCreditosSemestre = Label(self, text = "Creditos del Semestre")
        LCreditosSemestre.place(x =50, y = 240)
        txtcreditos = StringVar()
        Creditos_Semestre = Entry(self, textvariable = txtcreditos, width = "15")
        Creditos_Semestre.place( x = 180, y = 240)
        LSemester = Label(self, text = "Semestre")
        LSemester.place( x= 50, y = 300)
        Semester = Spinbox(self, from_ = 1, to = 10, width = "5")
        Semester.place( x = 120, y = 300)

        def creditos_semestre():
            print("Cursos del Semestre " + Semester.get())
            suma = 0
            listado = []
            for curso in Cursos.listadoCursos:
                if int(curso[4]) == int(Semester.get()):
                    listado.append(curso[1])
                    suma = suma + int(curso[5])
            print(listado)
            print("\n")
            Creditos_Semestre.insert(0, str(suma))

        def limpiar2():
            Creditos_Semestre.delete(0, 'end')

        btnCreditosSemestre = Button(self, text = "Contar", command = creditos_semestre)
        btnCreditosSemestre.place( x = 200, y = 295)
        btnLimpiar2 = Button(self, text = "Limpiar", command = limpiar2)
        btnLimpiar2.place( x = 250, y = 295)
        def regresar():
            self.destroy()
        btnRegresar = Button(self, text = "Regresar", command = regresar)
        btnRegresar.place( x = 300, y = 350)