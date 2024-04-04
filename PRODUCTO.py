from enum import Enum

"""----------------------------------------
 Enumeraciones 
----------------------------------------"""

class Tipo(Enum):
    """----------------------------------------
    # Enumeraciones para los tipos de prodcutos
    ----------------------------------------"""
    PAPELERIA = 1
    SUPERMERCADO = 2
    FARMACIA = 3

class Producto:

    """----------------------------------------
    # Constantes
    ----------------------------------------"""
     
    __IVA_PAPELERIA = 0.16
    __IVA_SUPERMERCADO = 0.04
    __IVA_FARMACIA = 0.12

    """----------------------------------------
    # Atributo
    ----------------------------------------"""   
    __nombre = None
    __tipo = Enum('Tipo', ['PAPELERIA', 'SUPERMERCADO', 'FARMACIA'])    
    __valorUnitario = 0.0
    __cantidadBodega = 0
    __cantidadMinima = 0
    __cantidadUnidadesVendidas = 0

    """----------------------------------------
    # Metodos
    ----------------------------------------"""
    def __init__(self, tipo, pNombre, pValorUnitario, pCantidadBodega, pCantidadMinima, pCantidadUnidadesVendidas):
        self.__tipo=tipo	
        self.__nombre=pNombre
        self.__valorUnitario=pValorUnitario
        self.__cantidadBodega=pCantidadBodega
        self.__cantidadMinima=pCantidadMinima
        self.__cantidadBodega=pCantidadBodega
        self.__cantidadUnidadesVendidas= 0

    def getNombre(self):
        return self.__nombre
    
    def getTipo(self):
        return self.__tipo
    
    def getValorUnitario(self):
        return self.__valorUnitario
    
    def getCantidadBodega(self):
        return self.__cantidadBodega
    
    def getCantidadMinima(self):
        return self.__cantidadMinima
    
    def getCantidadUnidadesVendidas(self):
        return self.__cantidadUnidadesVendidas 

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setTipo(self, tipo):
        self.__tipo = tipo

    def setValorUnitario(self, valorUnitario):
        self.__valorUnitario = valorUnitario

    def setCantidadBodega(self, cantidadBodega):
        self.__cantidadBodega = cantidadBodega

    def setCantidadMinima(self, cantidadMinima):
        self.__cantidadMinima = cantidadMinima

    def setCantidadUnidadesVendidas(self, cantidadUnidadesVendidas):
        self.__cantidadUnidadesVendidas = cantidadUnidadesVendidas

    def Vender(self, cantidad):
        if cantidad > self.__cantidadBodega:
            self.__cantidadUnidadesVendidas += cantidad
            self.__cantidadBodega -= cantidad
        else: 
            print ("Cantidad no disponible")

    def HaySuficiente(self, cantidad):
        
        #Forma 1
        haySuficiente = False
        if cantidad <= self.__cantidadBodega:
            haySuficiente = True
        return haySuficiente

        #Forma 2 
        if cantidad <= self.__cantidadBodega:
            return True
        else: 
            return False
        
    def DarIva(self):
        if(self.__tipo=="PAPELERIA"):
            return self.__IVA_PAPELERIA
        elif(self.__tipo=="FARMACIA"):
            return self.__IVA_FARMACIA
        elif(self.__tipo=="SUPERMERCADO"):
            return self.__IVA_SUPERMERCADO
        else:
            print("Categoria de producto no existe") 
            
    def SubirValorUnitario(self):
        if (self.__valorUnitario < 1000.0):
            self.__valorUnitario += self.__valorUnitario * 0.01
        elif (self.__valorUnitario <= 1000.0, 5000.0):
            self.__valorUnitario += self.__valorUnitario * 0.02
        elif (1000.0 > self.__valorUnitario > 5000.0):
            self.__valorUnitario += self.__valorUnitario * 0.03

    def HacerPedido(self):
        if self.__cantidadBodega < self.__cantidadMinima:
        else

    def ambiarValorUnitario(self):

    def VenderProducto(self, nombre, cantidad):

    def CuantosPapeleria(self):


    #*Si el producto cuesta - de 1000 aumentar el 1%, si cuesta entre 1 y 5 mil aumenta el 2%, si cuesta ma s de 5000 el 3%
    #*Recibir un pedido solo si en la bodega se tiene menos unidades de las indicadas en el tope minimo, en caso contrario el metodo no debe hacer nada, el metodo se llama "Hace pedido" y tiene un parametro 
    #*modificar el precio del producto utilizando la siguiente politica, si el producto es de drogueria o papeleria debe dispminuir un 10%, si es de supermercado debe aumentar un 5%, el metodo se va allamar "Cambiar Valor Unitario"
    #*Vender una cierta cantidad de productos cuyo nombre es igual a el recibido como parametro, el metodo retorna el numeor de unidades efectivamente vendidas 
    #*Supongas el nombre que se recuibe como paramentro corresponde a uno de los productos de la tienda, utilice el metodo vender de la clase producto como parte de su solucion. El metodo se va a llamar "vender producto" y recibe 2 parametros: nombre de producto y cantidad
    #*Calcular el numeor de productos de papeleria que se venden en la tienda, el metodo se llama "Cuantos Papeleria"
