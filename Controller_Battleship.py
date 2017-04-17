# Caroline Tran, John Niemeyer, Faith Van Wig, Brendan Missel
# Chunky Jelly Fish Burritos Programming Group
# Battleship Controller

from Model_Battleship import ModelBattleship
from View_Battleship import ViewBattleship
from GameObjects import Board

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
                    break
                else:
                    self.view.display("Ship would overlap at this location. Try again: \n")

    def getShot(self):
        self.view.displayBoard(self.model.maskBoard(self.enemyBoard))
        while True:
            shot = self.view.getShot()
            if self.model.checkShot(self.enemyBoard, shot):
                self.model.placeShot(self.enemyBoard, shot)
                break
            else:
                self.view.display("Shot already placed in this location. Try again: \n")

    def makeDummyBoard(self):
        self.model.placeShip(self.enemyBoard, 5, [0, 0], 'v')
        self.model.placeShip(self.enemyBoard, 4, [0, 1], 'v')
        self.model.placeShip(self.enemyBoard, 3, [0, 2], 'v')
        self.model.placeShip(self.enemyBoard, 2, [0, 3], 'v')
        self.model.placeShip(self.enemyBoard, 1, [0, 4], 'v')


if __name__ == '__main__':
    controller = ControllerBattleship()
#    controller.ViewtoModel()
    view = ViewBattleship()
    model = ModelBattleship()
    controller.makeDummyBoard()
    view.display("Welcome to Battleship!")
    view.displayBoard(controller.playerBoard)
    controller.inputShips()
    view.displayBoard(controller.playerBoard)
    while 1:
        if model.checkWin(controller.enemyBoard) == False :
            controller.getShot()
        else:
            view.displayBoard(controller.enemyBoard)
            break
    view.display("Congrats you won!!")

