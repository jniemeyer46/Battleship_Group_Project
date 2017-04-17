# Caroline Tran, John Niemeyer, Faith Van Wig, Brendan Missel
# Chunky Jelly Fish Burritos Programming Group
# Battleship View

class ViewBattleship():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    ships = ["airship carrier", "battleship", "cruiser", "destroyer", "submarine"]

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

    def convertCoordinates(self, head):
        if head == 'A':
            return '0'
        elif head == 'B':
            return '1'
        elif head == 'C':
            return '2'
        elif head == 'D':
            return '3'
        elif head == 'E':
            return '4'
        elif head == 'F':
            return '5'
        elif head == 'G':
            return '6'
        elif head == 'H':
            return '7'
        elif head == 'I':
            return '8'
        elif head == 'J':
            return '9'

    def getShips(self, shipNum):
        while 1:
            ac_head = input("Where would you like to place your " + self.ships[shipNum] + " (length = " + str((5 - shipNum)) + ")? ")
            if ac_head[0] not in self.letters or ac_head[1] not in self.numbers:
                print("Not a valid coordinate. Please input coordinates of the head. e.g. A6 or E2 ")
            else:
                break
        while 1:
            ac_orient = input("What orientation would you like to place your ship? Type v for vertical, h for horizontal. ")
            if ac_orient != 'v' and ac_orient != 'h':
                print("Not a valid orientation. Please input v or h. ")
            else:
                break
        ac_head = list(ac_head)
        ac_head[0] = self.convertCoordinates(ac_head[0])
        ac_head[0], ac_head[1] = ac_head[1], ac_head[0]
        ac_head = "".join(ac_head)
        location = (ac_head, ac_orient)
        return location

    def getShot(self):
        shot = input("Time to fire! Where would you like to place your shot? e.g. A6 or E2 ")
        shot = list(shot)
        shot[0] = self.convertCoordinates(shot[0])
        shot[0], shot[1] = int(shot[1]), int(shot[0])
        return shot

    def display(self, string):
        print(string)
