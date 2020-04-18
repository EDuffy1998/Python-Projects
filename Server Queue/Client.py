'''
Operating Systems II
Student Name: Edward Duffy
Student Number: 117501529
Date: 05/02/19
Assignment 1: Round Robin Scheduling
'''

class Process(object):

    def __init__(self,state,priority,process_name):
        self._state = state
        self._priority = priority
        self._process_name = process_name

    def getState(self):
        return self._state

    def setState(self, state):
        self._state = state

    def getPriority(self):
        return self._priority

    def setPriority(self, priority):
        self._priority = priority

    def getProcessName(self):
        return self._process_name

    def setProcessName(self, process_name):
        self._process_name = process_name


class CPU(Process):

    def __init__(self, state, priority, process_name):
        Process.__init__(self, state, priority, process_name)
        self._ready_queue = []
        self._blocked_queue = []

    def getReadyQueue(self):
        return self._ready_queue

    def setReadyQueue(self):
        self._ready_queue = []

    def getBlockedQueue(self):
        return self._blocked_queue

    def addReadyProcess(self, state, priority, process_name):
        ready_queue = self._ready_queue
        ready_state = "READY"
        if ready_state == state.upper():
            process_list = [state, priority, process_name]
            ready_queue.appened(process_list)
        else:
            return "Error invalid process state"

    def addBlockedProcess(self, state, priority, process_name):
        blocked_queue = self._blocked_queue
        ready_queue = self._ready_queue
        blocked_state = "BLOCKED"
        input_output_operation = input("This a blocked state do you wish to unblock it? Yes or No")
        if blocked_state == input_output_operation.upper():
            blocked_list = [state, priority, process_name]
            blocked_queue.append(blocked_list)
        elif input_output_operation.upper == "YES":
            ready_process_list = [state, priority, process_name]
            ready_queue.append(ready_process_list)
        else:
            return "Error Invalid/state"

    def addSuspendedProcess(self, state, priority, process_name):
        blocked_queue = self._blocked_queue
        input_output_operation = input("Suspended process if you like to un-suspend it and make it ready/blocked or no")
        if input_output_operation.upper() == "NO":
            return "process suspended"
        elif input_output_operation.upper() == "READY":
            CPU.addReadyProcess(self,input_output_operation, priority, process_name)
        elif input_output_operation.upper() == "BLOCKED":
            CPU.addBlockedProcess(self, input_output_operation, priority, process_name)
        else:
            return "Error"

    def runProcesses(self):
        ready_queue = self._ready_queue
        blocked_queue = self._blocked_queue
        length_of_ready_queue = len(ready_queue)
        length_of_blocked_queue = len(blocked_queue)
        if length_of_ready_queue != 0:
            for processes in ready_queue:
                print(processes)
        elif length_of_blocked_queue != 0:
            for processes in blocked_queue:
                print(processes)


if __name__ == "__main__":
    process1 = Process("READY", 1, "Process_name")
    CPU1 = CPU.addReadyProcess(CPU,"READY",1,"Process_1")





