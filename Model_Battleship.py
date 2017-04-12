# Caroline Tran, John Niemeyer, Faith Van Wig, Brendan Missel
# Chunky Jelly Fish Burritos Programming Group
# Battleship Model

class ModelBattleship:
    def placeShip(self, myBoard, type, start, orient):
        try:
            myBoard.board[start[0]][start[1]] = 'O'
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
            elif myBoard.board[location[0]][location[1]] == 'O':
                myBoard.board[location[0]][location[1]] = 'X'
        except:
            print("Shot is out of bounds! Try again.")

    def checkWin(self, myBoard):
        for i in myBoard.board:
            if 'O' in i:
                return False
        return True

