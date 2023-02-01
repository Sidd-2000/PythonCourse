arr=[3,563,63,235,346,743763,525,5,5,3]
for index,i in enumerate(arr):
  print(i)
  if(index==3):
    print("this is bigest value")


for index,i in enumerate(arr,start=2):
  print(i)
  if(index==3):
    print("this is bigest value")