#Tupla
my_tuple = tuple()      #1er forma
my_other_tuple = (20, 65, 36)      #2da forma

my_tuple = ('carlos', 'silva', 25, 1.70)
print(type(my_tuple))
print(my_tuple)
print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count('silva'))
print(my_tuple.index(25))           #Indica el indice del parametro indicado

'''
__Las tuplas son INMUTABLES es decir que una vez declarados sus datos no se pueden cambiar ni agregar mas datos 

my_tuple[1] = 'fernandez'
print(my_tuple)

TypeError: 'tuple' object does not support item assignment
'''

my_new_tuple = my_tuple + my_other_tuple
print(my_new_tuple) 
print(my_new_tuple[3:6])

#Transformar una tupla a list para modificar los datos o añadir mas  
my_list = list(my_tuple)
print(type(my_list))
my_list[1] = 'Eduardo'
print(my_list)

# del my_tuple
# print(my_tuple)       NameError: name 'my_tuple' is not defined