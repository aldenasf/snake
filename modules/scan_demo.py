import queue
import socket


target:str = '137.74.187.100'
ports = queue.Queue()
for port in range(1,10001):
    ports.put(int(port))

def scan(port:int):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect(('137.74.187.100', 2))
        print(result)
    except socket.error as err:
        print("Error " + str(err))

# while not ports.empty():
#     scan(ports.get())

scan(1)