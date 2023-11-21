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
        #Se asigna el controlador
        self.__controlador = control

    def ingreso(self):
        #Función que nos servirá para llevar a cabo el funcionamiento del botón de ingreso
        self.edit_password = QLineEdit(self)
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
        self.menu()
        
    def menu(self):
        self.boton_menuadmin.accepted.connect(self.opcion)
        self.boton_menuadmin.rejected.connect(lambda:self.close())
    
    def opcion(self):
        item = self.menu_admin.currentText()
        if item == 'Ver Residentes':
            ventana=VistaResidente(self)
            self.hide()
            ventana.show() 
        elif item == 'Agregar Residente':
            ventana=AgregarResidente(self)
            self.hide()
            ventana.show()
        elif item == 'Actualizar Datos':
            ventana= ModificarResidente(self)
            self.hide()
            ventana.show()
        elif item == 'Eliminar Residente':
            ventana=EliminarResidente(self)
            self.hide()
            ventana.show()

class VistaResidente (VentanaAdmin):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/vista_admin.ui",self)

class AgregarResidente (VentanaAdmin):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/agregar_residente.ui",self)
        self.__ventanaPadre = ppal

    def enviarInfo(self):
        nombre=self.mod_name.text()
        cedula=self.mod_cedula.text()
        edad= self.mod_age.text()
        self.__ventanaPadre.recibir_infoRec(nombre,cedula,edad)
        self.__ventanaPadre.show()

class ModificarResidente(VentanaAdmin):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/modificar_residente.ui",self)
        self.menu2()
        
    def menu2(self):
        self.boton_modificar.accepted.connect(self.eleccion)
        self.boton_modificar.rejected.connect(lambda:self.close())
    
    def eleccion(self):
        item2 = self.menu_modificacion.currentText()
        if item2 == 'Residente':
            ventana=DatosResidente(self)
            self.hide()
            ventana.show() 
        elif item2 == 'Contacto 1':
            ventana=DatosContacto1(self)
            self.hide()
            ventana.show()
        elif item2 == 'Contacto 2':
            ventana=DatosContacto2(self)
            self.hide()
            ventana.show()
            
class DatosResidente(ModificarResidente):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/mod_residente.ui",self)

class DatosContacto1(ModificarResidente):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/mod_contacto1.ui",self)

class DatosContacto2(ModificarResidente):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/mod_contacto2.ui",self)

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
        resultado=self.__coordinador.buscarResidente(cedula,self.__listaResidentes)
        if resultado:
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
