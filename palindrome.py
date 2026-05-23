no=int(input("Enter no:"))
rev=0
save=no
while no>0:
    rem=no%10
    rev=rev*10+rem
    no=no//10
    
if rev==save:
    print("Palindrome")
else:
    print("Not palindrome")
    