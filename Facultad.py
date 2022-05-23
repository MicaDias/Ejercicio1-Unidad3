from Carrera import Carrera
class Facultad:
    __codigo=0
    __nombre=''
    __direccion=''
    __localidad=''
    __telefono=''
    __listaCarrera=[]
    def __init__(self,codigo=0,nombre='',direccion='',localidad='',telefono='',listaCarrera=[]):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__direccion=direccion
        self.__localidad=localidad
        self.__telefono=telefono
        self.__listaCarrera=[]
        for i in range(len(listaCarrera)):
            self.__listaCarrera.append(Carrera(listaCarrera[i][1],listaCarrera[i][2],listaCarrera[i][3],listaCarrera[i][4],listaCarrera[i][5]))
    def getNombre(self):
        return self.__nombre
    def mostrarCarreras(self):
        for i in range(len(self.__listaCarrera)):
            print(self.__listaCarrera[i])
    def verificarCodigo(self,codigo):
        return self.__codigo==codigo
    def buscarNombre(self,carrera):
        i=0
        longitud=len(self.__listaCarrera)
        bandera=True
        resul=-1
        while i<longitud and bandera:
            if self.__listaCarrera[i].verificarNombre(carrera):
                bandera=False
            else:
                i+=1
        if not bandera:
            resul=i
        return resul
    def mostrarDatosCarreras(self,pos):
        print("Codigo:{}, Facultad:{}, Localidad:{}".format(str(self.__codigo)+str(self.__listaCarrera[pos].getCodigo()),self.__nombre,self.__localidad))
    def funcionTestFacultad(self):
        facultad2=Facultad(2,'Facultad de Filosofía, Humanidades y Artes','Av. José Ignacio de la Roza Oeste 230, J5400','Capital, San Juan','2644230415',[])
        print("*****Fucion test Facultad*****")
        print("*****Metodo getNombre()****")
        print("Nombre:{}".format(facultad2.getNombre()))