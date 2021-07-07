# Create a simple browser using Python3

"""
    Socket is the endpoint that you are going to send and receive data to inside your computer.
"""
import socket

# make a phone
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# dialing the phone to a domain name
# domain name and a port of this domain name
try:
    mysocket.connect(('data.pr4e.org', 80))
except:
    print("Connection failed(maybe domain name is not correct).")

# convert to bytecode
# `\r\n` return a newline and you have to hit it twice, the enter at the beginning of the first line, then remember we had to put that blank line in because to say no headers.
# first \r\n for next line
# second \r\n is put a blank line in because to say no headers. 


# why we need to encode().
# And then you have to use encode. And encode means that the data sent across the Internet is generally sent in what's called UTF-8. Inside of Python, the data is in Unicode, so that you can put literally any character in a Python string. And then preparing it to send it out across the Internet, we encode it into the more dense, more compressed UTF-8 format, rather than we don't send strings across the Internet in Unicode in general.
cmd = 'GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n'.encode()

# send the request
mysocket.send(cmd)

# receive and decode data
# the next part of this is we're going to have a little loop. So the protocol tells us we're supposed to receive data until the socket's closed.

file = open('demo.txt', 'w')

count = 0
while True:
    count += 1
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    file.write(data.decode())
    print(data.decode(), end='')

print(count)
mysocket.close()