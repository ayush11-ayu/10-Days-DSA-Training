no=int(input("Enter no: "))
res=no%10
print(res)

#sum of 2 digit no
no=int(input("Enter no: "))
n1=no%10 #5
n2=no%10 #4
res=n1+n2
print(res)

# sum of 3 digit no
no=int(input("Enter no:"))
n1=no%10
no=no//10
n2=no%10
no=no//10
n3=no%10


res=n1+n2+n3
print(res)


#sum of 5 digits
no=int(input("Enter no:"))
n1=no%10
no=no//10
n2=no%10
no=no//10
n3=no%10
no=no//10
n4=no%10
no=no//10
n5=no%10



res=n1+n2+n3+n4+n5
print(res)


#reverse of 3 digit
no=int(input("Enter no:"))
n1=no%10
no=no//10
n2=no%10
no=no//10
n3=no%10
rev=n1*100+n2*10+n3*1
print(res)


