from functools import reduce
def cube(x):
    return x*x*x

l=[i for i in range(5)]
# MAP   

#list1=list(map(cube,l))
#print(list1)

#Filter
def filter_function(a):
   return a<4


newl=list(filter(filter_function,l))
print(newl)

#  Reduce function
# reduce function operates with the next value of the arguments

numbers=[1,5,25,63]
def mysum(x,y):
    return x+y
sum=reduce(mysum,numbers)

print(sum)
