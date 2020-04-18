'''
Student Name: Edward Duffy
Student Number: 117501529
Date: 19/10/2019
Module: CS3311 Middleware
Lab/Assignment: Lab3
Lab/Assignment Description: Client - server / subscriber publisher - notification service
'''
# from the socket module import all
from socket import *
# importing datetime so that we can get the current date and time to put into the textfile later on in the program
import datetime

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
server_address = (hostname, 10000)
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
                if data_capitalised == "I WANT TO SUBSCRIBE TO AN EVENT TYPE":
                    service_message = "what event type would you like to subscribe to?"
                    connection.sendall(service_message.encode())
                    # really want to put awhile statement here not sure how to do it for a client server model
                if data_capitalised == "WHAT EVENT TYPES ARE THERE":
                    #services = str(list_of_services.keys())
                    sports_scores = "Sport Scores"
                    weather_report = "\n Weather report"
                    connection.send(sports_scores.encode())
                    connection.send(weather_report.encode())
                elif data_capitalised == "SPORT SCORES":
                            service_message = "if would you like to access this service ,\n""you can access it by subscribing connecting to the publisher directly"
                            sports_scores_attributes = str(dictionary_of_event_attributes["SPORT SCORES"])
                            connection.send(message_to_client.encode())
                            connection.send("\n".encode())
                            connection.send(sports_scores_attributes.encode())
                            connection.send("\n".encode())
                            connection.send(service_message.encode())
                elif data_capitalised == "WEATHER REPORT":
                    #for keys, values in list_of_services:
                        #if keys == "STRING REVERSER":
                            service_message = "This service is available ,\n you can access it by connecting to the publisher directly"
                            weather_report_attributes = str(dictionary_of_event_attributes["WEATHER REPORT"])
                            connection.send(message_to_client.encode())
                            connection.send("\n".encode())
                            connection.send(weather_report_attributes.encode())
                            connection.send("\n".encode())
                            connection.send(service_message.encode())
                elif data_capitalised == "I WANT TO SUBSCRIBE TO SPORT SCORES":
                            subscribed_message = "You have successfully subscribed to receive sport score notifications"
                            connection.send(subscribed_message.encode())
                elif data_capitalised == "I WANT TO SUBSCRIBE TO WEATHER REPORT":
                            subscribed_message = "You have successfully subscribed to receive weather report notifications"
                            connection.send(subscribed_message.encode())
                elif data_capitalised == "UNSUBSCRIBE TO SPORT SCORES":
                            unsubscribed_message = "You have unsubscribed from sport scores and will not receive anymore notifications"
                            connection.send(unsubscribed_message.encode())
                elif data_capitalised == "UNSUBSCRIBE TO WEATHER REPORT":
                    unsubscribed_message = "You have unsubscribed from sport scores and will not receive anymore notifications"
                    connection.send(unsubscribed_message.encode())
                elif data_capitalised == "INFO":
                    welcome_message = "Welcome to the Notification Manager to interact please enter the following"
                    option_a = "\n if you want to subscribe to a service , enter ""I want to subscribe to (name of the service) e.g SPORT SCORES """
                    option_b = "\n if you want to know what event types are available for you to subscribe to , enter what event types are there"
                    option_c = "\n if you want to know more about a certain event type , enter the name of the event type e.g SPORT SCORES or WEATHER REPORT"
                    connection.send(welcome_message.encode())
                    connection.send(option_a.encode())
                    connection.send(option_b.encode())
                    connection.send(option_c.encode())
    finally:
        # closing connection
        connection.close()

# closing connection to the socket
sock.close()

