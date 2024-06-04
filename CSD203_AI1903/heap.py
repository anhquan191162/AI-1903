class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index != 0 and self.heap[self.parent(index)] > self.heap[index]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def get_min(self):
        if not self.heap:
            return None
        return self.heap[0]

    def size(self):
        return len(self.heap)

    def is_empty(self):
        return len(self.heap) == 0

    def print_heap(self):
        print(self.heap)

# Example Usage
if __name__ == "__main__":
    min_heap = MinHeap()
    min_heap.insert(3)
    min_heap.insert(2)
    min_heap.insert(15)
    min_heap.insert(5)
    min_heap.insert(4)
    min_heap.insert(45)
    
    print("Min-Heap array:")
    min_heap.print_heap()
    
    print("Extracted min:", min_heap.extract_min())
    print("Min-Heap array after extraction:")
    min_heap.print_heap()
    
    print("Current min:", min_heap.get_min())
    print("Heap size:", min_heap.size())
    print("Is heap empty?", min_heap.is_empty())