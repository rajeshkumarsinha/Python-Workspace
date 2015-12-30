##def F(s):
##    if len(s)<=1:
##        return s
##    else:
##        return F(F(s[1:]))+s[0]
##
##
##print(F("rajesh"))

n=int(input())

if n%2==0:
    if n%4==0:
        print((n//4)-1)
    else:
        print((n//4))
else:
    print(0)
            
    
