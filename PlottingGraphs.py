import pylab

import math

l1=list()
l2=list()

i=float(0)

while i<=2*math.pi:
    l1=l1+[i,]
    l2=l2+[math.sin(i),]
    i+=0.001

pylab.title("Graph Of Sin Function")
pylab.xlabel("x-value")
pylab.ylabel("sin x value")
pylab.plot(l1,l2)

pylab.show()
ar=[1,2,2,3,4]
pylab.hist(ar,5)

pylab.show()
