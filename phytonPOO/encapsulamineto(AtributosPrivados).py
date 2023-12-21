class RegistroUsuario:
    def __init__(self, nombre, apellidos, DNI,correo, contraseña):
       
        self.nombre = nombre
        self.apelliedos = apellidos
        self.__DNI = DNI #atributo privado
        self.correo = correo
        self.__contraseña = contraseña

    def MostrarDatos(self):
        print(f"El nombre de este usuario es {self.nombre} sus apellidos {self.apelliedos} y su correo {self.correo} los demas datos son privados")
        #aunque sean privados dentro de la clase podemos crera metodos para acceder a ellos

    #METODO GETTER   
    def get_DNI(self): #POR CONVENCION PARA DEVOLVER UN ATRIBUTO PRIVADO PONEMOS GET 
        return self.__DNI
   
    def get_contraseña(self):
        return self.__contraseña
    
    #METODO SETTER
    def set_contraseña(self, contraseña):
        self.__contraseña = contraseña


usuario1 = RegistroUsuario("Manuel","Gonzalez", 12345678, "ejemplo@...", 123456)

usuario1.MostrarDatos()


#se puede acceder a los datos privados mediante funciones (que son las que crea el programadr, pero desde fuera no)
#print(usuario1.__contraseña) #en consola pone que no existe y es xq es privado y da error

print(usuario1.get_contraseña())
usuario1.set_contraseña(2549)
print(usuario1.get_contraseña())