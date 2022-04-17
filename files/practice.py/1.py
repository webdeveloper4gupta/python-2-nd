

f1=open("poem.txt")
data=f1.read()
if 'twinkl 'in data:
    print("yes it is found")
else:
    print("not found")
