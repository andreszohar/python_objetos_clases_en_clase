centinela = input("ingrese  si(s) / no (n)")
centiela: 'si'
contTotal = 0
cont = 0
cont2 = 0
while (centinela=='s'):
    genero = input("ingrese el genero femenino(f), masculino(m): ")
    if genero=='f':
        cont = cont + 1
    else:
        cont2 = cont2 + 1
        
    centinela = input ("desea continuar si(s), no (n)")
    contTotal = cont + cont2
print('el numero de mujeres es :  ', cont)
print('el numero de hombres es :  ', cont2)
print('el numero de total es :  ', contTotal)
# *****************************************************************************************************************************************************************
# se desea reclutar personal para los cargos de analista, desarrollador, arquitecto de software y el salario para cada uno tiene un estimado de la siguiente manera
# analista 870000, arquitecto 790000, desarrollador :2300000, se requiere saber el numero de personas que se presentan para cada uno de los cargos y conocer cuanto
#  seria el costo de inversion segun la cantidad de personas que se presentan.


aspirante = input("desea postularse en carvajal s o n: ")
a = 0
q = 0
d = 0
T_contratacion = 0
T_alt = 0
T_arq = 0
T_dev = 0
T_asp = 0


while aspirante=='s':
    vacante= input("ingrese la vacante a ocupar analista(a), arquitecto(q), desarrollador(d): ")
    a = a + 1
    d = d + 1
    q = q + 1
    T_alt = a * 700000
    T_dev = d * 2300000
    T_arq = q * 790000
    T_contratacion = T_alt + T_arq + T_dev
    T_asp = a+d+q	
    aspirante = input("desea continuar s o n: ")
print("la inversión en la contratación es de:  ", T_contratacion )
print("la contratación es de:  ", T_asp, "aspirantes" )

# ********************************************************************************************************************************************************************
# Se necesita conocer e numero de personas que asisten a comfama de las ballenitas y conocer el porcentaje de adultos, niños que ingresan al parque, la clasificacion
#  de niños esta desde  el mes de nacido hasta 15- joven de 16 a 18, y adulto de 18 en adelante. 
ninos = 0
jovenes = 0
adultos = 0
centinela = ''
personas = 0


centinela = input("deseas ingresar al parque? si o no: ")
while (centinela == 'si'):
    personas +=1
    age = int(input("ingresa tu edad: "))
    if (age <= 15):
        ninos+=1
        centinela = input("deseas ingresar al parque? si o no: ")
    elif(age >16 and  age <=18):
        jovenes+=1
        centinela = input("deseas ingresar al parque? si o no: ")
    else:
        adultos+=1
        centinela = input("deseas ingresar al parque? si o no: ")
print("El número de personas que ingresaron fuerón: ", personas)
print("El porcentage  de niños fue:  ", round(ninos / personas * 100),"%")               
print("El porcentage  de jovenes fue:  ", round(jovenes / personas * 100) ,"%")  
print("El porcentage  de adultos fue:  ", round(adultos / personas * 100),"%") 



# *******************************************************************************************************************************************************************
# Se requiere saber el numero de personas qe ingresan a un lavadero de vehiculos,  y establecer la cantidad de de personas por cada uno de los servicios,
#  si el servicio es sencillo o full, si el sencillo tiene un costo de 12000 y el full de 17000, ¿cual es la cantidad de dinero que se recolecto por cada uno de los
# servicios?

"""LAVADERO"""
personas = 0
full = 0
valorFull = 12000
sencillo = 0
valorSencillo = 17000
servicio = 0
tipo = ''

servicio = input("Desea alistar su vehículo si o no: ")
while (servicio == 'si'):
    personas +=1
    tipo = input("como desea el servicio Full(f), o sencillo (s): ")
    if (tipo == 'f'):
        full+=1
        servicio = input("Desea alistar su vehículo si o no: ")
    else:
        sencillo+= 1
        servicio = input("Desea alistar su vehículo si o no: ")

print("las personas que tomaron el servicio fue: ", personas)
print("las personas que tomaron el servicio full fue: ", full )
print("El total recaudado por el servicio full fue: ", full * valorFull)
print("las personas que tomaron el servicio sencillo fue: ", sencillo )
print("El total recaudado por el servicio sencillo fue: ", sencillo * valorSencillo)


# # **********************************************************
# 1.mostrar los primeros 10 numeros (imprimir contador)
num = 0 
while num < 10:
    num+= 1
    print(num)
# ********************************************************
# 2.mostrar los primeros 10 numeros positivos ( con modulo)
num = 0 
while num < 10:
    num+= 1
    if num % 2 == 0:
         print(num)
# ********************************************************
# 3.mostrar los primeros 10 numeros negativos impares.
num = 0 
while num > -10:
    num-= 1
    if num % 2 == 1:
        print(num)

# ********************************************************
# 4.mostrar la suma de los primeros 30 numeros pares
num = 0 
sum = 0
while num <=30 :
   
    num+= 2

    sum = sum + num
    print(num)
  
print(sum)

# *******************************************************
# 5.mostrar la suma de los primeros 10 numeros impares.
num = 0 
sum = 0
while num <=10 :
    num +=1
    if num % 2 == 1:
        
        sum = sum + num
        print(num)
print(sum)
# *******************************************************
# 6.mostrar la serie fibonaci.
fib = 0
suma = 1
num = 0
print(suma)
while fib <100:
    fib =  suma + num
    num = suma
    suma = fib
    
    print (fib)
# **********************************************************************************************************************************************************
# 7.El estadio atanasio girardot realizará el clasico de la montaña, se requiere
# saber el numero de boletas que se venden conociendo que la capacidad del estadio 
# es de 45000, pero no se vende necesariamente el total de boletas, ademas conocer
# el numero de personas que ingresaron a tribuna norte,sur, oriente, occidente
# el numero de mujeres y hombres que ingresaron.

capacidad = 450000
#Personas Norte = ?
#Personas Sur = ?
#Personas Oriente = ?
#Personas Occidente = ?

#Personas Hombres = ?
#Personas Mujeres = ?

norte = 0
sur = 0
oriente = 0
occidente = 0
mujeres = 0
hombres = 0
personas = 0
personas = input("Quieres disfrutar del clásico en vivo si o no : ")
while (personas == 'si'):
	genero = input("ingrese su genero masculino (m), femenino(f) : ")
	if (genero == 'f'):
		mujeres +=1
		ubicacion = input("ingrese su ubicación en las tribunas norte(n), sur(s), oriente(or), occidente(oc): ")
		if (ubicacion == 'n'):
			norte +=1
			personas = input("Quieres disfrutar del clásico en vivo si o no : ")	
		elif (ubicacion == 's'):
			sur += 1
			personas = input("Quieres disfrutar del clásico en vivo si o no : ")
		elif (ubicacion == 'or'):
			oriente += 1
			personas = input("Quieres disfrutar del clásico en vivo si o no : ")
		else:
			occidente += 1
			personas = input("Quieres disfrutar del clásico en vivo si o no : ")   
	if (genero =='m'):
		hombres +=1
		ubicacion = input("ingrese su ubicación en las tribunas norte(n), sur(s), oriente(or), occidente(oc): ")
		if (ubicacion == 'n'):
			norte +=1
			personas = input("Quieres disfrutar del clásico en vivo si o no : ")	
		elif (ubicacion == 's'):
			sur += 1
			personas = input("Quieres disfrutar del clásico en vivo si o no : ")
		elif (ubicacion == 'or'):
			oriente += 1
			personas = input("Quieres disfrutar del clásico en vivo si o no : ")
		else:
			occidente += 1
			personas = input("Quieres disfrutar del clásico en vivo si o no : ")
		
		
		
	
	       

print("el total de personas que ingresaron fueron: ", mujeres + hombres)
print("las personas que ingresaron a norte fueron: ", norte)
print("las personas que ingresaron a sur fueron: ", sur)
print("las personas que ingresaron a oriente fueron: ", oriente)
print("las personas que ingresaron a occidente fueron: ", occidente)
# ***********************************************************************************************************************************
# 8.La escuela de natación de la ciudad de medellín ofrece cursos para las edades
# (4 años a 8 años), (9 años a 12 años), con niveles basico, experimentado,
#  profesional, cada nivel tiene unos costos de 120000 nivel basico, 
# 250000 experimentado y profesional 280000.

age = 0
basico = 0
valorBasico = 120000
experimentado = 0
valorExperimentado = 250000
profecional = 0
valorProfecional = 280000
alumnos = 0
parbulos = 0
adolecentes = 0

centinela = input("Deseas inscribirte en el curso de natación si o no : ")
while (centinela == 'si'):
    alumnos += 1
    age = int(input("primero dinos tu edad: "))
    if (age > 12):
        print ('tienes demasiados años')
    elif (age <= 8):
        parbulos +=1
    elif(age >=9):
        adolecentes+=1

    nivel = input("En que nivel te vas a matricular basico(b), experimentado(e), profecional(p): ")
    if (nivel == 'b'):
        basico+=1
    elif (nivel == 'e'):
            experimentado +=1
    else:
            profecional+=1
    centinela = input("Deseas inscribirte en el curso de natación si o no : ")

print("alumnos matriculados: ", alumnos)  
print("alumnos menores de 8: ", parbulos)
print("alumnos mayores de 9: ", adolecentes)  
print("alumnos matriculados en nivel basico: ", basico)
print("Recaudo  en nivel basico: ", basico * valorBasico)
print("alumnos matriculados en nivel experimetado: ", experimentado)
print("Recaudo  en nivel basico: ", basico * valorExperimentado)
print("alumnos matriculados en nivel experimetado: ", profecional)
print("Recaudo  en nivel basico: ", basico * valorProfecional)


