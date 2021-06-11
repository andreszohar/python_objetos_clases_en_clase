nombre = input ("Para empezar, Cúal es tu nombre: ")
cali1 = float(input(nombre + " Cúal es tu calificación en Matemáticas: "))
cali2 = float(input(nombre + " Cúal es tu calificación en Español: "))
cali3 = float(input(nombre + " Cúal es tu calificación en Sociles: "))
resultado = cali1 + cali2 + cali3
promedio = resultado / 3
promedio = int(promedio)
if promedio >= 6 :
    print ('Felicidades '+ nombre + ' "Aprobaste" con un promedio de: ', promedio)

print ("Fin.")