import socket
import sys

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mysocket.connect(('127.0.0.1', 9000))
except socket.error as e:
    print(e)
    sys.exit()

cmd = 'GET http://127.0.0.1/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysocket.send(cmd)

while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysocket.close()
