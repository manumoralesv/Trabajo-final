from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtCore import Qt,QRegExp
import sys 

class VentanaPrincipal(QMainWindow):
    def __init__(self, ppal =None):
        super().__init__()
        self.__listaMedActual = {}
        loadUi('interfaces/ventana_principal.ui',self)
        self.setup()


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
        
#prueba