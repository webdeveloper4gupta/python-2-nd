class rectangle:
    length=10# class attribute
    breadth=10# class attribute
  
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return self.length*self.breadth*self.height
r=rectangle()
r.height=5# object attribute
rectangle
ans=r.perimeter()
print(ans)