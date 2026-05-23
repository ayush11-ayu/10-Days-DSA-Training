arr = [-1, 2, -3, 4, 5, -6]

pos = []
neg = []

# separate positive and negative numbers
for i in arr:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)

result = []

i = 0
j = 0

# arrange alternately
while i < len(neg) and j < len(pos):
    result.append(neg[i])
    result.append(pos[j])

    i += 1
    j += 1

# remaining elements
while i < len(neg):
    result.append(neg[i])
    i += 1

while j < len(pos):
    result.append(pos[j])
    j += 1

print(result)