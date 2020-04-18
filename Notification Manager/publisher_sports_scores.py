'''
Student Name: Edward Duffy
Student Number: 117501529
Date: 20/10/2019
Module: CS3311 Middleware
Lab/Assignment: Lab3
Program Description: Sends notifications about sports scores to the client
'''
import random
from socket import *
from datetime import *
import sched
import time


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
        data = connection.recv(60).decode()
        if data:
            data_capitalised = data.upper()
            if data_capitalised == "RECEIVE NOTIFICATIONS":
                message_to_subscriber = "******Sending Notifications********"

                score1 = random.randint(0,4)
                score2 = random.randint(0,4)
                score3 = random.randint(0,4)
                score4 = random.randint(0,4)
                score5 = random.randint(0,4)
                score6 = random.randint(0,4)
                score7 = random.randint(0,4)
                score8 = random.randint(0,4)
                x = str(score1)
                y = str(score2)
                w = str(score3)
                z = str(score4)
                Manchester_city_score = str(score4)
                Tottenham_score = str(score4)
                Newcastle_score = str(score4)
                Leicester_score = str(score4)


                arsenal = "Arsenal"
                manchester_united = "Man Utd"
                match = "\nArsenal"+" "+"  "+x+" "+"Man Utd"+" "+y
                match1 = "\nChelsea"+" "+"  "+w+" "+"Liverpool"+" "+z
                match2 = "\nManchester City"+" "+"  "+Manchester_city_score+" "+"Tottenham"+" "+Tottenham_score
                match3 = "\nNewcastle"+" "+"  "+Newcastle_score+" "+"leicester City"+" "+Leicester_score

                # match = "Arsenal 0 Manchester United 0"
                # match_2 = ""
                connection.send(message_to_subscriber.encode())
                connection.send(match.encode())
                connection.send(match1.encode())
                connection.send(match2.encode())
                connection.send(match3.encode())




        # Receive the data in small chunks and retransmit it

    finally:
        # closing connection
        connection.close()

# closing connection to the socket
sock.close()


