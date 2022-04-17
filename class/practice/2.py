class calculator:

    def __init__(sef,n1):
        sef.n1=n1
      
    def cal(self):# gives the squae of number
        return self. n1**2
    @staticmethod
    def greet():
            print("hello")
c=calculator(4)
d=c.cal()
c.greet()
print(d)