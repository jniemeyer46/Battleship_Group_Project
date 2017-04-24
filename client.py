import socket
# import json
# import time
import os
from View_Battleship import ViewBattleship


class Client:
    # client data
    shutdown = False
    host = socket.gethostbyname(socket.gethostname())
    port = 5000
    server = (host, port)
    buffer = 1024

    def __init__(self):
        view = ViewBattleship()
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            sock.connect((self.host, self.port))
        except socket.error:
            view.display("Error connecting to the server.")
            os._exit(1)

        sock.sendto(str.encode(view.get_username()), self.server)
        data, server = sock.recvfrom(self.buffer)
        data = data.decode('utf-8')
        view.display(data)

        while not self.shutdown:
            data, server = sock.recvfrom(self.buffer)
            data = data.decode('utf-8')
            view.display(data)
            x = input("What would you like to send to the server? ")
            if x == '>:(':
                sock.sendto(str.encode(x), server)
                shutdown = True
                break
            else:
                sock.sendto(str.encode(x), server)

# test
client = Client()

