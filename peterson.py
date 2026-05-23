# Peterson Number Program in Python

no = int(input("Enter number: "))
save = no
sum = 0

while no > 0:
    rem = no % 10


    fact = 1
    for i in range(1, rem + 1):
        fact = fact * i

    sum = sum + fact
    no = no // 10

if sum == save:
    print("Peterson number")
else:
    print("Not Peterson number")
