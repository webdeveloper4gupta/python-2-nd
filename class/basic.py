class rectangle:
    length=10# class attribute
    breadth=10# class attribute
  
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return self.length*self.breadth*self.height
r=rectangle()
r.height=5# object attribute
ans=r.perimeter()
r1=rectangle()
#print(r1.height) it shows errror as object and class has no attribute height
#data=r1.perimeter() it also gives errror
print(ans)