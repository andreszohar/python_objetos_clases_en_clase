capurgana=1500000
nuqui=1200000
islamargarita=200
islagalapagos=400
mukura=1200000
islasanandres=1500000
# tasa
tasacapurgana=0.15
tasanuqui=0.09
tasamargarita=.016
tasagalapagos=0.08
tasamukura=0.09
tasasanandres=0.12
# impuestos
impuestoscapurgana=0.2
impuestosnuqui=0.19
impuestosmargarita=0.11
impuestosgalapagos=0.09
impuestosmukura=0.11
impuestossanandres=0.13

# contadores

contadorcapurgana=0
contadornuqui=0
contadorislamargarita=0
contadorislagalapagos=0
contadormukura=0
contadorislasanandres=0

pasajeros=0
# tarifatotal=0



breakcentinela=input('desea salir de vaciones con covid-19 incluido si o no ?    ')
while (breakcentinela=='si'):
    pasajeros=int(input( 'numero de pasajeros que desean viajar    '))  
    contador=0
    while (contador<pasajeros):
        contador+=1
        print(contador)
        print('"1" = capurgana ')
        print('"2" = nuqui  ')
        print('"3" = isla margarita  ')
        print('"4" = isla galapago  ')
        print('"5" = isla mukura  ')
        print('"6" = isla san andres  ')
        viajes=0
        viajes=int(input('eliga un numero para su destino    ')) 
        if (viajes==1):
            contadorcapurgana+=1
            tarifatotal=capurgana*impuestoscapurgana*tasacapurgana
        elif (viajes==2):
            contadornuqui+=1
            tarifatotal=nuqui*impuestosnuqui*tasanuqui
        elif (viajes==3):
            contadorislamargarita+=1
            tarifatotal=islamargarita*impuestosmargarita*tasamargarita
        elif (viajes==4):
            contadorislagalapagos+=1
            tarifatotal=islagalapagos+impuestosgalapagos+tasagalapagos
        elif (viajes==5):
            contadormukura+=1
            tarifatotal=mukura*impuestosmukura*tasamukura
        elif (viajes==6):
            contadorislasanandres+=1
            tarifatotal=islasanandres*impuestossanandres*tasasanandres

        breakcentinela=input('desea salir de vaciones con covid-19 incluido si o no?  ')
        

        print('valor de la tarifa   por viaje  ',tarifatotal,'\n')
        print('total de pasajeros  para viajar  ',pasajeros,'\n')


   
print('total de los viajes    ',viajes ,'\n')
print('total de a viajar  pasajeros  ',contador ,'\n')




       
    


