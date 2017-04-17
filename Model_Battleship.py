# Caroline Tran, John Niemeyer, Faith Van Wig, Brendan Missel
# Chunky Jelly Fish Burritos Programming Group
# Battleship Model

from copy import copy, deepcopy
import random


class ModelBattleship:
    def placeShip(self, myBoard, type, start, orient):
        try:
            # myBoard.board[start[0]][start[1]] = 'O'
            if orient == 'v':
                for i in range(0, type):
                    myBoard.board[start[0]+i][start[1]] = 'O'
            elif orient == 'h':
                for i in range(0, type):
                    myBoard.board[start[0]][start[1]+i] = 'O'
        except:
            print("Boat is out of bounds! Try again.")

    def placeShot(self, myBoard, location):
        try:
            if  myBoard.board[location[0]][location[1]] == ' ':
                myBoard.board[location[0]][location[1]] = '*'
                myBoard.score = myBoard.score - 10

            elif myBoard.board[location[0]][location[1]] == 'O':
                myBoard.board[location[0]][location[1]] = 'X'
                myBoard.score = myBoard.score + 100
        except:
            print("Shot is out of bounds! Try again.")

    def checkWin(self, myBoard):
        for i in myBoard.board:
            if 'O' in i:
                return False
        return True

    def maskBoard(self, myBoard):
        maskedBoard = deepcopy(myBoard)
        for i in range(0, 10):
            for j in range(0, 10):
                if maskedBoard.board[j][i] == 'O':
                    maskedBoard.board[j][i] = ' '
        return maskedBoard

    def checkShot(self, myBoard, location):
        if myBoard.board[location[0]][location[1]] == '*' or myBoard.board[location[0]][location[1]] == 'X':
            return False
        elif myBoard.board[location[0]][location[1]] == ' ' or myBoard.board[location[0]][location[1]] == 'O':
            return True
        else:
            print("Invalid shot")

    def overlapCheck(self, myBoard, type, start, orient):
        if orient == 'v':
            for i in range(0, type):
                if myBoard.board[start[0]+i][start[1]] == 'O':
                    return False
                else:
                    return True
        if orient == 'h':
            for i in range(0, type):
                if myBoard.board[start[0]][start[1]+i] == 'O':
                    return False
                else:
                    return True

    def randAI(self, myBoard):  # random shot placement
        failure = True
        while failure:
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            shot = (col, row)
            failure = not self.checkShot(myBoard, shot)
            self.placeShot(myBoard, shot)

    def boundaryCheck(self, type, start, orient):
        if orient == 'v':
            for i in range(0, type):
                print(str(start[1] + i))
                if start[1] + i > 9:
                    return False
                else:
                    return True
        if orient == 'h':
            for i in range(0, type):
                print(str(start[0] + i))
                if start[0] + i > 9:
                    return False
                else:
                    return True




