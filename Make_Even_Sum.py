n=int(input())
arr=list(map(int,input().split()))
k=sum(arr)
if k%2==0:
    print("1")
else:
    print("0")