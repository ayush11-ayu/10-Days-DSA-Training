import sys

class GetNode:
    def __init__(self) -> None:
        self.data=None
        self.link=None

class LinkedList:
    def __init__(self) -> None:
        self.head=None

    def append(self):
        data=int(input("enter data :"))
        newNode=GetNode()
        newNode.data =data
        if self.head==None:
            self.head=newNode
        else:
            ptr=self.head
            while ptr.link!=None:
                ptr=ptr.link
            ptr.link =newNode
            print(data,"is added..")

    def traverse(self):
        if self.head==None:
            print("linked list not present")
        else:
            ptr=self.head
            while ptr!=None:
                print(ptr.data,"->",end=" ")
                ptr=ptr.link

    def begin(self):
        data=int(input("enter data :"))
        newNode=GetNode()
        newNode.data =data
        if self.head==None:
            self.head=newNode
        else:
            ptr = self.head
            newNode.link=ptr
            self.head = newNode
    
    def addAtbetween(self):
        data=int(input("enter data :"))
        key=int(input("enter data after inserted: "))
        newNode=GetNode()
        newNode.data =data
        if self.head==None:
            self.head=newNode
        else:
            ptr=self.head
            while ptr.link!=None:
                if key==ptr.data:
                    break;
                else:
                    ptr=ptr.link
            if ptr.link==None:
                print("key not found")
            else:
                ptr1=ptr.link
                ptr.link=newNode
                newNode.link=ptr1
                print(data,"is added..")


    def deleteAtbegin(self):
        if self.head==None:
            print("list not present")
        else:
            ptr=self.head
            ptr1=ptr.link
            ptr.link=None
            ptr1=self.head
            print(ptr.data,"is deletd")

    def deleteAtend(self):
        data=int(input("enter data :"))
        key=int(input("enter data after inserted: "))
        newNode=GetNode()
        newNode.data =data
        if self.head==None:
            self.head=newNode
        else:
            ptr=self.head
            while ptr.link!=None:
                ptr1=ptr
                ptr=ptr.link
                ptr1.link=None
                print(ptr.data,"is deleted...")






if __name__ == '__main__':
    obj=LinkedList()
    while True:
        print("\n 1. Append")
        print("2. Traverse")
        
        print("3. Add at Begin")
        print("4. ADD at end")
        print("5. Add at Between")

        print("6. delete at begin ")
        print("7. delete at end ")
        print("8. delet at between") 
        
        print("9. serach")
        print("0. Exit")

        n=int(input("Selet any choice: "))
        if n==1:
            obj.append()
        elif n==2:
            obj.traverse()
        elif n==3:
            obj.begin()
        elif n==4:
            obj.addAtbetween()
        elif n==5:
            obj.deleteAtend()

        elif n==0:
            sys.exit(0)
