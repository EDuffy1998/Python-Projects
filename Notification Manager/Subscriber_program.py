'''
Student Name: Edward Duffy
Student Number: 117501529
Date: 21/10/2019
Module: CS3311 Middleware
Lab/Assignment: Lab 3
Program Description: Subscriber program which can subscribe to receive notifications by contacting the notification manager
'''
from socket import *
list_of_events_subscribed_to = ["SPORTS_SCORES","WEATHER REPORTS"]

user_input = input("Would you like to connect to the notification manager or to a publisher directly?")
user_input_capitalised = user_input.upper()

if user_input_capitalised == "NOTIFICATION MANAGER":
    sock = socket(AF_INET, SOCK_STREAM)
    hostname = gethostname()
    server_address = (hostname, 10000)
    # output to terminal some info on the address details
    print('connecting to server at %s port %s' % server_address)
    # Connect the socket to the host and port
    sock.connect(server_address)
    while True:
        # user_input_connect_to_notification_manager = input("Do you still want to contact/connect to the notification manager")
        # while user_input_connect_to_notification_manager.upper() == "YES":
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
        sock.close()



elif user_input_capitalised == "PUBLISHER":
    user_input_publisher_choice = input("Which publisher would you like to subscribe to?")
    users_choice = user_input_publisher_choice.upper()
    if users_choice == "SPORTS SCORES":
        sock = socket(AF_INET, SOCK_STREAM)
        hostname = gethostname()
        server_address = (hostname, 9000)
        # output to terminal some info on the address details
        print('connecting to server at %s port %s' % server_address)
        # Connect the socket to the host and port
        sock.connect(server_address)
        while True:
                message = input("Enter receive notifications:")
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

    elif users_choice =="WEATHER REPORT":
            sock = socket(AF_INET, SOCK_STREAM)
            hostname = gethostname()
            server_address = (hostname, 8000)
            # output to terminal some info on the address details
            print('connecting to server at %s port %s' % server_address)
            # Connect the socket to the host and port
            sock.connect(server_address)
            while True:
                message = input("Enter receive notifications:")
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

