import random
class Asiento:
    def _init_(self,color, precio, registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    def cambiarColor(self,color):
        pass

class Auto:
    def __init__(self,modelo,precio,asientos,marca,motor,registro,cantidadCreados):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
        self.cantodadCreados=cantidadCreados
    def cantidadAsientos():
        pass
    def verificarIntegridad():
        pass

class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
    def cambiarRegistro(self,registro):
        pass
    def asignarTipo(self,tipo):
        pass
    
