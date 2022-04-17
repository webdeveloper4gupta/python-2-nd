class rectangle:
    length=10# class attribute
    breadth=10# class attribute
    def __init__(self):# constructor invoke
        self.length=0 # now the lenth and breadth consider as zero
        self.breadth=0
        print("constructor invoke")
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return self.length*self.breadth*self.height

r=rectangle()
r.height=5# object attribute
ans=r.perimeter()
print(ans)