class rectangle:
    length=10# class attribute
    breadth=10# class attribute
  
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return self.length*self.breadth*self.height

    @staticmethod
    def greet():
        print("happy birthday aman")
r=rectangle()
r.height=5# object attribute
r.greet()
r.height=1# changing of object attribute
ans=r.perimeter()
print(ans)