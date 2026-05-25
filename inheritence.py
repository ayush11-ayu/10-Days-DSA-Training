class A:
    def showA(self):
        print("i am in class A")
class B(A):
    def showB(self):
        print("i am cass B")
if __name__=="__main__":
    obj=B()
    obj.showA()
    obj.showB()