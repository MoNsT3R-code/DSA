#Lab 7- Recursion Time Complexity and Stack/Queue Implementations

#	a) Linear Recursion

def rec_sum(n):                   #O(1)
    if n <= 0:                    #O(1)
        return 0                  #O(n)
    return n + rec_sum(n - 1)     #O(n)

# The total time complexity of this recursive function is O(n) because the loop is executed n times

#	b) Logarithmic Recursion

def rec_halve(n):                   #O(1)
    if n <= 1:                      #O(log n)
        return 1                    #O(n<=0)
    return 1 + rec_halve(n // 2)    #O(log n)

# The total time complexity of this recursive function is O(log n) because n<=0 and mod of 2 total calls are log base 2 (n)

#	c) Exponential Recursion – Fibonacci

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# The total time complexity of this recursive function is O(2**n) because each line in fib seq except base line is executed O(2**n) times.

# 2. Implement a Stack Using the Array Class

class DynamicArray:               #using previous lab code

    def __init__(self, initial_capacity=2):          
        self.capacity = initial_capacity           
        self.size = 0
        self.array = [None] * self.capacity
    def append(self, value):
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = value
        self.size += 1
    def get(self, index):
        if index < 0 or index >= self.size:
            return "error"
        return self.array[index]
    def set(self, index, value):
        if index < 0 or index >= self.size:
            return "error"
        self.array[index] = value
        return value
    def resize(self):
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
    def remove_last(self):
        if self.size == 0:
            return "error"
        last = self.array[self.size - 1]
        self.size -= 1
        return last
    def get_last(self):
        if self.size == 0:
            return "error"
        return self.array[self.size - 1]
    def is_empty(self):
        return self.size == 0
    def remove_first(self):
        if self.size == 0:
            return "error"
        first = self.array[0]
        for i in range(1, self.size):
            self.array[i - 1] = self.array[i]
        self.size -= 1
        return first
    def get_first(self):
        if self.size == 0:
            return "error"
        return self.array[0]
    def is_empty(self):
        return self.size == 0

class Stack:               

    def __init__(self):
        self.array = DynamicArray()
    def push(self, element):
        self.array.append(element)
    def pop(self):
        if self.is_empty():
            return "error: stack is empty"
        return self.array.remove_last()

    def peek(self):
        if self.is_empty():
            return "error: stack is empty"
        return self.array.get_last()
    def is_empty(self):
        return self.array.is_empty()


s = Stack()
s.push(5)
s.push(10)
s.push(15)
print(s.pop())    
print(s.peek())   


class Queue:

    def __init__(self):
        self.array = DynamicArray()
    def enqueue(self, element):
        self.array.append(element)
    def dequeue(self):
        if self.is_empty():
            return "error: queue is empty"
        return self.array.remove_first()
    def peek(self):
        if self.is_empty():
            return "error: queue is empty"
        return self.array.get_first()
    def is_empty(self):
        return self.array.is_empty()
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            for i in range(self.array.size):
                print(self.array.get(i), end=' ')
            print()


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  
print(q.peek())     

def reverse_queue(q):
    stack = Stack()
    while not q.is_empty():
        stack.push(q.dequeue())
    while not stack.is_empty():
        q.enqueue(stack.pop())


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
reverse_queue(q)
q.display()