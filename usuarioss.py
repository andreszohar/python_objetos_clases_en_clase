# 6. Se tiene una matriz con un tamaño para 100 registro de correos que le llega a un usuario donde se almacena un código consecutivo, la fuente (correo del remitente), el asunto y la descripción del correo y la fecha
# Se debe de hacer un algoritmo que cada que ingrese un nuevo correo lo haga de atrás hacia adelante es decir del ultimo enviado hacia la primera posición.  Con el objetivo de simular que los primeros queden visibles, se deben imprimir en ese orden.


# La mas sencilla e intuitiva
print("************(correo del remitente)*****************")
datos = [0 for x in range(10)]
for i in range(0,len(datos)):
    datos[i] = input( "-------Dime tu correo {} :  ".format(i+1) )
    
print ("*******Estos son los correos al reves   :  ********** ")
for i in range(len(datos),0,-1):
    print (" el orden es {} :".format(i), datos[i-1] )