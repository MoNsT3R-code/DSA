class HeapPriorityQueue:

    def __init__(self):

        self.heap = []

    def enqueue(self, key, value):

        self.heap.append((key, value))
        self.upheap(len(self.heap)-1)

    def dequeue(self):

        if len (self.heap) == 0:

            return None
        
        if len (self.heap) == 1:

            return self.heap.pop
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.downheap(0)
        return root

    def downheap(self, index):

        Left_child = 2 * index + 1
        Right_child = 2 * index + 2
        smallest = index
    
        if Left_child < len(self.heap) and self.heap[Left_child][0] < self.heap[smallest][0]:

            smallest = Left_child

        if Right_child < len(self.heap) and self.heap[Right_child][0] < self.heap[smallest][0]:

            smallest = Right_child

        if smallest != index:

            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.downheap(smallest)
        
    def upheap(self, index):

        Parent = (index - 1) // 2

        if index > 0 and self.heap[Parent][0] > self.heap[index][0]:

            self.heap[index], self.heap[Parent] = self.heap[Parent], self.heap[index]
            self.upheap(Parent)


    def min(self):

        if self.heap == 0:
            return None
        else:
            return self.heap[0]

    def __len__(self):

        return len(self.heap)

pq = HeapPriorityQueue()
pq.enqueue(5, "TaskA")
pq.enqueue(1, "TaskC")
pq.enqueue(3, "TaskB")
print(pq.min())
pq.dequeue() 
print(len(pq))

def is_heap(arr):

    n = len(arr)

    for index in range(n):
        Left_child = 2 * index + 1
        Right_child = 2 * index + 2

        if Left_child < n and arr[Left_child] < arr[index]:

            return False
        
        elif Right_child < n and arr[Right_child] < arr[index]:

            return False
        
        else:

            return True
        
arr1 = [1, 3, 6, 5, 9, 8]
arr2 = [3, 1, 6, 5, 9, 8]
print(is_heap(arr1)) 
print(is_heap(arr2))
        


