import art

import random

def black_jack():
  print(art.logo)

  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

  user = []

  npc =  []

  def user_value():
    user = random.sample(cards,k=2)
    return (user)


  def npc_value():
    npc = random.sample(cards,k=2)
    return (npc)



  user_list = user_value()
  user_sum = sum(user_list)
  print(f"Your cards: {user_list} ,current score {user_sum}")

  npc_list = npc_value()
  npc_sum = sum(npc_list)
  print(f"This is NPC first card - '{npc_list[0]}'")

  more_cards = input("Do you want another card? Type 'y' or 'n':")

  def compare(user_sum, npc_sum):

    if user_sum > 21 and npc_sum > 21:
      return "You went over. You lose 😤"
    elif user_sum == npc_sum:
      return "Draw 🙃"
    elif user_sum > 21:
      return "You went over. You lose 😭"
    elif npc_sum > 21:
      return "Opponent went over. You win 😁"
    elif user_sum > npc_sum:
      return "You win 😃"
    else:
      return "You lose 😤"

  while more_cards == "y":
    if more_cards == "n":
        break
    x =  random.choice(cards)
    user_list.append(x)
    user_sum = user_sum + x
    print(f"Your cards: {user_list} ,current score {user_sum}")
    if user_sum == 21:
        break
    if user_sum > 21:
        break
    more_cards = input("Do you want another card? Type 'y' or 'n':")


  while npc_sum < 17:
    x = random.choice(cards)
    npc_list.append(x)
    print(f"This is NPC hand:{npc_list}")
    npc_sum = npc_sum + x
    if npc_sum == 21:
        break
    elif npc_sum > 21:
      break

  print(f"This is NPC final score {npc_sum} and final hand: {npc_list}")
  print(f"This is your final scrore {user_sum} and your final cards: {user_list}")
  print(compare(user_sum, npc_sum))
  print("Game over")

import replit

black_jack()
choice = input("Do you want to play another round? y or n?")

while choice == "y":
  if choice == "n":
      break
  replit.clear()
  black_jack()
  choice = input("Do you want to play another round? y or n?")
print("Thank you for playing")
