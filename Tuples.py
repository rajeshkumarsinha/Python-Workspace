##
##a=('rajesh','kumar','sinha','suyash')
##
##
##for words in a:
##    for letters in words:
##        print(letters,end='')
##    print()
##
##
##y=3
##
##def fun(x):
##    global y
##    y+=2
##    x+=1
##
##fun(3)
##print(y)

#you can't change the values in the tuple
##tup=()
##
##for i in range(1,10):
##    tup=tup+(i,)
##    print(tup)
##tup[4]=-4
##
###lists are like arrays.

d={1:'3','rajesh':'sinha'}
d1=d
d[1]='mochhu'
print(d)
print(d1)

for k in d.items():
    print(k)
    
