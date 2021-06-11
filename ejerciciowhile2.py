

cont=0
suma=0
cont_gan=0
cont_per=0
nota=0
while (cont<2):
    nombre=input("ingrese su nombre")
    print(cont)
    cont1=0
    while (cont1<2):
        notaMateria=float(input("ingrese las notas"))
        print(cont1) 
        suma=suma+nota
        cont1=cont1+1
cont=cont+1
promedio=suma/5
if (promedio>3.0):
    print("gano materia")
    cont_gan=cont_gan+1
else:
    print("no gano la materia ")
    cont_per=cont_per+1
    cont=cont+1

print("el numero total de estudiantes que ganaron es  ",cont_gan)
print("el numero total de estudiantes que perdieron  es  ",cont_per)

# ejercicio de equipos
equipos=0


while (equipos<2):
    nombreEquipo=input("ingrese el nombre del equipo")
    print(equipos)
    jugadores=0
    while (jugadores<2):
        identidadJugador=input("ingrese el identidad Jugador")
        nombrejugador=input("ingrese el nombre jugador")
        jugadores+=1
    equipos+=1

print("total de equipos es   ",equipos, '\n')
print("total de jugadores es   ",jugadores)
     
        

