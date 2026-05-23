arr = [5, 3, 9, 2, 8]
max = arr[0]
min = arr[0]

for i in arr:
    if i > max:
        max = i

    if i < min:
        min = i

print("Maximum =", max)
print("Minimum =", min)