import json
import socket
import threading
import os
from GameObjects import Player, Board
from Model_Battleship import ModelBattleship
from copy import deepcopy


# import time

# JSON templates
incom_shot = '{"username":"bmissel", "action":"incoming shot", "data":{"coordinate":""}}'
outg_shot = '{"username":"bmissel", "action":"outgoing shot", "data":{"coordinate":"", "result":""}}'
send_board = '{"username":"bmissel", "action":"board", "data":{"board":""}}'


# This is the Server object file that will be launched from the controller.
# This functions of this class are as follows:
#   Start the server and listen for clients trying to connect.
#   Listen to the connected clients for incoming JSON strings.
#   Send a response back to the clients with a success flag and response statement.

class Server:
    # Member Variables
    m_port = 5000
    m_host = socket.gethostbyname(socket.gethostname())
    client_lobby = []  # username, addr
    clients = []
    in_game = [()]
    buffer = 1024
    server_end = False
    boards_received = False
    model = ModelBattleship()
    # Open the socket
    server_i = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # JSON template
    # result = '{"username": "", "action": "result", "data": { "success_flag": "", "response": ""} }'

    def sendResult(self, addr, string):
        self.server_i.sendto(string, addr)

    # Member Functions
    def __init__(self):
        # Bind to the port
        try:
            self.server_i.bind((Server.m_host, Server.m_port))
            print("Server started. Listening for incoming connections...")
        except:
            pass
        # Main loop to add new clients
        while True:
            data, addr = self.server_i.recvfrom(self.buffer)
            # print(str(addr) + ": " + data.decode('utf-8'))
            data = data.decode('utf-8')
            if addr not in self.clients:
                self.clients.append(addr)
                self.client_lobby.append((data, addr))
                print(data + ' has joined the server.')
                if len(self.client_lobby) == 2:
                    p1 = Player(self.client_lobby[0][0], self.client_lobby[0][1], 1)
                    p2 = Player(self.client_lobby[1][0], self.client_lobby[1][1], 1)
                    self.client_lobby = []
                    self.in_game[0] = (p1, p2)
                    print(self.in_game[0][0].username + ' and ' + self.in_game[0][1].username + ' have started a game together.')
                    index = 0
                    d1 = 'player 1'
                    t = threading.Thread(target=Server.receiving_thread, args=(self, index, d1, True))
                    t.start()
                    d2 = 'player 2'
                    t1 = threading.Thread(target=Server.receiving_thread, args=(self, index, d2, True))
                    t1.start()
                connected = "Connected to the server. Waiting for another player..."
                Server.sendResult(self, addr, str.encode(connected))
            else:
                index = self.clients.index(addr)
                t = threading.Thread(target=Server.receiving_thread, args=(self, index, data, False))
                t.start()

    def receiving_thread(self, i, data, welc):
        addr = Server.clients[i]
        data_j = ''
        try:
            data_j = json.loads(data)
        except:
            pass
        if data == '>:(':
            os._exit(0)  # RAGE QUIT!!
        elif welc:
            if data == 'player 1':
                send_back = "You have been connected with " + self.in_game[i][1].username
                Server.sendResult(self, self.in_game[i][0].address, str.encode(send_back))
            if data == 'player 2':
                send_back = "You have been connected with " + self.in_game[i][0].username
                Server.sendResult(self, self.in_game[i][1].address, str.encode(send_back))
        elif data_j['action'] == 'board':
            for j in range(0, 2):
                if self.in_game[0][j].address == addr:
                    self.in_game[0][j].board = deepcopy(data_j['data']['board'])
                    print("Board initial board stored for " + self.in_game[0][j].username)
                    # print(str(self.in_game[0][j].board))
                    self.in_game[0][j].board_filled = True
            if self.in_game[0][0].board_filled and self.in_game[0][1].board_filled:
                self.boards_received = True
            if self.boards_received:
                print('Both user boards submitted. Time to fire!')
                self.server_i.sendto(str.encode('Game begin'), self.in_game[0][0].address)
                self.server_i.sendto(str.encode('Game begin'), self.in_game[0][1].address)

        elif data_j['action'] == 'outgoing shot' and data_j['data']['result'] == 'awaiting response':
            location = data_j['data']['coordinate']
            print(location)
            for i in range(0, 2):
                if self.in_game[0][i].address != addr:
                    board = deepcopy(self.in_game[0][i].board)
                    print(location[0] + ' ' + location[1])
                    print(board[location[0]][location[1]])
                    name = self.in_game[0][i].username
                    self.model.placeShot(board, location)
                    if board[location[0]][location[1]] == 'X':
                        result = 'hit'
                    elif board[location[0]][location[1]] == '*':
                        result = 'miss'
                    server_shot = '{"username":"' + name + '", "action":"server shot", "data":{"coordinate":"' + location + '", "result":"' + result + '"}}'
                    self.server_i.sendall(str.encode(server_shot))
                    self.in_game[0][i].board = deepcopy(board)
                    break


        else:
            print(data)
            send_back = "Server received your message, but did nothing because you suck!"
            Server.sendResult(self, addr, str.encode(send_back))
		
# for testing purposing
if __name__ == "__main__":
    server = Server()
