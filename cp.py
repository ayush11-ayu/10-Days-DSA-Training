cp = int(input("Enter the cost price: "))

st = input("Are you student? (y/n): ")

if st == 'y':
    if cp > 500:
        d = 0.10 * cp
    else:
        d = 0.05 * cp

elif st == 'n':
    if cp > 500:
        d = 0.08 * cp
    else:
        d = 0.02 * cp

net = cp - d

print("Ds is:", d)
print("Net:", net)

