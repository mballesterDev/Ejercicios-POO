#Herencia de clases 

"""La herencia es un proceso mediante el cual se puede crear una clase hija que hereda de una clase padre, 
compartiendo sus métodos y atributos. Además de ello, una clase hija puede sobreescribir los métodos o atributos, 
o incluso definir unos nuevos."""

class UsuarioBasico:#SUPERCLASE  #esta plnatilla es buena pero si queremos crear por ej un usuario premium que comparta los mismos métodos (el constructor para crear los datos del )
    cuenta = "NoPremium" #usuario, podemos usar la herencia y se heredaran todos los atributos y métodos
    permisos="5|10"
    anuncios= "Si"
    pantallasIlimitadas= False

    def __init__(self,nombre,edad,email,contraseña,usuario):
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.contraseña = contraseña
        self.usuario = usuario

    def MostrarDatos(self):
        print(f"Tu nombre es {self.nombre}, tienes {self.edad} años, tu correo es {self.email}, tu usuario es {self.usuario}")
           

Usuario1 = UsuarioBasico("Federico", 22, "ejemplo@...",454545, "Federico123")
Usuario1.MostrarDatos()

class UsuarioPremium(UsuarioBasico):#UsuarioPremium = SUBCLASE #de esta forma hemos heredado los atributos y métodos de la SUPERCLASE(UsuarioBásico)
    cuenta = "Premium"
    anuncios ="No"

    
print(UsuarioPremium.permisos) # Aunque no esté en el código hemos heredado los mismos permisoso que el usuario básico, por eso tenemos los mismos permisos
                               # y los atributos cuenta y anuncios se heredan tmb, pero en este caso los sobreescribimos para que tenga caracteristicas premium

Usuario2 = UsuarioPremium("Juan",12,"ejemplo@gmail",454654,"Juan2")

Usuario2.MostrarDatos()

class UsuarioSuperPremium(UsuarioPremium): #segunda subclase
    permisos = "10|10"
    pantallasIlimitadas= True

Usuario3 = UsuarioSuperPremium("anonimo",111,"ej3plo@gmail",454,"anonimo23")

Usuario3.MostrarDatos()