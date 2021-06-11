# def suma(a,b):
#     sumas=a+b
#     return sumas

# x=(suma(5, 2))
# print(x)


def subtotal(producto,cantidad):
    subtotalesss=producto*cantidad
    return subtotalesss

t=subtotal(23000, 5)

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

    cantidad=int(input('ingrese la cantidad :  ')) 
    total += subtotal(precio, cantidad)
print(f"el precio del productos es : {total}")
print(f"el subtotales es : {t}")