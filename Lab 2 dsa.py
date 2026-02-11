class  DynamicArray:

    def __init__ (self, initial_capacity):

        self.capacity = initial_capacity
        self.size = 0
        self.array = [None] * self.capacity

    def append(self, value):
        
        if self.size == self.capacity:
             
            self.resize()
             
        self.array[self.size] = value
        self.size += 1

    def get(self, index):

        if index <= 0 or index >= self.size:
                return "error"
        return self.array[index]

    def set(self, index, value):

        if index < 0 or index >= 0:
                return "error"
        self.array[index] = value
        return value
   
    def resize(self) :

        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range (self.size):
            new_array[i] = self.array[i]
            self.array = new_array
    

arr = DynamicArray(2)
arr.append(5)
arr.append(6)
arr.append(7)
print(arr.get(1))
print(arr.set(1, 10))
print(arr.get(1))
#print(arr.display())

print()
class Dynamic_array:

    def __init__ (self):

        self.array = []

    def append(self, value):

        self.array.append(value)
        

    def find_longest(self):

        return max(self.array, key = len)

arr = Dynamic_array()
arr.append("cat")
arr.append("elephant")
arr.append("dog")
print(arr.find_longest())
            
print()

class Dynamic_Error:
     
    def __init__ (self):

        self.array = []

    def append(self, value):

        self.array.append(value)
        
    def remove_duplicates(self):

        return list(set(self.array))

arr = Dynamic_Error()
arr.append("apple")
arr.append("apple")
arr.append("banana")
arr.append("banana")
arr.append("cherry")
print(arr.remove_duplicates())