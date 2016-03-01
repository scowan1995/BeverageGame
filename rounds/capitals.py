from random import randint as alan

def capital_round(players):
    # import capitals
    with open('capitals.txt', 'r') as f:
        p = f.read().splitlines()
        capitals = [x.split(',') for x in p]

    for player in players:
        print(player.getName() + " YOUR TURN")
        capital = capitals[alan(0, len(capitals)-1)]
        answer = input("What is the capital of " +  capital[0] + "\n")
        if answer.lower()==capital[1].lower():
            print("Correct! Pick a person to drink!")
        else:
            print("WRONG! Drink! The answer is: " + capital[1])

