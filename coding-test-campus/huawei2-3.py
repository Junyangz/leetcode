import random

def TTT_solution(theBoard: list)-> int:
    firstPlayer, secondPlayer = 1, 2
    while True:
        if not checkBoard(theBoard):
            if isBoardFull(theBoard):
                return 0
            if theBoard.count(1) == theBoard.count(2):
                turn = firstPlayer
            else:
                turn = secondPlayer
            move = getNextMove(theBoard, turn)
            makeMove(theBoard, turn, move)
        else:
            return checkBoard(theBoard)


def isSpaceFree(board, move):
    return board[move] == 0

def makeMove(board, letter, move):
    board[move] = letter

def chooseRandomMoveFromList(board, movesList):
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
def getNextMove(board, pLetter):
    if pLetter == 1:
        opLetter = 2
    else:
        opLetter = 1

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, pLetter, i)
            if isWinner(copy, pLetter):
                return i

    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, opLetter, i)
            if isWinner(copy, opLetter):
                return i

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    if isSpaceFree(board, 5):
        return 5

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def checkBoard(bo):

    if (isWinner(bo, 1) and isWinner(bo, 2)) or (bo.count(1) - bo.count(2)) not in [1, 0]:
        return -1
    elif isWinner(bo, 1):
        return 1
    elif isWinner(bo, 2):
        return 2
    else:
        return 0

def getBoardCopy(board):
    dupeBoard = []

    for i in board:
        dupeBoard.append(i)

    return dupeBoard

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or 
    (bo[4] == le and bo[5] == le and bo[6] == le) or 
    (bo[1] == le and bo[2] == le and bo[3] == le) or 
    (bo[7] == le and bo[4] == le and bo[1] == le) or 
    (bo[8] == le and bo[5] == le and bo[2] == le) or 
    (bo[9] == le and bo[6] == le and bo[3] == le) or 
    (bo[7] == le and bo[5] == le and bo[3] == le) or 
    (bo[9] == le and bo[5] == le and bo[1] == le)) 

if __name__ == '__main__':

    test_case = int(input())
    
    for _ in range(test_case):
        theBoard = [-1]
        for _ in range(3):
            theBoard += list(map(int, input().split()))
        print(TTT_solution(theBoard))