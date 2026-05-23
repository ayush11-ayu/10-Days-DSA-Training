s = input("Enter string: ")

result = ""

for ch in s:
    if ch != " ":
        result = result + ch

print(result)