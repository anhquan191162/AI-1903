class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def addToHead(self, x):
        new_node = Node(x)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def addToTail(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def addAfter(self, p, x):
        new_node = Node(x)
        temp = self.head
        while temp and temp.data != p:
            temp = temp.next
        if not temp:
            return
        new_node.next = temp.next
        new_node.prev = temp
        if temp.next:
            temp.next.prev = new_node
        temp.next = new_node

    def deleteFromHead(self):
        if not self.head:
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        return data

    def deleteFromTail(self):
        if not self.head:
            return None
        if not self.head.next:
            data = self.head.data
            self.head = None
            return data
        temp = self.head
        while temp.next:
            temp = temp.next
        data = temp.data
        temp.prev.next = None
        return data

    def deleteAfter(self, p):
        temp = self.head
        while temp and temp.data != p:
            temp = temp.next
        if not temp or not temp.next:
            return None
        data = temp.next.data
        temp.next = temp.next.next
        if temp.next:
            temp.next.prev = temp
        return data

    def delNode(self, x):
        if not self.head:
            return
        if self.head.data == x:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        temp = self.head
        while temp and temp.data != x:
            temp = temp.next
        if not temp:
            return
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next

    def search(self, x):
        temp = self.head
        while temp:
            if temp.data == x:
                return temp
            temp = temp.next
        return None

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=' <-> ')
            temp = temp.next
        print('None')

# Example usage
dll = DoublyLinkedList()
dll.addToHead(1)
dll.addToHead(2)
dll.addToTail(3)
dll.traverse()  # 2 <-> 1 <-> 3 <-> None

dll.addAfter(1, 4)
dll.traverse()  # 2 <-> 1 <-> 4 <-> 3 <-> None

print(dll.deleteFromHead())  # 2
dll.traverse()  # 1 <-> 4 <-> 3 <-> None

print(dll.deleteFromTail())  # 3
dll.traverse()  # 1 <-> 4 <-> None

print(dll.deleteAfter(1))  # 4
dll.traverse()  # 1 <-> None

dll.delNode(1)
dll.traverse()  # None

print(dll.search(1))  # None