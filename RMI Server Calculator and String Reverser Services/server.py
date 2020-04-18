'''
Student Name: Edward Duffy
Student Number: 117501529
Date: 03/10/2019
Module: CS3311 Middleware
'''
# from the socket module import all
from socket import *
# importing datetime so that we can get the current date and time to put into the textfile later on in the program
import datetime

list_of_services = {"CALCULATOR": ["port number is 8000", "ip address", "The parameters are that you need to enter an equation for the calculator to solve"], "STRING REVERSER": ["port number 9000", "ip address", "parameter is that you enter a string"]}
message_to_client = "we have that service"
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
server_address = (hostname, 10000)
# output to terminal some info on the address details
print('*** Server is starting up on %s port %s ***' % server_address)
# Bind the socket to the host and port
sock.bind(server_address)

# Listen for one incoming connections to the server
sock.listen(1)

# def ClientCalculator():
#     #sock = socket(AF_INET, SOCK_STREAM)
#     #hostname = gethostbyname(gethostname())
#     #server_address = (hostname, 10000)
#     #sock.bind(server_address)
#     #connection, client_address = sock.accept()
#     input1 = 2
#     input2 = 3
#     operator = "+"
#     result = "five"
#     answer = str(result)
#     send_result = connection.send(answer.encode())
#     print(send_result)


# we want the server to run all the time, so set up a forever true while loop
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
                date = datetime.datetime.now()
                print("received " "%s", "at", "%s" % date, date)
                # decode() function returns string object
                data_capitalised = data.upper()
                if data_capitalised == "I WANT A SERVICE":
                    service_message = "what service would you like?"
                    connection.sendall(service_message.encode())
                    # really want to put awhile statement here not sure how to do it for a client server model
                if data_capitalised == "WHAT SERVICES ARE THERE":
                    services = str(list_of_services.keys())
                    calculator = "Calculator"
                    string_reverser = "\n String reverser"
                    connection.send(calculator.encode())
                    connection.send(string_reverser.encode())
                elif data_capitalised == "CALCULATOR":
                            service_message = "if would you like to access this service ,\n""you can access it via the parameters sent"
                            calculator_attributes = str(list_of_services["CALCULATOR"])
                            connection.send(message_to_client.encode())
                            connection.send("\n".encode())
                            connection.send(calculator_attributes.encode())
                            connection.send("\n".encode())
                            connection.send(service_message.encode())
                elif data_capitalised == "STRING REVERSER":
                    #for keys, values in list_of_services:
                        #if keys == "STRING REVERSER":
                            service_message = "This service is available ,\n you can access it via the parameters sent"
                            string_reverser_attributes = str(list_of_services["STRING REVERSER"])
                            connection.send(message_to_client.encode())
                            connection.send("\n".encode())
                            connection.send(string_reverser_attributes.encode())
                            connection.send("\n".encode())
                            connection.send(service_message.encode())
                elif data_capitalised == "INFO":
                    welcome_message = "Welcome to the directory server to interact please enter the following"
                    option_a = "\n if you want a service , enter ""I want a service """
                    option_b = "\n if you want to know what services are there , enter what services are there"
                    option_c = "\n if you want to know more about a service , enter the name of the service"
                    connection.send(welcome_message.encode())
                    connection.send(option_a.encode())
                    connection.send(option_b.encode())
                    connection.send(option_c.encode())
                # elif data_capitalised[0][1][2][3][4][5] == "ACCESS":
                #         connection.send("happy".encode())
                # elif data_capitalised == "ACCESS CALCULATOR":
                #     calculator_answer = connection.send(print(ClientCalculator()).encode())
                #     connection.send(calculator_answer.encode())
                #     break
                # else:
                #     client_message = "the service you have requested is not available you can see if other services are available"
                #     connection.send(client_message.encode())


                #print("Sending message to client")
                # setting variable date to the value of the current date and time
                # opening the file called logfile.txt with the intention of appending data denoted by use of the "a"
                #file = open ("logfile.txt","a")
                # writing the message in the variable data to the file logfile.txt
                #file.write(data)
                #closing connection to the file
                #file.close()
                # encode() function returns bytes object
                #connection.sendall(user_input.encode())
            #else:
                #print('no more data from', client_address)
                #break

    finally:
        # closing connection
        connection.close()

# closing connection to the socket
sock.close()



