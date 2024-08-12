#Módulos
import module
from module import concatenar, profesion               #Acceder especificamente a una funcion del fichero, acceder a 2 funciones a la vez
import math

module.suma(12, 56, 59)
concatenar('carlos', 'silva')
profesion('Programador')

print(math.pi)
print(math.pow(2, 8))


#Usar alias para una funcion
from math import pi as valor_pi
print(valor_pi)