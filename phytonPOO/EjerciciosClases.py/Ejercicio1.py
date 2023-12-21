class Persona:
    def __init__(self, nombre, edad, DNI):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

    # GETTERS

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_DNI(self):
        return self.DNI

    # SETTERS(EDITORES)

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad

    def set_DNI(self, DNI):
        self.DNI = DNI

    # MÉTODOS

    def esMayorEdad(self):
        if self.edad >= 18:
            return print("Es mayor de edad")
        else:
            return print("Es menor de edad")


persona1 = Persona("Pilar", 17, "4893929A")


"""Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:

Un constructor, donde los datos pueden estar vacíos.
Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
mostrar(): Muestra los datos de la persona.
esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad."""