class name:
    Name="aman"
    def get(self):
        print(self.Name)

class nam(name):
    Name="sukritan"
    len="am"
class am(nam):
    def m(self):
        super().get()
        print(self.Name)

a=am()
a.m()