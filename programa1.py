print ("hola")
numero_uno = 5
numero_dos = 45
resultado = numero_uno + numero_dos
resultado = str(resultado)
print ("El resultado es: " + resultado)


mensaje = "hola"
mensaje += " "
mensaje += "pedro"
print (mensaje)

print("Concatenación: ")
mensaje1 = "Hola como te va "
espacio = " "
nombre = "pedro"
print(mensaje1+espacio+nombre)

buscar_subcadena= mensaje1.find("pedro")
print (buscar_subcadena)

print("Extraer")

mensaje2 = "Hola pedro"
extraer_subcadena = mensaje2[0:6]
print (extraer_subcadena)

print ("COMPARACIÖN")

mensaje_uno ="Hola"
mensaje_dos = "Hola"

print(mensaje_uno == mensaje_dos)