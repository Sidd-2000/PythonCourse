dic={1:'siddharth',2:'vinay',3:"abdul",'vinay':"chor"}
dic2={4:'siddharth',5:'vinay',6:"abdul",7:"chor"}
dic.update(dic2)
print(dic)

dic2.clear()
print(dic2)
print(dic.pop(1))
print(dic.popitem())
