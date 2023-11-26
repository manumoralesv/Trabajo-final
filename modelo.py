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
    
    #Asignación de las variables de la semana
    def AsignarLunes(self,l):
        self.__lunes=l
        return self.__lunes 
    def AsignarMartes(self,m):
        self.__martes=m
        return self.__martes
    def AsignarMiercoles(self,w):
        self.__miercoles=w
        return self.__miercoles 
    def AsignarJueves(self,j):
        self.__jueves=j
        return self.__jueves
    def AsignarViernes(self,v):
        self.__viernes=v
        return self.__viernes 
    def AsignarSabado(self,s):
        self.__sabado=s
        return self.__sabado
    def AsignarDomingo(self,d):
        self.__domingo=d
        return self.__domingo

class Residente:
    def __init__(self):
        self.__nombre="" 
        self.__cedula=''
        
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
    
    def AsignarTelefono(self,t):
        self.__tel=t
        return self.__tel


class BaseDatos:
    def __init__(self):
        self.__archivo_residentes = "residentes.json"
        self.__archivo_horarios = "horario.json"
        self.cargar_residentes()

    def cargar_residentes(self):
        try:
            with open(self.__archivo_residentes, "r",encoding='UTF-8') as archivo:
                self.__listaResidentes = json.load(archivo)
        except:
            # Si el archivo no existe, se crea con un residente de ejemplo
            self.__listaResidentes = {'12345': {'Nombre': 'Mario Prueba', 'Edad': 23, 'Fecha de nacimiento': '05/18/1999','Contacto': {'Nombre': 'Sandra', 'Cedula': '654852', 'Telefono': '3220569874'}}}
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
        
    def agregarResidente(self,nombre,cedula,edad,date,nombre2,cedula2,telefono):
        p=Residente()
        n = p.AsignarNombre(nombre)
        doc = p.AsignarCedula(cedula)
        age = p.AsignarEdad(edad)
        birthdate = p.AsignarFechanacimiento(date)
        n_cont = p.AsignarNombre(nombre2)
        c_cont = p.AsignarCedula(cedula2)
        t_cont = p.AsignarTelefono(telefono)
        self.__listaResidentes[doc] = {'Nombre': n, 'Edad': age , 'Fecha de nacimiento': birthdate, 'Contacto': {'Nombre': n_cont, 'Cedula': c_cont, 'Telefono': t_cont}}
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
                    Datos contacto: 
                    Nombre: {residente['Contacto']['Nombre']}
                    Documento: {residente['Contacto']['Cedula']}
                    Telefono: {residente['Contacto']['Telefono']}'''
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
    
    def guardar_horario(self,list):
        with open(self.__archivo_horarios, "w",encoding='UTF-8') as archivo:
            json.dump(list, archivo)
                
    def asignarHorario(self,l,m,w,j,v,s,d):
        p=Sistema()
        lunes = p.AsignarLunes(l)
        martes = p.AsignarMartes(m)
        miercoles = p.AsignarMiercoles(w)
        jueves = p.AsignarJueves(j)
        viernes = p.AsignarViernes(v)
        sabado = p.AsignarSabado(s)
        domingo = p.AsignarDomingo(d)
        self.__horarios = {'Lunes': lunes, 'Martes': martes, 'Miercoles': miercoles, 'Jueves': jueves, 'Viernes': viernes, 'Sabado': sabado, 'Domingo': domingo}
        self.guardar_horario(self.__horarios)
    
    def verHorario(self,a):
        with open(self.__archivo_horarios, "r",encoding='UTF-8') as archivo:
                datos_horarios = json.load(archivo)
        if a == 'L':
            horario = datos_horarios.get('Lunes')
            return horario
        elif a == 'M':
            horario = datos_horarios.get('Martes')
            return horario
        elif a == 'W':
            horario = datos_horarios.get('Miercoles')
            return horario
        elif a == 'J':
            horario = datos_horarios.get('Jueves')
            return horario
        elif a == 'V':
            horario = datos_horarios.get('Viernes')
            return horario
        elif a == 'S':
            horario = datos_horarios.get('Sabado')
            return horario
        elif a == 'D':
            horario = datos_horarios.get('Domingo')
            return horario
        else:
            return "No un horario establecido."
    
    def modDatosRes(self,doc,nombre,edad, f_nacimiento):
        with open(self.__archivo_residentes, "r",encoding='UTF-8') as archivo:
                datos_residentes = json.load(archivo)
                archivo.close()
        datos_residentes[doc]['Nombre'] = nombre
        datos_residentes[doc]['Edad'] = edad
        datos_residentes[doc]['Fecha de nacimiento'] = f_nacimiento
        with open(self.__archivo_residentes, "w",encoding='UTF-8') as archivo:
                json.dump(datos_residentes, archivo)
                archivo.close()
    
    def modDatosCont(self,doc,nombre,cedula, telefono):
        with open(self.__archivo_residentes, "r",encoding='UTF-8') as archivo:
                datos_residentes = json.load(archivo)
                archivo.close()
        datos_residentes[doc]['Contacto']['Nombre'] = nombre
        datos_residentes[doc]['Contacto']['Cedula'] = cedula
        datos_residentes[doc]['Contacto']['Telefono'] = telefono
        with open(self.__archivo_residentes, "w",encoding='UTF-8') as archivo:
                json.dump(datos_residentes, archivo)
                archivo.close()        