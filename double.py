class A:
    def showA(self):
        print("i am in class A")
class B(A):
    def showB(self):
        print("i am cass B")
class C(B):
    def showC(self):
        print("I am in class C")
if __name__=="__main__":
    obj=C()
    obj.showA()
    obj.showB()
    obj.showC()