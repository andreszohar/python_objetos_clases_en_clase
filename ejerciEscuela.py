contador =0 
nombreEquipo=''
nombrejugador=''
documento=''
posicionJugador=''

while (contador<3):
    nombreEquipo=input('ingrese el nombre del equipo   ')
    contador+=1
    contador1=0
    while (contador1<3):
        contador1+=1
        nombrejugador=input('ingrese el nombre del jugador  ')
        documento=input('ingrese el documento del jugador  ')
        posicionJugador=input('en que posicion juega  ')
        print('nombre de los equipos a participar  : '+ nombreEquipo)
        print('nombre de los jugadores del equipo  : '+ nombrejugador)
        print('posicion del jugador en la cancha   : '+ posicionJugador)
print('estamos listos para jugar')