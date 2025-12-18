palabra = "10 / 2   "

expresion = palabra.split()

try:
    numero1 = float(expresion[0])
    numero2 = float(expresion[2])    
    operacion = expresion[1]

    match operacion:
        case "+":
            print(numero1 + numero2)
            
        case "-":
            print(numero1 - numero2)
        
        case "/":
            if numero2 == 0:
                print("No se puede dividir entre 0")
            else:
                print(numero1 / numero2)    
            
        case "*":
            print(numero1 * numero2)
            
        case _:
            print("Operacion no valida")

except Exception as e:
    print(f"ERROR: {e}")


       