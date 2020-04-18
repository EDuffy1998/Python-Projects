'''
Student Name: Edward Duffy
Student Number: 117501529
Module: CS3311 Middleware
Assignment: Lab 5
Description: Message Queue
'''


class MessageProducer(object):

    def __init__(self, message, id):
        self.message = message
        self.id = id

    def getMessage(self):
        return self.message

    def setMessage(self,message):
        self.message = message

    def getID(self):
        return self.id

    def setID(self, id):
        self.id = id

class Client(object):

    def __init__(self,message,id):
        self.message = message
        self.id = id

    def getMessage(self):
        return self.message

    def setMessage(self,message):
        self.message = message

    def getID(self):
        return self.id

    def setID(self, id):
        self.id = id

class Message:

    def __init__(self,data=None):
        self.data = data

class MessageQueue:

    def __init__(self):
        self.queue = []

    def queueIsEmpty(self):
        return len(self.queue) == []

    def insertMessage(self, new_message):
        new_message = Message(Client)
        self.queue.append(new_message)

    def removeMessage(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max]:
                    max = i
                message = self.queue[max]
                del self.queue[max]
                return message
        except IndexError:
            print()
            exit()





