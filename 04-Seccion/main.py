rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

hands = [rock,paper,scissors]
select_hand = int(input("What would you choose? Rock = 0, paper = 1, scissors = 2:\n"))

hand_computer = random.randint(0,2)

if select_hand >= 3 or select_hand <=0:
  print("Number Invaled, You Lose")
else:
  print(f"\nComputer:\n{hands[hand_computer]}")
  print(f"You:\n{hands[select_hand]}")
  
  if select_hand == 0 and hand_computer == 2:
    print("You Win")
  elif select_hand == 2 and hand_computer == 1:
    print("You Win")
  elif select_hand == 1 and hand_computer == 0:
    print("You Win")
  elif select_hand == hand_computer:
    print("Tie")
  else:
    print("You Lose")