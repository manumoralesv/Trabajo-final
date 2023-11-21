import sys
from PyQt5.QtWidgets import QApplication 
from vista import VentanaPrincipal
import sys
from PyQt5.QtWidgets import QApplication
from modelo import Sistema

class Coordinador(object):
    def __init__(self,vista,sistema):
        self.__vista = vista
        self.__sistema = sistema
    
    def verificar_usuario(self, u, p):
        return self.__sistema.validarAdmin(u,p)
    
    def buscarResidente(self,cedula):
        resultado = self.__sistema.validarRec(cedula)
        if resultado:
            return False
        else:
            #self.__sistema.verInfoResidente(nombre,cedula,edad)
            return True
class Principal(object):
    #Se crea el init el cual nos hará las conexiones entre vista, modelo y controlador
    def __init__(self):
        self.__app = QApplication(sys.argv)
        self.__vista = VentanaPrincipal()
        self.__sistema = Sistema()
        self.__coordinador = Coordinador(self.__vista, self.__sistema)
        self.__vista.asignarControlador(self.__coordinador)
    
    #Se crea la función para mostrar en pantalla
    def main(self):
        self.__vista.show()
        sys.exit(self.__app.exec_())   

#se crean los objetos para la ejecucion    
p = Principal()
p.main()   