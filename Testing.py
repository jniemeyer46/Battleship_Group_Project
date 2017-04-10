# Caroline Tran, John Niemeyer, Faith Van Wig, Brendan Missel
# Chunky Jelly Fish Burritos Programming Group
# Battleship Testing File

import unittest
from Model_Battleship import ModelBattleship
from View_Battleship import ViewBattleship
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


if __name__ == '__main__':
    b = BattleshipTest()
    b.testGameBoardInit()