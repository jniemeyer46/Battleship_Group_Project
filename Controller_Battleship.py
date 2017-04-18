# Caroline Tran, John Niemeyer, Faith Van Wig, Brendan Missel
# Chunky Jelly Fish Burritos Programming Group
# Battleship Controller

from Model_Battleship import ModelBattleship
from View_Battleship import ViewBattleship
from GameObjects import Board
import random

class ControllerBattleship:
    playerBoard = Board()
    enemyBoard = Board()
    view = ViewBattleship()
    model = ModelBattleship()

    def inputShips(self):
        print("Time to place your ships! Please input coordinates of the head. e.g. A6 or E2 ")
        for i in range(0, 5):
            while 1:
                loc = self.view.getShips(i)
                if self.model.overlapCheck(self.playerBoard, 5-i, [int(loc[0][0]), int(loc[0][1])], loc[1]):
                    self.model.placeShip(self.playerBoard, 5-i, [int(loc[0][0]), int(loc[0][1])], loc[1])
                    self.view.displayBoard(self.playerBoard)
                    break
                else:
                    self.view.display("Ship would overlap at this location. Try again: \n")

    def getShot(self):
        while True:
            shot = self.view.getShot()
            if self.model.checkShot(self.enemyBoard, shot):
                self.model.placeShot(self.enemyBoard, shot)
                break
            else:
                self.view.display("Shot already placed in this location. Try again: \n")
        self.view.displayScore(self.enemyBoard)

    def makeAIBoard(self):
        for i in range(0, 5):
            while 1:
                start = [random.randint(0, 9), random.randint(0, 9)]
                orient = random.choice(['v', 'h'])
                loc = (start, orient)
                if self.model.boundaryCheck(i+1, [int(loc[0][0]), int(loc[0][1])], loc[1]) and self.model.overlapCheck(self.enemyBoard, i+1, [int(loc[0][0]), int(loc[0][1])], loc[1]):
                    try:
                        self.enemyBoard.board[start[0]][start[1]] = str(i+1)
                        if orient == 'v':
                            for j in range(0, i+1):
                                self.enemyBoard.board[start[0] + j][start[1]] = 'O'
                            break
                        elif orient == 'h':
                            for j in range(0, i+1):
                                self.enemyBoard.board[start[0]][start[1] + j] = 'O'
                            break
                    except:
                        pass

                    break


        '''
        self.model.placeShip(self.enemyBoard, 5, [0, 0], 'v')
        self.model.placeShip(self.enemyBoard, 4, [0, 1], 'v')
        self.model.placeShip(self.enemyBoard, 3, [0, 2], 'v')
        self.model.placeShip(self.enemyBoard, 2, [0, 3], 'v')
        self.model.placeShip(self.enemyBoard, 1, [0, 4], 'v')
        '''


if __name__ == '__main__':
    controller = ControllerBattleship()
    view = ViewBattleship()
    model = ModelBattleship()
    controller.makeAIBoard()
    userInput = view.displayMenu()
    view.displayBoard(controller.playerBoard)
    controller.inputShips()
    if userInput[0] == '1':
        if userInput[1] == '1':
            while 1:
                view.display("Enemy Board: ")
                view.displayBoard(model.maskBoard(controller.enemyBoard))
                controller.getShot()
                if model.checkWin(controller.enemyBoard):
                    view.display("Congrats you won!!")
                    break
                else:
                    model.randAI(controller.playerBoard)
                    view.display("Your Board: ")
                    view.displayBoard(controller.playerBoard)
                    if model.checkWin(controller.playerBoard):
                        view.display("Oh no you lost!!")
                        break
            view.displayBoard(controller.enemyBoard)
        elif userInput[1] == '2':
            pass
