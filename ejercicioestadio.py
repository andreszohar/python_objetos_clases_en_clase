# <<<<<<< HEAD
boletas=0
capacidad=45000
hombres=0
mujeres=0
personas=0

solicitud="si"

solicitud=input("desea comprar boletas (si o no ) :  ")
while (solicitud=="si"):
    venta=int(input("cuantas boletas desea comprara  : "))
    if(venta<=capacidad):
        boletas=boletas+1
    tribuna=input("escoja tribuna a la que desea ingresar norte sur oriental occidente  : ")  
    if(tribuna=="norte")or (tribuna=="sur")or (tribuna=="oriental")or(tribuna=="ocidental"):
        personas=personas+1
    genero=input("ingeresa tu genero hombre o mujer  : ")
    if(genero=="hombres"):
        hombres=hombres+1
    elif(genero=="mujeres"):
        mujeres=mujeres+1
    solicitud=input("desea comprar boletas (si o no ) :  ")

    

totalventas=boletas+venta
m=hombres
f=mujeres
ingresos=m+f
print("total de ventas es  :",totalventas)
print("total de ingreso por genero ",ingresos)
print("total de hombres son :",m)
print("total de mujeres son :",f)
print("total de boletas vendida son  :",venta)
print("capacidad total : ",capacidad-venta)




=======
boletas=0
capacidad=45000
hombres=0
mujeres=0
personas=0

solicitud="si"

solicitud=input("desea comprar boletas (si o no ) :  ")
while (solicitud=="si"):
    venta=int(input("cuantas boletas desea comprara  : "))
    if(venta<=capacidad):
        boletas=boletas+1
    tribuna=input("escoja tribuna a la que desea ingresar norte sur oriental occidente  : ")  
    if(tribuna=="norte")or (tribuna=="sur")or (tribuna=="oriental")or(tribuna=="ocidental"):
        personas=personas+1
    genero=input("ingeresa tu genero hombre o mujer  : ")
    if(genero=="hombres"):
        hombres=hombres+1
    elif(genero=="mujeres"):
        mujeres=mujeres+1
    solicitud=input("desea comprar boletas (si o no ) :  ")

    

totalventas=boletas+venta
m=hombres
f=mujeres
ingresos=m+f
print("total de ventas es  :",totalventas)
print("total de ingreso por genero ",ingresos)
print("total de hombres son :",m)
print("total de mujeres son :",f)
print("total de boletas vendida son  :",venta)
print("capacidad total : ",capacidad-venta)




>>>>>>> 28e3dae935986658287930d8ace2adf434424120
