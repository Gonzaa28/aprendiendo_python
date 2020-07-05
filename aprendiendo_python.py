class Persona:
    def __init__(self, nombre = None, apellido = None):
        self.nombre = nombre
        self.apellido = apellido

    def escribirNombre(self):
        print(self.nombre, self.apellido)

class Estudiante(Persona):
    def __init__(self, nombre, apellido, anio_graduacion):
        super().__init__(nombre, apellido)
        self.anio_graduacion = anio_graduacion

    def bienvenido(self):
        print("Bienvenido", self.nombre, self.apellido, "a la clase de", self.anio_graduacion)

if __name__ == "__main__":
    #import random
    #print(random.randrange(1, 10))

    #p1 = Persona("Gonzalo", "Ajuria")
    p1 = Persona("Gonzalo", "Ajuria")
    p1.escribirNombre()

    #e1 = Estudiante("Agustin", "Bordon", 2020)
    #e1.bienvenido()

    #Lista (list)
    #lista = ["manzana", "banana", "cereza"]

    #Tupla (tuple)
    #Conjunto (set)

    #Diccionario (dict)
    """
    hijo1 = {
        "nombre": "Juan",
        "edad": 7
    },
    hijo2 = {
        "nombre": "Pedro",
        "edad": 18
    },
    hijo3 = {
        "nombre": "Marcos",
        "edad": 12
    }

    familia = {
        "hijo1": hijo1,
        "hijo2": hijo2,
        "hijo3": hijo3
    }

    print(familia)
    """