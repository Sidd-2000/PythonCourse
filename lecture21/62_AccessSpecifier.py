class employee:
  def __init__(self,name,id):
    self.__name="Harry"#protected variable
    self._id=343

c=employee("siddharth",54)
# c.show()#show error then
print("\n")
print(c._employee__name)
print("\n")
print(c.__dir__())