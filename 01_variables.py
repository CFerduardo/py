#Declarar variables 
string = 'string'
numFloat = 5.9
bool = False 


#Saber el tippo de variables 
print(type(string))
#Concatenar el tipo de variables en un print 
print(type(string), type(numFloat), type(bool))


#Imprimmir en texto multilinea
print('''
    Comentario 
    multilinea
    ''')


#varaiables en una sola linea 
name, lastName, alias, age = 'carlos', 'silva', 'apache', 25
print('me llamo ', name, lastName, ' me dicen ', alias, ' y tengo ', age, ' de edad')


#Devuelve el número de elementos en una lista
print(len(string))


#Conversion de datos 
numero = 36
aTexto = str(numero)
print(type(aTexto))

texto = '310'
aNumero = int(texto)
print(type(aNumero))


#inputs 
indicaTuNombre = input('Escribe tu nombre : ')
indicaTuEdad = input('Escribe tu edad : ')

print(indicaTuNombre)
print(indicaTuEdad)
