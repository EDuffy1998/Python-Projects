'''
CS3311 Middleware
Student Name: Edward Duffy
Student Number: 117501529
Date: 09/11/2019
Assignment: Lab 5
Message: FIFO Queue
'''

class MessageProducer(object):

    def __init__(self,message,prioirty,ID):
        self.message = message
        self.priority = prioirty
        self.ID = ID

    def getID(self):
        return self.ID

    def setID(self, ID):
        self.ID = ID

    def getMessage(self):
        return self.message

    def setMessage(self, message):
        self.message = message

    def getPriority(self):
        return self.priority

    def setPriority(self, priority):
        self.priority = priority


class Message:

    def __init__(self,data=None):
        self.data = data

class MessageQueue:

    def __init__(self):
        self.messageQueue = []
        self.user_number = 0
        self.queue_index = 0

    def createLogfile(self):
        logfile = open("logfile.txt", "w+") # w+ means create logfile if one doesnt exist
        logfile.close() # close the connection to the logfile once it has been created
        print("logfile created")

    def addMessage(self, MessageProducer):

        new_message = Message(MessageProducer)
        message_queue = self.messageQueue
        locked_message = "Locked to user %s" % self.user_number
        print(locked_message)
        self.user_number +=1
        unlocked_message = "Queue has been unlocked"
        message_to_logfile = "\nProducer added a message to the message queue"
        message_queue.insert(self.queue_index,new_message)
        logfile = open("logfile.txt","a+")
        logfile.write(message_to_logfile)
        print("Message successfully added to the queue")
        print("Service is now unlocked")
        logfile.close()
        self.queue_index +=1

    def popMessage(self):
        # index_accumulator = 0
        # message_queue = self.messageQueue
        # if len(message_queue) == 0:
        #     print("There are no messages in the queue to pop off")
        # else:
        return self.messageQueue




    def IsQueueEmpty(self):
        message_queue = self.messageQueue
        logfile = open("logfile.txt","a+")
        message_to_logfile = "\nUser checked to see was the queue empty"
        if len(message_queue) == 0:
            print("The message queue is empty")
            logfile.write(message_to_logfile)
            logfile.close()
        else:
            print("Message queue is not empty")
            logfile.write(message_to_logfile)
            logfile.close()

    def LengthOfMessageQueue(self):
        message_queue = self.messageQueue
        logfile = open("logfile.txt","a+")
        length_of_message_queue = len(message_queue)
        message_to_logfile = "\n User checked the length of the message queue"
        logfile.write(message_to_logfile)
        print("the length of the message queue is",length_of_message_queue)
        logfile.close()

    def __str__(self):
        return "The contents of the message queue is %s" % self.messageQueue


if __name__ == "__main__":
    message = MessageProducer("This is the first message","High Priority","ID:123456")
    message1 = MessageProducer("This is the first message", "High Priority", "ID:123456")
    message2 = MessageProducer("This is the first message", "High Priority", "ID:123456")
    message3 = MessageProducer("This is the first message", "High Priority", "ID:123456")
    message_queue = MessageQueue()
    message_queue.createLogfile()
    message_queue.addMessage(message)
    message_queue.addMessage(message1)
    message_queue.addMessage(message2)
    message_queue.addMessage(message3)
    message_queue.LengthOfMessageQueue()
    message_queue.IsQueueEmpty()
    message_queue.popMessage()
    message_queue.__str__()





















