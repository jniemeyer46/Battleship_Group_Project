# Caroline Tran, John Niemeyer, Faith Van Wig, Brendan Missel
# Chunky Jelly Fish Burritos Programming Group
# Battleship Model

class ModelBattleship:
    def placeShip(self, myBoard, type, start, orient):
        myBoard.board[start[0]][start[1]] = 'O'
        if orient == 'v':
            for i in range(0, type):
                myBoard.board[start[0]][start[1]+i] = 'O'
        elif orient == 'h':
           for i in range(0, type):
                myBoard.board[start[0]+i][start[1]] = 'O'


