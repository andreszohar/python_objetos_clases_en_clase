# <<<<<<< HEAD
solicitud=input("desea ingresar (si o no)")
adultos=0
ninos=0

contadorninos=0
contadoradultos=0

while (solicitud=="si"):
    edad=int(input("cuantos anos tienes?  "))
    if(edad<=15):
        contadorninos+=1
    else:
        contadoradultos+=1
    solicitud=input("desea ingresar (si o no)")

contadortotalpersonas=contadorninos+contadoradultos

print("el porcentaje adulto es  ",round(contadoradultos/contadortotalpersonas,2))
print("el porcentaje nino es  ",round(contadorninos/contadortotalpersonas,2))
=======
solicitud=input("desea ingresar (si o no)")
adultos=0
ninos=0

contadorninos=0
contadoradultos=0

while (solicitud=="si"):
    edad=int(input("cuantos anos tienes?  "))
    if(edad<=15):
        contadorninos+=1
    else:
        contadoradultos+=1
    solicitud=input("desea ingresar (si o no)")

contadortotalpersonas=contadorninos+contadoradultos

print("el porcentaje adulto es  ",round(contadoradultos/contadortotalpersonas,2))
print("el porcentaje nino es  ",round(contadorninos/contadortotalpersonas,2))

