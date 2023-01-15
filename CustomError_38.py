# a=int(input("enter your age"))
# if a<=17:
#   raise print("you are taking wrong value")
# else:
#   print("good")

a=input("enter anything\n")
if(a=="quite"):
  print("you are safe")

elif(a.isdigit()):
  print("you are entered right value are entered right value")
else:
  raise ValueError("enter write value")