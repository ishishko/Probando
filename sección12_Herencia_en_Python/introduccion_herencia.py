#!usr/bin/python3
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Empleado(Persona):
    def __init__(self, sueldo, nombre, edad):
        super().__init__(nombre, edad)
        self.sueldo = sueldo


empleado1 = Empleado("shimbo", 40, 5000)
print(empleado1.nombre)
