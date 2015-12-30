x=0
y=0

import math
import random
##n=int(input())
##for _ in range(n):
##    z=random.randint(1,4)
##    if z==1:
##        x+=1
##    if z==2:
##        x-=1
##    if z==3:
##        y+=1
##    if z==4:
##        y-=1
##
##print(math.sqrt(x*x+y*y))

c=0
for _ in range(10000000):
   if random.random()<=0.5:
       c+=1
print(c/10000000)
