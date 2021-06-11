edad=0
estatura=0
peso=0
imc =0 
pesoideal=0

cont=0
contedad=0
contpeso=0
contestatura=0

while (cont<2):
    

    edad=input("ingrese la edad")
    peso=float(input("ingrese el peso solo los numeros")) 
    estatura=float(input("ingrese la estatura "))
    print(cont)

    imc=(peso/estatura)
    pesoideal=imc*(100/10)
    if (imc>pesoideal):
        
        print("estas godo")
        contpeso+=1

    else:
        
        print("estas delgado")
        
        contestatura+=1
    cont=cont+1
print("el peso es " ,contpeso)
print("el estatura es " ,contestatura)

    