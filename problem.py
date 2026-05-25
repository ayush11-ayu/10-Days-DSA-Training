n = int(input("Enter no of semester: "))

subjects = []

for i in range(n):
    x = int(input(f"Enter no of subjects in {i+1} semester: "))
    subjects.append(x)

for i in range(n):
    print(f"Marks obtained in semester {i+1}:")
    
    maxi = 0

    for j in range(subjects[i]):
        mark = int(input())

        if mark < 0 or mark > 100:
            print("You have entered invalid mark.")
            break

        if mark > maxi:
            maxi = mark

    else:
        print(f"Maximum mark in {i+1} semester:{maxi}")