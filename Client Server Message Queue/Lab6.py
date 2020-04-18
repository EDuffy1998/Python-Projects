'''
Student Name: Edward Duffy
Student Number: 117501529
Date: 12/11/2019
Module: CS3311 Middleware
Lab/Assignment: Lab 6
Lab Description: Client - Server Messaging queues
There is a general queue where clients send their messages with the requested operation and the corresponding operands
The servers consume the appropriate message that matches each
individual service, and will return the result as a message in another queue
'''

'''
Client Pseudocode:
1 - Establish a connection to the server
2 - Wait for a successful connection and inform the user a connection has been established
3 - Send the message to the server
--- Message format:
  - ID of the sender
  - The operation they want to access
  - The parameter's needed for the function

4 - Convert the user's message into a list data structure so each part of the message can be accessed easily by the server
5 - Message is sent to the server
6 - Client waits for the server to respond
7 - Client decodes the message sent by the server
8 - Client prints the result received 
'''

'''
Server Pseudocode:
1 - Establish a connection with the client/end-user
2 - Once a connection has been established with the end-user wait for any incoming messages requests
3 - Once a request/message has been received decode the message
4 - Once message has been decoded iterate through the message find the index where the service the user requests is stored
5 - Once the service the user wants to use has been found contact the service and pass through the parameters that the user sent
6 - Once the request/service performs it's action put the result into a queue
7 - Enqueue the result and send encode it
8 - Send the encoded result back to the client

'''

# class Client(object):
#
#     def __init__(self,type,size,operands,clientID):
#         self.type = type
#         self.size = size
#         self.operands = operands
#         self.clientID = clientID
#         self.clientIDGenerator = 0
#
#
#     def getType(self):
#         return self.type
#
#     def getSize(self):
#         return self.size
#
#     def getOperands(self):
#         return self.operands
#
#     def getClientID(self):
#         return self.clientID
#
#     def setType(self, type):
#         self.type = type
#
#     def setSize(self, size):
#         self.size = size
#
#     def setOperands(self, operands):
#         self.operands = operands
#
#     def setClient(self):
#         self.clientID = self.clientID+self.clientIDGenerator
#         self.clientIDGenerator += 1

'''
Place inputs here:
Input = service you want
Input 2 = User enters Operands/parameters 
Convert to upper case
'''
import re
class Server:

    def __init__(self):
        self.demandqueue = []
        self.resultqueue = []

    def AddToDemandQueue(self,request):
        # logfile = open("logfileMessageQueues.txt","w+")
        # logfile.close()
        # print("logfile has been created")
        print("request that was received was", request)
        if request[0] == "CALCULATOR":
            print("This is a request for the calculator service which will be added to the demand queue")
            self.demandqueue.insert(0,request)
            equation = str(request[1]+request[2]+request[3])
            # logfile.write("Request for the calculator service has been added to the demand queue")
            # logfile.close()
            Server.Calcualtor(self, equation)
        elif request[0] == "STRING REVERSER":
            print("This is a request for the string reverser in a string service and will be added to the demand queue")
            self.demandqueue.insert(0,request)
            string = request[1]
            # logfile.write("Request for the string reverser service has been added to the demand queue")
            # logfile.close()
            Server.StringReverser(self, string)
        elif request[0] == "BUBBLESORT":
            self.demandqueue.insert(0,request)
            print("This is a request for the sorting algorithm and this request will be added to the demand queue ")
            unsorted_list = list(request[1])
            # logfile.write("Request for the sorting algorithm has been added to the demand queue ")
            # logfile.close()
            Server.BubbleSortAlgorithm(self, unsorted_list)
        elif request[0] == "SELECTION SORT":
            self.demandqueue.insert(0,request)
            print("This is a request for the sorting algorithm and this request will be added to the demand queue ")
            unsorted_list = list(request[1])
            # logfile.write("Request for the sorting algorithm has been added to the demand queue ")
            # logfile.close()
            Server.SelectionSortAlgorithm(self, unsorted_list)
        elif request[0] == "INSERTION SORT":
            self.demandqueue.insert(0,request)
            print("This is a request for the sorting algorithm and this request will be added to the demand queue ")
            unsorted_list = list(request[1])
            # logfile.write("Request for the sorting algorithm has been added to the demand queue ")
            # logfile.close()
            Server.InsertionSortAlgorithm(self,unsorted_list)



    def Calcualtor(self,equation):
        # logfile = open("logfileMessageQueues.txt","a+")
        # logfile.write("Calculator service has been activated")
        # logfile.close()
        print("Received equation %s" % equation)
        length_of_equation = len(equation)
        if length_of_equation == 0:
            # logfile.write("Invalid input entered by the user")
            print("An equation has not been entered! Please try again")
        else:
            answer = str(eval(equation))
            # logfile.write("The answer calculated by the calculator was %s" % answer)
            print("The answer to your equation is"+answer)
            self.resultqueue.insert(0,answer)


    def StringReverser(self,string):
        length_of_string = len(string)
        if length_of_string == 0:
            print("Invalid String was not entered")
        else:
            reversed_string = string[::-1]
            print("The reversed string is %s" % reversed_string)
            self.resultqueue.insert(0,reversed_string)


    def BubbleSortAlgorithm(self,unsorted_list):
    #     logfile = open("logfileMessageQueues.txt", "a+")
    #     logfile.write("The Sorting Algorithm service was activated")
    #     logfile.close()
        for passnum in range(len(unsorted_list) - 1, 0, -1):
            for i in range(passnum):
                if unsorted_list[i] > unsorted_list[i + 1]:
                    temp = unsorted_list[i]
                    unsorted_list[i] = unsorted_list[i + 1]
                    unsorted_list[i + 1] = temp
        self.resultqueue.insert(0, unsorted_list)
        print(unsorted_list)

    def InsertionSortAlgorithm(self,unsorted_list):
        # Traverse through 1 to len(arr)
        for i in range(1, len(unsorted_list)):

            key = unsorted_list[i]

            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i - 1
            while j >= 0 and key < unsorted_list[j]:
                unsorted_list[j + 1] = unsorted_list[j]
                j -= 1
            unsorted_list[j + 1] = key
        print(unsorted_list)
        self.resultqueue.insert(0,unsorted_list)

    def SelectionSortAlgorithm(self, unsorted_list):
        for i in range(len(unsorted_list)):

            # Find the minimum element in remaining
            # unsorted array
            min_idx = i
            for j in range(i + 1, len(unsorted_list)):
                if unsorted_list[min_idx] > unsorted_list[j]:
                    min_idx = j

                    # Swap the found minimum element with
            # the first element
            unsorted_list[i], unsorted_list[min_idx] = unsorted_list[min_idx], unsorted_list[i]
        print(unsorted_list)
        self.resultqueue.insert(0,unsorted_list)

    def sizeofResultQueue(self):
        result_queue = self.resultqueue
        length_of_result_queue = len(result_queue)
        logfile = open("logfileMessageQueues.txt", "a+")
        logfile.write("The Client wanted to check the size of the result queue")
        logfile.write("The length of the result queue at that time was %s " % length_of_result_queue)
        logfile.close()
        print("The length of the result queue was",length_of_result_queue)




    def sizeOfDemandQueue(self):
        demand_queue = self.demandqueue
        logfile = open("logfileMessageQueues.txt", "a+")
        logfile.write("Client wanted to know the size of the demand queue")
        size_of_demand_queue = len(demand_queue)
        print("The size of the demand queue is",size_of_demand_queue)
        logfile.write("The size of the demand queue at that time was %s" % size_of_demand_queue)
        logfile.close()

if __name__ == "__main__":
    # Request format [users,choice,parameters]
        server = Server()
        user_input_choose_to_perform_tests = input("Would you like to perform all the tests or use as normal client")
        user_input_test_choice = user_input_choose_to_perform_tests.upper()
        if user_input_test_choice == "TEST":
            print("********PERFORMING TESTS****************")
            server.AddToDemandQueue(["CALCULATOR", "23", "+", "40"])
            server.AddToDemandQueue(["STRING REVERSER","messagequeue"])
            server.AddToDemandQueue(["BUBBLESORT",[1,3,4,6,5,6,7,8,5,5,346,4,747,4,3,]])
            server.AddToDemandQueue(["INSERTION SORT",[1,2,3,43,2,12,44,5,6,4,3,5,6,75,4]])
            server.AddToDemandQueue(["SELECTION SORT",[12,3,4,56,432,4,5,34,2,3,12,3,4,5,6]])
            server.AddToDemandQueue(["CALCULATOR", "300", "-", "197"])
            server.sizeOfDemandQueue()
            server.sizeofResultQueue()
        elif user_input_test_choice == "CLIENT":
            list_of_services_available = ["CALCULATOR", "SORTING ALGORITHM", "STRING REVERSER"]
            service_input_choice = input("Which service would you like to access")
            users_service_choice = service_input_choice.upper()
            if users_service_choice not in list_of_services_available:
                print("The service you have chosen is not available")
                print("We have the following services available")
                for services in list_of_services_available:
                    print("\n", services)
            else:
                if users_service_choice == "CALCULATOR":
                    users_choice = "CALCULATOR"
                    user_input_first_number = input("Please enter the first number")
                    user_input_operator = input("Please enter the operator")
                    user_input_second_number = input("Please enter the second number")
                    request = [users_choice, user_input_first_number, user_input_operator, user_input_second_number]
                    print("Your request will be sent to the demand queue")
                    server.AddToDemandQueue(request)

                elif users_service_choice == "SORTING ALGORITHM":
                    users_choice = "SORTING ALGORITHM"
                    list_of_algorithms = ["BUBBLESORT", "INSERTION SORT", "SELECTION SORT"]
                    user_input_sorting_algorithm_choice = input("Please enter the sorting algorithm you would like to request to access")
                    algorithm_choice = user_input_sorting_algorithm_choice.upper()

                    if algorithm_choice == "BUBBLESORT":
                        print("You have entered bubble sort")
                        user_input_unsorted_list = input("please enter the unsorted list you wish to sort")
                        unsorted_list = list(user_input_unsorted_list)
                        if user_input_unsorted_list == unsorted_list.sort():
                            print("List entered is already sorted")
                        else:
                            user_algorithm_choice = "BUBBLESORT"
                            print("Request is being sent to the demand queue")
                            request = [user_input_sorting_algorithm_choice, user_input_unsorted_list]
                            server.AddToDemandQueue(request)

                    elif algorithm_choice == "INSERTION SORT":
                        print("You have selected insertion sort")
                        user_input_unsorted_list = input("please enter the unsorted list you wish to sort")
                        unsorted_list = list(user_input_unsorted_list)
                        if user_input_unsorted_list == unsorted_list.sort():
                            print("List entered is already sorted")
                        else:
                            user_algorithm_choice = "INSERTION SORT"
                            print("Request is being sent to the demand queue")
                            request = [user_algorithm_choice, user_input_unsorted_list]
                            server.AddToDemandQueue(request)

                    elif algorithm_choice == "SELECTION SORT":
                        print("You have selected selection sort")
                        user_input_unsorted_list = input("please enter the unsorted list you wish to sort")
                        unsorted_list = list(user_input_unsorted_list)
                        if user_input_unsorted_list == unsorted_list.sort():
                            print("List entered is already sorted")
                        else:
                            user_algorithm_choice = "SELECTION SORT"
                            print("Request is being sent to the demand queue")
                            request = [user_algorithm_choice, user_input_unsorted_list]
                            server.AddToDemandQueue(request)

                elif users_service_choice == "STRING REVERSER":
                    users_choice = "STRING REVERSER"
                    user_input_string = input("Please enter the string you want to reverse")
                    string_length = len(user_input_string)
                    if string_length == 0:
                        print("The string you have entered has no length or you did not enter anything")
                    else:
                        print("Your request is being sent to the demand queue")
                        request = [users_choice, user_input_string]
                        server.AddToDemandQueue(request)
