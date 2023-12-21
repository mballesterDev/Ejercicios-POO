# CREAR UNA CLASE MOROCICLETA CON SUS CARACTERISTICAS, UNA FUNCION PARA CALCULAR LA GASOLINA QUE CONSUME Y OTRO PARA REPOSTAR GASOLINA

class Motocicleta:
    condición = "nueva"
    motor = "apagado"

    def __init__(self, color, matricula, combustibleTotal, combustibleActual, combustibleKM, numeroRuedas, marca, velocidadPunta, peso):
        self.color = color
        self.matricula = matricula
        self.combustibleTotal = combustibleTotal
        self.combustibleActual = combustibleActual
        self.combustibleKM = combustibleKM
        self.numeroRuedas = numeroRuedas
        self.marca = marca
        self.velocidadPunta = velocidadPunta
        self.peso = peso

    def calcularGasolina(self):
        print(f"Esta moto tiene una capacidad de {self.combustibleTotal} y consume {self.combustibleKM} por KM")
        r1 = int(input("\nCuantos KM quiere recorrer?"))  # 10 KM = 1 LITRO
        return print(f"Va a gastar {r1 * self.combustibleKM} litros de gasolina")

    def repostarGasolina(self):
            LG = 0
            while True:
                print(f"\nEl deposito tiene actualmente {LG} Litros")
                r3 = int(input("\nCuantos euro quiere ingresar? "))
                r4 = input("\n(Pulse s para SALIR u otra tecla para continuar)")
                LG = r3 * 0.87
                print(f"\nHa ingresado {r3} euros, recibirá {LG} litros de gasolina")
                print(f"\nPor lo tanto podrá recorrer {LG * 10} KM en total")
                
                if r4 =="s":
                    break

moto1 = Motocicleta("verde", "1234", 10, 0, 10, 2, "honda", 10, 1000)
moto1.repostarGasolina()