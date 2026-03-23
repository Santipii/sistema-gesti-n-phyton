from entities.persona import Persona

class Medico(Persona):
    def __init__(self, nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular, especialidad_medico):
        super().__init__(nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular)
        self.__especialidad=especialidad_medico

    @property
    def especialidad(self):
        return self.__especialidad