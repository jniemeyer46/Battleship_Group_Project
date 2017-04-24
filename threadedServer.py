import json
import socket
import threading
import os
from GameObjects import Player, Board


# import time

# JSONs
incom_shot = '{"username":"bmissel", "action":"incoming shot", "data":{"coordinate":"A6"}}'
outg_shot = '{"username":"bmissel", "action":"outgoing shot", "data":{"coordinate":"A6", "result":"hit"}}'
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
    listening = True
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
                if len(self.client_lobby) == 2:
                    p1 = Player(self.client_lobby[0][0], self.client_lobby[0][1], 1)
                    p2 = Player(self.client_lobby[1][0], self.client_lobby[1][1], 1)
                    self.client_lobby = []
                    self.in_game[0] = (p1, p2)
                    print(self.in_game[0][0].username)
                    print(self.in_game[0][1].username)
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
        if data == '>:(':
            os._exit(0)  # RAGE QUIT!!
        elif welc:
            if data == 'player 1':
                send_back = "You have been connected with " + self.in_game[i][1].username
                Server.sendResult(self, self.in_game[i][0].address, str.encode(send_back))
            if data == 'player 2':
                send_back = "You have been connected with " + self.in_game[i][0].username
                Server.sendResult(self, self.in_game[i][1].address, str.encode(send_back))
        else:
            print(data)
            send_back = "Server received your message, but did nothing because you suck!"
            Server.sendResult(self, addr, str.encode(send_back))
		
# for testing purposing
if __name__ == "__main__":
    server = Server()