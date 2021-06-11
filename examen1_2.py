# 2.	Santiago desea adquirir un carro para ello le solicitan el 30% de la cuota inicial, y el resto para financiamiento, teniendo en cuenta las políticas del negocio, permite la financiación si el préstamo se hace como mínimo 3 años y máximo 5 años para su cancelación; el préstamo cuenta con una tasa del 12.5% anual.
# ¿Cuánto dinero se paga en el mes?
# ¿cuánto dinero para de acuerdo con la cantidad de años seleccionados por el cliente?

# Nota: debe solicitar el valor del vehículo  y el tiempo de financiación de este.

print("hola Santiago recuerdo que si deseas obtener un vehiculo con nosotros necesitas el 30 porciento de la cuota inicial del valor del vehiculo  ")


valorvehiculo=int(input(" Ingrese el valor del vehiculo   "))
treintaPorciento=valorvehiculo*0.3
valordelafinanciacion=valorvehiculo+treintaPorciento
impuestos=0.125
print("este es el porcentaje que debe de tener para este vehiculo  ")
print(treintaPorciento)

print("A cuantos tiempo desea financiar su vehiculo  ")
print("Máximo a 5 años = 60 meses")
print("Minimo a 3 años = 36 meses")
print("Por ejemplo 4 años exactos= 48 meses")
tiempo=int(input("por favor indique solo el número en meses  :  "))

if(tiempo<=35 or tiempo>=61):
    print("se sale del premedio de meses por favor reitentarlo  ")
else:
    print("Así quedara la financiación de su vehiculo segun los meses ")
    interesestotalesdelafinaciacion=valordelafinanciacion*(tiempo/12)*impuestos
    totalvalordelcredito=interesestotalesdelafinaciacion+valordelafinanciacion
    totalpagoporsimplemensual=totalvalordelcredito/tiempo

    print("-----------------------------------------------------------")
    print("Los intereses a pagar son  :  ")
    print(round(interesestotalesdelafinaciacion)) 
    print("La deuda total de su vehiculo es   :  ")
    print(round(totalvalordelcredito))
    print("Mensualmente pagas a interes simple por su vehiculo :  ")
    print(round(totalpagoporsimplemensual))