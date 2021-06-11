# <<<<<<< HEAD


fibonacci=1 
auxiliar=0
init = 1


while (init<=10):
     auxiliar += fibonacci 
     fibonacci = auxiliar - fibonacci
     init += 1
     print(fibonacci)
=======


auxiliar, fibonacci, init = 1, 0, 1
_INFO = """Ingrese un numero para iniciar la sucesion de fibonacci"""
print(_INFO)
limite = int(input("este numero es un Array para que lo tengo : "))

if limite > 0:
    while init <= limite:
        print("[{0}]".format(fibonacci), end=" ")
        auxiliar += fibonacci 
        fibonacci = auxiliar - fibonacci
        init += 1
    print()
else:
    print("El numero que ingrese debe ser mayor a cero!!")

