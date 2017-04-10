# Caroline Tran, John Niemeyer, Faith Van Wig, Brendan Missel
# Chunky Jelly Fish Burritos Programming Group
# Battleship View

class ViewBattleship():
    def displayBoard(self, myBoard):
        counter = 0
        hl = '  +---+---+---+---+---+---+---+---+---+---+'
        print("    A   B   C   D   E   F   G   H   I   J")
        print(hl)
        for i in myBoard.board:
            print(counter, '| ', end='')
            print(' | '.join(i), '|')
            print(hl)
            counter += 1
