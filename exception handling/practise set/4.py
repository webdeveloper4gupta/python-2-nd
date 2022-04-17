a=int(input("enter the number"))
b=int(input("enter the number"))
try:
    c=a/b
    print(c)
except ZeroDivisionError as e:
    print("zero division error")
