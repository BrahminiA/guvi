n,k=input().split()
n=int(n)
k=int(k)
l=list(map(int,input().split()))
l.sort()
print(l[-k])
