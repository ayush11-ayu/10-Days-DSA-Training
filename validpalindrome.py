s = "A man, a plan, a canal : panama"

new_str = ""


for i in range(len(s)):
    if s[i].isalpha():
        new_str = new_str + s[i].lower()

rev = new_str[::-1]


if new_str == rev:
    print("Valid Palindrome")
else:
    print("Not Palindrome")

