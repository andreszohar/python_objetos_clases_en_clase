asignatura = {
    "calculo":6,
    "etica":2,
    "fisica": 3,
    "programacion":5,
    "baseDT":5
}

total_creditos = 0

for materia,creditos in asignatura.items():
    print(materia, 'tiene ', creditos)
    total_creditos+= creditos
print('el total del credito es : ',total_creditos)

maticula = {}
centinela = "s"
while centinela == "s": 
    clave= input(' introduccir el producto que deseas comprar    :   ')
    valor = input(clave+ '  :  ')
    maticula[clave]= valor
    print(maticula)
    centinela = input('si desea continuar aprima s de lo contrario oprima cualquiera tecla  :  ')
print(maticula)