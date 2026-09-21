import random


r='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)         '''


p='''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)     '''


s='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)           '''

l=[r,p,s]
print("\n\n\n-----------------------ROCK!PAPER!SCISSOR!---------------------")
choice=int(input("\n\nEnter your choice:\n  0-  For Rock\n  1-  For Paper\n  2-  For Scissors\n\n"))

echoice=random.randint(0,2)


if choice == echoice:
    print("Your Choice:\n\n")
    print(l[choice])
    print("Computer Choice:\n\n")
    print(l[echoice]) 
    print("\n----------Draw!!!-----------")
elif choice>2:
    print("INVALID CHOICE!")
elif (choice == 0 and echoice == 2) or \
     (choice == 1 and echoice == 0) or \
     (choice == 2 and echoice == 1):
    print("Your Choice:\n\n")
    print(l[choice])
    print("Computer Choice:\n\n")
    print(l[echoice]) 
    print("\n-----------------------You Won!!!!----------------------")
else:
    print("Your Choice:\n\n")
    print(l[choice])
    print("Computer Choice:\n\n")
    print(l[echoice]) 
    print("\n-----------You Lost----------")