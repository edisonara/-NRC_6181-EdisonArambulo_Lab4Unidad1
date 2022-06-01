class Gato:
    especie= "mamifero"
    aliment=[5]
    def __init__(self, nombre, edad):  ##(init) es un constructor
        ### (self) es ===== "a ti mismo ponte el servicio(service)'
        self.atributo1=nombre
        self.atributo2=edad

    def Adult(self):
        if self.edad >1:
            (self.nombre, "es adulto")
        else:
            print(self.nombre, "cachorro")

    def alimetofaf(self, alimento):
        return alimento in self.alimentos

#### 1 instanciar

michu= Gato("michu", 1)
## atributo
print(michu.atributo1)
## 
nombre= input('ingrese frace: ')
michu.atributo1= nombre
## 
print(michu.atributo1)
## falta 
michu.aliment = input("ingrese datos a una lita")
print(michu.aliment)



