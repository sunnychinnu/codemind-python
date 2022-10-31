n=int(input())
m=int(input())
for i in range(n,m+1):
    x=i
    s=0
    a=0
    while i:
        d=i%10
        i=i//10
        s+=1
        if d!=0:
            if x%d==0:
                a+=1
    if s==a:
        print(x,end=" ")
