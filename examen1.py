# 1.	La escuela marceliano desea obtener el promedio de notas de un grupo de 25 estudiantes, y los 25 se les solicita 5 notas  por cada una de las materias (matemática y lenguaje).
# Se debe imprimir el promedio de notas por cada materia, se debe imprimir el promedio de notas de las dos asignaturas por estudiante y se debe imprimir el total general del grupo.
# (Ciclos anidados)


notas=0
materias=5
# // por notas 
notaMatematicas=0
notaLenguaje=0
# //por matrias 
notaTotalMatematicas=0
notaTotalLenguaje=0

print("******************Colegio Marceliano*****************\n ")

while(notas<materias):  
    notaPorMatematicas=0
    materias=1
    print("Ingrese las 5 Notas de la asignatura materia Matemáticas")
    while(materias<6):
        notaMatematicas=float(input("Ingrese Nota "+str(materias)+" "))
        notaPorMatematicas=notaPorMatematicas+notaMatematicas
        materias=materias+1
    promedioMatematicasXalumno=notaPorMatematicas/5
    print("El promedio de la materia matemáticas es: "+str(promedioMatematicasXalumno))
    notaTotalMatematicas=notaTotalMatematicas+notaPorMatematicas


    
    notaPorLenguaje=0
    materias=1
    print("Ingrese las 5 Notas de la asignatura materia Lenguaje")
    while(materias<6):
        notaLenguaje=float(input("Ingrese Nota "+str(materias)+" "))
        notaPorLenguaje=notaPorLenguaje+notaLenguaje
        materias=materias+1
    promedioLenguajeXalumno=notaPorLenguaje/5
    print("El promedio de la materia Lenguaje es: "+str(promedioLenguajeXalumno))

    print("--------------------------------")
    
    promedioDosMaterias=(notaMatematicas+notaPorLenguaje)/10
    print("El promedio de las dos Asignaturas es= "+str(promedioDosMaterias))
    notaTotalMatematicas=notaTotalMatematicas+notaPorMatematicas

    
    notas=notas+1


print("--------------------------------")
promedioPorTodos=(notaTotalLenguaje+notaTotalMatematicas)/50
print("El promedio Total del grupo es: "+str(promedioPorTodos))
