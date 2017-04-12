# Caroline Tran, John Niemeyer, Faith Van Wig, Brendan Missel
# Chunky Jelly Fish Burritos Programming Group
# Battleship GameObjects file

class Board():
    '''
        A cell can be reference to using board[row][column]
    '''
    def __init__(self):
        self.size = 10
        self.board = [[' ' for i in range(0, self.size)] for i in range(0, self.size)]

