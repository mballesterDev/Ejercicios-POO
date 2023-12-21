class Coche:  # asi se crea una clase (molde)
    color = ""
    año = 2004
    placa = ""


cochePolicia = Coche()  # asi se crea un objeto
print(cochePolicia.año)

print()
class Empleado:
    pass  # el pas sirve para decir que acabe ahi la clase sino estaria creando el objeto dentro de la clase
    # y eso es obviamente incorrecto


manel = Empleado()

manel.puesto = "Ejecutivo"
manel. edad = "20"
manel.sexo = "Hombre"

print(manel.puesto)

print(manel.edad)

print(manel.sexo)

class Ninja:  
    hp = 100 #Aqui los atributos
    altura = "170cm"
    XP = 1
    resistencia = 50

    def game_over(self): #aqui las funciones
        print("GAME OVER HUMANO")


ninja1 = Ninja()

print(ninja1.hp)
r1 = int(input("escribe la vida del humano"))
ninja1.hp = r1

if ninja1.hp ==0:
    ninja1.game_over()
else:
    print("Sigues con vida")

class Empleado:
    def __init__(self, nombre, telefono, cargo, edad):
        self.nombre = nombre
        self.telefono = telefono
        self.cargo = cargo
        self.edad = edad
        
    def CalcularSueldo(self, sueldoBruto, impuestos):
        return sueldoBruto - (sueldoBruto * impuestos / 100)

empleado1 = Empleado("Manel", "768 5858 484" ,"director" , 25 )
sueldoNeto = empleado1.CalcularSueldo(100, 20)

print(empleado1.nombre)
print(empleado1.telefono)
print(empleado1.cargo)
print(empleado1.edad)
print(sueldoNeto)    



#constructor + listas

class Alumno:
    def __init__(self, nombre, edad): #AQUI NO DEJA LISTAS
        self.nombre = nombre
        self.edad = edad
        self.asingnaturas = [] #al ser lista es mejor no phyton no deja pasarlo como argumento aariba


alumno001 = Alumno("Manel", 12)

alumno001.asingnaturas.append ("ingles") #simplemente se hace asi, se appen mediante objeto
alumno001.asingnaturas.append ("mates")

print(alumno001.asingnaturas)



#clase jugador que sea una plantilla para crear mas jugadores
class Jugador:
    def __init__(self,nombre,hp,nivel):
        self.nombre = nombre
        self.hp = hp
        self.nivel = nivel
    def saludar(self):
        print("Hola humano")
    
        

Jugador1 = Jugador("Roberto", 100, 10)

print(Jugador1.nombre, Jugador1.nivel, Jugador1.hp)

Jugador1.saludar()

