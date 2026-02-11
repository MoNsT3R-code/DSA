class Parent:

    def __init__ (self, value):

        self.value = value
        self.left = None
        self.right = None

class BinaryTree:

    def __init__ (self):

        self.root = None

    def insert(self, value):

        if not self.root:
            self.root = Parent(value)
        
        else:
            self._insert(self.root, value)

    def _insert(self, parent, value):

        if value < parent.value:

            if parent.left:
                self._insert(parent.left, value)

            else:

                parent.left = Parent(value)

            if parent.right:

                self._insert(parent.right, value)

            else:

                Parent.right = Parent(value)

    def inorder(self):

        return self._inorder(self.root)
    
    def _inorder(self, parent):

        if parent:

            return self._inorder(parent.left) + [parent.value] + self._inorder(parent.right)
        
        return []

    def preorder(self):

        return self._preorder(self.root)
    
    def _preorder(self, parent):

        if parent:

            return [parent.value] + self._preorder(parent.left) + self._preorder(parent.right)
        
        return []

    def postorder(self):

        return self._postorder(self.root)
    
    def _postorder(self, parent):

        if parent:

            return self._postorder(parent.left) + self._postorder(parent.right) + [parent.value]
            
        return []
    
    def find(self, value):

        return self._find(self.root, value)
    
    def _find(self, parent, value):

        if not parent:
            return False
        
        if parent.value == value:
            return True
        
        elif value < parent.value:
            return self._find(parent.left, value)

        else:
            return self._find(parent.right, value)
        
    def height(self):

        return self._height(self.root)
    
    def _height(self, parent):

        if not parent:

            return 0
        
        else:

            return 1 + max(self._height(parent.left), self._height(parent.right))

    def is_empty(self):

        return self.root is None

    def __len__ (self):

        return self._len(self.root)
    
    def _len(self, parent):

        if not parent:
            return 0 
        return 1 + self._len(parent.left) + self._len(parent.right)
    
    def delete(self, value):
    
        self.root = self._delete(self.root, value)

    def _delete(self, parent, value):

        if not parent:
            return parent
        
        if value < parent.value:
            parent.left = self._delete(parent.left, value)

        elif value > parent.value or value == parent.value :
            parent.right = self._delete(parent.right, value)

        else:
            
            if not parent.left and not parent.right:

                return None
            elif not parent.left:
                return parent.right
            elif not parent.right:
                return parent.left
            else:
                min_parent = self._find_min(parent.right)
                parent.value = min_parent.value
                parent.right=self._del(parent.right, min_parent.value)

        return parent

        

bst = BinaryTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)

print("Inorder: ", (bst.inorder()))  
print("preorder: ", (bst.preorder()))
print("Postorder: ", (bst.postorder()))

print("Finding 30: ", (bst.find(30)))
print("Height: ", (bst.height()))
print("Is Empty: ", (bst.is_empty()))
print("Length of tree: ", len(bst))

bst.delete(30)
print("Inorder after del 30: ", (bst.inorder()))  
print("preorder: ", (bst.preorder()))
print("Postorder: ", (bst.postorder()))