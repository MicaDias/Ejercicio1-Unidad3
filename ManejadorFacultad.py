import csv
from Facultad import Facultad
from Carrera import Carrera
class ManejaFacultades:
    __listaFacultades=[]
    
    def __init__(self):
        self.__listaFacultades=[]
    def agregarFacultad(self,facultad):
        if type(facultad)==Facultad:
            self.__listaFacultades.append(facultad)
        else:
            print("No se puedo agregar el elemento")
    def cargarArchivo(self):
        archivo=open("Facultades.csv",encoding='utf-8')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        listaCarreras=[]
        facu=None
        for fila in reader:
            if bandera==True: 
                facu=fila
                bandera=False
            else:
                if fila[0]==facu[0]:
                    listaCarreras.append(fila)
                else:
                    nuevaFacultad=Facultad(int(facu[0]),facu[1],facu[2],facu[3],facu[4],listaCarreras)
                    self.agregarFacultad(nuevaFacultad)
                    facu=fila
                    listaCarreras=[]
        self.agregarFacultad(Facultad(int(facu[0]),facu[1],facu[2],facu[3],facu[4],listaCarreras))
        archivo.close()
    def buscarCodigo(self,codigo):
        i=0
        lon=len(self.__listaFacultades)
        bandera=True
        resultado=0
        while i<lon and bandera:
            if self.__listaFacultades[i].verificarCodigo(codigo):
                bandera=False
            else:
                i+=1
        if bandera:
            resultado=-1
        else:
            resultado=i
        return resultado
    def mostrarDatosFacultad(self,pos):
        if pos==-1:
            print("No se encontro")
        else:
            print(self.__listaFacultades[pos].getNombre())
            self.__listaFacultades[pos].mostrarCarreras()
    def buscarCarrera(self,carrera):
        i=0
        longitudF=len(self.__listaFacultades)
        bandera=True
        posicionFacu=0
        while i<longitudF and bandera:
            pos=self.__listaFacultades[i].buscarNombre(carrera)
            if pos!=-1:
                bandera=False
                posicionFacu=i
            else:
                i+=1
        if not bandera:
            self.__listaFacultades[posicionFacu].mostrarDatosCarreras(pos)
        else:
            print("No se encontro la carrera")
    def funcionTestManejador(self):
        manejador=ManejaFacultades()
        print("-------Funcion Test ManejaFacultades-----")
        manejador.cargarArchivo()
        facultad1=Facultad(3,'Facultad de Ciencias Sociales','J5402DCH, Av. José Ignacio de la Roza Oeste 727','Rivadavia, San Juan','2644230414',[])
        print("****Metodo agregarFacultad()*******")
        manejador.agregarFacultad(facultad1)
        print("****Metodo buscarCodigo()*******")
        posicion=manejador.buscarCodigo(1)
        print("*******Metodo mostrarDatosFacultad()*******")
        manejador.mostrarDatosFacultad(posicion)
        print("*********Metodo buscarCarrera()*********")
        manejador.buscarCarrera('Licenciatura en Sistemas de Información')