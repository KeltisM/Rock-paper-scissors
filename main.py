import random
while True:
 actions=["rock","paper","scissor"]
 computer=random.choice(actions)
 user=input("enter your choice, -rock/paper/scissor \t")
 print("computer choice is ,",computer)
 if(user==computer):
  print("its a tie")
 else:
  if(user=="rock"):
    if(computer=="paper"):
      print("computer wins")
    else:
      print("you win!")
  if(user=="paper"):
    if(computer=="rock"):
      print("you win!")
    else:
      print("computer wins")
  if(user=="scissor"):
    if(computer=="rock"):
      print("computer wins")
    else:
      print("you win")
  a=input("do you want to play again y/n \t")
  if(a!="y"):
    break
     
  