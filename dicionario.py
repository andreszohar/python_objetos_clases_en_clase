
frutas = {
    "platano": 135,
    "manzana": 200, 
    "pera": 100, 
    "naranjas": 500
}
fruta = input('Que frutas deseas :  ')
kg = int(input('¿Cuantos kilos quiere : '))

if fruta in frutas:
    valor = frutas[fruta]*kg 
    print(f"el precio de {fruta} es : {valor}") 
else:
     print('no esta')
     print('no se encuentra el producto selecionado')



