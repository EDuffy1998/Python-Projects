'''
Student Name: Edward Duffy
Student Number: 117501529
Date: 01/10/2019
Module: CS3311 Middleware
Assignment/Lab: 2
Description: The client looks up services which are running and available.
'''
'''
PseudoCode: What I will be working off of
Create a connection with a server using sockets , ip addresses and port numbers
Once connection is established do the following
    Send a message to the server program asking is server available.
    Wait for response
    if/else:
        if server is available then query the server to check to see if a service is available on another server
        else: program closes
        
'''
# from the socket module import all
from socket import *

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
user_input = input("Would you like to connect to the directory server or a service from server")
# choice = user_input.upper()
if user_input.upper() == "DIRECTORY SERVER":
    sock = socket(AF_INET, SOCK_STREAM)
# set values for host 'localhost' - meaning this machine and port number 10000
# the machine address and port number have to be the same as the server is using.
    hostname = gethostname()
    server_address = (hostname,10000)
# output to terminal some info on the address details
    print('connecting to server at %s port %s' % server_address)
# Connect the socket to the host and port
    sock.connect(server_address)
    while True:
        # Send data
        message = input("Enter message here:")
        print('sending "%s"' % message)
                # Data is transmitted to the server with sendall()
                # encode() function returns bytes object
        sock.sendall(message.encode())
    # Look for the response
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
    	    # Data is read from the connection with recv()
            # decode() function returns string object
            data = sock.recv(1000000000).decode()

            amount_received += len(data)
            print('received "%s"' % data)
    else:
        sock.close()# close connection
elif user_input.upper() == "SERVICE FROM SERVER":
    service_choice_input = input("what service would you like to connect to?")
    service_choice = service_choice_input.upper()
    if service_choice == "CALCULATOR":
        # user_input_ip_address = input("please enter the ip address of the calculator").isnumeric()
        # user_input_port_number = input("Please enter the port number of the calculator service").isnumeric()
        hostname = gethostname()
        server_address = (hostname, 8000)
        sock = socket(AF_INET, SOCK_STREAM)
        # # hostname = gethostname()
        # address_of_server = (user_input_ip_address, user_input_port_number)
        print('connecting to server at %s port %s' % server_address)
        sock.connect(server_address)
        while True:
            while True:
                # Send data
                user_input_equation = input("please enter the equation you want the calculator to solve here:")
                print('sending "%s"' % user_input_equation)
                # Data is transmitted to the server with sendall()
                # encode() function returns bytes object
                sock.sendall(user_input_equation.encode())
                # Look for the response
                amount_received = 0
                amount_expected = len(user_input_equation)

                while amount_received < amount_expected:
                    # Data is read from the connection with recv()
                    # decode() function returns string object
                    data = sock.recv(1000000000).decode()

                    amount_received += len(data)
                    print('received "%s"' % data)
    elif service_choice == "STRING REVERSER":
        #user_input_ip_address = input("Please enter the ip address of string converter")
        #user_input_port_number = input("Please enter the port number that the string reverser service is running on")
        sock = socket(AF_INET, SOCK_STREAM)
        #hostname = gethostname()
        hostname = gethostname()
        server_address = (hostname, 9000)
        #address_of_server = (user_input_ip_address, user_input_port_number)
        #print('connecting to server at %s port %s' % address_of_server)
        print('connecting to server at %s port %s' % server_address)
        # sock.connect(address_of_server)
        sock.connect(server_address)
        while True:
            while True:
                # Send data
                message = input("Enter message here you would like to reverse:")
                print('sending "%s"' % message)
                # Data is transmitted to the server with sendall()
                # encode() function returns bytes object
                sock.sendall(message.encode())

                # Look for the response
                amount_received = 0
                amount_expected = len(message)

                while amount_received < amount_expected:
                    # Data is read from the connection with recv()
                    # decode() function returns string object
                    data = sock.recv(1000000000).decode()

                    amount_received += len(data)
                    print('received "%s"' % data)


