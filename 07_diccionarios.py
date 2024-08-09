#Declarar Diccionarios 
my_dicc = dict()            #1er forma
my_other_dicc = {}            #2da forma

print(type(my_dicc))
print(type(my_other_dicc))

#Relacion clave-valor
my_other_dicc = {
    1:"Python",
    "nombre":"carlos",
    "apellido":"silva",
    "edad":25,
    "venezolano":True
}

print(my_other_dicc)
print(len(my_other_dicc))


my_dicc = {
    "nombre":"carlos",
    "apellido":"silva",
    "edad":25,
    "venezolano":True,
    "languajes":{"python", "php", "GO"}
}

print(my_dicc)
print(len(my_dicc))


#Acceder a los valores por indice 
print(my_other_dicc[1])
print(my_dicc["languajes"])
print(my_other_dicc["venezolano"])

#Cambiar valores por el indice 
my_dicc["nombre"] = "eduardo"
print(my_dicc["nombre"])

#Agregar nuevas claves-valores
my_other_dicc["signo"] = "Geminis"
print(my_other_dicc["signo"])

#Eliminar en el diccionario
del my_dicc["venezolano"]
print(my_dicc)

#Para comprobar si un elemento existe dentro del diccionario (busca por el indice)
print('carlos' in my_other_dicc)        
print('nombre' in my_other_dicc)        

print(my_other_dicc.items())        #Imprime clave-valor de un diccionario
print(my_other_dicc.keys())         #Imprime por clave
print(my_other_dicc.values())       #Imprime por valor

my_new_dicc = dict.fromkeys(my_dicc)    #Crear un nuevo diccionario con claves anteriores y valores nulos
print(my_new_dicc)

my_new_dicc2 = dict.fromkeys(my_other_dicc, '123')      #Indicar el mismo valor a todas las claves 
print(my_new_dicc2)

