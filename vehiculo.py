# 5.Realice un algoritmo que permita obtener el valor de cada uno de los vehículos teniendo la siguiente tabla de información.
 
 
# Marca	Precio	% Descuento
# Mazda	70.000.000	10%
# Renault	56.000.000	20%
# Chevrolet	64.000.000	11%
# Audi	170.000.000	10%
# Fiat	79.000.000	7%
# Toyota	80.000.000	12%

vehiculo=["Mazda", "Renault", "Chevrolet","Audi","Fiat","Toyota"]
valor=[(70000000/1.010),(56000000/1.020),(1.011),(170000000/1.010),(79000000/1.070),(80000000/1.012)]

print("los vehiculos es incritados segun este orden")
print("     0 = Mazda  ")
print("     1 = Renault ")
print("     2 = Chevrolet	 ")
print("     3 = Audi ")
print("     4 = Fiat ")
print("     5 = Toyota ")


brand = int(input("indique la marca por numeros del 0 AL 5  :   "))
if (brand>6):
    print("este numero no existe ")

else:

    cars = vehiculo[brand]
    precio = valor[brand]


print('-------------------------------------')

print(cars, precio)