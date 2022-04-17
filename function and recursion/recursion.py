def val(i):
    if(i==0):
        return
    else:
        print(i)
        return val(i-1)
val(10)