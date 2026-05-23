no = 2025

n1 = no % 100
n2 = no // 100

sum = n1 + n2

sq = sum * sum

if sq == no:
    print("Tech Number")
else:
    print("Not Tech Number")

