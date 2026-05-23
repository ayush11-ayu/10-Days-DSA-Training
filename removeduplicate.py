s = "ABCDABBCDABBBCCCDDEEEF"

new = ""

for i in s:
    if i not in new:
        new = new + i

print(new)



s = "ABCDABBCDABBBCCCDDEEEF"

x = ""

for i in s:
    if i not in x:
        x = x + i

print(x)

