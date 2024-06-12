class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def addToHead(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node.next = self.head
            self.head = new_node
            temp.next = self.head

    def addToTail(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def addAfter(self, p, x):
        new_node = Node(x)
        temp = self.head
        while temp.data != p:
            temp = temp.next
            if temp == self.head:
                return
        new_node.next = temp.next
        temp.next = new_node

    def deleteFromHead(self):
        if not self.head:
            return None
        data = self.head.data
        if self.head.next == self.head:
            self.head = None
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
        return data

    def deleteFromTail(self):
        if not self.head:
            return None
        if self.head.next == self.head:
            data = self.head.data
            self.head = None
            return data
        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next
        data = temp.next.data
        temp.next = self.head
        return data
    def deleteAfter(self, p):
        temp = self.head
        while temp.data != p:
            temp = temp.next
            if temp == self.head:
                return None
        if temp.next == self.head:
            return None
        data = temp.next.data
        temp.next = temp.next.next
        return data

    def delNode(self, x):
        if not self.head:
            return
        if self.head.data == x and self.head.next == self.head:
            self.head = None
            return
        temp = self.head
        prev = None
        while temp.data != x:
            prev = temp
            temp = temp.next
            if temp == self.head:
                return
        if temp == self.head:
            while temp.next != self.head:
                temp = temp.next
            temp.next = self.head.next
            self.head = self.head.next
        else:
            prev.next = temp.next

    def search(self, x):
        temp = self.head
        if not temp:
            return None
        while True:
            if temp.data == x:
                return temp
            temp = temp.next
            if temp == self.head:
                break
        return None

    def traverse(self):
        if not self.head:
            print('None')
            return
        temp = self.head
        while True:
            print(temp.data, end=' -> ')
            temp = temp.next
            if temp == self.head:
                break
        print('HEAD')

# Example usage
cll = CircularLinkedList()
cll.addToHead(1)
cll.addToHead(2)
cll.addToTail(3)
cll.traverse()  # 2 -> 1 -> 3 -> HEAD

cll.addAfter(1, 4)
cll.traverse()  # 2 -> 1 -> 4 -> 3 -> HEAD

print(cll.deleteFromHead())  # 2
cll.traverse()  # 1 -> 4 -> 3 -> HEAD

print(cll.deleteFromTail())  # 3
cll.traverse()  # 1 -> 4 -> HEAD

print(cll.deleteAfter(1))  # 4
cll.traverse()  # 1 -> HEAD

cll.delNode(1)
cll.traverse()  # None

print(cll.search(1))