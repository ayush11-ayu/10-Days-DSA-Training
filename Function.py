def sub():
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    res=a-b
    print("Subtraction is ",res)
    
if __name__ == '__main__':
    sub()


#parameterized functon 
def sub(a,b):

    res=a-b
    print("Subtraction is ",res)
    
if __name__ == '__main__':
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    sub(a,b)
    
    
#parameter return
def sub(a,b):
    res=a-b
    return res
if __name__ == '__main__':
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    r=sub(a,b)
    print("Subtraction is ",r)
    
    