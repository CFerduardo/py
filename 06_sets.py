#Declarar Set
my_set = set()          #1er forma
my_other_set = {}       #2da forma 

print(type(my_set))
print(type(my_other_set))       #Princialment es un diccionario

my_other_set = {'carlos', 'silva', 25}
print(type(my_other_set))
print(len(my_other_set))        #Cuenta los elementos de una lista de elementos


'''
Un set no es una estructura ordenda, por ello si intentamos acceder al un elemento no va a dar error

print(my_other_set[1])         TypeError: 'set' object is not subscriptable
'''


my_other_set.add('Eduardo')
my_other_set.add('Eduardo')
print(my_other_set)             #Un set no admite repetidos


#Para comprobar si un elemento exite dentro de un set (Boolean)
print('carlo' in my_other_set)
print('carlos' in my_other_set)
print('Carlos' in my_other_set)

my_other_set.remove('Eduardo')
print(my_other_set)

my_other_set.clear()
print(my_other_set)

# del my_set 
# print(my_set)           #NameError: name 'my_set' is not defined


my_set = {'camila', 'silva', 4}
my_list = list(my_set)
print(my_list[2])
print(type(my_list))

other_set = {'python', 'js', 'php'}
union_set = my_set.union(other_set)          #Operacion para unir dos conjuntos
print(union_set)
print(union_set.union({'java', 'mariolga'}))

print(union_set.difference(my_set))          #Diferencias entre los sets