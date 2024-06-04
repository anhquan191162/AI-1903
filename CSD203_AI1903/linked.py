class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedList:
    def __init__(self):
        self.head = None
    
    def push(self,new):
        n_node = Node(new)
        n_node.next = self.head
        self.head = n_node
    def insert2(self,prev,new):
        if prev is None:
            return
        n_node = Node(new)
        n_node.next = prev.next
        prev.next = n_node
    def insert3(self,new):
        n_node = Node(new)
        if self.head is None:
            self.head = n_node
            return
        l = self.head
        while l.next:
            l.next
        l = n_node
    def delete(self,pos):
        
        temp = self.head
        prev = self.head
        for i in range(pos):
            if i == 0 and pos == 1:
                self.head = self.head.next
            else:
                if i == pos - 1 and temp is not None:
                    prev.next = temp.next
                else:
                    prev = temp
                    if prev is None:
                        break
                    temp = temp.next
        return self.head
    
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    

                
    def traversal(self):
        current = self.head
        while current:
            print(current.data,end='->')
            current = current.next
        print('NULL')
        print()

    def getNth(self,index):
        current = self.head
        count = 0   
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        return
    def printNthFromLast(self,N):
        curr = self.head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        if N > length:
            return
        curr = self.head
        for i in range(length - N):
            curr = curr.next

        print(curr.data)


if __name__ == "__main__":
    llist = linkedList()
    llist.push(20)
    llist.push(4)
    llist.push(15)
    llist.push(35)

    # Function call
    llist.traversal()
    llist.printNthFromLast(4)