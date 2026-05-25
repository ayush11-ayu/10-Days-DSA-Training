def sum():
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n+sum(n-1)
print(sum(2))
    