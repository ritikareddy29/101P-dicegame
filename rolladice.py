import random
question = input("Do you want to roll the dice or not? (y/n)")
while question != "n":
    if question == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(die1, die2)
        question = input('Would you like to roll the dice (y/n)')
    else:
        print('Please type "y" or "n".')
        question = input('Would you like to roll the dice [y/n]?')        
