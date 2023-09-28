#Part 1: Create a BSTNode class
class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.contents = []
    
    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return str(self.data)
    
#Part 2: Create a BST class
class BST:
    def __init__(self, root=None):
        self.root = root

    def __str__(self):
        if self.root == None:
            return "The Tree is empty!"
        else:
            self.output = ""
            self.print_tree(node=self.root)
            return self.output

    def print_tree(self, node, level=0):
        if node != None:
            self.print_tree(node.right, level + 1)
            self.output += ' ' * 4 * level + '->' + str(node.data) + ''
            self.print_tree(node.left, level + 1)

    def add(self, node):
      if type(node) != int and type(node) != BSTNode:
        raise ValueError('Invalid Type/Value')
      
      if type(node) == int:
        node = BSTNode(node)

      if node.data in self.contents:
        return

      

node1 = BSTNode(3)
print(node1)

node2 = BSTNode(4, left=None)
print(node2)

node3 = BSTNode()
print(node3)
node3.data = 5
print(node3)

bst = BST()
print(bst)

bst.root = node2
print(bst)

node2.right = node3
print(bst)

  #Part 3: Add functionality to your BST class
