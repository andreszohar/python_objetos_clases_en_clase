# 1.Inserte valores numéricos en el siguiente vector y ordénelos de forma ascendente, descendente. Muestre el menor valor y el mayor valor.
print("--------------- 1.Inserte valores numéricos ----------------------")
datos=[]
mayor = 0
menor = 0
for i in range(0,4):
    nuevoDato=int(input('Inserte numéros enteros  :   '  ))
    datos.append(nuevoDato)

print('-------------------------------------')

# vector asendente

datos.sort()
print(f'ascendentes {datos} ')
print()

print('---------------------------------------------')

# vector desendente
datos.reverse()
print(f'descendente  {datos}')
print()

print('---------------------------------------------')


# mayor y menor 
mayor = max(datos)
menor = min(datos)

print(f"este es el mayor {mayor}")
print()
print('---------------------------------------------')
print()
print(f"este es el menor {menor}")
print()

print()


# 2 Se tiene un vector de 20 posiciones donde se desean almacenar marcas de vehículos , y se tiene un segundo vector donde se almacenan los precios del mismo.Un cliente puede seleccionar cualquiera de las marcas que se ofrecen, deberá imprimir el valor de este.
print("-------------------2 Se tiene un vector de 20 posiciones-----------------------")

vehiculo=["Ford", "Volvo", "BMW","mazda","Renault","chevrolt","toyota" , "izusu", "international", "kembort", "daf", "cummis ","paccar ","yamaha " , "kinko", "nmax", "dt", "soldodas" , "kinua","duster"]
valor=[15000,5000,258,25888888,4563,789,258456,369,147,45688888,2225888,133333,14777777,354777777,15666666,16444444,1777777777,1822222,19000000,200000000000000000]
print()
print("************los vehiculos es incriptados segun este orden************")
print("     0 = Ford  ")
print("     1 = Volvo ")
print("     2 = BMW ")
print("     3 = mazda ")
print("     4 = Renault ")
print("     5 = chevrolet ")
print("     6 = toyota ")
print("     7 = izusu ")
print("     8 = international ")
print("     9 = kembort ")
print("     10 = daf ")
print("     11 = cummis ")
print("     12 = paccar ")
print("     13 = yamaha ")
print("     14 = kinko ")
print("     15 = nmax ")
print("     16 = dt ")
print("     17 = soldodas ")
print("     18 = kinua ")
print("     19 = duster ")

brand = int(input("indique la marca por numeros del 0 AL 19  :   "))
if (brand>19):
    print(" Error ******* este numero no existe **********************")

else:
    cars = vehiculo[brand]
    precio = valor[brand]


print(f'---este modelo {cars}, tiene un precio de  {precio} ------------------------')

print()

print()

# 3.Se tiene un vector que almacenara los nombres científicos de hongos, se deberá realizar un algoritmo que permita insertar los nombres en el vector, realizar la búsqueda, realizar la consulta por nombre. Para un total de 10 muestras.
print("------3.Se tiene un vector que almacenara los nombres científicos de hongos-----------")
print()
hongo = []
for i in range(0,5):
    nuevoHongo=str(input('insertar los nombres de los Hongos   :  '  ))
    hongo.append(nuevoHongo)


for i in range(0,5):
    print(hongo[i])
    print('-------------------------------------')

print()
Hongo_buscar = input('cual es el Hongo que deseas buscar  : ')
for i in range(0,5):

    if hongo[i]== Hongo_buscar:
        print(hongo[i],i)
        print("---------------------------------")

print("-------lista de hongos-------------")

for i in range(len(hongo)):
    print(hongo[i])

print()

# 4.Se desea realizar un algoritmo que almacene las letras del alfabeto, y debe mostrar las posiciones de las letras donde se encuentran cuando una persona, digita un nombre o una palabra.
print("--------4. algoritmo que almacene las letras del alfabeto,-----")
print()
import string
letra=[]
def listAlphabet():
  return list(string.ascii_lowercase)
print(listAlphabet())
letra=listAlphabet()
print("------------   orden en numeros del alfabeto------------------------------")
print()
for i in range(len(listAlphabet())):
      print(i)

print("---------------------------------+-----------------------------------------")
print()   

#  5.Se desea realizar un algoritmo que permita almacenar dos valores que son ingresados en código binario, y se debe de realizar la suma y la resta de estos dos valores.
print("------------5 numeros binarios ------------------------")

def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"
    binario = ""
    while decimal > 0:
        residuo = int(decimal % 2)
        decimal = int(decimal / 2)
        binario = str(residuo) + binario
    return binario

def decimal_a_binario2(decimal2):
    if decimal <= 0:
        return "0"
    binario2 = ""
    while decimal2 > 0:
        residuo2 = int(decimal2 % 2)
        decimal2 = int(decimal2 / 2)
        binario2 = str(residuo2) + binario2
    return binario2

print("-----------ingrese el un numero que desee convertir en binario-----------")
print()
decimal = int(input("Ingresa un número  : "))
binario = decimal_a_binario(decimal)
print("---------------------------------+-----------------------------------------")
print()
decimal2 = int(input("Ingresa un segundo número  : "))
print("---------------------------------+-----------------------------------------")
print()
binario2 = decimal_a_binario2(decimal2)
print("-------este es el resultado de los numeros convertidos en binarios ------------")
print(f"El número {decimal} es {binario} en binario")
print()
print("---------------------------------+-----------------------------------------")
print(f"El número {decimal2} es {binario2} en binario")
print()
suma = decimal+decimal2
resta = decimal-decimal2
print("---------------------------------+-----------------------------------------")
print(f"Esta es la suma de los número {suma}")
print()
print("--------------------------------------------------------------------------")
print(f"Esta es la resta de los número {resta}")



# 6.Se desea almacenar en un vector seis posiciones que corresponde a las caras de un dado, con la formula de valores aleatorios debe de generar un valor de uno a seis, se debe solicitar el numero de lanzamientos a realizar y luego calcular el valor obtenido en cada uno de los lances.
print()
print("-----------6 dados en juego----------------------------")
print()
import random
def unico(x,L):
  esUnico=True
  for i in range(len(L)):
    if x==L[i]:
      esUnico=False
      break
  return esUnico
L=[]
j=0
while j<6:
  x=random.randint(1,6)
  if unico(x,L):
    L.append(x)
    j+=1
print()
print("--------------a lanzar-----------------------------")
Lanzar=int(input("numero el cual desea lanzara del 1 al 6  :  "))
print()
esUnico = unico(x, L)
print("---------------------------------+-----------------------------------------")
print(f"numero aleatorio como los dados {L}")
print()
print("---------------------------------+-----------------------------------------")
print(f"el valor obtenido en cada uno de los lances {x}")











