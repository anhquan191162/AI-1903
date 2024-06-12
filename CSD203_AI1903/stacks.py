class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stacks:
    def __init__(self):
        self.length = 0
        self.head = None
    def push(self,data):
        new = Node(data)
        if self.head == None:
            self.head = new
            self.length +=1
        else:
            new.next = self.head
            self.head = new
            self.length += 1
    def isEmpty(self):
        return self.length == 0
    def pop(self):
        if self.isEmpty():
            return 
        else:
            pnode = self.head
            self.head = self.head.next
            pnode.next = None
            return pnode.data
    def peek(self):
        if self.isEmpty():
            return
        else:
            return self.head.data
    def display(self):
        current = self.node

        if self.isEmpty():
            return
        else:
            while current!= None:
                print(current.data,end='->')
                current = current.next
            print('NULL')
      