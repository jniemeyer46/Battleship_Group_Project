# Caroline Tran, John Niemeyer, Faith Van Wig, Brendan Missel
# Chunky Jelly Fish Burritos Programming Group
# Battleship GameObjects file

class Board():
    def __init__(self):
        self.size = 10
        row = [' ' for i in range(0, self.size - 1)]
        self.board = [row for i in range(0, self.size - 1)]

