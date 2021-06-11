bello = 0
sanAntonio = 0
sanJavier = 0
dia = int(input("digita el dia del muestreo: "))
i = 0
total = 0

while i<=dia:
    i = i +1 
    bello = dia*2   
    sanAntonio = bello * 1.2
    sanJavier = dia * 1.2
total = bello + sanAntonio + sanJavier   

    
  

print("los pasajeros en Bello son: " , bello)
print("los pasajeros en sanAntonio son: " , int(sanAntonio))
print("los pasajeros en sanJavier son: " , int(sanJavier))
print("los pasajeros en total son: " , int(total))