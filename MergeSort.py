
num=list(map(int,input().split()))

def merge(low,mid,high):
    global num
    temp=list()
    i=low
    j=mid+1
    while i<=mid and j<=high:
        if num[i]<num[j]:
            temp=temp+[num[i],]
            i+=1
        else:
            temp=temp+[num[j],]
            j+=1
    while i<=mid:
        temp=temp+[num[i],]
        i+=1
    while j<=high:
        temp=temp+[num[j],]
        j+=1
    for z in range(low,high+1):
        num[z]=temp[z-low]
        
def divide(low,high):
    global num
    if low<high:
        mid=(low+high)//2
        divide(low,mid)
        divide(mid+1,high)
        merge(low,mid,high)




divide(0,len(num)-1)
print(num)



