
board = [" " for x in range(10)]


def insertLetter(letter, position):
    board[position] = letter

def isSpaceFree(position):
    return board[position] == " "
    
def printBoard(board):
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |   ")
    print("------------")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |   ")
    print("------------")
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |   ")

def isBoardFull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True
    
def winner(b, l):
    return (b[1] == l and b[2] == l and b[3] == l) or (b[4] == l and b[5] == l and b[6] == l) or (b[7] == l and b[8] == l and b[9] == l) or (b[1] == l and b[4] == l and b[7] == l) or (b[2] == l and b[5] == l and b[8] == l) or (b[3] == l and b[6] == l and b[9] == l) or (b[1] == l and b[5] == l and b[9] == l) or (b[3] == l and b[5] == l and b[7] == l)
    
def playerMove():
    run = True
    while run:
        move = input("Please choose a position to enter the X between 1 and 9")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if isSpaceFree(move):
                    run = False
                    insertLetter("X", move)
                else:
                    print("This space is taken")
            else:
                print("Please type a number between 1 and 9")

        except:
            print("Please typa a number")


def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == " " and x != 0]      
    move = 0

    for let in ["O", "X"]:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let     
            if winner(boardcopy, let):
                move = i
                return move        

    cornersOpen = []
    for i in possibleMoves:
        for i in [1, 3, 7, 9,]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom()
        return move
    
    if 5 in possibleMoves:
        move = 5
        return move
    
    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom()
        return move
    
    def selectRandom(list):
        import random
        ln = len(list)
        r = random.randrange(0, ln)
        return list[r]
        
def main():
    print("Welcom to the game of Tic Tac Toe!")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(winner(board, "O")):
            playerMove()
            printBoard(board)
        else:
            print("Loser :(")
            break

        if not(winner(board, "X")):
            move = compMove()
            if move == 0:
                print ("Tie Game!")
            else:
                insertLetter("O", move)
                print("Computer has made the move!", move, ":" )
                printBoard(board)

        else:
            print("Winner Winner Chicken Dinner!")
            break


    if isBoardFull(board):
        print("Tie Game!")

