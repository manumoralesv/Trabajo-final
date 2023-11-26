from PyQt5.QtWidgets import QMessageBox
class Sistema(object):
    def __init__(self):
        self.__usuarios = {}
        #se crea un usuario inicial para arrancar el sistema
        self.__usuarios['Admin'] = 'admin951'
    
    def validarAdmin(self, u, p):
        try:
            #Si existe el usuario se verifica la clave
            if self.__usuarios[u] == p:
                return True
            else:
                return False
        except: #Se retorna un False si el usuario no es el mismo que la clave del diccionario
            return False

class Residente:
    def __init__(self):
        self.db = {}
        self.data = {}
        self.status = {}
        #Sujeto de prueba
        self.db['12345'] = {'Nombre': 'Mario Prueba','Edad': 23 ,'Estado': {'Físico':'Bien','Mental': 'mal'}}
    
    def validarRec(self, cedula):
        if self.db[cedula]:
            return True
        else: 
            return False
        
    def guardarDatos(self,name,doc,age):
        self.__name= name
        self.__doc= doc
        self.__age= age
        
        self.data['Nombre'] = self.__name
        self.data['Edad'] = self.__age
        
    def guardarStatus(self,doc,fisico,mental):
        try:
            if self.db[doc]:
                self.__fisico = fisico
                self.__mental = mental
                
                self.status['Físico'] = self.__fisico
                self.status['Mental'] = self.__mental
                self.data['Estado'] = self.status
        except:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Resultado")
            msg.setText("El documento ingresado no se encuentra en la base de datos")
            msg.show()
            
    def agregarResidente(self):
        self.db[self.__doc] = self.data

    def VerDatos(self,cedula):
        txt = f'''
            Nombre: {self.db[cedula]['Nombre']}
            Edad: {self.db[cedula]['Edad']}
            Estado físico: {self.db[cedula]['Estado']['Físico']}
            Estado mental: {self.db[cedula]['Estado']['Mental']}'''
        return txt

    def seeAllData(self):
        list = ''
        cont = 1
        for i in self.db:
            list += f'{cont} = Doc: {i} - Nombre: {self.db[i]["Nombre"]}'
            cont+=1
        return list