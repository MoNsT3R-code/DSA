'''
stack = []
stack.append("aeroplane")
stack.append("banana")
stack.append("cat")
stack.append("dog")
print(stack)
stack.pop()
print(stack)
size = len(stack)
print(size)
peek = stack[-1]
print(peek)
if stack == []:
    print(True)
else:
    print(False)
print(stack)
class Stack:
    def __init__ (self):
        self.stack = []
    def push (self, element):
        self.stack.append(element)
    def pop(self):
        if self.stack == []:
            return "stack is empty"
        return self.stack.pop()
    def size(self):
        return len(self.stack)
    def peek(self):
        if self.stack == []:
            return "stack is empty"
        return self.stack[-1]
    def IsEmpty(self):
        if self.stack == []:
            return True
        else:
            return False
name = Stack()
name.push("Ali")
name.push("Zara")
name.push("Hassan")
name.push("Wali")
name.push("Nara")
print(name.stack)
name.pop()
print(name.stack)
print(name.pop())
print(name.stack)
name.push("Wali")
name.push("Nara")
print(name.stack)
print(name.pop())
print(name.stack)
print(name.IsEmpty())
print(name.stack)
print(name.peek())
print(name.stack)
print(name.size())
print('Vimsa_123')
def Parenthesis(s: str) -> bool:
    stack = []
    for symbol in s:
        if symbol == "[" or symbol == "{" or symbol == "(":
            stack.append(symbol)
        elif symbol == ")" and stack and stack[-1] == "(":
            stack.pop() 
        elif symbol == "]" and stack and stack[-1] == "[":
            stack.pop()
        elif symbol == "}" and stack and stack[-1] == "{":
            stack.pop()
        else:
            return False
    return not stack
print(Parenthesis("([{}])"))
print(Parenthesis("{}{}(){}"))
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def preOrder(node):
    if node is None:
        return 
    print(node.data, end=", ")
    preOrder(node.left)
    preOrder(node.right)
root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')
root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

preOrder(root)
class TreeNode:

    def __init__ (self, data):
        self.data=data
        self.left=None
        self.right=None
def preorder(node):
    if node is None:
        return
    print(node.data, end=",")
    preorder(node.left)
    preorder(node.right)
root = TreeNode(7)
n1 = TreeNode(6)
n7 = TreeNode(3)
n2 = TreeNode(5)
n3 = TreeNode(4)
n4 = TreeNode(10)
n5 = TreeNode(9)
n6 = TreeNode(8)
n8 = TreeNode(7)        
root.left=n2
root.right=n4
n2.left=n1
n2.right=n3
n1.left=n7
n2.left=n1
n2.right=n3
n4.left=n6
n4.right=n5
preorder(root)
vimsa = [13, 2, 6, 3, 9, 10, 10]
vimsa.append(11)
print(vimsa)
vimsa.sort()
print(vimsa[0])
''''''
class Node:
    def __init__ (self, element):
        self.element=element
        self.next=None
class Stack:
    def __init__ (self):
        self.head=None
        self.size = []
    def push(self, element):
        new_node=Node(element)
        if self.head:
            new_node.next=self.head
        self.head=new_node
        self.size+=1
class Node:
    def __init__(self, element):
        self.element = element
        self.next= None
node1=Node(8)
node2=Node(9)
node3=Node(5)
node4=Node(17)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=None

currentnode = node1
while currentnode:
    print(currentnode.element, end="->")
    currentnode=currentnode.next
print(None)
  
class Node:
    def __init__ (self, element):
        self.element = element
        self.next = None
        self.prev = None
node1 = Node(11)
node2 = Node(12)
node3 = Node(13)
node4 = Node(14)
node5 = Node(15)
node1.next = node2
node2.next=node3
node2.prev=node1
node3.next=node4
node3.prev=node2
node4.next=node5
node4.prev=node3
node5.prev=node4
currentnode = node1
while currentnode:
    print(currentnode.element, end="_>")
    currentnode=currentnode.next
print("none")
currentnode = node4
while currentnode:
    print(currentnode.element, end="_>")
    currentnode=currentnode.prev
print("none")
def trans(head):
    currentNode = head
    while currentNode:
        print(currentNode.element, end=" -> ")
        currentNode = currentNode.next
    print("null")

def finflowest(head):
    minvalue=head.element
    currentnode=head.next
    while currentnode:
        if currentnode.element < minvalue :
            minvalue=currentnode.element
        currentnode=currentnode.next
    return minvalue
print(finflowest(node1))

def trans(head):
    currentnode=head
    while currentnode:
        print(currentnode.element, end="_>")
        currentnode=currentnode.next
    print("none")
trans(node1)

currentnode = node1
currentnode = node1
startnode=node1
print(currentnode.element, end="_>")
currentnode = currentnode.next
#        self.next=None
   #     self.prev=None
node1.next = node2
node2.next=node3
node3.next=node4
node4.next=node5
class Node:
    def __init__ (self, element):
        self.element = element
        self.left = None
        self.right = None


while currentnode != startnode:
    print(currentnode.element, end="_>")
    currentnode = currentnode.next
print("...")
binarytree=[1, 2, 3, 4, 4, None, 6, 7, None, None, 9]

def left_child_index(index):
    return (2*index) + 1
def right_child_index(index):
    return (2*index) + 2
def inorder(index):
    if  index>=len(binarytree) or binarytree[index] is None :
        return[]
    return inorder(left_child_index(index)) + [binarytree[index]] + inorder(right_child_index(index))
    if node is None:
        return
    inorder(node.left)
    print(node.element, end="_>")
    inorder(node.right)

def preorder(index):
    if index>=len(binarytree) or binarytree[index] is None :
        return []
    return [binarytree[index]] + preorder(left_child_index(index)) + preorder(right_child_index(index))
def postorder(index):
    if  index>=len(binarytree) or binarytree[index] is None:
         return []
    return preorder(left_child_index(index)) + preorder(right_child_index(index)) + [binarytree[index]]
print(preorder(0))
print(inorder(0))
print(postorder(0))

root = Node(1)
node1 = Node(11)
node2 = Node(12)
node3 = Node(13)
node4 = Node(14)
node5 = Node(15)
root.left=node4
root.right=node2
node2.left=node1
node4.left=node3
node4.right=node5
inorder(root)
class TreeNode:

    def  __init__(self, element):
        self.element = element
        self.left=None
        self.right = None

def search(node, target):
    if node is None:
        return []
    elif node.element==target:
        return node
    elif node.element < target:
        return search(node.right, target)
    else:
        return search(node.left, target)
root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18

result = search(root, 5)
if result:
    print(f" Found:  {result.element} ")
else:
        print( "not found")
'''
'''
x=int(input("enter search: "))
result = search(root, x)
if result:
    print( f"node is found: {result.element}")
else:
    print("not found")
    
def search(node, target):
    if node is None:
        return []
    elif node.element == target:
        return node
    elif node.element > target:
        return search(node.left, target)
    else:
        return search(node.right, target)
''''''
# again practice
class TreeNode:

    def __init__(self, element):
        self.element=element
        self.left=None
        self.right=None
def inorder(node):
    if node is None:
        return 
    inorder(node.left)
    print(node.element, end=",")
    inorder(node.right)

root = TreeNode(13)
node7 = TreeNode(7)
node15 = TreeNode(15)
node3 = TreeNode(3)
node8 = TreeNode(8)
node14 = TreeNode(14)
node19 = TreeNode(19)
node18 = TreeNode(18)

root.left = node7
root.right = node15

node7.left = node3
node7.right = node8

node15.left = node14
node15.right = node19

node19.left = node18
inorder(root)
'''
'''
def findmin(node):
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr

print(findmin(root).element)
'''
'''
def insert(node, element):
    if node is None:
        return TreeNode(element)
    else:
        if element < node.element:
            node.left = insert(node.left, element)
        elif element>node.element:
            node.right = insert(node.right, element)
    return node

insert(root, 10)
'''

class Node:
    def __init__ (self, element):
        self.element=element
        self.left=None
        self.right = None
def insert(node, element):
    if node is None:
        return Node(element)
    else:
        if element > node.element:
            node.right = insert(node.left, element)
        else:
            node.left = insert(node.left, element)
    return node
root = Node(30)
insert(root, 50))
insert(root, 30)
insert(root, 70)

'''

### ✅ 1. **Binary Trees**

#### 🔹Concept:

A Binary Tree is a tree where each node has **at most 2 children** (left and right).

#### 🔹Types:

* **Binary Search Tree (BST)**: Left child < Node < Right child
* **Full Binary Tree**: Every node has 0 or 2 children
* **Complete Binary Tree**: All levels are full except possibly last

#### 🔹Common Operations:

* Insertion
* Traversal (in-order, pre-order, post-order)

#### ✅ BST Insert & In-Order Traversal:

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right

    def in_order(self):  # Left, Root, Right
        def traverse(node):
            if node:
                traverse(node.left)
                print(node.value, end=' ')
                traverse(node.right)
        traverse(self.root)
```

---

### ✅ 2. **Linked List**

#### 🔹Concept:

A linear data structure where each element (node) points to the next.

#### 🔹Types:

* Singly Linked List
* Doubly Linked List
* Circular Linked List

#### ✅ Singly Linked List:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")
```

---

### ✅ 3. **Sorting Algorithms**

| Algorithm   | Time (Best) | Time (Worst) | Space    | Stable |
| ----------- | ----------- | ------------ | -------- | ------ |
| Bubble Sort | O(n)        | O(n²)        | O(1)     | Yes    |
| Selection   | O(n²)       | O(n²)        | O(1)     | No     |
| Insertion   | O(n)        | O(n²)        | O(1)     | Yes    |
| Merge Sort  | O(n log n)  | O(n log n)   | O(n)     | Yes    |
| Quick Sort  | O(n log n)  | O(n²)        | O(log n) | No     |

#### ✅ Bubble Sort:

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

---

### ✅ 4. **Hashing**

#### 🔹Concept:

Storing values using a **key**, very fast lookups.

#### ✅ Simple Hash Table (with chaining):

```python
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        self.table[index].append(key)

    def display(self):
        for i, slot in enumerate(self.table):
            print(i, ":", slot)
```

---

### ✅ 5. **Heap**

#### 🔹Concept:

A binary tree where:

* **Min Heap**: Parent <= Children
* **Max Heap**: Parent >= Children

Used in **priority queues** and **heap sort**.

#### ✅ Min Heap (using heapq module):

```python
import heapq

arr = [3, 1, 4, 1, 5]
heapq.heapify(arr)  # Creates min-heap
heapq.heappush(arr, 2)
print(heapq.heappop(arr))  # Removes smallest
```

---

### ✅ 6. **Huffman’s Theorem (Huffman Coding)**

#### 🔹Concept:

Used for **data compression**. Greedy algorithm.

1. Build min-heap from frequency table
2. Remove two smallest items
3. Combine and push back
4. Repeat until one tree is left

#### ✅ Huffman Coding Concept Example:

Characters with frequencies:
A:5, B:9, C:12, D:13, E:16, F:45

You merge smallest 2 repeatedly and build a tree. Each left edge is `0`, right is `1`. Leaf to root gives binary code.

Actual coding is complex — but **understand concept and steps**.

---

### ✅ Exam Tips:

| Topic       | What They Might Ask              |
| ----------- | -------------------------------- |
| Binary Tree | Insert, Traversal (code/write)   |
| Linked List | Insert/Delete/Traverse           |
| Sorting     | Write or trace bubble/quick      |
| Hashing     | Hashing function, chaining       |
| Heap        | Insert/Delete, min-heap logic    |
| Huffman     | Steps to build tree, frequencies |

---

### 🧠 Pro Tips:

* Practice writing code by hand!
* For sorting, focus on Bubble, Selection, Insertion
* For Huffman, just **learn the algorithm steps** — no need to memorize code
* Use Python or C++ based on your exam requirement

---

Want me to give you **MCQs**, **coding practice questions**, or a **revision sheet** for each topic?
'''










