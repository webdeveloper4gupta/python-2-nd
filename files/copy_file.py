f=open("aman.txt")
data=f.read()
f.close()

f1=open("sukritan.txt",'w')
f1.write(data)
f.close()