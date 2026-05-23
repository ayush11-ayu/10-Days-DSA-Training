arr=[1,2,3,4,5,6,7,8]

n=int(input("enter size"))
for i in range(n):
    arr.append(int(input("enter numbers :")))
key=int(input("enter key element whice is to be inserted :"))
loc=int(input("enter location :"))

arr.append(0)
for i in range(len(arr)-2,loc+1):
    arr[i-1]=arr[i]
arr[loc]=key
print(arr)