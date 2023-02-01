a=4
b=5

# but is compare the location of the variables
print(a is b)


a1=[2,6,2]
b1=[2,6,2]
print(a1 is b1)  # # but is compare the location of the variables
# it is true when a=3 and b=3 but false in list tuple,dictionaries
print(a1==b1)   # true

c=None
d=None

print(c is d)# true
print(c ==d) # true
print(c is None)
