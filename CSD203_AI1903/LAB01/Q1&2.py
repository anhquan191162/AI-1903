class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def addToHead(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def addToTail(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def addAfter(self, p, x):
        new_node = Node(x)
        temp = self.head
        while temp and temp.data != p:
            temp = temp.next
        if not temp:
            return
        new_node.next = temp.next
        temp.next = new_node

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def deleteFromHead(self):
        if not self.head:
            return None
        temp = self.head
        self.head = self.head.next
        return temp.data

    def deleteFromTail(self):
        if not self.head:
            return None
        if not self.head.next:
            temp = self.head
            self.head = None
            return temp.data
        second_last = self.head
        while second_last.next.next:
            second_last = second_last.next
        temp = second_last.next
        second_last.next = None
        return temp.data

    def deleteAfter(self, p):
        temp = self.head
        while temp and temp.data != p:
            temp = temp.next
        if not temp or not temp.next:
            return None
        to_delete = temp.next
        temp.next = temp.next.next
        return to_delete.data

    def delNode(self, x):
        temp = self.head
        if temp and temp.data == x:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != x:
            prev = temp
            temp = temp.next
        if not temp:
            return
        prev.next = temp.next

    def search(self, x):
        temp = self.head
        while temp and temp.data != x:
            temp = temp.next
        return temp

    def count(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def deleteAt(self, i):
        if i < 0:
            return
        temp = self.head
        if i == 0:
            if temp:
                self.head = temp.next
            return
        prev = None
        count = 0
        while temp and count != i:
            prev = temp
            temp = temp.next
            count += 1
        if not temp:
            return
        prev.next = temp.next

    def sort(self):
        if not self.head or not self.head.next:
            return
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            sorted_list = self.sortedInsert(sorted_list, current)
            current = next_node
        self.head = sorted_list

    def sortedInsert(self, head_ref, new_node):
        if not head_ref or head_ref.data >= new_node.data:
            new_node.next = head_ref
            head_ref = new_node
        else:
            current = head_ref
            while current.next and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        return head_ref

    def delNodeByRef(self, p):
        temp = self.head
        previous = None
        while temp:
            if temp == p:
                if previous:
                    previous.next = temp.next
                else:
                    self.head = temp.next
                return
            previous = temp
            temp = temp.next

    def toArray(self):
        array = []
        temp = self.head
        while temp:
            array.append(temp.data)
            temp = temp.next
        return array

    def merge(self, other):
        dummy = Node(0)
        tail = dummy
        l1, l2 = self.head, other.head
        while l1 and l2:
            if l1.data < l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        tail.next = l1 or l2
        self.head = dummy.next

    def addBefore(self, p, x):
        new_node = Node(x)
        if not self.head:
            return
        if self.head.data == p:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        while temp.next and temp.next.data != p:
            temp = temp.next
        if not temp.next:
            return
        new_node.next = temp.next
        temp.next = new_node

    def attach(self, other):
        if not self.head:
            self.head = other.head
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = other.head

    def max(self):
        if not self.head:
            return None
        max_val = self.head.data
        temp = self.head.next
        while temp:
            if temp.data > max_val:
                max_val = temp.data
            temp = temp.next
        return max_val

    def min(self):
        if not self.head:
            return None
        min_val = self.head.data
        temp = self.head.next
        while temp:
            if temp.data < min_val:
                min_val = temp.data
            temp = temp.next
        return min_val

    def sum(self):
        total = 0
        temp = self.head
        while temp:
            total += temp.data
            temp = temp.next
        return total

    def avg(self):
        total = self.sum()
        count = self.count()
        return total / count if count != 0 else 0

    def sorted(self):
        temp = self.head
        while temp and temp.next:
            if temp.data > temp.next.data:
                return False
            temp = temp.next
        return True

    def insert(self, x):
        new_node = Node(x)
        if not self.head or self.head.data >= x:
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        while temp.next and temp.next.data < x:
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def compare(self, other):
        temp1 = self.head
        temp2 = other.head
        while temp1 and temp2:
            if temp1.data != temp2.data:
                return False
            temp1 = temp1.next
            temp2 = temp2.next
        return temp1 is None and temp2 is None


# Example usage
sll = SinglyLinkedList()
sll.addToHead(3)
sll.addToHead(2)
sll.addToHead(1)
sll.traverse()  # 1 -> 2 -> 3 -> None

sll.addToTail(4)
sll.traverse()  # 1 -> 2 -> 3 -> 4 -> None

sll.addAfter(2, 5)
sll.traverse()  # 1 -> 2 -> 5 -> 3 -> 4 -> None

print(sll.deleteFromHead())  # 1
sll.traverse()  # 2 -> 5 -> 3 -> 4 -> None

print(sll.deleteFromTail())  # 4
sll.traverse()  # 2 -> 5 -> 3 -> None

print(sll.deleteAfter(2))  # 5
sll.traverse()  # 2 -> 3 -> None

sll.delNode(2)
sll.traverse()  # 3 -> None

print(sll.search(3))  
print(sll.search(2))  # None

print(sll.count())  # 1

sll.addToTail(6)
sll.addToTail(9)
sll.addToTail(4)
sll.deleteAt(2)
sll.traverse()  # 3 -> 6 -> 4 -> None

sll.sort()
sll.traverse()  # 3 -> 4 -> 6 -> None

sll.delNodeByRef(sll.search(4))
sll.traverse()  # 3 -> 6 -> None

print(sll.toArray())  # [3, 6]

sll2 = SinglyLinkedList()
sll2.addToHead(7)
sll2.addToHead(1)
sll2.addToHead(5)

sll.merge(sll2)
sll.traverse()  # 1 -> 3 -> 6

