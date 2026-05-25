import sys

class BST:

    def __init__(self, key):
        self.leftChild = None
        self.data = key
        self.rightChild = None

    # Insert Node
    def insert(self, key):

        if self.data == key:
            return

        if key < self.data:

            if self.leftChild:
                self.leftChild.insert(key)

            else:
                self.leftChild = BST(key)

        else:

            if self.rightChild:
                self.rightChild.insert(key)

            else:
                self.rightChild = BST(key)

    # Search Node
    def search(self, key):

        if self.data == key:
            print("Node Found")
            return

        if key < self.data:

            if self.leftChild:
                self.leftChild.search(key)

            else:
                print("Node Not Found")

        else:

            if self.rightChild:
                self.rightChild.search(key)

            else:
                print("Node Not Found")

    # PreOrder Traversal
    def preorder(self):

        print(self.data, end="->")

        if self.leftChild:
            self.leftChild.preorder()

        if self.rightChild:
            self.rightChild.preorder()

    # InOrder Traversal
    def inorder(self):

        if self.leftChild:
            self.leftChild.inorder()

        print(self.data, end="->")

        if self.rightChild:
            self.rightChild.inorder()

    # PostOrder Traversal
    def postorder(self):

        if self.leftChild:
            self.leftChild.postorder()

        if self.rightChild:
            self.rightChild.postorder()

        print(self.data, end="->")


# Driver Code
if __name__ == "__main__":

    arr = [36, 26, 46, 21, 31, 11, 24, 41, 56, 51, 66]

    root = BST(arr[0])

    for i in arr[1:]:
        root.insert(i)

    while True:

        print("\n1. Insert")
        print("2. PostOrder")
        print("3. PreOrder")
        print("4. InOrder")
        print("5. Search")
        print("0. Exit")

        n = int(input("Select any choice: "))

        if n == 1:

            data = int(input("Enter data: "))
            root.insert(data)

        elif n == 2:

            print("PostOrder Traversal:")
            root.postorder()
            print()

        elif n == 3:

            print("PreOrder Traversal:")
            root.preorder()
            print()

        elif n == 4:

            print("InOrder Traversal:")
            root.inorder()
            print()

        elif n == 5:

            data = int(input("Enter element to search: "))
            root.search(data)

        elif n == 0:

            sys.exit(0)

        else:

            print("Invalid Choice")