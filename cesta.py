Cesta = {}
centinela = "s"
while centinela == "s": 
    clave= input(' introduccir el producto que deseas comprar    :   ')
    valor = int(input(clave+ '  :  '))
    Cesta[clave]= valor
    print(Cesta)
    centinela = input('si desea continuar aprima s de lo contrario oprima cualquiera tecla  :  ')
print(Cesta)

total = 0
for null,precio in Cesta.items():
    total += precio
print(f"el precio del productos es : {total}")