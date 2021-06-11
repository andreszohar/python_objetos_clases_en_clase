
print("bienvenido a la escula de natacion ")
solicitud=input("deseo ingresar a uno de nuestros cursos  si o  no    ")

nino=0
adolecentes=0
contadorninos=0
contadoradolecentes=0

basico=0
experimentado=0
profesional=0

while (solicitud=="si"):
    edad=int(input("cual es su  edad debe de ser entre 4 anos o 12 anos   : "))
    if(edad<=4)or(edad<=8):
        contadorninos+=1
    elif (edad>=9)or(edad<=12):
        contadoradolecentes+=1
    elif (edad>13)or(edad>=10000):
        print("ya estas mayor para este curso por favor saca la cc y pongase a trabajar")
    curso=input("cual es el curso que desea basico,experimentado,profesional  :  ")
    if (curso=="basico"):
        curso=basico+120000
        if (curso=="experimentado"):
            curso=experimentado+250000
            if (curso=="profesional"):
                curso=profesional+280000
    elif  (curso=="  ")or(curso!="basico")or(curso!="experimentado")or(curso!="profesional"):
        print("este curso no esta disponible o no existe ")
    solicitud=input("deseo ingresar a uno de nuestros cursos  si o  no    ")

controltotaldeninos=contadorninos+contadoradolecentes



print("total de ninos son  : ",controltotaldeninos)
print("el curso que deseo cuesta  : ",curso)
# =======
print("bienvenido a la escula de natacion ")
solicitud=input("deseo ingresar a uno de nuestros cursos  si o  no    ")

nino=0
adolecentes=0
contadorninos=0
contadoradolecentes=0

basico=0
experimentado=0
profesional=0

while (solicitud=="si"):
    edad=int(input("cual es su  edad debe de ser entre 4 anos o 12 anos   : "))
    if(edad<=4)or(edad<=8):
        contadorninos+=1
    elif (edad>=9)or(edad<=12):
        contadoradolecentes+=1
    elif (edad>13)or(edad>=10000):
        print("ya estas mayor para este curso por favor saca la cc y pongase a trabajar")
    curso=input("cual es el curso que desea basico,experimentado,profesional  :  ")
    if (curso=="basico"):
        curso=basico+120000
        if (curso=="experimentado"):
            curso=experimentado+250000
            if (curso=="profesional"):
                curso=profesional+280000
    elif  (curso=="  ")or(curso!="basico")or(curso!="experimentado")or(curso!="profesional"):
        print("este curso no esta disponible o no existe ")
    solicitud=input("deseo ingresar a uno de nuestros cursos  si o  no    ")

controltotaldeninos=contadorninos+contadoradolecentes



print("total de ninos son  : ",controltotaldeninos)
print("el curso que deseo cuesta  : ",curso)

