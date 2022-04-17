def increment(num):
    try:
        return 1/int(num)
    except:
        raise ValueError ("this is not wright")# for raising value error
a=increment("0")
print(a)