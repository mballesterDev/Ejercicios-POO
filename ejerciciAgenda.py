
class AgendaContacos :
    contactos = ["Manel", "Vera", "Marc", "Eustaquio",  "Rafa"]

    def mostrarContactos (self):  # El uso de self en este contexto se refiere a la instancia de la clase y permite acceder a los atributos de la instancia.
        for nombre in self.contactos:
            print(nombre, end=" ")
   
    def añadirContacto(self):
        r1 = input("Que nombre quiere añadir?")
        self.contactos.append(r1)

    def eliminarContacto(self):
        r1 ="zz"
        while r1 not in self.contactos:  
            r1 = input("\n¿Qué contacto desea eliminar? (nombre del contacto): ")
            if r1 in self.contactos:
                self.contactos.remove(r1)
                print(f"\nContacto '{r1}' eliminado correctamente.")
            else:
                print(f"\nEl contacto '{r1}' no existe en la lista.")


agenda = AgendaContacos()

while True:
    # Menú de opciones
    print("\n--- Menú ---")
    print("1. Mostrar contactos")
    print("2. Añadir contacto")
    print("3. Eliminar contacto")
    print("s. Salir")

    opcion = input("\nSeleccione una opción: ")

    if opcion == '1':
        agenda.mostrarContactos()
    elif opcion == '2':
        agenda.añadirContacto()
    elif opcion == '3':
        agenda.eliminarContacto()
    elif opcion.lower() == 's':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")


