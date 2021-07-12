import socket

"""
So we're going to make a function called createServer that we're going to call right down here, and it's going to print out how you're suppose to access it and then start the server. Now the whole idea of the server is that the server is woke up to wait for incoming connections. So the server already exists. So when you start talking to a web server, that server is in that computer already. The server software is already running, registering its interest in incoming requests. So that's what we do. So when this Python program starts, it's going to sit there and wait in an infinite loop for incoming requests.
"""


def create_server(port=5500):
    # So the first thing we do is we're going to make a socket. It's an endpoint. It's not actually making the phone call. Remember, I said this socket call is making the phone.

    # simpley making a phone
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # I am willing on port 9000 to receive the phone calls.
        server_socket.bind(('localhost', 9000))
        # One application gets the phone calls. The 5 on there says, "Dear operating system, if I'm busy handling one phone call, you can hold on to four more and queue them and then I'll come back and get them for you." That you're asking the operating system to queue incoming calls. Don't just say you're busy, shut down.
        server_socket.listen(5)

        while True:
            # Receive the phone call
            (client_socket, address) = server_socket.accept()

            # read data and decode it utf-8 to unicode
            read_data = client_socket.recv(5000).decode()
            pieces = read_data.split('\n')

            if len(pieces) > 0:
                print(pieces[0])

            # header data
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            
            # send it to client
            client_socket.sendall(data.encode())
            client_socket.shutdown(socket.SHUT_WR)

    except KeyboardInterrupt:
        print('\nShuting Down\n')
    except Exception as e:
        print("\nError:\n")
        print(e)

    server_socket.close()
print("Access on http://localhost:9000")
create_server()