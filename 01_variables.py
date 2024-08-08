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

'''
### operators arimetics###

print(3 + 4)
print(10 - 5)
print(15 * 8)
print(200 / 9)
print(int(200 / 9)) 
print(10 % 2)         #operador de modulo = es el residuo de una divison
print(10 % 3) 
print(10 // 3)        #flor division convierte el numero flotante a un entero
print(2 ** 3)         #exponente 2 elevado a 3

### concatenar ###

print("hola " + "python" + " que tal?")
print("numero " + str(5))
print("hola " * (2 ** 3))



### operators comparative ###

print(3 < 4)
print(3 > 4)
print(3 <= 4)
print(3 >= 4)
print(3 == 4)
print(3 != 4)


### ordenacion alfabetica ###
print("hola" < "python")
print("hola" > "python")
print("aaa" >= "aaa")
print(len("aaa") >= len("aba"))           ### cuenta caracteres ###
print("hola" <= "python")
print("hola" >= "python")
print("hola" == "python")
print("hola" != "python")


### operators logic###

print(3 < 4 and "hola" < "python")
print(3 > 4 or "hola" < "python")
print(3 > 4 and "hola" > "python")
print(3 > 4 or "hola" > "python")
print(not(3 > 4))


'''