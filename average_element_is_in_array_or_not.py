n=int(input())
arr=list(map(int,input().split()))
c=0
t=sum(arr)//n
for i in range(0,n):
    if t==arr[i]:
        c+=1
if c==0:
    print("False")
else:
    print("True")