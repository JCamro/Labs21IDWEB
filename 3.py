import geometria as geo

           
figura = geo.Figura()
rectangulo = geo.Rectangulo(10, 5)
triangulo = geo.Triangulo(10, 3, 15, 16)
circulo = geo.Circulo(5)

lista = [figura, rectangulo, triangulo, circulo]

for objeto in lista:
    print(objeto.mostrar_datos())
        
        