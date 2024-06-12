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
    
class Node2:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    def addF(self,data):
        new = Node2(data)
        if self.isEmpty():
            self.front = self.rear = new
        else:
            new.next = self.front
            self.front.prev = new
            self.front = new
        self.length += 1

    def addR(self,data):
        new = Node2(data)
        if self.isEmpty():
            self.front = self.rear = new
        else:
            new.prev = self.rear
            self.rear.next = new
            self.rear = new
        self.length += 1

    def removeF(self):
        if self.isEmpty():
            return
        res = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None
        self.length -=1
        return res
    def removeR(self):
        if self.isEmpty():
            return
        res = self.rear.data
        self.rear = self.rear.prev
        if self.rear is None:
            self.front = None
        else:
            self.rear.next = None
        self.length -=1
        return res
    def peekR(self):
        if self.isEmpty():
            return
        return self.rear.data
    def peekF(self):
        if self.isEmpty():
            return
        return self.front.data

    def isEmpty(self):
        return self.length == 0
    def getSize(self):
        return self.length
    
class Node3:
    def __init__(self,data,pr):
        self.data = data
        self.pr = pr
        self.next = None
class PriorityQueue:
    def __init__(self):
        self.front = None
    def isEmpty(self):
        return True if self.front == None else False
    def push(self,data,pr):
        if self.isEmpty() == True:
            self.front = Node3(data,pr)
        else:
            if self.front.pr > pr:
                newNode = Node3(data,pr)
                newNode.next = self.front
                self.front = newNode
            else:
                temp = self.front
                while temp:
                    if pr <= temp.next.pr:
                        break

                    temp = temp.next
                newNode = Node3(data,pr)
                newNode.next = temp.next
                temp.next = newNode
    def pop(self):
        if self.isEmpty() == True:
            return
        else:
            self.front = self.front.next
    def peek(self):
        if self.isEmpty() == True:
            return
        else:
            return self.front.data
    def traverse(self):
        if self.isEmpty() == True:
            return
        else:
            temp = self.front
            while temp:
                print(temp.data,end=' ')
                temp = temp.next


        
