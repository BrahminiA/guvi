def rev(m,a):
    rev=a[::-1]
    for i in range(0,m):
        if(i==m-1):
            print(rev[i])
        else:
            print(rev[i],end="->")
            
m=int(input())
a=list(map(int,input().split()))
rev(m,a)
    
        
