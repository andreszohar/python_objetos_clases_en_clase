#Un estudiante realiza un préstamo para pagar su semestre de un monto N, para pagar en 12 meses, la cuota mensual tiene una tasa del  1.8%, a continuacion de solución respondiendo las siguientes preguntas:

#1)¿Cuánto ha pagado los dos primeros meses de intereses?
#2)¿Cuánto es el valor de la cuota mensual?
#3)¿Cuánto dinero se ha cancelado a los 9 meses de estar pagando el crédito?
#4)¿Cuánto es el total pagado por concepto de intereses?


valorPrestamo=int(input("Ingrese su monto a prestar: "))
interesMensual=0.018*(valorPrestamo/12)
pagoMensual=interesMensual+(valorPrestamo/12)

print("En los dos primeros meses a pagado en intereses: ",interesMensual*2, "$")
print("El valor de la cuota mensual es de: " , pagoMensual)
print("A los nueve meses a cancelado un total de: ",pagoMensual*9)
print("El total pagado con los intereses al finalizar la deuda es de: " ,pagoMensual*12)