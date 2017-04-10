# Caroline Tran, John Niemeyer, Faith Van Wig, Brendan Missel
# Chunky Jelly Fish Burritos Programming Group
# Battleship Controller

from Model_Battleship import ModelBattleship
from View_Battleship import ViewBattleship
from GameObjects import Board

class ControllerBattleship:
#    def ViewToModel(self):
    pass



if __name__ == '__main__':
#    controller = ControllerBattleship()
#    controller.ViewtoModel()
    view = ViewBattleship()

    myBoard = Board()
    view.displayBoard(myBoard)

