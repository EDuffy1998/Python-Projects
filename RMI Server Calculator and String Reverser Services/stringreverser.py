'''
Student Name: Edward Duffy
Student Number: 117501529
Date: 03/10/19
Module: CS3311 Middleware
'''
from socket import *
from datetime import *
# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
sock = socket(AF_INET, SOCK_STREAM)
# if we did not import everything from socket, then we would have to write the previous line as:
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# set values for host 'localhost' - meaning this machine and port number 10000
# getting the hostname via the method gethostname()
hostname = gethostbyname(gethostname())
# getting server address via the host name and sending on port 10,000
server_address = (hostname, 9000)
# output to terminal some info on the address details
print('*** Server is starting up on %s port %s ***' % server_address)
# Bind the socket to the host and port
sock.bind(server_address)

# Listen for one incoming connections to the server
sock.listen(1)

while True:

    # print statement to tell user that we are connecting to the client
    print('*** Waiting for a connection ***')
    # accept() returns an open connection between the server and client, along with the address of the client
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(60).decode()
            if data:
                date = datetime.now()
                print("received " "%s", "at", "%s" % date, date)
                original_string = data
                original_string_message = "the original string %s" % original_string
                connection.send(original_string_message.encode())
                string_reversed = original_string[::-1]
                reversed_string_message = "\n the reversed string %s" % string_reversed
                connection.send(reversed_string_message.encode())
                connection_close_message = "\n Closing connection to service"
                connection.send(connection_close_message.encode())
                connection.close()
                sock.close()
            else:
                 client_message = "service did not receive any data"
                 connection.send(client_message.encode())
    finally:
        # closing connection
        connection.close()

# closing connection to the socket
sock.close()


