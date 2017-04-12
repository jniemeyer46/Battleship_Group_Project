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
        arr = self.view.getShips()
        for i in range(0, 5):
            self.model.placeShip(self.playerBoard, i+1, [int(arr[i][0][0]), int(arr[i][0][1])], arr[i][1])
    def getShot(self):
        self.view.displayBoard(self.model.maskBoard(self.enemyBoard))
        shot = self.view.getShot()
        self.model.placeShot(self.enemyBoard, shot)
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

