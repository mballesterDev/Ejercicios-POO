#CREA UN CAJERO AUTOMÁTICO



class Cuenta:
    def __init__(self, persona, cuenta =0.0):
        self.persona = persona
        self.__cuenta = cuenta

    def set_persona(self, persona)    :
        self.persona = persona
        print("Su nombre ha sido registrado")

    def ingresar_cuenta(self):
        r1 = int(input(f"Cuanto dinero quieroe añadir a su cuenta, que tiene acuatalmente {self.__cuenta} euros"))
        self.__cuenta = r1 + self.__cuenta
   
    def sacar_cuenta(self):
        r1 = int(input(f"Cuanto dinero quieroe sacar de su cuenta, que tiene acuatalmente {self.__cuenta} euros"))
        self.__cuenta = self.__cuenta - r1    

    def get_cuenta(self):
        return print(f"Su cuenta tiene {self.__cuenta} euros")   

    def get_persona(self):
        return print(f"Su cuenta tiene el nombre de {self.persona}") 



cuenta1 = Cuenta("Titular")
while True:
    opcion=int(input("Elige la operación que quieras realizar \n1. Cambiar nombreCuenta \n2. Anadir dinero \n3. Sacar dinero \n4. Ver saldo \n5. Ver nombre cuenta \n6. Salir "))
    
    if opcion == 1:
        r1 = input("Diga el nombre de su cuenta")
        print()
        cuenta1.set_persona(r1)
        print()
    elif opcion ==2:
        print()
        cuenta1.ingresar_cuenta()
        print()
    elif opcion ==3:
        print()
        cuenta1.sacar_cuenta()
        print()
    elif opcion ==4:
        print()
        cuenta1.get_cuenta()
        print()
    elif opcion ==5:
        print()
        cuenta1.get_persona()
        print()
    elif opcion ==6:
        break    
    else:
        print()
        print("Opción inválida. Por favor, elija una opción válida.")
        print()

