class Cursos():
    listadoCursos = []
    def __init__(self, codigo, nombre, prerrequisito, obligatorio, semestre, creditos, estado):
        super().__init__()
        self.codigo = codigo
        self.nombre = nombre
        self.prerrequisito = prerrequisito
        self. obligatorio = obligatorio
        self.semestre = semestre
        self.creditos = creditos
        self.estado = estado
    def get_cod(codigo):
        return codigo
    def set_cod(self, codigo):
        self.codigo = codigo

    def get_nombre(nombre):
        return nombre
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_prerrequisito(prerrequisito):
        return prerrequisito
    def set_prerrequisito(self, prerrequisito):
        self.prerrequisito = prerrequisito

    def get_obligatorio(obligatorio):
        return obligatorio
    def set_obligatorio(self, obligatorio):
        self.obligatorio = obligatorio
    def get_obligatorio_status(obligatorio):
        if obligatorio == 1:
            return "Obligatorio"
        elif obligatorio == 0:
            return "Opcional"
        else:
            return None

    def get_semestre(semestre):
        return semestre
    def set_semestre(self, semestre):
        self.semestre = semestre

    def get_creditos(creditos):
        return creditos
    def set_creditos(self, creditos):
        self.creditos = creditos 

    def get_estado(estado):
        return estado     
    def set_estado(self, estado):
        self.estado = estado  
    def set_estado_inf(estado):
        if estado == 0:
            return "Aprobado"
        elif estado == 1:
            return "Cursando"
        elif estado == -1:
            return "Pendiente"
        else:
            return None