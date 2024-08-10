#Functions (def = para declarar funciones) 

def my_function(a, b):
    print(a + b)

my_function(27, 36)
my_function('2', '6')
my_function(1.5, 6.9)



def suma_valore(c, d):
    sum = c + d
    return sum

result = suma_valore(596, 3.265)
print(result)



def nombre_invertido(nombre, apellid0):
    print(f"{nombre} {apellid0}")


nombre_invertido("carlos", "silva")



#Pasar multiples parametros *
def textos(*text):
    print(text)

textos('a', 'b', 'c', 'd', 'e', 'f')


def a_mayusculas(*palabras):
    for convertidas in palabras:
        print(convertidas.upper())

a_mayusculas('javascript', 'kotlin', 'python', 'php', 'go')