datos=[]
for i in range(0,4):
    nuevoDato=int(input('ingrese valores enteros    '  ))
    datos.append(nuevoDato)

for i in range(0,4):
    print(datos[i])
    print('-------------------------------------')


valor_buscar=(int(input('cual es el numero que quiere buscar  ')))
for i in range(0,4):

    if datos[i]== valor_buscar:
        print(datos[i],i)

valor_buscar_eliminar=(int(input('cual es el numero que quiere eliminar  ')))
for i in range(0,4):

    if datos[i]== valor_buscar_eliminar:
        print(datos[i],i)
        datos[i]=0

for i in range(0,4):
    print(datos[i])

print('-------------------------------------------------------------------------------------------------------')

for i in range(0,1):
    datos.reverse()
    print('descendente')
    print(datos)

print('-----------------------------------------------------------------------------------------------------')
for i in range(0,1):
    datos.sort()
    print('ascendentes')
    print(datos)

print('-----------------------------------------------------------------------------------------------------')

    
    
    


