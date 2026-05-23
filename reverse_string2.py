s="learning python is very easy from Ashish sir"
ls=s.split()
ans=""
for x in range(len(ls)):
    ans=ans+[x][::-1]+" "
print(ans)