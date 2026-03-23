from abc import ABC, abstractmethod
class Persona(ABC):
    def __init__(self, nombre, apellido, ci, fecha_nacimiento, fecha_ingreso, celular):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__ci = ci
        self.__fecha_nacimiento = fecha_nacimiento
        self.__fecha_ingreso = fecha_ingreso
        self.__celular = celular

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @property
    def ci(self):
        return self.__ci

    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento

    @property
    def fecha_ingreso(self):
        return self.__fecha_ingreso

    @property
    def celular(self):
        return self.__celular


    