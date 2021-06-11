#1. Un cliente realiza un préstamo al banco con una tasa anual de 13,6%, se requiere saber cual es el valor de la cuota a pagar si el préstamo se hace a 5 años, y la tasa es fija.

valorPrestamo=float(input("Ingrese el valor de prestamo: "))
intereses=float((valorPrestamo)*(0.0136))

cuotaMensual=intereses+(valorPrestamo/60)


print("La cuota mensual es de : " ,cuotaMensual)