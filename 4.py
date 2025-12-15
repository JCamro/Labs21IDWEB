class Libro:
    
    def __init__(self, titulo, autor, año):
        self.__titulo = titulo
        self.__autor = autor
        self.__año = año
        self.__disponible = True
        
    @property
    def disponible(self):
        return self.__disponible
    
    @disponible.setter
    def prestar(self):
        if self.__disponible == True:
            self.__disponible = False
            return True
        
        else:
            return False
        
    @disponible.setter
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
        
    @property
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
        for clave, libro in self.__lista_libros:
            print(libro.mostrar_datos())
            
    def prestar_libro(self, autor):
        if self.__lista_libros.get(autor).prestar():
            print("Se presto libro correctamente")
        else:
            print("Hubo un error al prestar el libro") 
        
        
    def devolver_libro(self, autor):
        self.__lista_libros.get(autor).devolver()