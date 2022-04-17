try:

    t1=open("aman.txt")
    a=t1.read()
    print(a)
    print('\n')
    t2=open("suk.txt")
    b=t2.read()
    print(b)
    print('\n')
    t3=open("s.txt")
    c=t3.read()
    print(c)

except:
    print("not found")
