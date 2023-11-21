class Sistema(object):
    def __init__(self):
        self.__usuarios = {}
        self.__listaResidentes = {}
        #se crea un usuario inicial para arrancar el sistema
        self.__usuarios['Admin'] = 'admin951'
    
    def agregarResidente(self,nombre,cedula,edad):
        p=Residente()
        p.AsignarNombre(nombre)
        p.AsignarCedula(cedula)
        p.AsignarEdad(edad)
        #p.AsignarVisita(visita)
        self.__listaResidentes[cedula] = p
    
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
        self.__nombre="" 
        self.__cedula=0
        self.__edad=0  
        #self.__lista_visita = {} 

    def AsignarNombre(self,n):
        self.__nombre=n 

    def AsignarCedula(self,c):
        self.__cedula=c 
    
    def AsignarEdad(self,e):
        self.__cedula=e
    #metodo para asignar todos las visita
  
    #def AsignarVisita(self,m):
        #self.__lista_visita = m 

    def VerNombre(self):
        return self.__nombre 

    def VerCedula(self):
        return self.__cedula 
