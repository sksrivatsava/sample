for t in range(int(input())):
    e,k=map(int,input().split())

    c=0
    while e>=1:
        e=e//k
        c=c+1
    print(c)
