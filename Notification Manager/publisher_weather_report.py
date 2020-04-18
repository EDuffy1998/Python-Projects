'''
Student Name: Edward Duffy
Student Number: 117501529
Date: 20/10/2019
Module: CS3311 Middleware
Lab/Assignment: Lab3
Description of program: Publishes notifications to client about the weather
'''

# from the socket module import all
from socket import *
# importing datetime so that we can get the current date and time to put into the textfile later on in the program
import datetime
import random

list_of_events_types = []
dictionary_of_event_attributes = {"SPORT SCORES" : ["Parameters", "Notification every time a team scores", "Event ID"],"WEATHER REPORT" : ["parameters", "Notification every time there will be a change in the weather", "Event ID"]}
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
server_address = (hostname, 8000)
# output to terminal some info on the address details
print('*** Server is starting up on %s port %s ***' % server_address)
# Bind the socket to the host and port
sock.bind(server_address)

# Listen for one incoming connections to the server
sock.listen(1)

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
                print("received " "%s", "at", "%s" % data, date)
                # decode() function returns string object
                data_capitalised = data.upper()
                if data_capitalised == "RECEIVE NOTIFICATIONS":
                    temperature_figure = random.randint(0, 20)
                    temperature = str(temperature_figure)
                    weather_choices = random.choice(["Today it will be overcast with the chance of showers and the temperature will be 5 degrees","clear skies with no chance of rain temperature will be 10 degrees","sunny with no chance of cloud and the temperature will be 15 degrees"])
                    weather = str(weather_choices)
                    service_message = "*****SENDING NOTIFICATIONS*****"
                    connection.send(service_message.encode())
                    # weather_report_1 = "\nIt's going to be"+" "+weather+" ""and the temperature will be "+temperature+" "+"degrees"
                    # connection.send(weather_report_1.encode())
                    connection.send(weather.encode())

    finally:
        # closing connection
        connection.close()

# closing connection to the socket
sock.close()



