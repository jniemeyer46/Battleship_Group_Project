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
send_request_w = '{"username":"", "action":"win request", "data":{"win_c":""}}'

class Client:
    # client data
    shutdown = False
    host = socket.gethostbyname(socket.gethostname())
    port = 5000
    server = (host, port)
    buffer = 1024
    player_board = Board()
    player_shot = False
    enemy_board = Board()
    enemy_shot = False
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
                send = '{"username":"' + self.username + '", "action":"win request", "data":{"win_c":""}}'
                sock.sendto(str.encode(send), server)
                win_c, server = sock.recvfrom(self.buffer)
                win_c = json.loads(win_c.decode('utf-8'))
                if win_c['data']['win_c'] == 'true' and win_c['username'] == self.username:
                    self.view.display("Congrats you won!!")
                    break
                if win_c['data']['win_c'] == 'true' and win_c['username'] != self.username:
                    self.view.display("Oh no you lost!!")
                    break
                shot = self.view.getShot()
                out_shot = '{"username":"' + self.username + '", "action":"outgoing shot", "data":{"coordinate":"' + str(
                    shot[0]) + ' ' + str(shot[1]) + '", "result":"awaiting response"}}'
                if self.model.checkShot(self.enemy_board, shot):
                    sock.sendto(str.encode(out_shot), self.server)
                    self.getShot(sock)
                else:
                    self.view.display("Shot already placed in this location. Try again: \n")
                self.view.displayScore(self.enemy_board)


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
            if self.enemy_shot and self.player_shot:
                self.view.display("Your board: ")
                self.view.displayBoard(self.player_board)
                self.view.display("Enemy Board: ")
                self.view.displayBoard(self.enemy_board)
                self.enemy_shot = False
                self.player_shot = False
                break
            data, server = sock.recvfrom(self.buffer)
            data = json.loads(data.decode('utf-8'))
            if data['action'] == 'server shot' and data['username'] != self.username:
                result = (data['data']['coordinate'], data['data']['result'])
                coord = (int(result[0][1]), int(result[0][4]))

                if result[1] == 'hit':
                    self.enemy_board.board[coord[0]][coord[1]] = 'X'
                    self.enemy_board.score = self.enemy_board.score + 100
                elif result[1] == 'miss':
                    self.enemy_board.board[coord[0]][coord[1]] = '*'
                    self.enemy_board.score = self.enemy_board.score - 10
                self.player_shot = True
            if data['action'] == 'server shot' and data['username'] == self.username:
                result = (data['data']['coordinate'], data['data']['result'])
                coord = (int(result[0][1]), int(result[0][4]))
                if result[1] == 'hit':
                    self.player_board.board[coord[0]][coord[1]] = 'X'
                elif result[1] == 'miss':
                    self.player_board.board[coord[0]][coord[1]] = '*'
                self.enemy_shot = True

