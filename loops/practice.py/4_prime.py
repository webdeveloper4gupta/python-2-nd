number=int(input("enter the number"))
flag=True
for i in range(2,number):
    if number%i==0:
        flag=False
        break


if flag:
    print("yes it is prime number")
else:
    print("not a prime number")