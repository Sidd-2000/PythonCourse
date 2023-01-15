
a={3,6,2,6}
b={7,7,456,235,7,35}
c=a.union(b)
print(c,"\n")
print(a.intersection(b),"\n")

a.update(b)
print(a,b)
a.intersection_update(b)
print(a)
# c=a.symmetric_difference(b)
# print(c)
# d=a.difference(b)
# print(d)

# print(a.isdisjoint(b))
# a.remove("siddharth")
# print(a)
# a.add("siddharth")

# a.discard(3)
# print(a)
# a.remove(6)
# print(a)

# tem=a.pop()
# print(tem)
# del b
# print(b)