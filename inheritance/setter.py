class name:
    Name="aman"
    len="kl"
    def get(self):
        print(self.Name)
    @property
    def g(self):
        return self.Name
    @g.setter
    def g(self,val):
        self.len=val

e=name()
print(e.g)
print(e.len)
 