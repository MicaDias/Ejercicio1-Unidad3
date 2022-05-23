class Carrera:
    __codigo=0
    __nombre=''
    __titulo=''
    __duracion=''
    __tipo=''
    def __init__(self,codigo=0,nombre='',titulo='',duracion='',tipo=''):
        self.__codigo=codigo
        self.__nombre=nombre
        self.__titulo=titulo
        self.__duracion=duracion
        self.__tipo=tipo
    def getNombre(self):
        return self.__nombre
    def getDuracion(self):
        return self.__duracion
    def __str__(self):
        return 'Carrera:{}, Duracion:{}'.format(self.__nombre,self.__duracion)
    def verificarNombre(self,carrera):
        return self.__nombre==carrera
    def getCodigo(self):
        return self.__codigo
    def funcionTestCarrera(self):
        carrera1=Carrera(29,'Licenciatura en Biologia','Licenciado en Biologia','Diez semestres','Grado')
        print("*****Funcion Test Carrera*****")
        print("*****Metodo getNombre()*****")
        print("Carrera:{}".format(carrera1.getNombre()))
        print("****Metodo getDuracion()****")
        print("Duracion:{}".format(carrera1.getDuracion()))
        print("****Metodo getCodigo()****")
        print("Codigo:{}".format(carrera1.getCodigo()))
