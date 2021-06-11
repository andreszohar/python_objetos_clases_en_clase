# Tic Tac Toe

import random

def drawBoard(board):
   # Esta función imprime el tablero que se aprobó.

     # "tablero" es una lista de 10 cadenas que representan el tablero (ignore el índice 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    # Dejemos que el jugador escriba qué letra quiere ser.
     # Devuelve una lista con la letra del jugador como primer elemento y la
     # letra de la computadora como la segunda.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('¿Quieres ser X u O?')
        letter = input().upper()

    # el primer elemento de la tupla es la letra del jugador, el segundo es
     # la carta de la computadora.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
   # Elija aleatoriamente el jugador que va primero.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    # Esta función devuelve True si el jugador quiere volver a jugar, de lo contrario
     # devuelve False.
    print('¿Quieres jugar de nuevo? (sí o no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(bo, le):
   # Dado un tablero y la letra de un jugador, esta función devuelve Verdadero si eso
     # jugador ha ganado. Usamos bo en lugar de board y le en lugar de letter, así que
     # no tenemos que escribir tanto.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # a través de la cima
    (bo[4] == le and bo[5] == le and bo[6] == le) or # en el medio
    (bo[1] == le and bo[2] == le and bo[3] == le) or # en la parte inferior
    (bo[7] == le and bo[4] == le and bo[1] == le) or #  por el lado izquierdo
    (bo[8] == le and bo[5] == le and bo[2] == le) or # por la mitad
    (bo[9] == le and bo[6] == le and bo[3] == le) or # por el lado derecho
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
    # Haga un duplicado de la lista del tablero y devuélvale el duplicado.
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isSpaceFree(board, move):
    #Devuelve verdadero si el movimiento pasado está libre en el tablero pasado.
    return board[move] == ' '

def getPlayerMove(board):
    #Deja que la jugadora escriba en su movimiento.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('¿Cuál es tu próximo movimiento? (1-9) ')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, movesList):
    # Devuelve un movimiento válido de la lista de pases en el tablero de pases.
     # Devuelve Ninguno si no hay un movimiento válido.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def getComputerMove(board, computerLetter):
    # Dada una pizarra y la letra de la computadora, determine dónde moverse y
     # devuelve ese movimiento.
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Aquí está nuestro algoritmo para nuestro Tic Tac Toe AI:
     # Primero, compruebe si podemos ganar en el próximo movimiento
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

   # Comprueba si el jugador puede ganar en su próximo movimiento y bloquéalo.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

   # Intenta tomar una de las esquinas, si están libres.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

   # Trate de tomar el centro, si es gratis.
    if isSpaceFree(board, 5):
        return 5

  # Muévete por uno de los lados.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    # Devuelve Verdadero si se han ocupado todos los espacios del tablero. De lo contrario
     # falso retorno.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('¡Bienvenido al juego del triqui!')

while True:
    # Reiniciar la placa
    theBoard = [' '] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print('El ' + turn + ' Irá primero.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            # Turno del jugador.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('¡Hurra! ¡Has ganado el juego!')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('¡El juego es un empate!')
                    break
                else:
                    turn = 'computer'

        else:
            # Computer's turn.
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('¡La computadora te ha vencido! Tú pierdes.')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('¡El juego es un empate!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break