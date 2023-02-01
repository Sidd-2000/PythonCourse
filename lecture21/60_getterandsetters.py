class Myclass:
  def __init__(self,value):
    self._value=value
  def show(self):
    print(f'value is {self._value}')
    #getter is initialized here
  @property
  def Ten_value(self):
    return 10*self._value
#setter is initialized here
  @Ten_value.setter
  def Ten_value(self,new_value):
    self._value=new_value/5
    
obj=Myclass(10)
obj.Ten_value=49
print(obj.Ten_value)
obj.show()
