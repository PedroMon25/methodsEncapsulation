import tkinter as tk

class Window:
    __ancho = 20
    __alto = 20
    __titulo = "Test"
    __resize = False

    def setDimensions(self, width, height):
        self.__ancho = width
        self.__alto = height

    def getDimensions(self):
        return [self.__ancho, self.__alto]

    def setResize(self, resize):
        self.__resize = resize

    def getResize(self):
        return self.__resize

    def setTitle(self, titulo):
        self.__titulo = titulo

    def getTitle(self):
        return self.__titulo

    def crear_ventana(self):

       # Crear la ventana principal

       ventana = tk.Tk()

       ventana.title( self.__titulo )


       # Establecer el tamaño de la ventana (n x m píxeles)

       ventana.geometry(f"{self.__ancho}x{self.__alto}")


       # Evitar que la ventana sea redimensionable

       ventana.resizable(self.__resize, self.__resize)


       # Iniciar el bucle principal de la ventana

       ventana.mainloop()