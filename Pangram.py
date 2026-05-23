s = input("Enter string: ").lower()

alphabet = "abcdefghijklmnopqrstuvwxyz"

flag = True

for ch in alphabet:
    if ch not in s:
        flag = False
        break

if flag:
    print("Pangram")
else:
    print("Not Pangram")