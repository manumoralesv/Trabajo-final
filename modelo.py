from datetime import *
class Sistema(object):
    def __init__(self):
        self.__usuarios = {}
        #se crea un usuario inicial para arrancar el sistema
        self.__usuarios['Admin'] = 'admin951'
    
    def validarRec (self, cedula):
        return cedula not in self.__listaResidentes
    
    def validarAdmin(self, u, p):
        try:
            #Si existe el usuario se verifica la clave
            if self.__usuarios[u] == p:
                return True
            else:
                return False
        except: #Se retorna un False si la clave no es el mismo que la clave del diccionario
            return False

class Residente:
    def __init__(self):
        self.db = {}
        self.data = {}
        self.visitas = {}
        
    
    def agregarVisita(self,day,month,year,number,entry,output):
        date = 1
        self.visitas['Fecha'] = date
        self.visitas['Número de visitantes'] = number
        self.visitas['Hora de entrada'] = entry
        self.visitas['Hora de salida'] = output
    
    def agregarDatos(self,name,doc,age,visit):
        self.__name= name
        self.__doc= doc
        self.__age= age
        self.__visit = visit
        
        self.data['Nombre'] = self.__name
        self.data['Edad'] = self.__age
        self.data['Visitas'] = self.__visit
    
    def agregarResidente(self):
        self.db[self.__doc] = self.data

    def VerDatos(self):
        pass
