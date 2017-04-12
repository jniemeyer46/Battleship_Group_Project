# Caroline Tran, John Niemeyer, Faith Van Wig, Brendan Missel
# Chunky Jelly Fish Burritos Programming Group
# Battleship View

class ViewBattleship():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

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

    def getShips(self):
        arr = [None, None, None, None, None]
        print("Time to place your ships! Please input coordinates of the head. e.g. A6 or E2 ")
        while 1:
            ac_head = input("Where would you like to place your aircraft carrier (length = 5)? ")
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
        arr[4] = (ac_head, ac_orient)
        while 1:
            bs_head = input("Where would you like to place your battleship (length = 4)? ")
            if bs_head[0] not in self.letters or bs_head[1] not in self.numbers:
                print("Not a valid coordinate. Please input coordinates of the head. e.g. A6 or E2 ")
            else:
                break
        while 1:
            bs_orient = input("What orientation would you like to place your ship? Type 'v' for vertical, 'h' for horizontal. ")
            if bs_orient != 'v' and bs_orient != 'h':
                print("Not a valid orientation. Please input v or h. ")
            else:
                break
        bs_head = list(bs_head)
        bs_head[0] = self.convertCoordinates(bs_head[0])
        bs_head[0], bs_head[1] = bs_head[1], bs_head[0]
        bs_head = "".join(bs_head)
        arr[3] = (bs_head, bs_orient)
        while 1:
            cr_head = input("Where would you like to place your cruiser (length = 3)? ")
            if cr_head[0] not in self.letters or cr_head[1] not in self.numbers:
                print("Not a valid coordinate. Please input coordinates of the head. e.g. A6 or E2 ")
            else:
                break
        while 1:
            cr_orient = input("What orientation would you like to place your ship? Type 'v' for vertical, 'h' for horizontal. ")
            if cr_orient != 'v' and cr_orient != 'h':
                print("Not a valid orientation. Please input v or h. ")
            else:
                break
        cr_head = list(cr_head)
        cr_head[0] = self.convertCoordinates(cr_head[0])
        cr_head[0], cr_head[1] = cr_head[1], cr_head[0]
        cr_head = "".join(cr_head)
        arr[2] = (cr_head, cr_orient)
        while 1:
            ds_head = input("Where would you like to place your destroyer (length = 2)? ")
            if ds_head[0] not in self.letters or ds_head[1] not in self.numbers:
                print("Not a valid coordinate. Please input coordinates of the head. e.g. A6 or E2 ")
            else:
                break
        while 1:
            ds_orient = input("What orientation would you like to place your ship? Type 'v' for vertical, 'h' for horizontal. ")
            if ds_orient != 'v' and ds_orient != 'h':
                print("Not a valid orientation. Please input v or h. ")
            else:
                break
        ds_head = list(ds_head)
        ds_head[0] = self.convertCoordinates(ds_head[0])
        ds_head[0], ds_head[1] = ds_head[1], ds_head[0]
        ds_head = "".join(ds_head)
        arr[1] = (ds_head, ds_orient)
        while 1:
            sb_head = input("Where would you like to place your submarine (length = 1)? ")
            if sb_head[0] not in self.letters or sb_head[1] not in self.numbers:
                print("Not a valid coordinate. Please input coordinates of the head. e.g. A6 or E2 ")
            else:
                break
        sb_orient = 'v'
        sb_head = list(sb_head)
        sb_head[0] = self.convertCoordinates(sb_head[0])
        sb_head[0], sb_head[1] = sb_head[1], sb_head[0]
        sb_head = "".join(sb_head)
        arr[0] = (sb_head, sb_orient)
        return arr

    def getShot(self):
        shot = input("Time to fire! Where would you like to place your shot? e.g. A6 or E2 ")
        shot = list(shot)
        shot[0] = self.convertCoordinates(shot[0])
        shot[0], shot[1] = int(shot[1]), int(shot[0])
        return shot

    def display(self, string):
        print(string)
