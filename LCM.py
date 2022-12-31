a,b=map(int,input().split())
if a>b:
    greater=a
else:
    greater=b
while True:
    if((greater%a==0)and(greater%b==0)):
        print(greater)
        break
    greater+=1