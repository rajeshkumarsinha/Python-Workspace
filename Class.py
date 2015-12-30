

class animal(object):
    def __init__(self,name,t):
        self.name=name
        self.type=t
    def getname(self):
        return self.name
    def gettype(self):
        return self.type
    #Operator OverLoading
    #OverRiding Methods
    def __add__(self,s):
        return self.name+s
    def __int__(self):
        return 10


obj=animal('tommy','dog')
print(obj.getname())
print(obj.gettype())
print(obj+"rajesh")
print(int(obj))

print(type(obj))
try:
    print(obj.fuck)
except Exception:
    print("wow you have raised an Exception")

print(animal.getname(obj))
