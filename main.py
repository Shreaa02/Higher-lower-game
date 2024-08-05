from art import logo, vs
from random import randint
from game_data import data

l = len(data)


def choice():
    """This will return a random dictionary from the game data list"""
    return data[randint(0, l - 1)]


def compare(a, b):
    """This will compare the number of followers of the two dictionaries and will return name from the dictionary
    having the highest number of followers"""
    if a['follower_count'] > b['follower_count']:
        return (a,'A')
    else:
        return (b,'B')


def higher_lower_game():
    sc = 0
    option_1 = choice()
    while True:
        option_2 = choice()
        while option_2 == option_1:
            option_2 = choice()
        # print(f"A : {option_1['follower_count']} ")
        # print(f"B: {option_2['follower_count']}")
        print(f"A : {option_1['name']} from {option_1['country']} , a {option_1['description']} ")
        print(vs)
        print(f"B : {option_2['name']} from {option_2['country']} , a {option_2['description']}")
        print("-" * 200)
        com,higher = compare(option_1, option_2)
        print("-" * 200)
        guess = input("Guess who is having more followers :").upper()
        print("-" * 200)
        if guess == higher:
            sc += 1
            option_1 = com
            print(f"score = {sc}")
            print("-" * 200)
        else:
            print(f"score = {sc}")
            return 0
            break


print(logo)
print("Welcome to higher lower game !!!\n")

while True:
    v = higher_lower_game()
    if v == 0:
        ch = input("Whether you want to continue playing\nyes --> 'y'\tno --> 'n'\nEnter choice:").lower()
        if ch == 'n':
            print("Game Over !!")
            break
        else:
            print("-" * 200)
            print("New Game")
