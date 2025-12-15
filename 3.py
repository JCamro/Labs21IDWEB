class Figura:
    
    def __init__(self):
        pass
    
    def mostrar_datos(self):
        print("Esta es una figura: Datos -> 0")
        
    def calcular_area(self):
        return None
        

class Rectangulo(Figura):
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
        
    def calcular_area(self):
        self.area = self.altura * self.base
        return self.area
    
    def calcular_perimetro(self):
        self.perimetro = self.altura * 2 + self.base * 2
        return self.perimetro
    
    def mostrar_datos(self):
        print(f"Rectangulo:\nBase: {self.base}\nAltura: {self.altura}\nArea: {self.calcular_area()}\nPerimetro: {self.calcular_perimetro()}")
        

class Triangulo(Rectangulo):
    
    def __init__(self, base, altura, lado2, lado3):
        self.lado2 = lado2
        self.lado3 = lado3
        super().__init__(base, altura)
        
    def calcular_area(self):
        self.area = self.altura * self.base * 0.5
        return self.area
    
    def calcular_perimetro(self):
        self.perimetro = self.base + self.lado2 + self.lado3
        return self.perimetro
    
    def mostrar_datos(self):
        print(f"Triangulo:\nBase: {self.base}\nAltura: {self.altura}\nArea: {self.calcular_area()}\nPerimetro: {self.calcular_perimetro()}")
        

class Circulo(Figura):
    PI = 3.14
    
    def __init__(self, radio):
        self.radio = radio  
        
    def calcular_area(self):
        self.area = self.radio ** 2 * self.PI
        return self.area
    
    def calcular_perimetro(self):
        self.perimetro = self.PI * 2 * self.radio
        return self.perimetro
    
    def mostrar_datos(self):
        print(f"Circulo:\nRadio: {self.radio}\nArea: {self.calcular_area()}\nPerimetro: {self.calcular_perimetro()}")
        
           
figura = Figura()
rectangulo = Rectangulo(10, 5)
triangulo = Triangulo(10, 3, 15, 16)
circulo = Circulo(5)

lista = [figura, rectangulo, triangulo, circulo]

for objeto in lista:
    print(objeto.mostrar_datos())
        
        