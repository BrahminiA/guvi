n=int(input())
l=list(map(int,input().split()))
for i in range(n-1):
    if(l[i]>l[i+1]):
        print(l[i+1],end=" ")
    else:
        print("-1",end=" ")
print(-1)
