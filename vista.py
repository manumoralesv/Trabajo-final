from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QLineEdit
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtCore import Qt,QRegExp
import sys 

class VentanaPrincipal(QMainWindow):
    def __init__(self, ppal =None):
        super().__init__()
        loadUi('interfaces/ventana_principal.ui',self)
        self.setup()
    
    def setup(self):
        #se programa la señal para el boton
        self.boton_ingreso.clicked.connect(self.ingreso)
        self.boton_invitado.clicked.connect(self.ingreso_inv)
    
    def asignarControlador(self,control):
        self.__controlador = control

    
    def ingreso(self):
        user = self.usuario.text()
        password = self.clave.text()
        #esta informacion la debemos pasar al controlador
        resultado = self.__controlador.verificar_usuario(user,password)
        #se crea la ventana de resultado
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Resultado")
        if resultado == True:
            ventana_ingreso=VentanaAdmin(self)
            self.hide()
            ventana_ingreso.show()
        else:
            msg.setText("Usuario o contraseña no validos")
            msg.show()
            
    def ingreso_inv(self):
        ventana_ingreso=VentanaInvitado(self)
        self.hide()
        ventana_ingreso.show()
        
class VentanaAdmin (QDialog):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/menu_admin.ui",self)
        
class VistaResidente (VentanaAdmin):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/vista_admin.ui",self)

class AgregarResidente (VentanaAdmin):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/agregar_residente.ui",self)

class ModificarResidente (VentanaAdmin):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/modificar_residente.ui",self)

class EliminarResidente (VentanaAdmin):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/eliminar_residente.ui",self)
        
        
class VentanaInvitado (QDialog):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/menu_invitado.ui",self)
        
class ModificarResidente (VentanaInvitado):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/vista_invtado.ui",self)
