#Exceptions (python no es capaz de sumar un numero con una cadena de texto)
num_1 = 5
num_2 = 6
num_3 = "6"

#Controlando un error 
if type(num_3) == int:
    print(num_1 + num_2)
    print("no hay error")
else:
    print('no se cumple')


#Al no cumplirse el 1er bloque(try:) salta de inmediato al bloque(except:) 
try: 
    print(num_1 + num_3)
    print("no hay error")
except:
    print("se ha producido un error")


#try except else finally
try: 
    print(num_1 + num_2)
    print("no hay error")
except:
    print("se ha producido un error")
else:       #Opcional
    print("La ejecucion continua")          #Esta linea solo se ejecuta si el codigo entre el try y el except no da error
finally:    #Opcional
    print("Fin de la ejecucion")            #Se ejecuta siempre


#Exceptions por tipo
try:
    print(num_1 + num_3)
    print("no hay error")
except ValueError:
    print("Se ha producido ValueError")
except TypeError:
    print("Se ha producido TypeError")


#Captura de la informacion de la excepcion 
try:
    print(num_1 + num_3)
    print("no hay error")
except ValueError as error:
    print(error)
except TypeError as errorType:
    print(errorType)
except Exception as errorException:
    print(errorException)           #Exception genérica