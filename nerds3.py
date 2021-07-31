n=int(input())

x=[]

for i in range(n):
    x.append(input())

x.sort(key=lambda x:len(x))
c=0
for i in range(n):
    l=[0]*n
    for j in range(i+1,n):
        if x[i] in x[j] and l[j]==0:
            c=c+1
            #print(x[i],x[j])
            for k in range(j+1,n):
                if x[j] in x[k]:
                    l[k]=1
print(c)
            
