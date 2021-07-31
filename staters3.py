def fsum(l):

    s=0
    n=len(l)
    for i in range(n):
        s=s+(l[i]^i)
    return s

for t in range(int(input())):
    n,k=map(int,input().split())

    l=[i for i in range(2**n)]

    s=0
    n=len(l)
    for i in range(k):
        l[i],l[n-i-1]=l[n-i-1],l[i]

    print(fsum(l))


