s,l=map(int,input().split())

lis =[list() for _ in range(100001)]

for i in range(1,l+1):
    lis[i & (~ (i-1))].append(i)

num=int(pow(2,s.bit_length()-1))

invalid=1
ans=list()
while num:
    if num & s:
        temp=num
        length=1
        while temp:
            while len(lis[temp]):
                if length==0:
                    break
                ans.append(lis[temp].pop())
                length-=1
            length=length<<1
            temp>>=1
        if length:
            invalid=0
    num>>=1

if invalid:
    print(len(ans))
    for var in ans:
        print(var,end=" ")
else:
    print(-1)
