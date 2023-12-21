
class Trabajador:
   
    empresa = "CartonajesUnión"
    sueldo = "básico"
    rango="bajo"
  
    def __init__(self,nombre,edad,anyosEmpresa,domicilo):
        self.nombre = nombre
        self.edad = edad
        self.anyosEmpresa = anyosEmpresa
        self.domicilio = domicilo
        
    def MostrarDatos(self):
       print(f"Tu nombre es {self.nombre}, tienes {self.edad} años, tienes {self.anyosEmpresa} años en la empresa, tu domicilio es {self.domicilio}")

    """Entnces en esta vlase tenemos los atributos creados = empresa sueldo y rango
    y los atributos que cremos con el cosntructor son = nombre, edad, anyosEmpresa y domicilio"""


trababajador001 = Trabajador("Marc", 25, 5, "Calle 1")
trababajador001.MostrarDatos()

class TrabajadorAR(Trabajador):
    sueldo = "Premium"
    rango = "Alto"
    
    def __init__(self, nombre, edad, anyosEmpresa, domicilo, permisos, empleados): #hay que reeimportar los init anteriores
        self.permisos = permisos
        self.empleados = empleados
        
        super().__init__(nombre, edad, anyosEmpresa, domicilo) # con super se reeimporta

    def MostrarDatos(self): #con el super tambien podemos completar funciones
        super().MostrarDatos()
        print()
        print (f"Adenás tienes {self.permisos} permisos y tienes a {self.empleados} trabajando para ti")
        print()


trabajador002 = TrabajadorAR("Manel", 23, 2, "Sagunto", "10|10", "10")  
trabajador002.MostrarDatos()
print(trabajador002.sueldo)

"""En esta clase tenemos los atributos creados = sueldo rango y empresa
y los atributos que creamos con el cosntructor son = nombre, edad, anyosEmpresa domicilio, Y AÑADIMOS permisos y empleados"""


class Jefe(TrabajadorAR):       
    rango ="Jefe"
    flexibilidad = "true"
    
    
jefe001 = Jefe("federico", 12, 1, "monca", "10|10", "10")
jefe001.MostrarDatos()  

"""Aqui tenemos los atributos creados = sueldo rango empresa y añadimos flexibilidad flexibilidad
y los del metodo constructor son los mismos"""
