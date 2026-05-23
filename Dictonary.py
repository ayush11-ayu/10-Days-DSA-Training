d={}
d[100]="ayush"
d[200]="prashant"
d[300]="sandip"
print(d)

rec={}
n=int(input("Enter number of students: "))
for i in range(n):
    name=input("Enter name: ")
    per=float(input("Enter perc: "))
    rec[name]=per

print(rec)
for x in rec:
    print(x,"\t",rec[x])
    
