#greeting
print("Welcome to The Rock roll playing game.")
get_name=input('What is your name?')
print('Hello', get_name)
#number generator
import random
# sum_of_four_six_sided_dice_with_lowest_dropped
res = sum(random.sample(range(1, 6), 3))
#dice total
print ("Your dice total for this roll is : " +str(res))

#assigned variable
if res ==7:
    print("Strength")
elif res ==8:
    print("Dexterity")
elif res ==9:
    print("Constitution")
elif res ==10:
    print("Intelligence")
elif res ==11:
    print("Wisdom")
elif res ==12:
    print("Charisma")

#get_ability_modifier
import random
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]


ability=random.choice(num)

if ability ==1:
    print("Modifier -5")
elif ability ==(2, 3):
    print("Modifier -4")
elif ability ==(4, 5):
    print("Modifier -3")
elif ability == (6, 7):
    print("Modifier -2")
elif ability ==(8, 9):
    print("Modifier -1")
elif ability ==(10, 11):
    print("Modifier +0")
elif ability ==(12, 13):
    print("Modifier +1")
elif ability ==(14, 15):
    print("Modifier +2")
elif ability ==(16, 17):
    print("Modifier +3")
elif ability ==18:
    print("Modifier +4")

#creates loop
for x in range (4):
#choose action
def player_choice(question):
    """Asks a question, accepts only Attach, negotiate, search or eat"""
    while True:
        player_choice = input(question).strip().upper()
        if player_choice in ("attack, negotiatem, search, eat")
            return player_choice
class wronganswer_exception):
    """Custom exception, multiple options"""
    pass

player_choice=input("What action would you like to take? Type attack, negotiate, search or eat" (attack, negotiate, search, eat))
print(player_choice)


#roll dice for attack
from random import randint
while true:
for attack in player_choice:
if player_choice ==attack:
    Dice_Sides = 20
Attack_dice_roll=(random.randint(1,Dice_Sides))
Player_score=Attack_dice_roll+ability
#six_sided_dice
six_Dice_Sides = 6
Win_Attack_dice_roll=(random.randint(1,six_Dice_Sides))

if Player_score> 12:
    print("You Hit!")
second_attack_round= (random.randint(1,six_Dice_Sides)+ Player_score)

print("Nice, you earned a damage score of: ", second_attack_round)
if Player_score == 12:
    print("You Hit!")
if Player_score< 12:
    print("You missed!")

    raise Wronganswer()
else:

#negotiate
while true:
for negotiate in player_choice:
elif player_choicew ==negotiate:
Attack_dice_roll=(random.randint(1,Dice_Sides))
negotiate_player=Attack_dice_roll+ability
if negotiate_player> 15:
    print("You Successfully negotiated a truce.")
if negotiate_player == 15:
    print("You Successfully negotiated a truce.")
else:
    print("You missed!")
    break
else:
#search
while true:
for search in player_choice:
elif player_choice ==search
Attack_dice_roll=(random.randint(1,Dice_Sides))
Search_player=Attack_dice_roll+ability
if Search_player > 12:
    print("You have found a treasure!")
if Search_player == 12
    print("You have found a treasure!")
if Search_player < 12:
    print("You have found nothing.")
    break
else:

#eat choice
while true:
for eat in player_choice:
elif player_choice ==eat
Attack_dice_roll = (random.randint(1, Dice_Sides))
eat_player=Attack_dice_roll+ability
if eat_player > 10
    print("Your were able to handle the rancid food.")
if eat_player== 10
    print("Your were able to handle the rancid food.")
if eat_player < 10
    print("You are sick, stay in bed and feel better.")





