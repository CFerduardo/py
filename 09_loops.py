'''
Se le puede indicar a un bucle que pare con break o que siga ejecutando con continue
'''

#While
condition = 0

while condition < 10:
    print('while')
    condition += 1 
else:
    print('ya no cumple la condicion')



#For 
my_list = [35, 62, 24, 25, 30, 30]

for elements in my_list:
    print(elements)


my_set = {'camila', 'silva', 4}

for elements in my_set:
    print(elements)


my_dicc = {
    "nombre":"carlos",
    "apellido":"silva",
    "edad":25,
    "venezolano":True,
    "languajes":{"python", "php", "GO"}
}

for elements in my_dicc:
    print(elements)
    if elements == "edad":
        break


my_tuple = ('carlos', 'silva', 25, 1.70)

for elements in my_dicc:
    print(elements)