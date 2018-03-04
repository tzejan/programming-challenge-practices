# implement a queue using an array/list
class Queue(object):
    def __init__(self):
        self.queue = []
        self.head = 0
        self.tail = 0

    def push(self, obj):
        self.queue.append(obj)
        self.tail += 1

    def pop(self):
        item = None
        if self.tail - self.head > 0:
            item = self.queue[self.head]
            self.head += 1
        return item


    def compact(self):
        del self.queue[:self.head]

        
        #for i in range(self.tail - self.head):
        #    self.queue[i] = self.queue[self.head+i]
        self.tail -= self.head
        self.head = 0
        #del self.queue[self.tail:]

    def printContents(self):
        print self.head, self.tail
        print self.queue, self.queue[self.head:self.tail]

import random
random.seed("g")

q = Queue()
for i in range(10):
    q.push(random.randrange(100))
    q.printContents()

q.printContents()

for i in range(11):
    print q.pop()
    q.printContents()
    if i >= 5:
        q.compact()

q.printContents()
