# Caroline Tran, John Niemeyer, Faith Van Wig, Brendan Missel
# Chunky Jelly Fish Burritos Programming Group
# Battleship View
import os

class ViewBattleship():
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    menuOptions = ['1', '0']
    difficultyOptions = ['1', '2']
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
            return 0
        elif head == 'B':
            return 1
        elif head == 'C':
            return 2
        elif head == 'D':
            return 3
        elif head == 'E':
            return 4
        elif head == 'F':
            return 5
        elif head == 'G':
            return 6
        elif head == 'H':
            return 7
        elif head == 'I':
            return 8
        elif head == 'J':
            return 9

    def getShips(self, shipNum):
        length = 5- shipNum
        while 1:
            while 1:
                ac_head = input("Where would you like to place your " + self.ships[shipNum] + " (length = " + str(length) + ")? ")
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
            ac_head[1] = int(ac_head[1])
            ac_head[0], ac_head[1] = ac_head[1], ac_head[0]
            if ac_orient == 'v':
                if (ac_head[0] + length) > 9:
                    print("Error: Ship out of bounds! Try again. ")
                else:
                    break
            elif ac_orient == 'h':
                if (ac_head[1] + length) > 9:
                    print("Error: Ship out of bounds! Try again. ")
                else:
                    break
        location = (ac_head, ac_orient)
        return location

    def getShot(self):
        while 1:
            shot = input("Time to fire! Where would you like to place your shot? e.g. A6 or E2 ")
            try:
                if shot[1] in self.numbers:
                    shot = list(shot)
                    shot[0] = self.convertCoordinates(shot[0])
                    shot[0], shot[1] = int(shot[1]), int(shot[0])
                    return shot
            except:
                print("Error!! Try again! ")

    def display(self, string):
        print(string)

    def displayScore(self, myBoard):
        print("SCORE: " + str(myBoard.score))

    def displayMenu(self):
        print("Welcome to Battleship!!! ")
        while 1:
            gamemode = input("Please choose a gamemode: \n 1. Play against the computer \n 0. Quit \n")
            if gamemode in self.menuOptions:
                break
            else:
                print("Error: Try again. ")
        if gamemode != '0':
            while 1:
                difficulty = input("Choose a difficulty level: \n 1. Normal \n 2. You will lose \n")
                if difficulty in self.difficultyOptions:
                    break
                else:
                    print("Error: Try again. ")
            userInput = (gamemode, difficulty)
            return userInput
        else:
            print("Goodbye! ")
            os._exit(0)