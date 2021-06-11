edad=0
eps=''
consentimiento="si"
generomasculino="m"
generofemenino="f"

contadorgenerofemino=0
contadorgeneromasculino=0
contadoredad=0

porcentajemujeres=0
porcontajehombres=0
participantes=0
contadorgenero=0

consentimiento=input('Este es el consentimiento para poder volar en el parapente esta de acuerdo si o no  ? :  ')
while (consentimiento=='si'):
    participantes=float(input('número de participantes para volar como gallinas: '))
    contador=0
    promedioM = 0
    promedioF = 0
    while (contador<participantes):
        edad=float(input('cuantos anos tiene  : '))
        contador+=1
    #    genero=float(input('genero m = masculino f = femenino'))
        eps=input('que eps esta afiliado    :   ')
        if (edad>15 and edad<=60):
            
            contadoredad+=1
        else:
            print("No tienes la edad adecuada para volar en parapente...  ")
            consentimiento = 'no' 
        genero=input('genero m = masculino f = femenino  :     ')       
        if  (genero=="m"):
            contadorgeneromasculino+=1
            print(contador)
            print(contadorgeneromasculino)
        elif  (genero=="f"):
            contadorgenerofemino+=1
            print(contador)
            print(contadorgenerofemino)
    promedioM = (contadorgeneromasculino / contador) * 100 
    promedioF = (contadorgenerofemino / contador) * 100
    recaudado = 80000*contador    
    print('promedio de mayores  :  ', contadoredad)
    print('El total de hombres es  : ', contadorgeneromasculino)
    print('promedio de hombres   :', round(promedioM),'%' )
    print('promedio de de mujeres   : ', round(promedioF),'%')
    print('El total recaudado es de    :  ', recaudado)    
    consentimiento=input('Este es el consentimiento para poder volar en el parapente esta de acuerdo si o no  ?  :  ') 