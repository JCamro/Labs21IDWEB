
import threading
import time
def descargar(nombre, tiempo):
    print(f"Iniciando {nombre}")
    time.sleep(tiempo)
    print(f"Finalizó {nombre}")
tareas = [
 ("Archivo A", 5),
 ("Archivo B", 5)
]

inicio = time.time()
hilos = []

for nombre, t in tareas:
    h = threading.Thread(target=descargar, args=(nombre, t))
    h.start()
    hilos.append(h)
for h in hilos:
    h.join()
    
print("Tiempo total:", time.time() - inicio)