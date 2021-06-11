

colegios=0

ingresos=input('desea ingresar al colegio  si o no  :  ')
while (ingresos=='si'):
    colegios+=1
    nombrecolegio=input('ingrese el nombre del colegio : ')
    numeroalumnos=0
    while (numeroalumnos<3):
        numeroalumnos+=1
        cursos=input('en que curso desea participar :  ')
        edadalumno=float(input('cuantos anos tiene el alumno  :  '))
        print('el nombre del colegio es  '+nombrecolegio+ 'el alumno va a cursas el curso  ' +cursos)
ingresos=('quieres ingresar otro colegio ')

