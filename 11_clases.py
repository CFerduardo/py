#Clases 
class Persona:
    pass                #Indica quew un bloque de código está vacío pero que igual funcione

print(Persona)



#Constructor de clase (__init__ = construc)
class DefinirPersona:
    def __init__(self, name, lastName, age, alias = 'Apache'):
        self.fullName = f"{name} {lastName} {age} ({alias})"

    def caminar(self):
        print(f"{self.fullName} Está caminado")
        

usuario = DefinirPersona('carlos', 'silva', 25)
usuario.caminar() 
print(usuario.fullName)


usuario2 = DefinirPersona('mariolga', 'blanco', 31, 'coocoyo')
usuario2.caminar()

#Propiedades privadas 
class DefinirGente:
    def __init__(self, nombre, apellido, edad, apodo = 'mi bebe'):
        self.nombreCompleto = f"{nombre} {apellido} {edad} ({apodo})"   #Publica
        self.__nombre = nombre                                          #__ Pivado

    def get_nombre(self):
        return self.__nombre

    def correr(self):
        print(f"{self.nombreCompleto} Está corriendo")
        

gente1 = DefinirGente('camila', 'silva', 4)
gente1.correr() 
print(gente1.nombreCompleto)


usuario2 = DefinirPersona('mariolga', 'blanco', 31, 'coocoyo')
