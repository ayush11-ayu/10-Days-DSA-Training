import sys

class Queue:

    def __init__(self):
        self.queue = []
        self.front = -1
        self.rear = -1
        self.CAPACITY = 5

    def isFull(self):
        return self.rear == self.CAPACITY - 1

    def isEmpty(self):
        return self.front == -1 or self.front > self.rear

    def insert(self, ele):
        if self.isFull():
            print("Queue is Full")
        else:
            if self.front == -1:
                self.front = 0

            self.rear += 1
            self.queue.append(ele)
            print(ele, "is inserted")

    def delete(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            ele = self.queue[self.front]
            self.front += 1
            return ele

    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("Front element is:", self.queue[self.front])

    def traverse(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i])


if __name__ == '__main__':

    obj = Queue()

    while True:

        print("\n1. Insert")
        print("2. Delete")
        print("3. Peek")
        print("4. Traverse")
        print("0. Exit")

        ch = int(input("Select any choice : "))

        if ch == 1:
            ele = int(input("Enter data : "))
            obj.insert(ele)

        elif ch == 2:
            ele = obj.delete()
            if ele is not None:
                print(ele, "is deleted")

        elif ch == 3:
            obj.peek()

        elif ch == 4:
            obj.traverse()

        elif ch == 0:
            sys.exit(0)