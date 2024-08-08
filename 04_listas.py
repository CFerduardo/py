#Declarar listas
my_list = list()        #1era forma (si no se define list antes de los parentesis sería una tupla)
my_other_list = []      #2da forma

my_list = [35, 62, 24, 25, 30, 30]
print(my_list)
print(len(my_list))

my_other_list = [25, 1.70, 'carlos', 'silva']
print(type(my_other_list))
print(my_other_list[1])                         #Imprime el contenido de la poscion numero 1
print(my_other_list[-2])
print(my_other_list.count('carlos'))            #Retorna el numero de ocurrencias de un valor

age, height, name, lastName = my_other_list     #Desempaquetar la lista en variables (tiene que ser el mismo numero de variables que los datos de la lista)
print(name)


#Concatenar 2 listas
print(my_list + my_other_list)


my_other_list.append('PY')                      #Insertar un elemento en la ultima posicion
print(my_other_list)

my_other_list.insert(1, 'microsoft')            #Insertar el elemento en la posicion indicada
print(my_other_list)

del my_list[2]                                  #Eliminar un obj en la posicion indicada
print(my_list)

my_other_list.remove('microsoft')               #Elimina la primera ocurrencia que este especificada
print(my_other_list)

my_list.pop()                                   #Elimina el ultimo elemento por defecto
print(my_list)

my_new_list = my_list.copy()                    #Copia todos los elemenetos de una lista

my_list.clear()                                 #Elimina todos los elementos de una lista 
print(my_list)                  
print(my_new_list)

my_new_list.reverse()                           #Devuelve la lista a la inversa
print(my_new_list)

my_new_list.sort()                              #Devuelve la lista de manera ordena (alfabeticamente o numericamente) ascendente por defecto
print(my_new_list)