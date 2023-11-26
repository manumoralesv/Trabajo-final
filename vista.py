import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox, QLineEdit, QDateTimeEdit, QWidget
from PyQt5.uic import loadUi
import sys 
from modelo import BaseDatos 

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
        elif item == 'Crear Horario':
            ventana=AgregarHorario(self)
            self.hide()
            ventana.show()
        elif item == 'Ver Horario':
            ventana=VistaHorario(self)
            self.hide()
            ventana.show()
        elif item == 'Actualizar Datos':
            ventana= VentanaModificar(self)
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
        self.n_cont = self.name_cont.text()
        self.c_cont = self.doc_cont.text()
        self.t_cont = self.tel_cont.text()
        funcion = BaseDatos()
        funcion.agregarResidente(self.nombre,self.cedula,self.edad,self.f_nacimiento,self.n_cont,self.c_cont,self.t_cont)
    
    def cerrar(self):
        self.close() 
        self.__ventanaPadre.show()
        
class AgregarHorario(QDialog):
    def __init__(self, ppal = None):
        super().__init__(ppal)
        loadUi("interfaces/agg_horario.ui",self)
        self.__ventanaPadre = ppal
        self.setup()
    
    def setup(self):
        #se programa la señal para el boton
        self.boton_agghorario.accepted.connect(self.add_horario)
        self.boton_agghorario.rejected.connect(self.cerrar)
    
    def add_horario(self):
        self.lunes = self.esp_lunes.text()
        self.martes = self.esp_martes.text()
        self.miercoles = self.esp_miercoles.text()
        self.jueves = self.esp_jueves.text()
        self.viernes = self.esp_viernes.text()
        self.sabado = self.esp_sabado.text()
        self.domingo = self.esp_domingo.text()
        funcion = BaseDatos()
        funcion.asignarHorario(self.lunes,self.martes,self.miercoles,self.jueves,self.viernes,self.sabado,self.domingo)
        self.cerrar()
        
    def cerrar(self):
        self.close() 
        self.__ventanaPadre.show()
               
class VistaHorario(QDialog):
    def __init__(self, ppal = None):
        super().__init__(ppal)
        loadUi("interfaces/vista_horario.ui",self)
        self.__ventanaPadre = ppal
        self.setup()
        
    def setup(self):
        #se programa la señal para el boton
        self.see_horario()
        self.boton_horario.clicked.connect(self.cerrar)
    
    def see_horario(self):
        opcion = BaseDatos()
        l = opcion.verHorario('L')
        m = opcion.verHorario('M')
        w = opcion.verHorario('W')
        j = opcion.verHorario('J')
        v = opcion.verHorario('V')
        s = opcion.verHorario('S')
        d = opcion.verHorario('D')
        
        self.label_lunes.setText(l)
        self.label_martes.setText(m)
        self.label_miercoles.setText(w)
        self.label_jueves.setText(j)
        self.label_viernes.setText(v)
        self.label_sabado.setText(s)
        self.label_domingo.setText(d)
    
    def cerrar(self):
        self.close() 
        self.__ventanaPadre.show()

class VentanaModificar(QDialog):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/busc_mod.ui",self)
        self.__ventanaPadre = ppal
        self.setup()
    
    def setup(self):
        #se programa la señal para el boton
        self.boton_buscmod.accepted.connect(self.buscar_Residente)
        self.boton_buscmod.rejected.connect(self.cerrar)
    
    def buscar_Residente(self):
        self.cedula = self.busc_resmod.text()
        opcion = BaseDatos()
        opcion.validarRec(self.cedula)
        if opcion:
            # Al encontrar el residente, se procede a abrir la ventana donde se visualiza la informacion.
            ventana_mod = ModificarResidente(self.cedula)
            self.hide()
            ventana_mod.show()
        else:
            mensaje = "El residente no se encuentra en la base de datos, intente de nuevo"
            msj= QMessageBox(self)
            msj.setIcon(QMessageBox.Warning) 
            msj.setText(mensaje)
            msj.show()
    
    def cerrar(self):
        self.close() 
        self.__ventanaPadre.show()
                
class ModificarResidente(QDialog):
    def __init__(self,doc, ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/modificar_residente.ui",self)
        self.doc = doc
        self.menu2()
        
    def menu2(self):
        self.boton_modificar.accepted.connect(self.eleccion)
        self.boton_modificar.rejected.connect(lambda:self.close())
    
    def eleccion(self):
        item3 = self.menu_modificacion.currentText()
        if item3 == 'Residente':
            ventana1=DatosResidente(self.doc)
            self.hide()
            ventana1.show() 
        elif item3 == 'Contacto':
            ventana1=DatosContacto(self.doc)
            self.hide()
            ventana1.show()
            
class DatosResidente(QDialog):
    def __init__(self,doc, ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/mod_residente.ui",self)
        self.doc = doc
        self.setup()
    
    def setup(self):
        #se programa la señal para el boton
        self.mod_residente.accepted.connect(self.mod_datares)
        self.mod_residente.rejected.connect(lambda:self.close())
    
    def mod_datares(self):
        self.newname = self.mod_name.text()
        self.newage = self.mod_age.text()
        self.newdate = self.mod_birthdate.date().toString('MM/dd/yyyy')
        funcion = BaseDatos()
        funcion.modDatosRes(self.doc,self.newname,self.newage,self.newdate)
        
class DatosContacto(QDialog):
    def __init__(self,doc, ppal=None):
        super().__init__(ppal)
        loadUi("interfaces/mod_contacto.ui",self)
        self.doc = doc
        self.setup()
    
    def setup(self):
        #se programa la señal para el boton
        self.mod_cont.accepted.connect(self.mod_datacont)
        self.mod_cont.rejected.connect(lambda:self.close())
    
    def mod_datacont(self):
        self.newname2 = self.name_cont.text()
        self.newdoc2 = self.doc_cont.text()
        self.newtel2 = self.tel_cont.text()
        funcion = BaseDatos()
        funcion.modDatosCont(self.doc,self.newname2,self.newdoc2,self.newtel2)

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
        self.__ventanaPadre = ppal
        self.cedula = cedula
        self.setup()
    
    def setup(self):
        #se programa la señal para el boton
        self.vistaResidente()
        self.botonvista_invitado.clicked.connect(lambda:self.close())
    
    def vistaResidente(self):
        opcion2 = BaseDatos()
        info = opcion2.VerDatos(self.cedula)
        self.info_residente.setText(info)
    
    
    
    
