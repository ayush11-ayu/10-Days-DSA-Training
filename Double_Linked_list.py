import sys

class GetNode:
    def __init__(self) -> None:
        self.data= None
        self.left= None
        self.right= None

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head=None

    def append(self):
        data=int(input("enter data :"))
        newNode=GetNode()
        newNode.data=data # type: ignore
        if self.head is None:
            self.head=newNode
        else:
            ptr=self.head
            while ptr.right!=None:
                ptr=ptr.right
            ptr.right=newNode # type: ignore
            newNode.left=ptr # type: ignore


    def traverse(self):
        if self.head is None:
            print("list not present")
        else:
            ptr=self.head
            while ptr!=None:
                print(ptr.data,"->",end="")
                ptr=ptr.right

    def AddatBegin(self):
        data = int(input("enter data :"))
        newNode = GetNode()
        newNode.data = data
        if self.head is None:
            self.head = newNode
        else:
            newNode.right = self.head
            self.head.left = newNode
            self.head = newNode

    def AddatEnd(self):
        data = int(input("enter data :"))
        newNode = GetNode()
        newNode.data = data
        if self.head is None:
            self.head = newNode
        else:
            ptr=self.head
            while ptr.right!=None:
                ptr=ptr.right
            ptr.right=newNode
            newNode.left=ptr

    def AddatBetween(self):
        pos = int(input("Enter position : "))
        data = int(input("Enter data : "))
        newNode = GetNode()
        newNode.data = data
        ptr = self.head
        count = 1
        while count < pos - 1 and ptr != None:
            ptr = ptr.right
            count += 1
        if ptr == None:
            print("Position not found")
        else:
            newNode.right = ptr.right
            newNode.left = ptr
            if ptr.right != None:
                ptr.right.left = newNode
            ptr.right = newNode


if __name__ == '__main__':
    obj=DoubleLinkedList()
    while True:
        print("")
        print("1. Append")
        print("2. Traverse")
        print("3. ADD at Begin")
        print("4. ADD at END")
        print("5. ADD at between")
        print("0. Exit")

        n=int(input("Selet any choice: "))
        if n==1:
            obj.append()
        elif n==2:
            obj.traverse()
        elif n==3:
            obj.AddatBegin()
        elif n==4:
            obj.AddatEnd()
        elif n==4:
            obj.AddatBetween()
        elif n==0:
            sys.exit(0)