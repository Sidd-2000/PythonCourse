add=lambda x:x*x


def appl(fx,value):
    return 6+fx(value)


print(appl(add,5))
print(appl(lambda x:x+3,5))
#lambda function can not have name

#taking squre
print(appl(lambda x:x*x,6))
