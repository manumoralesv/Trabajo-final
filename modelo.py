import json 
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
        self.__nombre="" 
        self.__cedula=''
        self.__status = {} 
        
    def AsignarNombre(self,n):
        self.__nombre=n
        return self.__nombre 

    def AsignarCedula(self,c):
        self.__cedula=c 
        return self.__cedula
        
    def AsignarEdad(self,m):
        self.__edad = m 
        return self.__edad
    
    def AsignarFechanacimiento(self,d):
        self.__date=d
        return self.__date

    def AsignarStatus(self,doc,fisico,mental):
        self.__status = {}
        try:
            if self.__listaResidentes[doc]:
                self.__fisico = fisico
                self.__mental = mental
                
                self.__status['Físico'] = self.__fisico
                self.__status['Mental'] = self.__mental
                return self.__status
        except:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Resultado")
            msg.setText("El documento ingresado no se encuentra en la base de datos")
            msg.show()
        return self.__status


class BaseDatos:
    def __init__(self):
        self.__archivo_residentes = "residentes.json"
        self.cargar_residentes()

    def cargar_residentes(self):
        try:
            with open(self.__archivo_residentes, "r") as archivo:
                self.__listaResidentes = json.load(archivo)
        except:
            # Si el archivo no existe, se crea con un residente de ejemplo
            self.__listaResidentes = {'12345': {'Nombre': 'Mario Prueba', 'Edad': 23, 'Fecha de nacimiento': '05/18/1999', 'Estado': {'Físico': 'Bien', 'Mental': 'mal'}}}
            self.guardar_residentes(self.__listaResidentes)

    def guardar_residentes(self,list):
        with open(self.__archivo_residentes, "w",encoding='UTF-8') as archivo:
            json.dump(list, archivo)
            
    def validarRec(self, cedula):
        try: 
            if self.__listaResidentes[cedula]:
                return True
            else: 
                return False
        except:
            return False
        
    def agregarResidente(self,nombre,cedula,edad,date):
        p=Residente()
        n = p.AsignarNombre(nombre)
        doc = p.AsignarCedula(cedula)
        age = p.AsignarEdad(edad)
        birthdate = p.AsignarFechanacimiento(date)
        #estado = p.AsignarStatus(status)
        self.__listaResidentes[doc] = {'Nombre': n, 'Edad': age , 'Fecha de nacimiento': birthdate}
        print(self.__listaResidentes)
        self.guardar_residentes(self.__listaResidentes)
    
    def VerDatos(self,cedula):
        try:
            with open(self.__archivo_residentes, "r",encoding='UTF-8') as archivo:
                datos_residentes = json.load(archivo)
            residente = datos_residentes.get(cedula)
            if residente:
                txt = f'''
                    Nombre: {residente['Nombre']}
                    Edad: {residente['Edad']}
                    Fecha de nacimiento: {residente['Fecha de nacimiento']}
                    Estado físico: {residente['Estado']['Físico']}
                    Estado mental: {residente['Estado']['Mental']}'''
                return txt
            else:
                return "No se encontró al residente con la cédula proporcionada."
        except FileNotFoundError:
            return "La base de datos de residentes no existe. Por favor, agregue residentes primero."
            
    def seeAllData(self):
        try:
            with open(self.__archivo_residentes, "r",encoding='UTF-8') as archivo:
                datos_residentes = json.load(archivo)

            lista_residentes = []
            cont = 1
            for doc, residente in datos_residentes.items():
                info_residente = f'{cont} = Doc: {doc} - Nombre: {residente["Nombre"]}'
                lista_residentes.append(info_residente)
                cont+=1

            return lista_residentes
        except FileNotFoundError:
            return "La base de datos de residentes no existe. Por favor, agregue residentes primero."