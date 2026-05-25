class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # Push operation
    def push(self, data):
        newNode = Node(data)

        newNode.next = self.top
        self.top = newNode

        print(data, "inserted")

    # Pop operation
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
        else:
            temp = self.top
            print(temp.data, "deleted")
            self.top = self.top.next

    # Peek operation
    def peek(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            print("Top element is:", self.top.data)

    # Traverse stack
    def traverse(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            ptr = self.top
            while ptr is not None:
                print(ptr.data)
                ptr = ptr.next


# Driver Code
obj = Stack()

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Traverse")
    print("0. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        data = int(input("Enter data: "))
        obj.push(data)

    elif ch == 2:
        obj.pop()

    elif ch == 3:
        obj.peek()

    elif ch == 4:
        obj.traverse()

    elif ch == 0:
        break 