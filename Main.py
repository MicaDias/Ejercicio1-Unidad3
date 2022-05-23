from ManejadorFacultad import ManejaFacultades
from Menu import Menu
if __name__ == "__main__" :
    manejador=ManejaFacultades()
    manejador.cargarArchivo()
    menu=Menu()
    menu.lanzarMenu(manejador)