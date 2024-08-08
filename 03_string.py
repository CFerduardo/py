#Tabular
my_Tab = "\tEsto es un Tabulador "
print(my_Tab)

my_NewL_ine = "Esto es un \nsalto de linea"
print(my_NewL_ine)

escape = "\tEsto es un tab \ncon salto de linea"
print(escape)


#Formateo
name, lastName, age = "Carlos", "Silva", 25
print("my name is {} {} and my age is {}".format(name, lastName, age))  #1er forma se usan {} donde se llaman las variables y finaliza .format(variable, variable, variable)
print("my name is %s %s and my age is %d" %(name, lastName, age))       #2da forma (en caso de % se usa %s para variable string y %d para variable int)
print(f"my name is {name} {lastName} and my age is {age}")              #3ra forma f"Texto {variable} texto {variable}" 


#Desempaqueto de Caracteres (segregar el contenido de la variable a otras con la misma cantidad)
languaje = 'Python'
a, b, c, d, e, f = languaje

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

numeros = 123
uno, dos, tres = str(numeros)

print(uno)
print(dos)
print(tres)


#Division
languaje = 'Python'

languaje_slice = languaje[1:4]      #Imprime desde la posicion 1 hasta la posicion 4
print(languaje_slice)

languaje_slice = languaje[1:]       #Imprime desde la posicion 1 y el resto del caracter 
print(languaje_slice)

languaje_slice = languaje[0:6:2]    #Imprime de 0 a 6 los caracteres de 2 en 2  
print(languaje_slice)

languaje_slice = languaje[-2]       #Imprime de forma inversa la 2da posicion 
print(languaje_slice)


#Reserve 
reservet = 'javascrpipt'

reservet_languaje = reservet[::-1]  #Recorrer la cadena de atrás hacia adelante
print(reservet_languaje)


#Functions 
scripts = 'python developer'

print(scripts.capitalize())         #Imprime la primera letra en mayúscula
print(scripts.upper())              #Imprime todo en mayúscula
print(scripts.count('e'))           #Cuenta la cantidad de letras especificada
print(scripts.isnumeric())          #Imprime en boolean si es número o no
print(scripts.lower())              #Imprime todo en minúsculas
print(scripts.isupper())            #Imprime en bool si todas las letras son mayúsculas 
print(scripts.startswith('pyt'))    #Imprime en bool si la cadena especificada comienza con una secuencia determinada de caracteres (toman en cuneta si son mayúsculas o minúsculas)
