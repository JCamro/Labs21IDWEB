import json as js

lista = []

def crear_diccionario(nombre, pais, nivelAtaque, nivelDefensa):
    equipo = {
        "nombre": nombre,
        "pais": pais,
        "nivelAtaque": nivelAtaque,
        "nivelDefensa": nivelDefensa,
    }
    
    return equipo

for i in range(1, 4):
    lista.append(crear_diccionario("Barca", "España", 12, 10))

texto = js.dumps(lista)

print(texto)