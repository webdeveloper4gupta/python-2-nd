class Employee:
    company='microsoft'
    salary=1000000#class attribute
    def __init__(self):
        self. company="google"
        print("constructor invoke")
    def get(self):
        print(f"the company of employee is :{self. company}")
        print(f"the salary of employee is:{self.salary}")
e=Employee()# object formation
d=Employee.company
print(d)
e.salary=10#object attribute
e.get()