f=open('sample.txt')
data=f.readline(2)# 2 tells print only two characters
print(data)
data=f.readline()
print(data)
f.close()