from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QLineEdit, QComboBox
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
        self.edit_password = QLineEdit(self)
        user = self.usuario.text()
        password = self.clave.text()
        # Configurar la entrada de contraseña para ocultar caracteres
        #self.edit_password.setEchoMode(QLineEdit.clave.text())
        
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
        self.menu()
        
    def menu(self):
        self.boton_menuadmin.accepted.connect(self.opcion)
        self.boton_menuadmin.rejected.connect(lambda:self.close())
    
    def opcion(self):
        item = self.menu_admin.currentText()
        if item == 'Ver Residentes':
            ventana_see=VistaResidente(self)
            self.hide()
            ventana_see.show() 
        elif item == 'Agregar Residente':
            ventana_agg=AgregarResidente(self)
            self.hide()
            ventana_agg.show()
        elif item == 'Actualizar Datos':
            ventana_mod=ModificarResidente(self)
            self.hide()
            ventana_mod.show()
        elif item == 'Eliminar Residente':
            ventana_del=EliminarResidente(self)
            self.hide()
            ventana_del.show()
            
class VistaResidente (VentanaAdmin):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/vista_admin.ui",self)

class AgregarResidente (VentanaAdmin):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/agregar_residente.ui",self)
        self.__ventanaPadre = ppal
        self.setup()

    def enviarInfo(self):
        nombre=self.mod_name.text()
        cedula=self.mod_cedula.text()
        edad= self.mod_age.text()
        self.__ventanaPadre.recibir_infoRec(nombre,cedula,edad)
        self.__ventanaPadre.show()

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
        self.setup()
    
    def setup(self):
        #se programa la señal para el boton
        self.boton_invitado.clicked.connect(self.buscar_Residente)
        self.boton_invitado.clicked.connect(lambda:self.close())
    
    def buscar_Residente(self,cedula):
        cedula = self.busc_invitado.text()
        resultado=self.__coordinador.buscarResidente(cedula,self.__listaResidentes)
        if resultado== False:
            mensaje = "Paciente No existe, intente de nuevo"
        else:
            mensaje = "Paciente existe!!!!"

        msj= QMessageBox(self)
        msj.setIcon(QMessageBox.Warning) #Information
        msj.setText(mensaje)
        msj.show()
                
class VistaInvitado (VentanaInvitado):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/vista_invitado.ui",self)
