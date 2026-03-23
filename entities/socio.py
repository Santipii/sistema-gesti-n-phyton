from entities.persona import Persona

class Socio(Persona):
    def __init__(self, nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular, tipo):
        super().__init__(nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular)
        self.__tipo = tipo
        self.__deuda = 0

    @property
    def tipo(self):
        return self.__tipo

    @property
    def deuda(self):
        return self.__deuda
    
    @deuda.setter
    def deuda(self, valor):
        if self.__tipo == "1":
            self.__deuda += valor * 0.80
        else:
            self.__deuda += valor