class employee:
  def __init__(self,name,id):
    self.name=name
    self.id=id
  def show(self):
    print(f"the name of employee: {self.name} id is {self.id}")
class programmer(employee):
  pass

c=programmer("siddharth",54)
c.show()


