num = int(input("enter number"))
sum = 0
save = num
count = 0
temp = num


while temp > 0:
    temp = temp // 10
    count = count + 1

temp = num

while num > 0 :
    rem = num % 10
    sum = sum + (rem ** count)
    num = num // 10

if sum == save:
    print("armstrong")
else:
    print("not armstrong")
