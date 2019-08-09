# Implementation of the Queue data stucture in Python3

from random import randrange

class Queue:
    # Initializing with one list
    def __init__(self):
        self.queue = []
    def size(self):
        return len(self.queue)
    def isEmpty(self):
        return len(self.queue) == 0
    def enqueue(self,data):
        # Appending data to the front of the list
        self.queue.insert(0,data)
    def dequeue(self):
        # Removing items from the back of the list
        self.queue.pop()
    def printQueue(self):
        print(self.queue)

# Sample program to test queue
def runDriver():
    q = Queue()
    print("Size of Queue is:", q.size())
    print("Queue is Empty:", q.isEmpty())
    for k in range(5):
        q.enqueue(randrange(1,10))
    q.printQueue()
    print("Size of Queue is:", q.size())
    print("Queue is Empty:", q.isEmpty())
    for i in range((randrange(1,q.size()))):
        q.dequeue()
    q.printQueue()
    print("Size of Queue is:", q.size())
    print("Queue is Empty:", q.isEmpty())

