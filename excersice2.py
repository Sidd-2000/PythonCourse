import time
timestamp=time.strftime('%H:%M:%S')
hours=int(time.strftime("%H"))
print(hours)

if(hours>0 and hours<12):
  print("Good Morning It's a",hours," AM")
elif(hours>=12 and hours<15):
  print("Good Afternoon It's a",hours," PM")
elif(hours>=15 and hours<0):
  print("Good Evening It's a",hours," PM")