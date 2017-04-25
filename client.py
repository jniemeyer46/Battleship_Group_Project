import socket
import json
# import time
import os
from View_Battleship import ViewBattleship
from Model_Battleship import ModelBattleship
from GameObjects import Board

# JSON templates
incom_shot = '{"username":"bmissel", "action":"incoming shot", "data":{"coordinate":""}}'
outg_shot = '{"username":"bmissel", "action":"outgoing shot", "data":{"coordinate":"", "result":""}}'
server_shot = '{"username":"bmissel", "action":"server shot", "data":{"coordinate":"", "result":""}}'
send_board = '{"username":"bmissel", "action":"board", "data":{"board":""}}'


class Client:
    # client data
    shutdown = False
    host = socket.gethostbyname(socket.gethostname())
    port = 5000
    server = (host, port)
    buffer = 1024
    player_board = Board()
    enemy_board = Board()
    view = ViewBattleship()
    model = ModelBattleship()
    username = view.get_username()

    def __init__(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            sock.connect((self.host, self.port))
        except socket.error:
            self.view.display("Error connecting to the server.")
            os._exit(1)

        sock.sendto(str.encode(self.username), self.server)
        data, server = sock.recvfrom(self.buffer)
        data = data.decode('utf-8')
        self.view.display(data)
        # start here
        data, server = sock.recvfrom(self.buffer)
        data = data.decode('utf-8')
        self.view.display(data)
        self.view.displayBoard(self.player_board)
        self.inputShips()
        send_board = '{"username":"' + self.username + '", "action":"board", "data":{"board":"' + str(self.player_board.board) + '"}}'
        sock.sendto(str.encode(send_board), server)
        data, server = sock.recvfrom(self.buffer)
        data = data.decode('utf-8')
        if data == 'Game begin':
            while 1:
                self.view.display("Enemy Board: ")
                self.view.displayBoard(self.enemy_board)
                self.getShot(sock)


    def inputShips(self):  # copied from the Controller to please the Python gods.
        self.view.display("Time to place your ships! Please input coordinates of the head. e.g. A6 or E2 ")
        for i in range(0, 5):
            while 1:
                loc = self.view.getShips(i)
                if self.model.boundaryCheck(5 - i, [int(loc[0][0]), int(loc[0][1])],
                                            loc[1]) and self.model.overlapCheck(self.player_board, 5 - i,
                                                                                [int(loc[0][0]), int(loc[0][1])],
                                                                                loc[1]):
                    self.model.placeShip(self.player_board, 5 - i, [int(loc[0][0]), int(loc[0][1])], loc[1])
                    self.view.displayBoard(self.player_board)
                    break
                else:
                    self.view.display("Invalid ship location. Try again. \n")

    def getShot(self, sock):  # copied from the Controller to please the Python gods.
        while True:
            shot = self.view.getShot()
            out_shot = '{"username":"' + self.username + '", "action":"outgoing shot", "data":{"coordinate":"' + str(shot) + '", "result":"awaiting response"}}'
            if self.model.checkShot(self.enemy_board, shot):
                sock.sendto(str.encode(out_shot), self.server)
                data, server = sock.recvfrom(self.buffer)
                data = json.loads(data)
                if data['action'] == 'server shot' and data['username'] != self.username:
                    result = (data['data']['coordinate'], data['data']['result'])
                    if result[1] == 'hit':
                        self.enemy_board.board[result[0][1]][result[0][1]] = 'X'
                        self.enemy_board.score = self.enemy_board.score + 100
                    elif result[1] == 'miss':
                        self.enemy_board.board[result[0][1]][result[0][1]] = '*'
                    self.enemy_board.score = self.enemy_board.score - 10
                    break
                elif data['action'] == 'server shot' and data['username'] == self.username:
                    result = (data['data']['coordinate'], data['data']['result'])
                    if result[1] == 'hit':
                        self.player_board.board[result[0][1]][result[0][1]] = 'X'
                    elif result[1] == 'miss':
                        self.player_board.board[result[0][1]][result[0][1]] = '*'
                    break
            else:
                self.view.display("Shot already placed in this location. Try again: \n")
        self.view.displayScore(self.enemy_board)
