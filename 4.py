class Libro:
    
    def __init__(self, titulo, autor, año):
        self.__titulo = titulo
        self.__autor = autor
        self.__año = año
        self.__disponible = True
        
    def disponible(self):
        return self.__disponible
    
    def prestar(self):
        if self.__disponible == True:
            self.__disponible = False
            return True
        
        else:
            return False
        
    def devolver(self):
        if self.__disponible == False:
            self.__disponible = True
            return True
        
        else:
            return False
        
    def mostrar_datos(self):
        return f"\n---DATOS LIBRO--- \nTitulo: {self.__titulo}\nAutor: {self.__autor}\nAño: {self.__año}"
    
class Libro_Digital(Libro):
    
    
    def __init__(self, titulo, autor, año, formato, tamaño):
        super().__init__(titulo, autor, año)
        self.__formato = formato
        self.__tamaño = tamaño
        self.__veces_prestado = 0
        
    def veces_prestado(self):
        return self.__veces_prestado
    
    def prestar(self):
        self.__veces_prestado += 1
        return True
    
    def devolver(self):
        self.__veces_prestado -= 1
        return True
    
    def mostrar_datos(self):
        return super().mostrar_datos() + f"\nFormato: {self.__formato}\nTamaño: {self.__tamaño}"
    

class Biblioteca():
    
    def __init__(self):
        self.__lista_libros = {}
        
    def listar_libros(self):
        for clave in self.__lista_libros.values():
            print(clave.mostrar_datos())
            
    def prestar_libro(self, titulo):
        if self.__lista_libros.get(titulo).prestar():
            print("Se presto libro correctamente")
        else:
            print("Hubo un error al prestar el libro") 
        
        
    def devolver_libro(self, titulo):
        if self.__lista_libros.get(titulo).devolver():
            print("Se devolvio libro exitosamente")
        else:
            print("Hubo un error en la devolucion")
            
    def agregar_libro(self, titulo, autor, año):
        nuevo_libro = Libro(titulo, autor, año)
        self.__lista_libros[titulo] = nuevo_libro
        print("Se agrego el libro correctamente")
    
    def agregar_libro_digital(self, titulo, autor, año, formato, tamaño):
        nuevo_libro = Libro_Digital(titulo, autor, año, formato, tamaño)
        self.__lista_libros[titulo] = nuevo_libro
        print("Se agrego el libro correctamente")
    
    def buscar_libro(self, titulo):
        libro = self.__lista_libros.get(titulo)
        print(libro.mostrar_datos())

biblioteca = Biblioteca()

biblioteca.agregar_libro("Libro1", "Autor1", 2000)
biblioteca.agregar_libro("Libro2", "Autor2", 2040)
biblioteca.agregar_libro("Libro3", "Autor3", 2010)
biblioteca.agregar_libro_digital("Libro1V", "Autor1V", 1900, "PDF", 1000)
biblioteca.agregar_libro_digital("Libro2V", "Autor2V", 2003, "PDF", 10000)
biblioteca.prestar_libro("Libro1")
biblioteca.devolver_libro("Libro1")

biblioteca.buscar_libro("Libro3")

biblioteca.listar_libros()