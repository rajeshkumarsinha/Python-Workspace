
def match(a,b):
    a=a+b
    if a=='<>' or a=='[]' or a=='()' or a=='{}':
        return True
    else:
        return False

output=''
s=input()
braces=['(','[','{','<']
c=0
for char in s:
    if char in braces:
        output+=char
    elif len(output) and match(output[-1],char):
        output=output[:-1]
    elif len(output) and output[-1] in braces:
        output=output[:-1]
        c+=1
    else:
        output='invalid'
        break
if len(output)==0:
    print(c)
else:
    print('Impossible')
        
