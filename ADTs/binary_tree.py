class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, value):
        if self.data > value:
            if self.leftChild is None:
                self.leftChild = BinaryTreeNode(value)
            else:
                self.leftChild.insert(value)
        else:
            if self.rightChild is None:
                self.rightChild = BinaryTreeNode(value)
            else:
                self.rightChild.insert(value)

    def inOrderTraversal(self):
        if self.leftChild:
            self.leftChild.inOrderTraversal()
        print(self.data)
        if self.rightChild:
            self.rightChild.inOrderTraversal()

    def preOrderTraversal(self):
        print(self.data)
        if self.leftChild:
            self.leftChild.preOrderTraversal()
        if self.rightChild:
            self.rightChild.preOrderTraversal()

    def postOrderTraversal(self):
        if self.leftChild:
            self.leftChild.postOrderTraversal()
        if self.rightChild:
            self.rightChild.postOrderTraversal()
        print(self.data)

    def find(self, value):
        if self.data > value:
            if self.leftChild is None:
                return True
            else:
                self.leftChild.find(value)

tree = BinaryTreeNode(10)
tree.insert(3)
tree.insert(5)
tree.insert(7)
tree.insert(1)
tree.insert(4)
tree.insert(9)
tree.insert(11)
tree.insert(34)

tree.postOrderTraversal()
