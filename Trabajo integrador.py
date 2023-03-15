#Trabajo integrador


#clase Ingrediente

class ingrediente:
    def __init__(self,ingrediente, unidadMedida,cantidad):
        self.ingrediente = ingrediente
        self.unidadMedida = unidadMedida
        self.cantidad = cantidad
    
    def getterNombreIngrediente (self):
        return self.nombreIngrediente
    
    def getterUnidadMedida (self):
        return self.unidadMedida
    
    def getterCantidad (self):
        return self.cantidad
    
    def setterNombreIngrediente (self,ingrediente):
        self.ingrediente = ingrediente
    
    def setterUnidadMedida (self,medida):
        self.unidadMedida = medida
    
    def setterCantidad (self,cantidad):
        self.cantidad = cantidad
    
    


    

    

class Receta:
    def __init__(self,nombre, lista,image,tiempop, tiempoc, fechac,etiqueta, esFav):
        self.nombreReceta = nombre
        self.listaIngredientes = lista
        self.image = image
        self.tiempoPreparacion = tiempop
        self.tiempoCoccion = tiempoc
        self.fechaCreacion = fechac
        self.etiquetas = etiqueta
        self.esFavorita = esFav
    
    #getters

    def getterNombreReceta(self):
        return self.nombreReceta
    
    def getterListaIngredientes (self):
        return self.listaIngredientes
    
    def getterTiempoPreparacion (self):
        return self.tiempoPreparacion
    
    def getterTiempoCoccion (self):
        return self.tiempoCoccion
    
    def getterEtiquetas (self):
        return self.etiquetas
    
    def getterEsFavorita(self):
        return self.esFavorita
    
    #setters (van a servir para la modificacion de la receta)

    def setterNombreReceta(self,nombre):
        self.nombreReceta = nombre
    
    def setterListaIngredientes(self,lista):
        self.listaIngredientes = lista
    
    def setterTiempoPreparacion (self, tiempop):
        self.tiempoPreparacion = tiempop
    
    def setterTiempoCoccion (self, tiempoc):
        self.tiempoCoccion = tiempoc
    
    def setterEtiquetas (self,etiqueta):
        self.etiquetas = etiqueta
    
    def setterEsFavorita (self,fav):
        self.esFavorita = fav

    def ingresoListaIngredientes(self):
        #ingresar lista de ingredientes manualmente

    def ingresoEtiquetas(self):
        #ingreso de etiquetas manualmente

    #buscador de etiquetas, devuelve recetas que tengan la etiqueta pasada por parametro
    def buscarEtiquetas(self,etiqueta):

    #filtra y muestra recetas que tengan cierta etiqueta
    def filtrarPorEtiquetas(self,etiqueta): 
    
    def cambiarNombreReceta(self,nombre):
        self.setterNombreReceta(nombre)
        print (f"Nombre cambiado, nombre actual {self.getterNombreReceta()}")

    def cambiarListaIngredientes(self,lista):
        self.setterListaIngredientes(lista)
        print (f"Lista de ingredientes cambiada, lista de ingredientes {self.getterListaIngredientes()}")

    def cambiarTiempoPreparacion(self,tiempop):
        self.setterTiempoPreparacion(tiempop)
        print (f"Tiempo de preparacion cambiado, nuevo tiempo de preparacion {self.getterTiempoPreparacion()}")
        

    def cambiarTiempoCoccion(self,tiempoc):
        self.setterTiempoCoccion(tiempoc)
        print (f"Tiempo de Coccion cambiado, nuevo tiempo de coccion {self.getterTiempoCoccion()}")
    
    def cambiarEtiquetas(self,etiquetas):
        self.setterEtiquetas(etiquetas)
        print (f"Etiquetas cambiadas, mostrando nuevas etiquetas {self.getterEtiquetas()}")
    
    def cambiarFavorita(self):
        if (self.esFavorita):
            self.setterEsFavorita(False)
        else:
            self.setterEsFavorita(True)




class listaRecetas:
    def __init__(self,listaRecetas):
        self.recetas = listaRecetas

    def buscarReceta(self,recetaNombre):
        pos = -1
        #busqueda en la lista
        return pos
        
    #CAMBIAR Y USAR METODOS PARA QUE SEA MAS LEGIBLE Y FACIL DE ENTENDER
    def modificarReceta(self,receta,pos):
        #mostra menu sobre que se quiere modificar
        #Modificar algo particular o modificar todo
        print ("1 - Modificar el nombre de la receta")
        print ("2 - Modificar la lista de ingredientes")
        print ("3 - Modificar Tiempo de preparacion")
        print ("4 - Modificar Tiempo de Coccion")
        print ("5 - Modificar Etiquetas")
        print ("6 - Modificar es Favorita")
        print ("7 - Modificar toda la receta")
        resp = input()
        if resp == 1:
            nombre = input ("Ingrese el nuevo nombre de la receta")
            self.receta[pos].cambiarNombreReceta(nombre)
        elif resp == 2:
            lista = ingresoListaIngredientes()
            self.receta[pos].cambiarListaIngredientes(lista)
        elif resp == 3:
            tiempop = input ("ingrese el nuevo tiempo de preparacion")
            self.receta[pos].cambiarTiempoPreparacion(tiempop)
        elif resp == 4:
            tiempoc = input ("ingrese el nuevo tiempo de coccion")
            self.receta[pos].cambiarTiempoCoccion(tiempoc)
        elif resp == 5:
            etiquetas = ingresoEtiquetas() #implementar ingreso de etiquetas
            self.receta[pos].cambiarEtiquetas(etiquetas)
        elif resp == 6:
            self.receta[pos].cambiarFavorita()
        else:
            print("---- Cambio Nombre ----")
            nombre = input ("Ingrese el nuevo nombre de la receta")
            self.receta[pos].cambiarNombreReceta(nombre)
            print (f"Nombre cambiado, nombre actual {self.receta[pos].getterNombreReceta()}")
            print("---- Cambio Lista  de Ingredientes ----")
            lista = ingresoListaIngredientes() #implementar el ingreso de lista de ingredientes
            self.receta[pos].cambiarListaIngredientes(lista)
            print (f"Lista de ingredientes cambiada, lista de ingredientes {self.receta[pos].getterListaIngredientes()}") #implementar metodo para mostrar info lista ingredientes
            print("---- Cambio Tiempo de Preparacion ----")
            tiempop = input ("ingrese el nuevo tiempo de preparacion")
            self.receta[pos].cambiarTiempoPreparacion(tiempop)
            print (f"Tiempo de preparacion cambiado, nuevo tiempo de preparacion {self.receta[pos].getterTiempoPreparacion()}")
            print("---- Cambio Tiempo de Coccion ----")
            tiempoc = input ("ingrese el nuevo tiempo de coccion")
            self.receta[pos].cambiarTiempoCoccion(tiempoc)
            print (f"Tiempo de Coccion cambiado, nuevo tiempo de coccion {self.receta[pos].getterTiempoCoccion()}")
            print("---- Cambio de Etiquetas ----")
            etiquetas = ingresoEtiquetas() #implementar ingreso de etiquetas
            self.receta[pos].cambiarEtiquetas(etiquetas)
            print("---- Cambio Es Favorita ----")
            self.receta[pos].cambiarFavorita()
            


    def eliminarUnaReceta (self,recetaNombre):
        if (self.buscarReceta):
            self.eliminarReceta()
        else:
            print ("La receta no se encuentra almacenada")
        
        