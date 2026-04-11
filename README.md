├── README.md
├── practice questions summer 2025 dsa.docx
├── DSA practice.py
├── Lab 8 dsa.py (200 tokens)
├── Lab 2 dsa.py (500 tokens)
├── Lab 7 dsa (1).py (600 tokens)
├── lab 5 DSA.py (800 tokens)
├── Lab 1 DSA.py (800 tokens)
├── lab 4.py (800 tokens)
├── lab 6 dsa.py (1000 tokens)
├── Assignment 2 DSA.py (1100 tokens)
├── Lab 7 DSA.py (1100 tokens)
├── dsa.py (3900 tokens)
└── Assignment # 1_2 DSA.py (4500 tokens)


/README.md:
--------------------------------------------------------------------------------
1 | 
2 | 


--------------------------------------------------------------------------------
/practice questions summer 2025 dsa.docx:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/MoNsT3R-code/DSA/main/practice questions summer 2025 dsa.docx


--------------------------------------------------------------------------------
/DSA practice.py:
--------------------------------------------------------------------------------
 1 | a = "what is data modeling"
 2 | 
 3 | print(a.upper())
 4 | 
 5 | 
 6 | b = input("Answer: ")
 7 | 
 8 | if b == "data":
 9 | 
10 |     print("WRONG")
11 | 
12 | else:
13 | 
14 | 
15 |     print("Correct, now study its detail as you don't have sense")
16 | 


--------------------------------------------------------------------------------
/Lab 8 dsa.py:
--------------------------------------------------------------------------------
 1 | from collections import deque
 2 | 
 3 | def BFS(graph, vertex_start):
 4 | 
 5 |     visit = set()
 6 |     trans_order = []
 7 |     queue = deque([vertex_start])
 8 |     visit.add(vertex_start)
 9 | 
10 |     while queue:
11 | 
12 |         vrtx = queue.popleft()
13 |         trans_order.append(vrtx)
14 |         for nbr in graph[vrtx]:
15 |             if nbr not in visit:
16 |                 visit.add(nbr)
17 |                 queue.append(nbr)
18 | 
19 |     return trans_order
20 | 
21 | graph = {
22 |     'A': ['B', 'D'],
23 |     'B': ['A', 'C', 'E'],
24 |     'C': ['B', 'F'],
25 |     'D': ['A', 'E'],
26 |     'E': ['B', 'D', 'F'],
27 |     'F': ['C', 'E']
28 | }
29 | 
30 | start_node = 'A'
31 | trans_result = BFS(graph, start_node)
32 | print(trans_result)
33 | 
34 | 


--------------------------------------------------------------------------------
/Lab 2 dsa.py:
--------------------------------------------------------------------------------
 1 | class  DynamicArray:
 2 | 
 3 |     def __init__ (self, initial_capacity):
 4 | 
 5 |         self.capacity = initial_capacity
 6 |         self.size = 0
 7 |         self.array = [None] * self.capacity
 8 | 
 9 |     def append(self, value):
10 |         
11 |         if self.size == self.capacity:
12 |              
13 |             self.resize()
14 |              
15 |         self.array[self.size] = value
16 |         self.size += 1
17 | 
18 |     def get(self, index):
19 | 
20 |         if index <= 0 or index >= self.size:
21 |                 return "error"
22 |         return self.array[index]
23 | 
24 |     def set(self, index, value):
25 | 
26 |         if index < 0 or index >= 0:
27 |                 return "error"
28 |         self.array[index] = value
29 |         return value
30 |    
31 |     def resize(self) :
32 | 
33 |         self.capacity *= 2
34 |         new_array = [None] * self.capacity
35 |         for i in range (self.size):
36 |             new_array[i] = self.array[i]
37 |             self.array = new_array
38 |     
39 | 
40 | arr = DynamicArray(2)
41 | arr.append(5)
42 | arr.append(6)
43 | arr.append(7)
44 | print(arr.get(1))
45 | print(arr.set(1, 10))
46 | print(arr.get(1))
47 | #print(arr.display())
48 | 
49 | print()
50 | class Dynamic_array:
51 | 
52 |     def __init__ (self):
53 | 
54 |         self.array = []
55 | 
56 |     def append(self, value):
57 | 
58 |         self.array.append(value)
59 |         
60 | 
61 |     def find_longest(self):
62 | 
63 |         return max(self.array, key = len)
64 | 
65 | arr = Dynamic_array()
66 | arr.append("cat")
67 | arr.append("elephant")
68 | arr.append("dog")
69 | print(arr.find_longest())
70 |             
71 | print()
72 | 
73 | class Dynamic_Error:
74 |      
75 |     def __init__ (self):
76 | 
77 |         self.array = []
78 | 
79 |     def append(self, value):
80 | 
81 |         self.array.append(value)
82 |         
83 |     def remove_duplicates(self):
84 | 
85 |         return list(set(self.array))
86 | 
87 | arr = Dynamic_Error()
88 | arr.append("apple")
89 | arr.append("apple")
90 | arr.append("banana")
91 | arr.append("banana")
92 | arr.append("cherry")
93 | print(arr.remove_duplicates())


--------------------------------------------------------------------------------
/Lab 7 dsa (1).py:
--------------------------------------------------------------------------------
  1 | class HeapPriorityQueue:
  2 | 
  3 |     def __init__(self):
  4 | 
  5 |         self.heap = []
  6 | 
  7 |     def enqueue(self, key, value):
  8 | 
  9 |         self.heap.append((key, value))
 10 |         self.upheap(len(self.heap)-1)
 11 | 
 12 |     def dequeue(self):
 13 | 
 14 |         if len (self.heap) == 0:
 15 | 
 16 |             return None
 17 |         
 18 |         if len (self.heap) == 1:
 19 | 
 20 |             return self.heap.pop
 21 |         
 22 |         root = self.heap[0]
 23 |         self.heap[0] = self.heap.pop()
 24 |         self.downheap(0)
 25 |         return root
 26 | 
 27 |     def downheap(self, index):
 28 | 
 29 |         Left_child = 2 * index + 1
 30 |         Right_child = 2 * index + 2
 31 |         smallest = index
 32 |     
 33 |         if Left_child < len(self.heap) and self.heap[Left_child][0] < self.heap[smallest][0]:
 34 | 
 35 |             smallest = Left_child
 36 | 
 37 |         if Right_child < len(self.heap) and self.heap[Right_child][0] < self.heap[smallest][0]:
 38 | 
 39 |             smallest = Right_child
 40 | 
 41 |         if smallest != index:
 42 | 
 43 |             self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
 44 |             self.downheap(smallest)
 45 |         
 46 |     def upheap(self, index):
 47 | 
 48 |         Parent = (index - 1) // 2
 49 | 
 50 |         if index > 0 and self.heap[Parent][0] > self.heap[index][0]:
 51 | 
 52 |             self.heap[index], self.heap[Parent] = self.heap[Parent], self.heap[index]
 53 |             self.upheap(Parent)
 54 | 
 55 | 
 56 |     def min(self):
 57 | 
 58 |         if self.heap == 0:
 59 |             return None
 60 |         else:
 61 |             return self.heap[0]
 62 | 
 63 |     def __len__(self):
 64 | 
 65 |         return len(self.heap)
 66 | 
 67 | pq = HeapPriorityQueue()
 68 | pq.enqueue(5, "TaskA")
 69 | pq.enqueue(1, "TaskC")
 70 | pq.enqueue(3, "TaskB")
 71 | print(pq.min())
 72 | pq.dequeue() 
 73 | print(len(pq))
 74 | 
 75 | def is_heap(arr):
 76 | 
 77 |     n = len(arr)
 78 | 
 79 |     for index in range(n):
 80 |         Left_child = 2 * index + 1
 81 |         Right_child = 2 * index + 2
 82 | 
 83 |         if Left_child < n and arr[Left_child] < arr[index]:
 84 | 
 85 |             return False
 86 |         
 87 |         elif Right_child < n and arr[Right_child] < arr[index]:
 88 | 
 89 |             return False
 90 |         
 91 |         else:
 92 | 
 93 |             return True
 94 |         
 95 | arr1 = [1, 3, 6, 5, 9, 8]
 96 | arr2 = [3, 1, 6, 5, 9, 8]
 97 | print(is_heap(arr1)) 
 98 | print(is_heap(arr2))
 99 |         
100 | 
101 | 
102 | 


--------------------------------------------------------------------------------
/lab 5 DSA.py:
--------------------------------------------------------------------------------
  1 | print('Task 1')
  2 | print()
  3 | 
  4 | class Node:
  5 |     
  6 |     def __init__(self, data):
  7 |         
  8 |         self.data = data
  9 |         self.prev = None
 10 |         self.next = None
 11 | 
 12 | class DoublyLinkedList:
 13 |     
 14 |     def __init__(self):
 15 | 
 16 |         self.head = None
 17 | 
 18 |     def insert_at_beginning(self, data):
 19 | 
 20 |         new_node = Node(data)
 21 |         new_node.next = self.head
 22 | 
 23 |         if self.head:
 24 | 
 25 |             self.head.prev = new_node
 26 | 
 27 |         self.head = new_node
 28 | 
 29 |     def insert_at_end(self, data):
 30 | 
 31 |         new_node = Node(data)
 32 | 
 33 |         if not self.head:
 34 | 
 35 |             self.head = new_node
 36 |             return
 37 | 
 38 |         curr = self.head
 39 | 
 40 |         while curr.next:
 41 | 
 42 |             curr = curr.next
 43 | 
 44 |         curr.next = new_node
 45 |         new_node.prev = curr
 46 | 
 47 |     def delete_from_beginning(self):
 48 | 
 49 |         if not self.head:
 50 | 
 51 |             return
 52 | 
 53 |         self.head = self.head.next
 54 | 
 55 |         if self.head:
 56 | 
 57 |             self.head.prev = None
 58 | 
 59 |     def delete_from_end(self):
 60 | 
 61 |         if not self.head:
 62 | 
 63 |             return
 64 | 
 65 |         if not self.head.next:
 66 | 
 67 |             self.head = None
 68 |             return
 69 | 
 70 |         curr = self.head
 71 | 
 72 |         while curr.next:
 73 | 
 74 |             curr = curr.next
 75 | 
 76 |         curr.prev.next = None
 77 | 
 78 |     def display_forward(self):
 79 | 
 80 |         result = []
 81 |         curr = self.head
 82 | 
 83 |         while curr:
 84 | 
 85 |             result.append(curr.data)
 86 |             curr = curr.next
 87 | 
 88 |         print(result)
 89 | 
 90 |     def display_backward(self):
 91 | 
 92 |         result = []
 93 |         curr = self.head
 94 | 
 95 |         if not curr:
 96 | 
 97 |             print(result)
 98 |             return
 99 | 
100 |         while curr.next:
101 | 
102 |             curr = curr.next
103 | 
104 |         while curr:
105 | 
106 |             result.append(curr.data)
107 |             curr = curr.prev
108 | 
109 |         print(result)
110 | 
111 | dll = DoublyLinkedList()
112 | 
113 | dll.insert_at_beginning(10)
114 | dll.insert_at_end(20)
115 | dll.insert_at_beginning(5)
116 | dll.display_forward()
117 | 
118 | print()
119 | 
120 | dll.display_backward()
121 | dll.delete_from_beginning()
122 | dll.delete_from_end()
123 | 
124 | print()
125 | 
126 | dll.display_forward()
127 | 
128 | print()
129 | 
130 | print('Task 2')
131 | print()
132 | 
133 | def reverse_list(dll):
134 | 
135 |     current = dll.head
136 |     prev_node = None
137 | 
138 |     
139 |     while current:
140 | 
141 |         next_node = current.next
142 |         current.next = prev_node
143 |         current.prev = next_node
144 |         prev_node = current
145 |         current = next_node
146 |    
147 |     dll.head = prev_node
148 | 
149 | dll = DoublyLinkedList()
150 | 
151 | dll.insert_at_end(1)
152 | dll.insert_at_end(2)
153 | dll.insert_at_end(3)
154 | dll.display_forward()
155 | 
156 | print()
157 | 
158 | reverse_list(dll)
159 | dll.display_forward()
160 | 
161 | print()
162 | 
163 | dll.display_backward()    
164 | 


--------------------------------------------------------------------------------
/Lab 1 DSA.py:
--------------------------------------------------------------------------------
  1 | class Person(object):
  2 | 
  3 |     def __init__ (self, name, id_number):
  4 | 
  5 |         self.name = name
  6 |         self.id_number = id_number
  7 | 
  8 |     def display(self):
  9 | 
 10 |         print(self.name, self.id_number)
 11 | 
 12 |     def get_profile(self):
 13 | 
 14 |         return f"{self.name}, {self.age}"
 15 | 
 16 | class Student(Person):
 17 | 
 18 |     def __init__ (self, name, id_number, semester):
 19 |         super().__init__(name, id_number)
 20 | 
 21 |         self.semester = semester
 22 |         self.borrow_book = []
 23 | 
 24 |     def addborrowedbook(self, Book, Borrowed_date):
 25 | 
 26 |             Borrowed_book = Borrowedbook(Book, Borrowed_date)
 27 |             self.Borrowed_books.append(Borrowed_book)
 28 | 
 29 |     def get_details(self):
 30 |         
 31 | 
 32 |         return f'{self.name}, {self.id_number}, {self.semester}, {self.borrow_book}'
 33 | 
 34 | class Librarian(Person):
 35 | 
 36 |     def __init__ (self, name, id_number, staff_id, shift, display_student_list
 37 | ):
 38 |         super().__init__(name, id_number)
 39 | 
 40 |         self.staff_id = staff_id
 41 |         self.shift = shift
 42 |         self.display_student_list = display_student_list
 43 | 
 44 | class Book(object):
 45 | 
 46 |     def __init__ (self, title, author, isbn):
 47 | 
 48 |         self.title = title
 49 |         self.author = author
 50 |         self.isbn = isbn
 51 | 
 52 | class Borrowedbook(Book):
 53 | 
 54 |     def __init__ (self, Book, Borrow_date):
 55 |         
 56 |         self.Book = Book
 57 |         self.Borrow_date = Borrow_date
 58 | 
 59 | 
 60 | book1 = Book("Clean Code", "Robert Martin", "12345")
 61 | book2 = Book("Python 101", "Mike", "99999")
 62 | borrowed1 = BorrowedBook(book1, "2024-05-01")
 63 | borrowed2 = BorrowedBook(book2, "2024-05-05")
 64 | student = Student("Zain", 102, 5)
 65 | student.borrowed_books.extend([borrowed1, borrowed2])
 66 | librarian = Librarian("Huma", 201, "Evening")
 67 | librarian.students.append(student)
 68 | print_profiles([student, librarian])
 69 | 
 70 | '''
 71 | 
 72 | def helper(x):              #1
 73 |     count = 0               #1
 74 |     for i in range(x):      #n
 75 |         count += 1          #n
 76 |         return count        #1
 77 | def q2(n):                  #1
 78 |     total = 0               #1
 79 |     for j in range(1, n + 1): #n
 80 |         total += helper(j)    #1+2+3+...+n
 81 |         return total          #1
 82 | 
 83 | #it is the series of sum 1+2+3+...+n, let n = k, 1+2+3+...+k, (k(k+1))/2, (k^2+k)/2 = k^2 + k = n^2+n
 84 | #In big O we take the largest exponent digit so here the value of Big O is n^2
 85 | 
 86 | def q3(n):                     #1
 87 |     total = 0                  #1
 88 |     i = 1                      #log3(n)
 89 |     while i <= n:              #10log3(n)
 90 |         for j in range(10):    #10log3(n)
 91 |             total += 1         #10log3(n)
 92 |         i *= 3                 
 93 |     return total               #1
 94 | 
 95 | #the time complexity is log3n*10, as in while loop i<=n and i*=3 so we conclude that the value of n will be within 100
 96 | #10log3n
 97 | 
 98 | def q4(n):                  #1
 99 |     total = 0               #1
100 |     for i in range(1, n + 1): #n
101 |         for j in range(1, n + 1):  #n*n
102 |             total += 1             #n
103 |             if total > n:          #n
104 |                 break              #1
105 |     return total                   #1
106 | 
107 | #n**2
108 | '''


--------------------------------------------------------------------------------
/lab 4.py:
--------------------------------------------------------------------------------
  1 | class SinglyLinkedList:
  2 | 
  3 |     def __init__  (self, data = None):
  4 | 
  5 |         self.data = data
  6 |         self.next = None
  7 | 
  8 | class singly_linked_list:
  9 |     
 10 |     def __init__(self):
 11 | 
 12 |         self.head = None
 13 | 
 14 |     def insert_at_the_beginning(self, data):
 15 |         
 16 |         newnod = SinglyLinkedList(data)
 17 |         newnod.next = self.head
 18 |         self.head = newnod
 19 | 
 20 |     def insert_at_end(self, data):
 21 | 
 22 |         if not self.head:
 23 |             self.head = SinglyLinkedList(data)
 24 |             return
 25 |         curr = self.head
 26 |         while curr.next:
 27 |             curr = curr.next
 28 |         curr.next = SinglyLinkedList(data)
 29 | 
 30 |     def delete_from_beginning(self):
 31 | 
 32 |         if self.head:
 33 |             self.head = self.head.next
 34 | 
 35 |     def delete_from_end(self, ): 
 36 | 
 37 |         if not self.head:
 38 |             return
 39 |         if not self.head.next:
 40 |             self.head = None
 41 |             return
 42 |         curr = self.head
 43 |         while curr.next.next:
 44 |             curr = curr.next
 45 |         curr.next = None
 46 | 
 47 | 
 48 |     def insert_after(self, target, new_data):
 49 | 
 50 |         curr = self.head
 51 |         last_occ = None
 52 | 
 53 |         while curr:
 54 |             if curr.data == target:
 55 |                 last_occ = None
 56 |             curr = curr.next
 57 |             if last_occ:
 58 |                 newnod = SinglyLinkedList(new_data)
 59 |                 newnod.next = last_occ.next
 60 |                 last_occ.next = newnod
 61 |         
 62 | 
 63 |     def insert_before(self, next_data, new_data):
 64 | 
 65 |         if not self.head:
 66 |             return
 67 |         if self.head.data == next_data:
 68 |             self.insert_at_the_beginning(new_data)
 69 | 
 70 |         curr = self.head
 71 |         while curr.next:
 72 |             if curr.next.data == next_data:
 73 |                 newnod = SinglyLinkedList(new_data)
 74 |                 newnod.next = curr.next
 75 |                 curr.next = newnod
 76 |                 return
 77 |             curr = curr.next
 78 | 
 79 |     def display(self):
 80 |         no = []
 81 |         curr_nod = self.head
 82 |         while curr_nod:
 83 |             no.append(curr_nod.data)
 84 |             curr_nod = curr_nod.next
 85 |         print(no)
 86 | 
 87 |     
 88 | sll = singly_linked_list()
 89 | sll.insert_at_the_beginning(2)
 90 | sll.insert_at_end(3)
 91 | sll.insert_at_the_beginning(1)
 92 | sll.display()
 93 | 
 94 | sll.delete_from_beginning()
 95 | sll.display()
 96 | sll.delete_from_end()
 97 | sll.display()
 98 | 
 99 | sll.insert_at_end(3)
100 | sll.insert_at_end(2)
101 | sll.insert_after(2, 4)
102 | sll.display()
103 | 
104 | sll.insert_before(2, 0)
105 | sll.display()
106 | 
107 | def find_middle_node(self, sll):
108 | 
109 |         slow = sll.head
110 |         fast = sll.head
111 | 
112 |         if sll.head is None:
113 |             return None
114 | 
115 |         while fast is not None and fast.next is not None:
116 | 
117 |             slow = slow.next
118 |             fast = fast.next.next
119 | 
120 |         return slow.data 
121 | 
122 | 
123 | sll = singly_linked_list()
124 | sll.insert_at_end(1)
125 | sll.insert_at_end(2)
126 | sll.insert_at_end(3)
127 | 
128 | print(find_middle_node(sll))
129 | 
130 | sll2 = singly_linked_list()
131 | sll2.insert_at_end(1)
132 | sll2.insert_at_end(2)
133 | sll2.insert_at_end(3)
134 | sll2.insert_at_end(4)
135 | 
136 | print(find_middle_node(sll2))
137 | 
138 | sll3 = singly_linked_list()
139 | print(find_middle_node(sll3))
140 | 
141 | sll4 = singly_linked_list()
142 | sll4.insert_at_end(10)
143 | print(find_middle_node(sll4))
144 | 


--------------------------------------------------------------------------------
/lab 6 dsa.py:
--------------------------------------------------------------------------------
  1 | class Parent:
  2 | 
  3 |     def __init__ (self, value):
  4 | 
  5 |         self.value = value
  6 |         self.left = None
  7 |         self.right = None
  8 | 
  9 | class BinaryTree:
 10 | 
 11 |     def __init__ (self):
 12 | 
 13 |         self.root = None
 14 | 
 15 |     def insert(self, value):
 16 | 
 17 |         if not self.root:
 18 |             self.root = Parent(value)
 19 |         
 20 |         else:
 21 |             self._insert(self.root, value)
 22 | 
 23 |     def _insert(self, parent, value):
 24 | 
 25 |         if value < parent.value:
 26 | 
 27 |             if parent.left:
 28 |                 self._insert(parent.left, value)
 29 | 
 30 |             else:
 31 | 
 32 |                 parent.left = Parent(value)
 33 | 
 34 |             if parent.right:
 35 | 
 36 |                 self._insert(parent.right, value)
 37 | 
 38 |             else:
 39 | 
 40 |                 Parent.right = Parent(value)
 41 | 
 42 |     def inorder(self):
 43 | 
 44 |         return self._inorder(self.root)
 45 |     
 46 |     def _inorder(self, parent):
 47 | 
 48 |         if parent:
 49 | 
 50 |             return self._inorder(parent.left) + [parent.value] + self._inorder(parent.right)
 51 |         
 52 |         return []
 53 | 
 54 |     def preorder(self):
 55 | 
 56 |         return self._preorder(self.root)
 57 |     
 58 |     def _preorder(self, parent):
 59 | 
 60 |         if parent:
 61 | 
 62 |             return [parent.value] + self._preorder(parent.left) + self._preorder(parent.right)
 63 |         
 64 |         return []
 65 | 
 66 |     def postorder(self):
 67 | 
 68 |         return self._postorder(self.root)
 69 |     
 70 |     def _postorder(self, parent):
 71 | 
 72 |         if parent:
 73 | 
 74 |             return self._postorder(parent.left) + self._postorder(parent.right) + [parent.value]
 75 |             
 76 |         return []
 77 |     
 78 |     def find(self, value):
 79 | 
 80 |         return self._find(self.root, value)
 81 |     
 82 |     def _find(self, parent, value):
 83 | 
 84 |         if not parent:
 85 |             return False
 86 |         
 87 |         if parent.value == value:
 88 |             return True
 89 |         
 90 |         elif value < parent.value:
 91 |             return self._find(parent.left, value)
 92 | 
 93 |         else:
 94 |             return self._find(parent.right, value)
 95 |         
 96 |     def height(self):
 97 | 
 98 |         return self._height(self.root)
 99 |     
100 |     def _height(self, parent):
101 | 
102 |         if not parent:
103 | 
104 |             return 0
105 |         
106 |         else:
107 | 
108 |             return 1 + max(self._height(parent.left), self._height(parent.right))
109 | 
110 |     def is_empty(self):
111 | 
112 |         return self.root is None
113 | 
114 |     def __len__ (self):
115 | 
116 |         return self._len(self.root)
117 |     
118 |     def _len(self, parent):
119 | 
120 |         if not parent:
121 |             return 0 
122 |         return 1 + self._len(parent.left) + self._len(parent.right)
123 |     
124 |     def delete(self, value):
125 |     
126 |         self.root = self._delete(self.root, value)
127 | 
128 |     def _delete(self, parent, value):
129 | 
130 |         if not parent:
131 |             return parent
132 |         
133 |         if value < parent.value:
134 |             parent.left = self._delete(parent.left, value)
135 | 
136 |         elif value > parent.value or value == parent.value :
137 |             parent.right = self._delete(parent.right, value)
138 | 
139 |         else:
140 |             
141 |             if not parent.left and not parent.right:
142 | 
143 |                 return None
144 |             elif not parent.left:
145 |                 return parent.right
146 |             elif not parent.right:
147 |                 return parent.left
148 |             else:
149 |                 min_parent = self._find_min(parent.right)
150 |                 parent.value = min_parent.value
151 |                 parent.right=self._del(parent.right, min_parent.value)
152 | 
153 |         return parent
154 | 
155 |         
156 | 
157 | bst = BinaryTree()
158 | bst.insert(50)
159 | bst.insert(30)
160 | bst.insert(70)
161 | 
162 | print("Inorder: ", (bst.inorder()))  
163 | print("preorder: ", (bst.preorder()))
164 | print("Postorder: ", (bst.postorder()))
165 | 
166 | print("Finding 30: ", (bst.find(30)))
167 | print("Height: ", (bst.height()))
168 | print("Is Empty: ", (bst.is_empty()))
169 | print("Length of tree: ", len(bst))
170 | 
171 | bst.delete(30)
172 | print("Inorder after del 30: ", (bst.inorder()))  
173 | print("preorder: ", (bst.preorder()))
174 | print("Postorder: ", (bst.postorder()))


--------------------------------------------------------------------------------
/Assignment 2 DSA.py:
--------------------------------------------------------------------------------
  1 | import datetime
  2 | 
  3 | class Node:
  4 |     def __init__(self, match_id, team1_name, team2_name, match_date, winner, location):
  5 |         self.match_id = match_id
  6 |         self.team1 = {'name': team1_name, 'cricketers': []}
  7 |         self.team2 = {'name': team2_name, 'cricketers': []}
  8 |         self.match_date = match_date
  9 |         self.winner = winner
 10 |         self.location = location
 11 |         self.left = None
 12 |         self.right = None
 13 |         self.height = 1
 14 | 
 15 | class AVLTree:
 16 |     def __init__(self):
 17 |         self.root = None
 18 | 
 19 |     def add_match(self, match_id, team1_name, team2_name, match_date, winner, location):
 20 |         self.root = self._add_match(self.root, match_id, team1_name, team2_name, match_date, winner, location)
 21 | 
 22 |     def _add_match(self, node, match_id, team1_name, team2_name, match_date, winner, location):
 23 |         if node is None:
 24 |             return Node(match_id, team1_name, team2_name, match_date, winner, location)
 25 |         elif match_id < node.match_id:
 26 |             node.left = self._add_match(node.left, match_id, team1_name, team2_name, match_date, winner, location)
 27 |         else:
 28 |             node.right = self._add_match(node.right, match_id, team1_name, team2_name, match_date, winner, location)
 29 | 
 30 |         node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
 31 |         balance = self._get_balance(node)
 32 | 
 33 |         if balance > 1 and match_id < node.left.match_id:
 34 |             return self._right_rotate(node)
 35 |         if balance < -1 and match_id > node.right.match_id:
 36 |             return self._left_rotate(node)
 37 |         if balance > 1 and match_id > node.left.match_id:
 38 |             node.left = self._left_rotate(node.left)
 39 |             return self._right_rotate(node)
 40 |         if balance < -1 and match_id < node.right.match_id:
 41 |             node.right = self._right_rotate(node.right)
 42 |             return self._left_rotate(node)
 43 | 
 44 |         return node
 45 | 
 46 |     def _left_rotate(self, z):
 47 |         y = z.right
 48 |         T2 = y.left
 49 |         y.left = z
 50 |         z.right = T2
 51 |         z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
 52 |         y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
 53 |         return y
 54 | 
 55 |     def _right_rotate(self, z):
 56 |         y = z.left
 57 |         T3 = y.right
 58 |         y.right = z
 59 |         z.left = T3
 60 |         z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
 61 |         y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
 62 |         return y
 63 | 
 64 |     def _get_height(self, node):
 65 |         if node is None:
 66 |             return 0
 67 |         return node.height
 68 | 
 69 |     def _get_balance(self, node):
 70 |         if node is None:
 71 |             return 0
 72 |         return self._get_height(node.left) - self._get_height(node.right)
 73 | 
 74 |     def inorder_traversal(self):
 75 |         self._inorder_traversal(self.root)
 76 | 
 77 |     def _inorder_traversal(self, node):
 78 |         if node:
 79 |             self._inorder_traversal(node.left)
 80 |             print(f"Match ID: {node.match_id}")
 81 |             print(f"Team 1: {node.team1['name']}")
 82 |             print(f"Team 2: {node.team2['name']}")
 83 |             print(f"Match Date: {node.match_date}")
 84 |             print(f"Winner: {node.winner}")
 85 |             print(f"Location: {node.location}")
 86 |             print("------------------------")
 87 |             self._inorder_traversal(node.right)
 88 | 
 89 |     def save_to_file(self, filename):
 90 |         with open(filename, 'w') as f:
 91 |             self._save_to_file(self.root, f)
 92 | 
 93 |     def _save_to_file(self, node, f):
 94 |         if node:
 95 |             self._save_to_file(node.left, f)
 96 |             f.write(f"{node.match_id},{node.team1['name']},{node.team2['name']},{node.match_date},{node.winner},{node.location}\n")
 97 |             self._save_to_file(node.right, f)
 98 | 
 99 | tree = AVLTree()
100 | tree.add_match('M1', 'Team A', 'Team B', '2022-01-01', 'Team A', 'Location 1')
101 | tree.add_match('M2', 'Team C', 'Team D', '2022-01-15', 'Team C', 'Location 2')
102 | tree.inorder_traversal()
103 | tree.save_to_file('matches.txt')
104 | 
105 | def load_from_file(filename):
106 |     tree = AVLTree()
107 |     try:
108 |         with open(filename, 'r') as f:
109 |             for line in f.readlines():
110 |                 match_id, team1_name, team2_name, match_date, winner, location = line.strip().split(',')
111 |                 tree.add_match(match_id, team1_name, team2_name, match_date, winner, location)
112 |         return tree
113 |     except FileNotFoundError:
114 |         print("File not found.")
115 | 
116 | loaded_tree = load_from_file('matches.txt')
117 | loaded_tree.inorder_traversal()
118 | 


--------------------------------------------------------------------------------
/Lab 7 DSA.py:
--------------------------------------------------------------------------------
  1 | #Lab 7- Recursion Time Complexity and Stack/Queue Implementations
  2 | 
  3 | #	a) Linear Recursion
  4 | 
  5 | def rec_sum(n):                   #O(1)
  6 |     if n <= 0:                    #O(1)
  7 |         return 0                  #O(n)
  8 |     return n + rec_sum(n - 1)     #O(n)
  9 | 
 10 | # The total time complexity of this recursive function is O(n) because the loop is executed n times
 11 | 
 12 | #	b) Logarithmic Recursion
 13 | 
 14 | def rec_halve(n):                   #O(1)
 15 |     if n <= 1:                      #O(log n)
 16 |         return 1                    #O(n<=0)
 17 |     return 1 + rec_halve(n // 2)    #O(log n)
 18 | 
 19 | # The total time complexity of this recursive function is O(log n) because n<=0 and mod of 2 total calls are log base 2 (n)
 20 | 
 21 | #	c) Exponential Recursion – Fibonacci
 22 | 
 23 | def fib(n):
 24 |     if n <= 1:
 25 |         return n
 26 |     return fib(n - 1) + fib(n - 2)
 27 | 
 28 | # The total time complexity of this recursive function is O(2**n) because each line in fib seq except base line is executed O(2**n) times.
 29 | 
 30 | # 2. Implement a Stack Using the Array Class
 31 | 
 32 | class DynamicArray:               #using previous lab code
 33 | 
 34 |     def __init__(self, initial_capacity=2):          
 35 |         self.capacity = initial_capacity           
 36 |         self.size = 0
 37 |         self.array = [None] * self.capacity
 38 |     def append(self, value):
 39 |         if self.size == self.capacity:
 40 |             self.resize()
 41 |         self.array[self.size] = value
 42 |         self.size += 1
 43 |     def get(self, index):
 44 |         if index < 0 or index >= self.size:
 45 |             return "error"
 46 |         return self.array[index]
 47 |     def set(self, index, value):
 48 |         if index < 0 or index >= self.size:
 49 |             return "error"
 50 |         self.array[index] = value
 51 |         return value
 52 |     def resize(self):
 53 |         self.capacity *= 2
 54 |         new_array = [None] * self.capacity
 55 |         for i in range(self.size):
 56 |             new_array[i] = self.array[i]
 57 |         self.array = new_array
 58 |     def remove_last(self):
 59 |         if self.size == 0:
 60 |             return "error"
 61 |         last = self.array[self.size - 1]
 62 |         self.size -= 1
 63 |         return last
 64 |     def get_last(self):
 65 |         if self.size == 0:
 66 |             return "error"
 67 |         return self.array[self.size - 1]
 68 |     def is_empty(self):
 69 |         return self.size == 0
 70 |     def remove_first(self):
 71 |         if self.size == 0:
 72 |             return "error"
 73 |         first = self.array[0]
 74 |         for i in range(1, self.size):
 75 |             self.array[i - 1] = self.array[i]
 76 |         self.size -= 1
 77 |         return first
 78 |     def get_first(self):
 79 |         if self.size == 0:
 80 |             return "error"
 81 |         return self.array[0]
 82 |     def is_empty(self):
 83 |         return self.size == 0
 84 | 
 85 | class Stack:               
 86 | 
 87 |     def __init__(self):
 88 |         self.array = DynamicArray()
 89 |     def push(self, element):
 90 |         self.array.append(element)
 91 |     def pop(self):
 92 |         if self.is_empty():
 93 |             return "error: stack is empty"
 94 |         return self.array.remove_last()
 95 | 
 96 |     def peek(self):
 97 |         if self.is_empty():
 98 |             return "error: stack is empty"
 99 |         return self.array.get_last()
100 |     def is_empty(self):
101 |         return self.array.is_empty()
102 | 
103 | 
104 | s = Stack()
105 | s.push(5)
106 | s.push(10)
107 | s.push(15)
108 | print(s.pop())    
109 | print(s.peek())   
110 | 
111 | 
112 | class Queue:
113 | 
114 |     def __init__(self):
115 |         self.array = DynamicArray()
116 |     def enqueue(self, element):
117 |         self.array.append(element)
118 |     def dequeue(self):
119 |         if self.is_empty():
120 |             return "error: queue is empty"
121 |         return self.array.remove_first()
122 |     def peek(self):
123 |         if self.is_empty():
124 |             return "error: queue is empty"
125 |         return self.array.get_first()
126 |     def is_empty(self):
127 |         return self.array.is_empty()
128 |     def display(self):
129 |         if self.is_empty():
130 |             print("Queue is empty")
131 |         else:
132 |             for i in range(self.array.size):
133 |                 print(self.array.get(i), end=' ')
134 |             print()
135 | 
136 | 
137 | q = Queue()
138 | q.enqueue(1)
139 | q.enqueue(2)
140 | q.enqueue(3)
141 | print(q.dequeue())  
142 | print(q.peek())     
143 | 
144 | def reverse_queue(q):
145 |     stack = Stack()
146 |     while not q.is_empty():
147 |         stack.push(q.dequeue())
148 |     while not stack.is_empty():
149 |         q.enqueue(stack.pop())
150 | 
151 | 
152 | q = Queue()
153 | q.enqueue(10)
154 | q.enqueue(20)
155 | q.enqueue(30)
156 | reverse_queue(q)
157 | q.display()


--------------------------------------------------------------------------------
/dsa.py:
--------------------------------------------------------------------------------
  1 | '''
  2 | stack = []
  3 | stack.append("aeroplane")
  4 | stack.append("banana")
  5 | stack.append("cat")
  6 | stack.append("dog")
  7 | print(stack)
  8 | stack.pop()
  9 | print(stack)
 10 | size = len(stack)
 11 | print(size)
 12 | peek = stack[-1]
 13 | print(peek)
 14 | if stack == []:
 15 |     print(True)
 16 | else:
 17 |     print(False)
 18 | print(stack)
 19 | class Stack:
 20 |     def __init__ (self):
 21 |         self.stack = []
 22 |     def push (self, element):
 23 |         self.stack.append(element)
 24 |     def pop(self):
 25 |         if self.stack == []:
 26 |             return "stack is empty"
 27 |         return self.stack.pop()
 28 |     def size(self):
 29 |         return len(self.stack)
 30 |     def peek(self):
 31 |         if self.stack == []:
 32 |             return "stack is empty"
 33 |         return self.stack[-1]
 34 |     def IsEmpty(self):
 35 |         if self.stack == []:
 36 |             return True
 37 |         else:
 38 |             return False
 39 | name = Stack()
 40 | name.push("Ali")
 41 | name.push("Zara")
 42 | name.push("Hassan")
 43 | name.push("Wali")
 44 | name.push("Nara")
 45 | print(name.stack)
 46 | name.pop()
 47 | print(name.stack)
 48 | print(name.pop())
 49 | print(name.stack)
 50 | name.push("Wali")
 51 | name.push("Nara")
 52 | print(name.stack)
 53 | print(name.pop())
 54 | print(name.stack)
 55 | print(name.IsEmpty())
 56 | print(name.stack)
 57 | print(name.peek())
 58 | print(name.stack)
 59 | print(name.size())
 60 | print('Vimsa_123')
 61 | def Parenthesis(s: str) -> bool:
 62 |     stack = []
 63 |     for symbol in s:
 64 |         if symbol == "[" or symbol == "{" or symbol == "(":
 65 |             stack.append(symbol)
 66 |         elif symbol == ")" and stack and stack[-1] == "(":
 67 |             stack.pop() 
 68 |         elif symbol == "]" and stack and stack[-1] == "[":
 69 |             stack.pop()
 70 |         elif symbol == "}" and stack and stack[-1] == "{":
 71 |             stack.pop()
 72 |         else:
 73 |             return False
 74 |     return not stack
 75 | print(Parenthesis("([{}])"))
 76 | print(Parenthesis("{}{}(){}"))
 77 | class TreeNode:
 78 |     def __init__(self, data):
 79 |         self.data = data
 80 |         self.left = None
 81 |         self.right = None
 82 | def preOrder(node):
 83 |     if node is None:
 84 |         return 
 85 |     print(node.data, end=", ")
 86 |     preOrder(node.left)
 87 |     preOrder(node.right)
 88 | root = TreeNode('R')
 89 | nodeA = TreeNode('A')
 90 | nodeB = TreeNode('B')
 91 | nodeC = TreeNode('C')
 92 | nodeD = TreeNode('D')
 93 | nodeE = TreeNode('E')
 94 | nodeF = TreeNode('F')
 95 | nodeG = TreeNode('G')
 96 | root.left = nodeA
 97 | root.right = nodeB
 98 | 
 99 | nodeA.left = nodeC
100 | nodeA.right = nodeD
101 | 
102 | nodeB.left = nodeE
103 | nodeB.right = nodeF
104 | 
105 | nodeF.left = nodeG
106 | 
107 | preOrder(root)
108 | class TreeNode:
109 | 
110 |     def __init__ (self, data):
111 |         self.data=data
112 |         self.left=None
113 |         self.right=None
114 | def preorder(node):
115 |     if node is None:
116 |         return
117 |     print(node.data, end=",")
118 |     preorder(node.left)
119 |     preorder(node.right)
120 | root = TreeNode(7)
121 | n1 = TreeNode(6)
122 | n7 = TreeNode(3)
123 | n2 = TreeNode(5)
124 | n3 = TreeNode(4)
125 | n4 = TreeNode(10)
126 | n5 = TreeNode(9)
127 | n6 = TreeNode(8)
128 | n8 = TreeNode(7)        
129 | root.left=n2
130 | root.right=n4
131 | n2.left=n1
132 | n2.right=n3
133 | n1.left=n7
134 | n2.left=n1
135 | n2.right=n3
136 | n4.left=n6
137 | n4.right=n5
138 | preorder(root)
139 | vimsa = [13, 2, 6, 3, 9, 10, 10]
140 | vimsa.append(11)
141 | print(vimsa)
142 | vimsa.sort()
143 | print(vimsa[0])
144 | ''''''
145 | class Node:
146 |     def __init__ (self, element):
147 |         self.element=element
148 |         self.next=None
149 | class Stack:
150 |     def __init__ (self):
151 |         self.head=None
152 |         self.size = []
153 |     def push(self, element):
154 |         new_node=Node(element)
155 |         if self.head:
156 |             new_node.next=self.head
157 |         self.head=new_node
158 |         self.size+=1
159 | class Node:
160 |     def __init__(self, element):
161 |         self.element = element
162 |         self.next= None
163 | node1=Node(8)
164 | node2=Node(9)
165 | node3=Node(5)
166 | node4=Node(17)
167 | 
168 | node1.next=node2
169 | node2.next=node3
170 | node3.next=node4
171 | node4.next=None
172 | 
173 | currentnode = node1
174 | while currentnode:
175 |     print(currentnode.element, end="->")
176 |     currentnode=currentnode.next
177 | print(None)
178 |   
179 | class Node:
180 |     def __init__ (self, element):
181 |         self.element = element
182 |         self.next = None
183 |         self.prev = None
184 | node1 = Node(11)
185 | node2 = Node(12)
186 | node3 = Node(13)
187 | node4 = Node(14)
188 | node5 = Node(15)
189 | node1.next = node2
190 | node2.next=node3
191 | node2.prev=node1
192 | node3.next=node4
193 | node3.prev=node2
194 | node4.next=node5
195 | node4.prev=node3
196 | node5.prev=node4
197 | currentnode = node1
198 | while currentnode:
199 |     print(currentnode.element, end="_>")
200 |     currentnode=currentnode.next
201 | print("none")
202 | currentnode = node4
203 | while currentnode:
204 |     print(currentnode.element, end="_>")
205 |     currentnode=currentnode.prev
206 | print("none")
207 | def trans(head):
208 |     currentNode = head
209 |     while currentNode:
210 |         print(currentNode.element, end=" -> ")
211 |         currentNode = currentNode.next
212 |     print("null")
213 | 
214 | def finflowest(head):
215 |     minvalue=head.element
216 |     currentnode=head.next
217 |     while currentnode:
218 |         if currentnode.element < minvalue :
219 |             minvalue=currentnode.element
220 |         currentnode=currentnode.next
221 |     return minvalue
222 | print(finflowest(node1))
223 | 
224 | def trans(head):
225 |     currentnode=head
226 |     while currentnode:
227 |         print(currentnode.element, end="_>")
228 |         currentnode=currentnode.next
229 |     print("none")
230 | trans(node1)
231 | 
232 | currentnode = node1
233 | currentnode = node1
234 | startnode=node1
235 | print(currentnode.element, end="_>")
236 | currentnode = currentnode.next
237 | #        self.next=None
238 |    #     self.prev=None
239 | node1.next = node2
240 | node2.next=node3
241 | node3.next=node4
242 | node4.next=node5
243 | class Node:
244 |     def __init__ (self, element):
245 |         self.element = element
246 |         self.left = None
247 |         self.right = None
248 | 
249 | 
250 | while currentnode != startnode:
251 |     print(currentnode.element, end="_>")
252 |     currentnode = currentnode.next
253 | print("...")
254 | binarytree=[1, 2, 3, 4, 4, None, 6, 7, None, None, 9]
255 | 
256 | def left_child_index(index):
257 |     return (2*index) + 1
258 | def right_child_index(index):
259 |     return (2*index) + 2
260 | def inorder(index):
261 |     if  index>=len(binarytree) or binarytree[index] is None :
262 |         return[]
263 |     return inorder(left_child_index(index)) + [binarytree[index]] + inorder(right_child_index(index))
264 |     if node is None:
265 |         return
266 |     inorder(node.left)
267 |     print(node.element, end="_>")
268 |     inorder(node.right)
269 | 
270 | def preorder(index):
271 |     if index>=len(binarytree) or binarytree[index] is None :
272 |         return []
273 |     return [binarytree[index]] + preorder(left_child_index(index)) + preorder(right_child_index(index))
274 | def postorder(index):
275 |     if  index>=len(binarytree) or binarytree[index] is None:
276 |          return []
277 |     return preorder(left_child_index(index)) + preorder(right_child_index(index)) + [binarytree[index]]
278 | print(preorder(0))
279 | print(inorder(0))
280 | print(postorder(0))
281 | 
282 | root = Node(1)
283 | node1 = Node(11)
284 | node2 = Node(12)
285 | node3 = Node(13)
286 | node4 = Node(14)
287 | node5 = Node(15)
288 | root.left=node4
289 | root.right=node2
290 | node2.left=node1
291 | node4.left=node3
292 | node4.right=node5
293 | inorder(root)
294 | class TreeNode:
295 | 
296 |     def  __init__(self, element):
297 |         self.element = element
298 |         self.left=None
299 |         self.right = None
300 | 
301 | def search(node, target):
302 |     if node is None:
303 |         return []
304 |     elif node.element==target:
305 |         return node
306 |     elif node.element < target:
307 |         return search(node.right, target)
308 |     else:
309 |         return search(node.left, target)
310 | root = TreeNode(13)
311 | node7 = TreeNode(7)
312 | node15 = TreeNode(15)
313 | node3 = TreeNode(3)
314 | node8 = TreeNode(8)
315 | node14 = TreeNode(14)
316 | node19 = TreeNode(19)
317 | node18 = TreeNode(18)
318 | 
319 | root.left = node7
320 | root.right = node15
321 | 
322 | node7.left = node3
323 | node7.right = node8
324 | 
325 | node15.left = node14
326 | node15.right = node19
327 | 
328 | node19.left = node18
329 | 
330 | result = search(root, 5)
331 | if result:
332 |     print(f" Found:  {result.element} ")
333 | else:
334 |         print( "not found")
335 | '''
336 | '''
337 | x=int(input("enter search: "))
338 | result = search(root, x)
339 | if result:
340 |     print( f"node is found: {result.element}")
341 | else:
342 |     print("not found")
343 |     
344 | def search(node, target):
345 |     if node is None:
346 |         return []
347 |     elif node.element == target:
348 |         return node
349 |     elif node.element > target:
350 |         return search(node.left, target)
351 |     else:
352 |         return search(node.right, target)
353 | ''''''
354 | # again practice
355 | class TreeNode:
356 | 
357 |     def __init__(self, element):
358 |         self.element=element
359 |         self.left=None
360 |         self.right=None
361 | def inorder(node):
362 |     if node is None:
363 |         return 
364 |     inorder(node.left)
365 |     print(node.element, end=",")
366 |     inorder(node.right)
367 | 
368 | root = TreeNode(13)
369 | node7 = TreeNode(7)
370 | node15 = TreeNode(15)
371 | node3 = TreeNode(3)
372 | node8 = TreeNode(8)
373 | node14 = TreeNode(14)
374 | node19 = TreeNode(19)
375 | node18 = TreeNode(18)
376 | 
377 | root.left = node7
378 | root.right = node15
379 | 
380 | node7.left = node3
381 | node7.right = node8
382 | 
383 | node15.left = node14
384 | node15.right = node19
385 | 
386 | node19.left = node18
387 | inorder(root)
388 | '''
389 | '''
390 | def findmin(node):
391 |         curr = node
392 |         while curr.left is not None:
393 |             curr = curr.left
394 |         return curr
395 | 
396 | print(findmin(root).element)
397 | '''
398 | '''
399 | def insert(node, element):
400 |     if node is None:
401 |         return TreeNode(element)
402 |     else:
403 |         if element < node.element:
404 |             node.left = insert(node.left, element)
405 |         elif element>node.element:
406 |             node.right = insert(node.right, element)
407 |     return node
408 | 
409 | insert(root, 10)
410 | '''
411 | 
412 | class Node:
413 |     def __init__ (self, element):
414 |         self.element=element
415 |         self.left=None
416 |         self.right = None
417 | def insert(node, element):
418 |     if node is None:
419 |         return Node(element)
420 |     else:
421 |         if element > node.element:
422 |             node.right = insert(node.left, element)
423 |         else:
424 |             node.left = insert(node.left, element)
425 |     return node
426 | root = Node(30)
427 | insert(root, 50))
428 | insert(root, 30)
429 | insert(root, 70)
430 | 
431 | '''
432 | 
433 | ### ✅ 1. **Binary Trees**
434 | 
435 | #### 🔹Concept:
436 | 
437 | A Binary Tree is a tree where each node has **at most 2 children** (left and right).
438 | 
439 | #### 🔹Types:
440 | 
441 | * **Binary Search Tree (BST)**: Left child < Node < Right child
442 | * **Full Binary Tree**: Every node has 0 or 2 children
443 | * **Complete Binary Tree**: All levels are full except possibly last
444 | 
445 | #### 🔹Common Operations:
446 | 
447 | * Insertion
448 | * Traversal (in-order, pre-order, post-order)
449 | 
450 | #### ✅ BST Insert & In-Order Traversal:
451 | 
452 | ```python
453 | class Node:
454 |     def __init__(self, value):
455 |         self.value = value
456 |         self.left = None
457 |         self.right = None
458 | 
459 | class BinaryTree:
460 |     def __init__(self):
461 |         self.root = None
462 | 
463 |     def insert(self, value):
464 |         if self.root is None:
465 |             self.root = Node(value)
466 |             return
467 |         current = self.root
468 |         while True:
469 |             if value < current.value:
470 |                 if current.left is None:
471 |                     current.left = Node(value)
472 |                     return
473 |                 current = current.left
474 |             else:
475 |                 if current.right is None:
476 |                     current.right = Node(value)
477 |                     return
478 |                 current = current.right
479 | 
480 |     def in_order(self):  # Left, Root, Right
481 |         def traverse(node):
482 |             if node:
483 |                 traverse(node.left)
484 |                 print(node.value, end=' ')
485 |                 traverse(node.right)
486 |         traverse(self.root)
487 | ```
488 | 
489 | ---
490 | 
491 | ### ✅ 2. **Linked List**
492 | 
493 | #### 🔹Concept:
494 | 
495 | A linear data structure where each element (node) points to the next.
496 | 
497 | #### 🔹Types:
498 | 
499 | * Singly Linked List
500 | * Doubly Linked List
501 | * Circular Linked List
502 | 
503 | #### ✅ Singly Linked List:
504 | 
505 | ```python
506 | class Node:
507 |     def __init__(self, data):
508 |         self.data = data
509 |         self.next = None
510 | 
511 | class LinkedList:
512 |     def __init__(self):
513 |         self.head = None
514 | 
515 |     def insert_end(self, data):
516 |         new = Node(data)
517 |         if not self.head:
518 |             self.head = new
519 |             return
520 |         current = self.head
521 |         while current.next:
522 |             current = current.next
523 |         current.next = new
524 | 
525 |     def display(self):
526 |         current = self.head
527 |         while current:
528 |             print(current.data, end=' -> ')
529 |             current = current.next
530 |         print("None")
531 | ```
532 | 
533 | ---
534 | 
535 | ### ✅ 3. **Sorting Algorithms**
536 | 
537 | | Algorithm   | Time (Best) | Time (Worst) | Space    | Stable |
538 | | ----------- | ----------- | ------------ | -------- | ------ |
539 | | Bubble Sort | O(n)        | O(n²)        | O(1)     | Yes    |
540 | | Selection   | O(n²)       | O(n²)        | O(1)     | No     |
541 | | Insertion   | O(n)        | O(n²)        | O(1)     | Yes    |
542 | | Merge Sort  | O(n log n)  | O(n log n)   | O(n)     | Yes    |
543 | | Quick Sort  | O(n log n)  | O(n²)        | O(log n) | No     |
544 | 
545 | #### ✅ Bubble Sort:
546 | 
547 | ```python
548 | def bubble_sort(arr):
549 |     n = len(arr)
550 |     for i in range(n):
551 |         for j in range(0, n - i - 1):
552 |             if arr[j] > arr[j + 1]:
553 |                 arr[j], arr[j+1] = arr[j+1], arr[j]
554 | ```
555 | 
556 | ---
557 | 
558 | ### ✅ 4. **Hashing**
559 | 
560 | #### 🔹Concept:
561 | 
562 | Storing values using a **key**, very fast lookups.
563 | 
564 | #### ✅ Simple Hash Table (with chaining):
565 | 
566 | ```python
567 | class HashTable:
568 |     def __init__(self, size):
569 |         self.size = size
570 |         self.table = [[] for _ in range(size)]
571 | 
572 |     def hash_function(self, key):
573 |         return key % self.size
574 | 
575 |     def insert(self, key):
576 |         index = self.hash_function(key)
577 |         self.table[index].append(key)
578 | 
579 |     def display(self):
580 |         for i, slot in enumerate(self.table):
581 |             print(i, ":", slot)
582 | ```
583 | 
584 | ---
585 | 
586 | ### ✅ 5. **Heap**
587 | 
588 | #### 🔹Concept:
589 | 
590 | A binary tree where:
591 | 
592 | * **Min Heap**: Parent <= Children
593 | * **Max Heap**: Parent >= Children
594 | 
595 | Used in **priority queues** and **heap sort**.
596 | 
597 | #### ✅ Min Heap (using heapq module):
598 | 
599 | ```python
600 | import heapq
601 | 
602 | arr = [3, 1, 4, 1, 5]
603 | heapq.heapify(arr)  # Creates min-heap
604 | heapq.heappush(arr, 2)
605 | print(heapq.heappop(arr))  # Removes smallest
606 | ```
607 | 
608 | ---
609 | 
610 | ### ✅ 6. **Huffman’s Theorem (Huffman Coding)**
611 | 
612 | #### 🔹Concept:
613 | 
614 | Used for **data compression**. Greedy algorithm.
615 | 
616 | 1. Build min-heap from frequency table
617 | 2. Remove two smallest items
618 | 3. Combine and push back
619 | 4. Repeat until one tree is left
620 | 
621 | #### ✅ Huffman Coding Concept Example:
622 | 
623 | Characters with frequencies:
624 | A:5, B:9, C:12, D:13, E:16, F:45
625 | 
626 | You merge smallest 2 repeatedly and build a tree. Each left edge is `0`, right is `1`. Leaf to root gives binary code.
627 | 
628 | Actual coding is complex — but **understand concept and steps**.
629 | 
630 | ---
631 | 
632 | ### ✅ Exam Tips:
633 | 
634 | | Topic       | What They Might Ask              |
635 | | ----------- | -------------------------------- |
636 | | Binary Tree | Insert, Traversal (code/write)   |
637 | | Linked List | Insert/Delete/Traverse           |
638 | | Sorting     | Write or trace bubble/quick      |
639 | | Hashing     | Hashing function, chaining       |
640 | | Heap        | Insert/Delete, min-heap logic    |
641 | | Huffman     | Steps to build tree, frequencies |
642 | 
643 | ---
644 | 
645 | ### 🧠 Pro Tips:
646 | 
647 | * Practice writing code by hand!
648 | * For sorting, focus on Bubble, Selection, Insertion
649 | * For Huffman, just **learn the algorithm steps** — no need to memorize code
650 | * Use Python or C++ based on your exam requirement
651 | 
652 | ---
653 | 
654 | Want me to give you **MCQs**, **coding practice questions**, or a **revision sheet** for each topic?
655 | '''
656 | 
657 | 
658 | 
659 | 
660 | 
661 | 
662 | 
663 | 
664 | 
665 | 
666 | 


--------------------------------------------------------------------------------
/Assignment # 1_2 DSA.py:
--------------------------------------------------------------------------------
  1 | # Task 1
  2 | 
  3 | def get_priority(operator):
  4 | 
  5 |     if operator == '^':
  6 | 
  7 |         return 3
  8 | 
  9 |     elif operator in ('*', '/', '%'):
 10 | 
 11 |         return 2
 12 | 
 13 |     elif operator in ('+', '-'):
 14 | 
 15 |         return 1
 16 | 
 17 |     else:
 18 | 
 19 |         return 0
 20 | 
 21 | 
 22 | def convert_to_postfix(expression):
 23 | 
 24 |     stack = []
 25 |     result = []
 26 | 
 27 |     for ch in expression:
 28 | 
 29 |         if ch.isdigit():
 30 | 
 31 |             result.append(ch)
 32 | 
 33 |         elif ch == '(':
 34 | 
 35 |             stack.append(ch)
 36 | 
 37 |         elif ch == ')':
 38 | 
 39 |             while stack and stack[-1] != '(':
 40 |                 result.append(stack.pop())
 41 |             stack.pop()
 42 | 
 43 |         elif ch in '+-*/%^':
 44 | 
 45 |             while stack and get_priority(stack[-1]) >= get_priority(ch):
 46 |                 result.append(stack.pop())
 47 |             stack.append(ch)
 48 | 
 49 |     while stack:
 50 | 
 51 |         result.append(stack.pop())
 52 | 
 53 |     return result
 54 | 
 55 | def solve_postfix(postfix):
 56 | 
 57 |     numbers = []
 58 | 
 59 |     for item in postfix:
 60 | 
 61 |         if item.isdigit():
 62 |             numbers.append(int(item))
 63 | 
 64 |         else:
 65 | 
 66 |             b = numbers.pop()
 67 |             a = numbers.pop()
 68 | 
 69 |             if item == '+':
 70 | 
 71 |                 numbers.append(a + b)
 72 | 
 73 |             elif item == '-':
 74 | 
 75 |                 numbers.append(a - b)
 76 | 
 77 |             elif item == '*':
 78 | 
 79 |                 numbers.append(a * b)
 80 | 
 81 |             elif item == '/':
 82 | 
 83 |                 numbers.append(a / b)
 84 | 
 85 |             elif item == '%':
 86 | 
 87 |                 numbers.append(a % b)
 88 | 
 89 |             elif item == '^':
 90 | 
 91 |                 numbers.append(a ** b)
 92 | 
 93 |     return numbers[0]
 94 | 
 95 | 
 96 | def start_calculator():
 97 | 
 98 |     while True:
 99 | 
100 |         user_input = input("Enter expression to evaluate or a clr to quit:\n")
101 | 
102 |         if user_input.strip() == 'clr':
103 | 
104 |             print("Goodbye!")
105 |             break
106 | 
107 |         clean_input = user_input.replace(' ', '').replace('=', '')
108 |         postfix = convert_to_postfix(clean_input)
109 |         result = solve_postfix(postfix)
110 | 
111 |         print("Postfix Expression:", ' '.join(postfix))
112 |         print("Result =", result)
113 | 
114 | start_calculator()
115 | 
116 | # Task 2
117 | 
118 | class Queue:
119 | 
120 |     def __init__(self, max_size):
121 | 
122 |         self.items = []
123 |         self.max_size = max_size
124 | 
125 |     def enqueue(self, char):
126 | 
127 |         if not self.is_full():
128 | 
129 |             self.items.append(char)
130 | 
131 |         else:
132 | 
133 |             print("Queue is full. Cannot add more items.")
134 | 
135 | 
136 |     def dequeue(self):
137 | 
138 |         if not self.is_empty():
139 | 
140 |             return self.items.pop(0)
141 | 
142 |         else:
143 | 
144 |             print("Queue is empty.")
145 | 
146 |             return None
147 | 
148 | 
149 |     def front(self):
150 | 
151 |         if not self.is_empty():
152 | 
153 |             return self.items[0]
154 | 
155 |         else:
156 | 
157 |             print("Queue is empty.")
158 |             return None
159 | 
160 |     def is_empty(self):
161 | 
162 |         return len(self.items) == 0
163 | 
164 |     def is_full(self):
165 | 
166 |         return len(self.items) == self.max_size
167 | 
168 |     def get_size(self):
169 | 
170 |         return len(self.items)
171 | 
172 |     def print_queue(self):
173 | 
174 |         print("Queue:", self.items)
175 | 
176 | class Stack:
177 | 
178 |     def __init__(self):
179 | 
180 |         self.items = []
181 | 
182 |     def push(self, item):
183 | 
184 |         self.items.append(item)
185 | 
186 |     def pop(self):
187 | 
188 |         if not self.is_empty():
189 | 
190 |             return self.items.pop()
191 | 
192 |         else:
193 | 
194 |             print("Stack is empty.")
195 |             return None
196 | 
197 |     def is_empty(self):
198 | 
199 |         return len(self.items) == 0
200 | 
201 | def reverse_queue(queue):
202 | 
203 |     stack = Stack()
204 | 
205 |     while not queue.is_empty():
206 | 
207 |         stack.push(queue.dequeue())
208 | 
209 |     while not stack.is_empty():
210 | 
211 |         queue.enqueue(stack.pop())
212 | 
213 |     print("Queue after reversing:")
214 |     queue.print_queue()
215 | 
216 | def menu():
217 | 
218 |     max_size = int(input("Enter maximum size of the queue: "))
219 |     queue = Queue(max_size)
220 | 
221 |     while True:
222 | 
223 |         print("\n--- Queue Menu ---")
224 |         print("1. Enqueue (Add item)")
225 |         print("2. Dequeue (Remove item)")
226 |         print("3. Show Front item")
227 |         print("4. Check if Queue is Empty")
228 |         print("5. Check if Queue is Full")
229 |         print("6. Get Queue Size")
230 |         print("7. Print Queue")
231 |         print("8. Reverse Queue")
232 |         print("9. Exit")
233 | 
234 |         choice = input("Enter your choice (1-9): ")
235 | 
236 |         if choice == '1':
237 | 
238 |             char = input("Enter a character to add: ")
239 |             queue.enqueue(char)
240 | 
241 |         elif choice == '2':
242 | 
243 |             removed = queue.dequeue()
244 |             if removed is not None:
245 | 
246 |                 print("Removed:", removed)
247 | 
248 |         elif choice == '3':
249 | 
250 |             front = queue.front()
251 |             if front is not None:
252 | 
253 |                 print("Front item:", front)
254 | 
255 |         elif choice == '4':
256 | 
257 |             print("Queue is empty?", queue.is_empty())
258 | 
259 |         elif choice == '5':
260 | 
261 |             print("Queue is full?", queue.is_full())
262 | 
263 |         elif choice == '6':
264 | 
265 |             print("Current size:", queue.get_size())
266 | 
267 |         elif choice == '7':
268 | 
269 |             queue.print_queue()
270 | 
271 |         elif choice == '8':
272 | 
273 |             reverse_queue(queue)
274 | 
275 |         elif choice == '9':
276 | 
277 |             print("Exiting program.")
278 | 
279 |             break
280 | 
281 |         else:
282 | 
283 |             print("Invalid choice. Please try again.")
284 | 
285 | menu()
286 | 
287 | # Task 3
288 | 
289 | class Deque:
290 | 
291 |     def __init__(self):
292 | 
293 |         self.items = []
294 | 
295 | 
296 |     def enqueue_right(self, item):
297 | 
298 |         self.items.append(item)
299 | 
300 | 
301 |     def enqueue_left(self, item):
302 | 
303 |         self.items.insert(0, item)
304 | 
305 | 
306 |     def dequeue_right(self):
307 | 
308 |         if not self.is_empty():
309 | 
310 |             return self.items.pop()
311 | 
312 |         else:
313 | 
314 |             print("Deque is empty.")
315 |             return None
316 | 
317 |     def dequeue_left(self):
318 | 
319 |         if not self.is_empty():
320 | 
321 |             return self.items.pop(0)
322 | 
323 |         else:
324 | 
325 |             print("Deque is empty.")
326 | 
327 |             return None
328 | 
329 |     def is_empty(self):
330 | 
331 |         return len(self.items) == 0
332 | 
333 |     def display(self):
334 | 
335 |         print("Deque:", self.items)
336 | 
337 | def input_restricted_menu():
338 | 
339 |     dq = Deque()
340 | 
341 |     while True:
342 | 
343 |         print("\n--- Input Restricted Deque ---")
344 |         print("1. Enqueue (Add item at right)")
345 |         print("2. Dequeue Right (Remove from rear)")
346 |         print("3. Dequeue Left (Remove from front)")
347 |         print("4. Display")
348 |         print("5. Exit")
349 | 
350 |         choice = input("Enter your choice: ")
351 | 
352 |         if choice == '1':
353 | 
354 |             item = input("Enter item to enqueue: ")
355 |             dq.enqueue_right(item)
356 | 
357 |         elif choice == '2':
358 | 
359 |             removed = dq.dequeue_right()
360 | 
361 |             if removed is not None:
362 | 
363 |                 print("Removed from right:", removed)
364 | 
365 |         elif choice == '3':
366 | 
367 |             removed = dq.dequeue_left()
368 | 
369 |             if removed is not None:
370 | 
371 |                 print("Removed from left:", removed)
372 | 
373 |         elif choice == '4':
374 | 
375 |             dq.display()
376 | 
377 |         elif choice == '5':
378 | 
379 |             print("Exiting Input Restricted Deque.")
380 | 
381 |             break
382 | 
383 |         else:
384 | 
385 |             print("Invalid choice. Try again.")
386 | 
387 | 
388 | 
389 | def output_restricted_menu():
390 | 
391 |     dq = Deque()
392 | 
393 |     while True:
394 | 
395 |         print("\n--- Output Restricted Deque ---")
396 | 
397 |         print("1. Enqueue Right (Add at end)")
398 | 
399 |         print("2. Enqueue Left (Add at front)")
400 | 
401 |         print("3. Dequeue (Remove from front only)")
402 | 
403 |         print("4. Display")
404 | 
405 |         print("5. Exit")
406 | 
407 | 
408 | 
409 |         choice = input("Enter your choice: ")
410 | 
411 | 
412 | 
413 |         if choice == '1':
414 | 
415 |             item = input("Enter item to enqueue at right: ")
416 | 
417 |             dq.enqueue_right(item)
418 | 
419 |         elif choice == '2':
420 | 
421 |             item = input("Enter item to enqueue at left: ")
422 | 
423 |             dq.enqueue_left(item)
424 | 
425 |         elif choice == '3':
426 | 
427 |             removed = dq.dequeue_left()
428 | 
429 |             if removed is not None:
430 | 
431 |                 print("Removed from left:", removed)
432 | 
433 |         elif choice == '4':
434 | 
435 |             dq.display()
436 | 
437 |         elif choice == '5':
438 | 
439 |             print("Exiting Output Restricted Deque.")
440 | 
441 |             break
442 | 
443 |         else:
444 | 
445 |             print("Invalid choice. Try again.")
446 | 
447 | 
448 | 
449 | def main_menu():
450 | 
451 |     while True:
452 | 
453 |         print("\nChoose Deque Type:")
454 | 
455 |         print("1. Input Restricted Deque")
456 | 
457 |         print("2. Output Restricted Deque")
458 | 
459 |         print("3. Exit")
460 | 
461 | 
462 |         choice = input("Enter your choice: ")
463 | 
464 | 
465 | 
466 |         if choice == '1':
467 | 
468 |             input_restricted_menu()
469 | 
470 |         elif choice == '2':
471 | 
472 |             output_restricted_menu()
473 | 
474 |         elif choice == '3':
475 | 
476 |             print("Exiting program.")
477 | 
478 |             break
479 | 
480 |         else:
481 | 
482 |             print("Invalid choice. Try again.")
483 | 
484 | 
485 | 
486 | main_menu()
487 | 
488 | 
489 | # Task 4
490 | 
491 | 
492 | class CricketerNode:
493 | 
494 |     def __init__(self, name):
495 | 
496 |         self.name = name
497 |         self.next = self.prev = self
498 | 
499 | class CricketerList:
500 | 
501 |     def __init__(self):
502 | 
503 |         self.head = None
504 | 
505 |     def add_cricketer(self, name):
506 | 
507 |         if self.find_cricketer(name):
508 | 
509 |             print(f"Cricketer {name} already exists.")
510 |             return
511 | 
512 |         new_node = CricketerNode(name)
513 | 
514 |         if not self.head:
515 | 
516 |             self.head = new_node
517 | 
518 |         else:
519 | 
520 |             tail = self.head.prev
521 |             tail.next = new_node
522 |             new_node.prev = tail
523 |             new_node.next = self.head
524 | 
525 |             self.head.prev = new_node
526 | 
527 |         print(f"Added cricketer {name}")
528 | 
529 |     def delete_cricketer(self, name):
530 | 
531 |         node = self.find_cricketer(name)
532 | 
533 |         if not node:
534 | 
535 |             print(f"Cricketer {name} not found.")
536 |             return False
537 | 
538 |         if node.next == node:
539 | 
540 |             self.head = None
541 | 
542 |         else:
543 | 
544 |             node.prev.next = node.next
545 |             node.next.prev = node.prev
546 | 
547 |             if self.head == node:
548 | 
549 |                 self.head = node.next
550 | 
551 |         print(f"Deleted cricketer {name}")
552 |         return True
553 | 
554 |     def find_cricketer(self, name):
555 | 
556 |         if not self.head:
557 | 
558 |             return None
559 | 
560 |         current = self.head
561 | 
562 |         while True:
563 | 
564 |             if current.name == name:
565 | 
566 |                 return current
567 | 
568 |             current = current.next
569 |             if current == self.head:
570 | 
571 |                 break
572 | 
573 |         return None
574 | 
575 |     def print_cricketers(self):
576 | 
577 |         if not self.head:
578 | 
579 |             print("No cricketers")
580 |             return
581 | 
582 |         current = self.head
583 |         names = []
584 | 
585 |         while True:
586 | 
587 |             names.append(current.name)
588 |             current = current.next
589 | 
590 |             if current == self.head:
591 | 
592 |                 break
593 | 
594 |         print(", ".join(names))
595 | 
596 | class MatchNode:
597 | 
598 |     def __init__(self, match_id, team1_name, team2_name, date, winner, location):
599 | 
600 |         self.match_id = match_id
601 |         self.team1_name = team1_name
602 |         self.team2_name = team2_name
603 |         self.date = date
604 |         self.winner = winner
605 |         self.location = location
606 |         self.team1_cricketers = CricketerList()
607 |         self.team2_cricketers = CricketerList()
608 |         self.next = self.prev = self
609 | 
610 | class MatchList:
611 | 
612 |     def __init__(self):
613 | 
614 |         self.head = None
615 | 
616 |     def _match_id_key(self, match_id):
617 | 
618 |         prefix = ''.join(filter(str.isalpha, match_id))
619 |         nums = ''.join(filter(lambda x: x.isdigit() or x == '-', match_id))
620 |         parts = nums.split('-')
621 | 
622 |         return (prefix, int(parts[0]), int(parts[1]))
623 | 
624 |     def add_match(self, match_id, team1_name, team2_name, date, winner, location):
625 | 
626 |         if self.find_match(match_id):
627 | 
628 |             print(f"Match {match_id} already exists.")
629 |             return
630 | 
631 |         new_node = MatchNode(match_id, team1_name, team2_name, date, winner, location)
632 | 
633 |         if not self.head:
634 | 
635 |             self.head = new_node
636 |             print(f"Added match {match_id} as the first match.")
637 |             return
638 | 
639 |         current = self.head
640 |         new_key = self._match_id_key(match_id)
641 | 
642 |         while True:
643 | 
644 |             current_key = self._match_id_key(current.match_id)
645 | 
646 |             if new_key < current_key:
647 |                 prev_node = current.prev
648 | 
649 |                 prev_node.next = new_node
650 |                 new_node.prev = prev_node
651 | 
652 |                 new_node.next = current
653 |                 current.prev = new_node
654 | 
655 |                 if current == self.head:
656 | 
657 |                     self.head = new_node
658 | 
659 |                 print(f"Inserted match {match_id} before {current.match_id}")
660 |                 return
661 | 
662 |             current = current.next
663 | 
664 |             if current == self.head:
665 |                 break
666 | 
667 |         tail = self.head.prev
668 |         tail.next = new_node
669 |         new_node.prev = tail
670 |         new_node.next = self.head
671 |         self.head.prev = new_node
672 |         print(f"Added match {match_id} at the end.")
673 | 
674 |     def delete_match(self, match_id):
675 | 
676 |         node = self.find_match(match_id)
677 | 
678 |         if not node:
679 | 
680 |             print(f"Match {match_id} not found.")
681 |             return False
682 | 
683 |         if node.next == node:  
684 | 
685 |             self.head = None
686 | 
687 |         else:
688 | 
689 |             node.prev.next = node.next
690 |             node.next.prev = node.prev
691 | 
692 |             if self.head == node:
693 | 
694 |                 self.head = node.next
695 | 
696 |         print(f"Deleted match {match_id}")
697 |         return True
698 | 
699 |     def find_match(self, match_id):
700 | 
701 |         if not self.head:
702 | 
703 |             return None
704 | 
705 |         current = self.head
706 |         while True:
707 | 
708 |             if current.match_id == match_id:
709 | 
710 |                 return current
711 | 
712 |             current = current.next
713 | 
714 |             if current == self.head:
715 | 
716 |                 break
717 | 
718 |         return None
719 | 
720 |     def print_matches(self):
721 | 
722 |         if not self.head:
723 | 
724 |             print("No matches available.")
725 |             return
726 |     
727 |         current = self.head
728 |     
729 |         while True:
730 |     
731 |             print(f"Match ID: {current.match_id}")
732 |             print(f" Date: {current.date}")
733 |             print(f" Location: {current.location}")
734 |             print(f" Winner: {current.winner}")
735 |             print(f" Team 1: {current.team1_name} - Players: ", end='')
736 |             current.team1_cricketers.print_cricketers()
737 |             print(f" Team 2: {current.team2_name} - Players: ", end='')
738 |             current.team2_cricketers.print_cricketers()
739 |             print("-" * 30)
740 |             current = current.next
741 |             if current == self.head:
742 |                 break
743 | 
744 |     def add_cricketer_to_match(self, match_id, team_number, cricketer_name):
745 |     
746 |         match = self.find_match(match_id)
747 |     
748 |         if not match:
749 |     
750 |             print(f"Match {match_id} not found.")
751 |             return
752 |     
753 |         if team_number == 1:
754 |     
755 |             match.team1_cricketers.add_cricketer(cricketer_name)
756 |     
757 |         elif team_number == 2:
758 |     
759 |             match.team2_cricketers.add_cricketer(cricketer_name)
760 |     
761 |         else:
762 |     
763 |             print("Invalid team number. Use 1 or 2.")
764 | 
765 |     def delete_cricketer_from_match(self, match_id, team_number, cricketer_name):
766 |     
767 |         match = self.find_match(match_id)
768 |         if not match:
769 |     
770 |             print(f"Match {match_id} not found.")
771 |             return
772 |     
773 |         if team_number == 1:
774 |     
775 |             match.team1_cricketers.delete_cricketer(cricketer_name)
776 |     
777 |         elif team_number == 2:
778 |     
779 |             match.team2_cricketers.delete_cricketer(cricketer_name)
780 |     
781 |         else:
782 |     
783 |             print("Invalid team number. Use 1 or 2.")
784 | 
785 |     def find_matches_by_cricketer(self, cricketer_name):
786 |     
787 |         result_list = MatchList()
788 |     
789 |         if not self.head:
790 |     
791 |             return result_list
792 |     
793 |         current = self.head
794 |     
795 |         while True:
796 |     
797 |             team1_found = current.team1_cricketers.find_cricketer(cricketer_name)
798 |             team2_found = current.team2_cricketers.find_cricketer(cricketer_name)
799 |     
800 |             if team1_found or team2_found:
801 |                 
802 |                 result_list.add_match(
803 |                     current.match_id,
804 |                     current.team1_name,
805 |                     current.team2_name,
806 |                     current.date,
807 |                     current.winner,
808 |                     current.location
809 |                 )
810 |            
811 |             current = current.next
812 |            
813 |             if current == self.head:
814 |            
815 |                 break
816 |      
817 |         return result_list
818 | 
819 | 
820 | 
821 | db = MatchList()
822 | db.add_match("PSL1-1", "Team1", "Team2", "2/2/2023", "Team2", "Pakistan")
823 | db.add_match("PSL1-4", "TeamA", "TeamB", "3/3/2023", "TeamA", "UAE")
824 | db.add_match("PSL1-2", "TeamX", "TeamY", "4/4/2023", "TeamY", "India")
825 | db.add_cricketer_to_match("PSL1-1", 1, "Cricketer1")
826 | db.add_cricketer_to_match("PSL1-1", 1, "Cricketer2")
827 | db.add_cricketer_to_match("PSL1-1", 1, "Cricketer3")
828 | db.add_cricketer_to_match("PSL1-1", 2, "Rizwan")
829 | db.add_cricketer_to_match("PSL1-1", 2, "Babar")
830 | db.add_cricketer_to_match("PSL1-1", 2, "Fakhar")
831 | 
832 | print("\nAll matches:")
833 | 
834 | db.print_matches()
835 | 
836 | print("\nMatches played by 'Babar':")
837 | 
838 | matches_with_babar = db.find_matches_by_cricketer("Babar")
839 | matches_with_babar.print_matches()
840 | 


--------------------------------------------------------------------------------

