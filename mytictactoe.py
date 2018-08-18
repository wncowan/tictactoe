import random

def drawBoard(board):
    
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def getPlayerMove(board):
    move = " "
    while move not in "1 2 3 4 5 6 7 8 9".split() or not isSpaceFree(board, int(move)):
        print("whats your next move? (1-9)")
        move = raw_input()
    return int(move)   

def getComputerMove(board, computerLetter):
    if computerLetter == "X":
        playerLetter = "O"
    else:
        playerLetter = "X"

    for i in range(1,10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i

    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    if isSpaceFree(board, 5):
        return 5

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    # We use bo instead of board and le instead of letter so we don't have to type as much.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board, move):
    return board[move] == " "
    
def makeMove(board, letter, move):
    board[move] = letter

def inputPlayerLetter():
    letter = ""
    while not (letter == "X" or letter == "O"):
        print("Do you want to be X or O?")
        letter = raw_input().upper()
    
    if letter == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]

def whoGoesFirst():
    if random.randint(0,1) == 0:
        return "computer"
    else:
        return "player"



    

print("welcome to ttt")
program_running = True

while program_running:

    theBoard = [" "] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    print "playerLetter", playerLetter, "computerLetter", computerLetter
    turn = whoGoesFirst()
    print "turn", turn
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == "player":
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print("you won!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("tie")
                    gameIsPlaying = False
                else:
                    turn = 'computer'

        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("computer wins!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("tie!")
                    gameIsPlaying = False
                else:
                    turn = "player"
    print('Do you want to play again? (yes or no)')
    if not raw_input().lower().startswith('y'):
        program_running = False

# start while loop for the program to run
# create a blank board -- empty list with empty spaces " "
# prompt user to choose "X" or "O", based on their choice assign a letter for the computer
# determine who goes first by random coin flip
# within while loop start a while game loop so when game ends, user can restart
# draw the board
# get the player's move
# check if that move is going to result in a win 
# the isWinner function will accept a board argument and the letter to check for
# isWinner will have all permutations resulting in a win
# check if that move will result in a full board aka tie  with isBoardFull
# else, make the move and then make it the computers turn

# if it is the computer's move, 
# we need to have the computer choose a move, 
# that will block the player from success, or will result in a computer win.
# When the board is blank or player has no chance of winning yet,
# have the computer preference a corner spot and then middle

# to check if the move would result in a win,
# we should make a copy of the board to not affect the original data
# go through each spot, make a move there, 
# check if on of the conditions is true 
# (player would win here so block, computer would win here so win)