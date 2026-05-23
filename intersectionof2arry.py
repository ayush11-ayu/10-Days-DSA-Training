arr1 = [1, 2, 2, 1]
arr2 = [2, 2]

intersection = []

for i in arr1:
    if i in arr2 and i not in intersection:
        intersection.append(i)

print(intersection)




arr1=[1,2,2,1]
arr2=[2,2]
arr3=[]
for i in arr1:
    for j in arr2:
        if i==j: 
            if i not in arr3:
                arr3.append(i)
print(arr3)