name=input("Please enter your name here \n")
print(f"Welcome to KBC {name}")
print("Start the game !!\n")
questions=["location of burj Khalifa","which animal is know as \"ship of the desert \"","how many days are there in a week","how many hours in a day","Rainbow consist of how many colors"]

answers=["dubai","camel","7","24","7"]
win=0
obtained=0
for i in range(0,5):
  print(f"Your {i+1} question is")
  print(questions[i])
  input1=input()
  if(input1==answers[i]):
    win=500
    obtained+=win
  else:
    win=0

if(obtained==0):
  print("\nYou are looser")
else:
  print(f"\nCongratulation you are win \n Please Collect your {obtained} ₹ ")