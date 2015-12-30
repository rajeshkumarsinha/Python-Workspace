
def NthRoot(x,n,epsilon):
    assert type(x) ==type(0.2) and type(n) == type(1)
    low=int(0)
    high=max(1.0,x)

    ans=low
    while abs(ans**n-x)>epsilon:
        ans=(low+high)/2

        if ans**n > x:
            high=ans
        else :
            low=ans
    print(ans)
    





x=float(input())
n=int(input())
epsilon=0.01

NthRoot(x,n,epsilon)
