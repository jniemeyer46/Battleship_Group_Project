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
        self.score = 0

class Player():
    def __init__(self, username, addr, game_id):
        self.username = username
        self.address = addr
        self.game_id = game_id
        self.board = Board()
        self.board_filled = False
