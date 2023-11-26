from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QLineEdit, QDateTimeEdit
from PyQt5.uic import loadUi
import sys 
from modelo import BaseDatos , Residente

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
            resultado = False 
        else:
            msg.setText("Usuario o contraseña no validos")
            msg.show()
            
    def ingreso_inv(self):
        ventana_ingreso2=VentanaInvitado(self)
        self.hide()
        ventana_ingreso2.show()
        
class VentanaAdmin (QDialog):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/menu_admin.ui",self)
        self.__ventanaPadre = ppal
        self.menu()
        
    def menu(self):
        self.boton_menuadmin.accepted.connect(self.opcion)
        self.boton_menuadmin.rejected.connect(self.cerrar)
    
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
            
    def cerrar(self):
        self.close() 
        self.__ventanaPadre.show()

class VistaResidente (QDialog):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/vista_admin.ui",self)
        self.__ventanaPadre = ppal
        self.menu()
    
    def menu(self):
        self.resident_data.setText(self.verDatos())
        self.botonvista_admin.clicked.connect(self.cerrar)
        
    def verDatos(self):
        opcion3 = BaseDatos()
        info2 = opcion3.seeAllData()
        print(info2)
        info = ''
        for i in info2:
            data = i
            info += data + '\n'
            print(info)
        return info
    
    def cerrar(self):
        self.close() 
        self.__ventanaPadre.show()
    
class AgregarResidente (QDialog):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/agregar_residente.ui",self)
        self.__ventanaPadre = ppal
        self.setup()
        
    def setup(self):
        self.boton_agregar.accepted.connect(self.enviarInfo)
        self.boton_agregar.rejected.connect(self.cerrar)
        
    def enviarInfo(self):
        self.nombre = self.name.text()
        self.cedula = self.doc.text()
        self.edad = self.age.text()
        self.f_nacimiento =  self.birthdate.date().toString('MM/dd/yyyy')
        funcion = BaseDatos()
        funcion.agregarResidente(self.nombre,self.cedula,self.edad,self.f_nacimiento)

    def cerrar(self):
        self.close() 
        self.__ventanaPadre.show()
        
class EstadoResidente(QDialog):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/status.ui",self)

class ModificarResidente(QDialog):
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
            
class DatosResidente(QDialog):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/mod_residente.ui",self)

class DatosContacto1(QDialog):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/mod_contacto1.ui",self)

class EliminarResidente (QDialog):
    def __init__(self, ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/eliminar_residente.ui",self)     
        
class VentanaInvitado (QDialog):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/menu_invitado.ui",self)
        self.__ventanaPadre = ppal
        self.setup()
    
    def setup(self):
        #se programa la señal para el boton
        self.boton_invitado.accepted.connect(self.buscar_Residente)
        self.boton_invitado.rejected.connect(self.cerrar)
    
    def buscar_Residente(self):
        self.cedula = self.busc_invitado.text()
        opcion = BaseDatos()
        opcion.validarRec(self.cedula)
        if opcion:
            # Al encontrar el residente, se procede a abrir la ventana donde se visualiza la informacion.
            ventana_In = VistaInvitado(self.cedula)
            self.hide()
            ventana_In.show()
        else:
            mensaje = "El residente no se encuentra en la base de datos, intente de nuevo"
            msj= QMessageBox(self)
            msj.setIcon(QMessageBox.Warning) 
            msj.setText(mensaje)
            msj.show()
    
    def cerrar(self):
        self.close() 
        self.__ventanaPadre.show()
        
class VistaInvitado (QDialog):
    def __init__(self,cedula, ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/vista_invitado.ui",self)
        self.__VentanaPadre = ppal
        self.cedula = cedula
        self.setup()
    
    def setup(self):
        #se programa la señal para el boton
        self.vistaResidente()
        self.botonvista_invitado.clicked.connect(lambda:self.close())
    
    def vistaResidente(self):
        opcion2 = BaseDatos()
        info = opcion2.VerDatos(self.cedula)
        if info == False:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Resultado")
            msg.setText("El documento ingresado no se encuentra en la base de datos")
            msg.show()
        else:
            self.info_residente.setText(info)
    
    
    
    