import math

def calc(a,x,b):
    return math.ceil((b-x)/2) + math.ceil((x-a)/2)

def indicate(a,b):
    flag = -1
    if a%2==0 and b%2==0:
    	flag = 1
    elif a%2==1 and b%2==1:
    	flag = 1
    else:
    	flag = 0
    	
    return flag

for i in range(int(input())):
    a,b = map(int,input().split())
    res = -32768
    M = a if a>=b else b
    m = b if M == a else a
    if a == b:
        res = 0
    else:
        res = calc(a,m+1,b) if indicate(a,b) else calc(a,m,b)
            
    print(res)
