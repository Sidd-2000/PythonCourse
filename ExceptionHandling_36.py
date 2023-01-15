a=input("enter the number")
try:
  for i in range(11):
    print(f"{a}*{i}={int(a)*i}")
except ValueError:
  print("ho")

  
#   print("please enter valid value")
# else:
#   print("not done properly\n")
# finally:
#   print("done !")