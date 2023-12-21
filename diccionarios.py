teclado1 = {
    "Categoria" : "Teclados",
    "Modelo" : "Razer V2",
    "Precio": "50.99"
}
teclado2 = {
    "Categoria" : "Teclados",
    "Modelo" : "Assus V3",
    "Precio": "80.99"
}

#Son como los objetos en otros lenguajes de programación

#OBTENER UN VALOR ESPECÍFICO
ModeloT2 = teclado2.get("Modelo")
print(ModeloT2)
ModeloT1 = teclado1["Modelo"] #de esta forma obtenemos el modelo(RazerV2)
print(ModeloT1)
#OBTENER TODOS LOS VALORES
print(dict(teclado1)) #asi obtenemos todos los valores de teclado1 es super util, sobretodo para listas muy largas
print(teclado1) #tambien se puede hacer con print

#MODIFICAR UN VALOR 
teclado2 ["Precio"] = 10
print(teclado2.get("Precio"))

#printeralo de una forma mas bonita
for i in teclado2:
    print(f"{i} : {teclado2[i]}")

#METODOS 

#SABER Cuantos elementos tiene una lista len
print(len(teclado2))

#Eliminbar un elemento .pop
print(teclado2.pop("Modelo"))
print(dict(teclado2))

#dejar un diccionario en blanco .clear
teclado2.clear()
print(teclado2)

#Añadir un elemento nuevo

teclado2["Peso"] = "0.9KG" 
print(teclado2)
teclado2.update({"rgb":"true"}) # o de esta forma

#Crear copia de un diccionario

tecladoCopia = teclado1.copy()
print(tecladoCopia)

tecladoCopia2 = dict(teclado2) #son lo mismo
print(tecladoCopia)

#Crear un constructor con dict

tecladocopia3 = dict(tecladoCopia,  #copiamos los datos de antes y añadimos mas valores como en las clases
                    Peso = "1KG",
                    Garantia = "Tiene"
                    )    
print()
print(tecladocopia3)

#Obtener solo los primeros valores
valores = teclado1.keys()
print()
print(valores)