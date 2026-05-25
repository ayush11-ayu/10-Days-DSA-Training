from itertools import permutations

a,b = 459,500

ans=[]

for i in permutations(str(a)):
    n=int(input("".join(i)))
    if n>int(b):
        ans.append(n)
if len(ans)==0:
    print(-1)
else:
    print(min(ans))