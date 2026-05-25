s = "ycce"
t = "ycsce"

if s == t:
    print(0)
else:
    print(abs(len(t) - len(s)))
    
    
    
if len(s)<len(t):
    output=len(t)-len(s)
elif len(t)<len(s):
    output=len(s)-len(t)
elif len(s)==len(t):
    for i in range(len(s)):
        if s[i]!=t[i]:
            count=count+1
    output=count
print(output)

