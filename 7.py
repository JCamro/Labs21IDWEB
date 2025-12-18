def copiar_archivo(archivo_original):
    with open(archivo_original, "r") as original:
        contenido = original.read()

    nombre_copia = archivo_original.replace(".txt", "_copia.txt")

    with open(nombre_copia, "w") as copia:
        copia.write(contenido)
    
copiar_archivo("ejermploPY.txt")
    