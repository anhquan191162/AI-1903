'''class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,ele):
        self.queue.append(ele)
    def isEmpty(self):
        return len(self.queue) == 0
    def size(self):
        return len(self.queue)
    def deque(self):
        if self.isEmpty():
            return
        return self.queue.pop(0)
    def peek(self):
        if self.isEmpty():
            return 
        return self.queue[0]'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    def enqueue(self,ele):
        n_data = Node(ele)
        if self.rear is None:
            self.front = self.rear = n_data
            self.length += 1
            return
        self.rear.next = n_data
        self.rear = n_data
        self.length += 1
    def deque(self):
        if self.isEmpty():
            return
        n = self.front
        self.front = n.next
        self.length -=1
        if self.front == None:
            self.rear = None
        return n.data
    def isEmpty(self):
        return self.length == 0
    def size(self):
        return self.length
    def peek(self):
        if self.isEmpty():
            return
        return self.front.data
    def display(self):
        current = self.front
        while current:
            print(current.data,end='->')
            current = current.next
        print('NULL')
    

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()
q.deque()
q.display()
