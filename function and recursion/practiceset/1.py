# greatest of three numbers
def great(n1,n2,n3):
    if(n1>n2 and n1>n3):
        print("n1 is greatesrt")
    elif(n2>n3 and n2>n1):
        print("n2 is greatest")
    else:
        print("n3 is greatest")

great(4,9,3)