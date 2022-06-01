
class Ejemplo:
    def __init__(self, parametro1, parametro2, parametro3):  ##(init) es un constructor
        ### (self) es ===== "a ti mismo ponte el servicio(service)'
        self.atributo1=parametro1
        self.atributo2=parametro2
        self.atributo3= parametro3


frace= input('ingrese frace: ')
#### instanciar un objeto pasando argumetos al constructor ( crear un  objeto )
unEjemplo= Ejemplo(": es una frace", "otro valor", frace)
fraceFinal=(unEjemplo.atributo3) + unEjemplo.atributo1
print(fraceFinal)

## vector[]    ========= es una lista. 






