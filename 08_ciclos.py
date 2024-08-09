#Conditionals 
age = 16

if age > 18 and age < 20:
    print('eres mayor de edad')
elif age >= 15 and age < 17:
    print('casi mayor de edad')
else:
    print('eres peque')


string = ""

if string:
    print('cadena texto vacia')

vacio = ""

if not vacio:
    print('cadena vacia negada')
