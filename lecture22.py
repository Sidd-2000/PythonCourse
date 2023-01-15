l = [2, 5, 6, "siddharth", True]
print(l)
print(type(l))
# print(l[0])
# print(l[1])
# print(l[2])
# print(l[3])

# print(l[-3])
# print(l[len(l)-3])
# print(l[5-3])
# print(l[2])

# if 6 in l:
#   print("yes found")
# else:
#   print("not found")

# if "ddh" in "siddharth":
#   print("yes")
# else:
#   print('NO')

# accessing list element
# print(l[:])
# print(l[:2:])
# print(l[::2])

#list comprehension
lst = [i * i for i in range(40)]
print(lst)

lst = [i * i for i in range(40) if i % 2 == 0]
print(lst)

cube = [item for item in lst if item % 3 == 0]
print(cube)
