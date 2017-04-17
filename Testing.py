# Caroline Tran, John Niemeyer, Faith Van Wig, Brendan Missel
# Chunky Jelly Fish Burritos Programming Group
# Battleship Testing File

import unittest
from Model_Battleship import ModelBattleship
from View_Battleship import ViewBattleship
from Controller_Battleship import ControllerBattleship
from GameObjects import Board


class BattleshipTest(unittest.TestCase):
    def testGameBoardInit(self):
        testObject = Board()

        # test the size of the board
        expectedValue = 10
        actualValue = testObject.size
        assert(actualValue == expectedValue)

        # test that the board is empty
        expectedValue = ' '
        actualValue = testObject.board[0][0]
        assert(actualValue == expectedValue)

    def testBoatLocation(self):
        testObject = Board()
        model = ModelBattleship()

        model.placeShip(testObject, 1, [0, 2], 'v')
        #view = ViewBattleship()
        #view.displayBoard(testObject)
        expectedValue = 'O'
        actualValue = testObject.board[0][2]
        assert(actualValue == expectedValue)

    def testBiggerBoatLocation(self):
        testObject = Board()
        model = ModelBattleship()

        model.placeShip(testObject, 3, [5, 2], 'v')
        #view = ViewBattleship()
        #view.displayBoard(testObject)
        expectedValue = 'O'
        actualValue = testObject.board[5][2]
        assert(actualValue == expectedValue)

        actualValue = testObject.board[6][2]
        assert (actualValue == expectedValue)

        actualValue = testObject.board[7][2]
        assert (actualValue == expectedValue)

    def testFireShot(self):
        testObject = Board()
        model = ModelBattleship()
        model.placeShip(testObject, 3, [5, 2], 'v')
        model.placeShot(testObject, [5, 2])

        expectedValue = 'X'
        actualValue = testObject.board[5][2]
        assert(actualValue == expectedValue)

        model.placeShot(testObject, [9,9])
        expectedValue = '*'
        actualValue = testObject.board[9][9]
        assert(actualValue == expectedValue)

    def testOutofBounds(self):
        testObject = Board()
        model = ModelBattleship()

        #model.placeShip(testObject, 8, [8,2], 'v')
        #model.placeShot(testObject, [10, 10])

    def testWin(self):
        testObject = Board()
        model = ModelBattleship()
        model.placeShip(testObject, 2, [0,0], 'v')
        model.placeShot(testObject, [0,0])

        expectedValue = False
        actualValue = model.checkWin(testObject)
        assert(actualValue == expectedValue)

        model.placeShot(testObject, [1, 0])
        expectedValue = True
        actualValue = model.checkWin(testObject)
        assert (actualValue == expectedValue)

    def testMaskBoard(self):
        testObject = Board()
        model = ModelBattleship()
        model.placeShip(testObject, 5, [0, 0], 'v')
        model.placeShip(testObject, 4, [0, 1], 'v')
        model.placeShip(testObject, 3, [0, 2], 'v')
        model.placeShip(testObject, 2, [0, 3], 'v')
        model.placeShip(testObject, 1, [0, 4], 'v')
        model.placeShot(testObject, [0,0])

        maskedBoard = model.maskBoard(testObject)
        actualValue = testObject
        expectedValue = maskedBoard
        assert(actualValue != expectedValue)

    def testCheckShot(self):
        testObject = Board()
        model = ModelBattleship()
        model.placeShip(testObject, 5, [0, 0], 'v')
        model.placeShip(testObject, 4, [0, 1], 'v')
        model.placeShip(testObject, 3, [0, 2], 'v')
        model.placeShip(testObject, 2, [0, 3], 'v')
        model.placeShip(testObject, 1, [0, 4], 'v')
        model.placeShot(testObject, [0, 0])
        actualValue = model.checkShot(testObject, [0, 0])
        expectedValue = False
        assert (actualValue == expectedValue)

    def testOverlapCheck(self):
        testObject = Board()
        model = ModelBattleship()
        model.placeShip(testObject, 5, [0, 0], 'v')

        actualValue = model.overlapCheck(testObject, 5, [0, 0], 'h')
        expectedValue = False
        assert(actualValue == expectedValue)

    def testScore(self):
        testObject = Board()
        model = ModelBattleship()
        model.placeShip(testObject, 3, [5, 2], 'v')
        model.placeShot(testObject, [5, 2])

        expectedValue = 100
        actualValue = testObject.score
        assert (actualValue == expectedValue)

        model.placeShot(testObject, [9, 9])
        expectedValue = 90
        actualValue = testObject.score
        assert (actualValue == expectedValue)



if __name__ == '__main__':
    b = BattleshipTest()
    b.testGameBoardInit()
    b.testBoatLocation()
    b.testBiggerBoatLocation()
    b.testFireShot()
    b.testOutofBounds()
    b.testWin()
    b.testMaskBoard()
    b.testCheckShot()
    b.testOverlapCheck()
    b.testScore()
