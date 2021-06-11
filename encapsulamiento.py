class inmueble:
       
  
    def _init_(self,referencia,mtc,prec,ubi,tipo):
        self.Referencia=referencia
        self.Metro_cuadrado=mtc
        self.precio=prec
        self.Ubicacion=ubi
        self.tipo=tipo
        self.datos=[]
        
    def insertar_valores(self, dato):
        self.datos.append(dato)
    
    def mostrar_valores(self,):
      print(self.datos) 
    
def get_Referencia(self):
    return self.Referencia

def set_Referencia(self, referencia):
    self.Referencia=referencia
    
    
def get_Metro_cuadrado(self):
        return self.Metro_cuadrado


def set_Metro_cuadrado(self, metro):
    self.Metro_cuadrado=metro
    
def get_Precio(self):
        return self.Precio

def set_Precio(self, p):
    self.Precio=p
    
def get_Ubicacion(self):
        return self.Ubicacion

def set_Ubicacion(self, ubic):
    self.Ubicacion=ubic
    
def get_Tipo(self):
    return self.tipo

def set_Tipo(self ,t):
    self.tipo=t

  
    
obj1=inmueble("",0,0,"","")
centinela="si"
while centinela=="si":
    set_Referencia=int(input("ingrese la referencia"))
    obj1.insertar_valores(set_Referencia)
    set_Metro_cuadrado=int(input("ingrese metro cuadrado"))
    obj1.insertar_valores(set_Metro_cuadrado)
    set_Ubicacion=input("ingrese ubicacion")
    obj1.insertar_valores(set_Ubicacion)
    set_Tipo=input("ingrese tipo de inmueble")
    obj1.insertar_valores(set_Tipo)
    centinela=input("desea continuar si /no")
    
obj1.mostrar_valores()