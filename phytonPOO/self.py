import math


class Operaciones:
    def __init__(self, n1, n2):
        self.suma = f"el resultado de la suma es {n1 + n2}"
        self.resta = f"el resultado de la resta es {n1 - n2}"
        self.multiplicar = f"el resultado de la multiplicación es {n1 * n2}"
        self.raizCuafrada = f"el resultado es {math.sqrt(n1)} "
        pass


while True:
    n1 = int(input("Introuce el primer número el cual quieras operar"))
    n2 = int(input("Introuce el segundo número el cual quieras operar"))

    ejercicio = Operaciones(n1, n2)
    print(ejercicio.suma)
    print(ejercicio.resta)
    print(ejercicio.multiplicar)
    print(ejercicio.raizCuafrada)
    r1 = int(input("Pulsa 4 para salir y cualquiero otro número para seguir"))

    if r1 == 4:
        break
