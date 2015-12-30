import math



t=int(input())


for _ in range(t):
    n,m=map(int,input().split())
    if n==2 and m==1:
        print("1 2")
    elif n>2 and n==m:
        for i in range(n):
            print(1+i,1+(i+1)%(n))
    else:
        print("-1 -1")
