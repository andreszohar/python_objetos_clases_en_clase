


contador=0
contador2=0
centinela=input("ingrese si o no ")
while (centinela=="si"): 
    genero=input("ingrese su genero")
    if (genero=="mujer"):
        contador=contador+1
    else:
        contador2=contador2+1
    
    
    print("ingrese si desea continuar  ")
    continuar=input("si o no")


contador_suma=contador+contador2

print("el numero de los hombres es   ",contador)
print("el numero de los mujeres es   ",contador2)
# =======


contador=0
contador2=0
centinela=input("ingrese si o no ")
while (centinela=="si"): 
    genero=input("ingrese su genero")
    if (genero=="mujer"):
        contador=contador+1
    else:
        contador2=contador2+1
    
    
    print("ingrese si desea continuar  ")
    continuar=input("si o no")


contador_suma=contador+contador2

print("el numero de los hombres es   ",contador)
print("el numero de los mujeres es   ",contador2)
>>>>>>> 28e3dae935986658287930d8ace2adf434424120
print("el numero de hombres y mujeres es    ",contador_suma)