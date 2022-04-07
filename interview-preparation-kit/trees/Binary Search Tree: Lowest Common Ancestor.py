class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

# lowest common anchestor value must be the value between v1 and v2
def lca(root, v1, v2):
    # start looking in the right if both v1 and v2 higher than current node value
    if root.info < v1 and root.info < v2:
        return lca(root.right,v1,v2)
    # start looking in the left if both v1 and v2 lower than current node value
    elif root.info > v1 and root.info > v2:
        return lca(root.left,v1,v2)
    # return the root if the value is between v1 and v2.
    else:
        return root

tree = BinarySearchTree()
