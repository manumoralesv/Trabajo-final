import sys
from PyQt5.QtWidgets import QApplication 
from vista import VentanaPrincipal
from PyQt5.QtWidgets import QApplication
from modelo import Sistema, BaseDatos ,Residente

class Coordinador(object):
    def __init__(self,vista,sistema,residente,bd):
        self.__vista = vista
        self.__sistema = sistema
        self.residente = residente
        self.__bd = bd
    
    def verificar_usuario(self, u, p):
        validacion = self.__sistema.validarAdmin(u,p)
        if validacion:
            return True
        else:
            return False
        
class Principal(object):
    #Se crea el init el cual nos hará las conexiones entre vista, modelo y controlador
    def __init__(self):
        self.__app = QApplication(sys.argv)
        self.__vista = VentanaPrincipal()
        self.__sistema = Sistema()
        self.__residente = Residente()
        self.__basedatos = BaseDatos()
        self.__coordinador = Coordinador(self.__vista, self.__sistema,self.__residente,self.__basedatos)
        self.__vista.asignarControlador(self.__coordinador)
    
    #Se crea la función para mostrar en pantalla
    def main(self):
        self.__vista.show()
        sys.exit(self.__app.exec_())   

#se crean los objetos para la ejecucion    
p = Principal()
p.main()   