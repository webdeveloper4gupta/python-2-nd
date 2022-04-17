l=[1,2,3,4,5,10,20]
def division(num):
    return num%5==0

c=list(filter(division,l))
print(c)