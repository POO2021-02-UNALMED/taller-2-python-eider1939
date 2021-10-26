import random
class Asiento:
    def _init_(self,color, precio, registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    def cambiarColor(self,color):
        if color=="rojo" or color=="amarillo" or color=="verde" or color=="negro" or color=="blanco":
            self.color=color
class Auto:
    cantidadCreados=0
    def __init__(self,modelo,precio,asientos,marca,Motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=Motor
        self.registro=registro
        
    def cantidadAsientos(self):
        cantidad=0
        for i in self.asientos:
            if type(i)==Asiento:
                cantidad+=1
        return cantidad
    def verificarIntegridad(self):
        if self.motor.registro==self.registro:
            for i in self.asientos:
                if type(i)== Asiento:
                    if self.registro==i.registro:
                        continue
                    else:
                        return 'Las piezas no son originales'
        else:
            return 'Las piezas no son originales'
        return 'Auto original'

class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
    def cambiarRegistro(self,registro):
        self.registro==registro
    def asignarTipo(self,tipo):
        if tipo=="electrico" or tipo=="gasolina":
            self.tipo==tipo


