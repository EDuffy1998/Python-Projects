'''
Student Name: Edward Duffy
Student Number: 117501529
Date: 03/10/19
Module: CS3311 Middleware
Calculator program to be called by the client server
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
server_address = (hostname, 8000)
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
                equation_from_user = connection.recv(1024)
                if equation_from_user:
                    date = datetime.now()
                    print("received " "%s", "at", "%s" % date, date)
                    welcome_message_to_user = "Welcome to the calculator service"
                    original_equation = "The equation you sent me was %s" % equation_from_user
                    solved_equation = eval(equation_from_user)
                    result_to_user = "the result to the equation you entered is %f" % solved_equation
                    connection.send(result_to_user.encode())
                    thank_you_message_to_user = "thank you for using this service\n connection will now be closed"
                    connection.close()


            # if number1 and operator and number2:

                                #
                                # message_to_client = ("we are going to return your original string %s", % data)
                                # connection.send(message_to_client.encode())
            # if operator == "+":
            #     digit1 = number1.isnumeric()
            #     digit2 = number2.isnumeric()
            #     result = (digit1 + digit2)
            #     message_to_user = "your answer is %s" % result
            #     connection.send(message_to_user.encode())
            #     connection.close()
            # elif operator == "*":
            #     digit1 = number1.isnumeric()
            #     digit2 = number2.isnumeric()
            #     result = (digit1 * digit2)
            #     message_to_user = "your answer is %s" % result
            #     connection.send(message_to_user.encode())
            #     connection.close()
            # elif operator == "/":
            #     digit1 = number1.isnumeric()
            #     digit2 = number2.isnumeric()
            #     result = (digit1 / digit2)
            #     message_to_user = "your answer is %s" % result
            #     connection.send(message_to_user.encode())
            #     connection.close()
            # elif operator == "-":
            #     digit1 = number1.isnumeric()
            #     digit2 = number2.isnumeric()
            #     result = (digit1 - digit2)
            #     message_to_user = "your answer is %s" % result
            #     connection.send(message_to_user.encode())
            #     connection.close()
    finally:
            # closing connection
            connection.close()

# closing connection to the socket
sock.close()



