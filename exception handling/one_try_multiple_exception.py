a=int(input())
try:
    c=1/a
    print(c)
except ValueError as e:
    print("enter the  correct  value")
except:
    print("wrong input")
print("thank you")