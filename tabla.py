# 4.Realice un algoritmo que permita realizar una tabla de multiplicación y que se pueda llenar sola de la tabla del 1 hasta la tabla 14. 


tabla_desde = 1 
tabla_hasta = 14 
desde = 1 
hasta = 14 

for factor1 in range(tabla_desde, tabla_hasta + 1):
	print(f'Tabla de multiplicar del {factor1}:') 
	for factor2 in range(desde, hasta + 1):
		print(f'{factor1} x {factor2} = {factor1 * factor2}')
	print("------------------------------------------------------------------") 