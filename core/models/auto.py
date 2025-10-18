import random

class Auto:
    def __init__(self, nombre, velocidad_maxima):
        self.__nombre=nombre
        self.__velocidad_maxima=velocidad_maxima
        self.__posicion_actual=0
    
    def avanzar(self):
        pass

    def mostrar_estado(self):
        return [self.__velocidad_maxima, self.__posicion_actual]

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value):
        self.__nombre=value
    
    @property
    def velocidad_maxima(self):
        return self.__velocidad_maxima
    
    
