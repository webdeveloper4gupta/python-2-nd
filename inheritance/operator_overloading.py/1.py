class base:
    def get(self,n):
        self.n=n
    def __add__(self,num2):
        return self.n+num2.n
    def __mul__(self,num2):
        return self.n*num2.n
    
    def __sub__(self,num2):
        return self.n-num2.n
n1=base()
n2=base()
n1.get(2)
n2.get(3)
s=n1+n2
g=n1*n2

k=n1-n2
print(s)
print(g)

print(k)