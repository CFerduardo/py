#operators arimetics
print(3 + 4)
print(10 - 5)
print(15 * 8)
print(200 / 9)
print(int(200 / 9))     #imprimirá el resultado de la división redondeado hacia abajo al entero más cercano
print(10 % 3) 
print(10 // 3)          #flor division, convierte el numero flotante a un entero
print(2 ** 3)           #exponente 2 elevado a 3


#concatenar
print("hola " + "python" + " que tal?")
print("numero " + str(5))
print("hola " * (2 ** 3))
print("hola " * 5)


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
print(len("aaa") >= len("aba"))         #cuenta caracteres
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