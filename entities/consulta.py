class Consulta:
    def __init__(self, especialidad, medico, fecha, pacientes):
        self.__especialidad = especialidad
        self.__medico = medico
        self.__fecha = fecha
        self.__pacientes = pacientes
        self.__cant_pacientes = len(pacientes)
        self.__tickets = 0

    @property
    def especialidad(self):
        return self.__especialidad

    @especialidad.setter
    def especialidad(self, especialidad):
        self.__especialidad = especialidad

    @property
    def medico(self):
        return self.__medico

    @medico.setter
    def medico(self, medico):
        self.__medico = medico

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha

    @property
    def pacientes(self):
        return self.__pacientes

    def borrar_paciente(self,pacientes):
        self.__pacientes.remove(pacientes)

    @property
    def cant_pacientes(self):
        return self.__cant_pacientes
    
    @property
    def tickets(self):
        return self.__tickets
    
    @tickets.setter
    def tickets(self, tickets):
        self.__tickets += tickets

