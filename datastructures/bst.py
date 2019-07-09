# jian li implemented July 5, 2019

class Node ():
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None

class binaryTree():

    def __init__(self):
        self.root = None

    def insert(self, root, val):
       newnode = Node(val)
       if self.root == None:
          self.root = newnode

       if val< root.data:
           if root.left is None:
               root.left = newnode
           else:
               self.insert(root.left, val)
       else:
           if root.right is None:
               root.right = newnode
           else:
               self.insert(root.right, val)

    def find(self,root, target):
        if root == None:
            return False

        if root.data == target:
            return True

        if target < root.data:
            self.find(root.left, target)
        else:
            self.find(root.right, target)

        return False

    def printInorder(self, root):
        if root:
            self.printInorder(root.left)
            print 'printing in order data:', root.data
            self.printInorder(root.right)

    def printPostorder(self, root):
        if root:
            self.printPostorder(root.left)
            self.printPostorder(root.right)
            print  'printing post order data:', root.data

    def printPreorder(self,root):
        if root:
            print 'printing preorder data:', root.data
            self.printPreorder(root.left)
            self.printPreorder(root.right)


bst = binaryTree();
root = Node(3)
bst.insert(root, 7)
bst.insert(root, 1)
bst.insert(root, 5)
bst.printInorder(root)
bst.printPreorder(root)
bst.printPostorder(root)

print (bst.find(root, 7))




