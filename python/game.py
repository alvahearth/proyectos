import re

# BASE STATS
health = 100
strength = 100
magic = 100
defense = 100

# BASE ATTACKS
slash = 70
kick = 50
punch = 30


def dañoCalculo(x):
    if x == 1:
        return int((slash * strength) / 150)
    if x == 2:
        return int((kick * strength) / 150)
    if x == 3:
        return int((punch * strength) / 150)


def dañoenemigo(x):
    return int(x * 1.5) - defense


def stats():
    print("Health:", " ", health)
    print("Strength:", strength)
    print("Magic:", "  ", magic)
    print("Defense:", "", defense)


def lineas():
    print("------------")


print(" ")
print("\t\t\t\t********************************")
print("\t\t\t\t*Welcome to the world of Astera*")
print("\t\t\t\t********************************")
print("")
print("You encounter yourself stranded in an island far away from your homeland")
print("You begin to search your surroundings to find anything useful")
print(
    "You see a suspicious looking chest and you think to yourself if you should actually open it or not\n"
)
while True:
    print("1.- Open chest , and see what you can find")
    print("2.- Ignore the chest , and just keep going")
    print("")
    user = input("What are you going to do: ")
    print("")
    if user == "1":
        print("You opened the chest and you found a magic apple")
        print("Wich for some reason boost your inner vitality")
        print('"Health + 20"')
        health = health + 20
        print("------------")
        stats()
        print("------------")
        break
    if user == "2":
        print(
            "You decide yourself to ignore the chest,even though it looked to good to bre true"
        )
        print("You keep going")
        stats()
        break
    else:
        print("You only have those two choices")
        continue
print("")
print("While you were walking you see far away an islander")
print(
    "You aproach him, he looks very rough and it appears that he hasn't showered for months or even more"
)
print(
    'You say "Hi" in a friendly manner waiting for a response and you do not get one.'
)
print("What are you going to do: ")

enemy1health = 100
islander1attack = 80

# Encounter with first enemy
while True:
    if enemy1health <= 0:
        print("")
        print(
            "You have killed the islander, even tought it makes you sick, there was no other way around, you scavenge the area for anything useful and you find some clothes that are way better than the raggs you have right now"
        )
        print("Your defense is increased by 50 points\n")
        defense = defense + 50
        stats()
        break
    print("")
    print("1.- Keep insisting")
    print("2.- Keep you efforts in something more worthwhile")
    print("")
    user1 = input("Choose wisely: ")
    print("")
    if user1 == "1":
        print(
            "You keep talking waiting for a response just before you lose hope for answers, the islander says something"
        )
        print(
            "But is not something you were expecting\nHe did not know how to speak your language"
        )
        print(
            "The islander rose up and gets in a battle position, you a your old knife are your only way out"
        )
        lineas()
        stats()
        lineas()
        # Player turns
        turno = 0
        while enemy1health > 0:
            if turno == 0:
                print("")
                print("It's your turn")
                print("1.- Slash")
                print("2.- Kick")
                print("3.- Punch")
                print("4,. See stats")
                print("")
                user = input("What action will you use :")
                print("")
                if user == "1":
                    number = int(user)
                    print("You use your knife to a slash to an enemy: ")
                    print(
                        "The islander receives", dañoCalculo(number), "points of damage"
                    )
                    enemy1health = enemy1health - dañoCalculo(number)
                    print("The health of the enemy is:", enemy1health)
                    turno = turno + 1
                elif user == "2":
                    number = int(user)
                    print("You kick your opponent and he loses stability")
                    print(
                        "Your opponents receives",
                        dañoCalculo(number),
                        " points of damage and you gain 20 points of health",
                    )
                    enemy1health = enemy1health - dañoCalculo(number)
                    print("The health of the enemy is:", enemy1health)
                    health = health + 20
                    print("Your current health is:", health)
                    turno = turno + 1
                elif user == "3":
                    number = int(user)
                    print("You punch your opponent")
                    print(
                        "It's not very effective but your opponent receives",
                        dañoCalculo(number),
                        "points of damage and you gain 40 points of health",
                    )
                    enemy1health = enemy1health - dañoCalculo(number)
                    health = health + 40
                    print("The health of the enemy is:", enemy1health)
                    print("Your current health is:", health)
                    turno = turno + 1
                elif user == "4":
                    lineas()
                    stats()
                    lineas()
                    continue
                elif user == "5":
                    break
            # Enemy turns
            elif turno == 1:
                print("")
                playerdamage = dañoenemigo(islander1attack)
                print(
                    "The enemy attacks you and deals", playerdamage, "points of damage"
                )
                health = health - playerdamage
                print("Your current health is: ", health)
                turno = turno - 1
                continue
    elif user1 == "2":
        print("You give up and peace out from there before things turn ugly\n")
        break
    else:
        print("You only have those options")
        continue
print("")
print(
    "You continue on your journey trought the island and you see very quaint fair\nThere are at least 15 vendors, and as you might guest there is more life in this island that it seemed at first"
)

print(
    'You search your pockets if you have something, anything valuable, and in the deepest corners of your pockets you find a little bag of coins, you say to yourself "This must be valuable", you ask around and in fact they ARE valuable'
)

print(
    "You open the bag and there are 20 of them, you decide to see what you can buy since there might not be a better time than this\nYou lay your eyes in four particular shops"
)

# Shopping sequence
coins = 20
while True:
    print("")
    print("1.- Weapon shop")
    print("2.- Armor shop")
    print("3.- Canteen")
    print("4.- See stats")
    print("5.- ????")
    print("6.- Leave shops")
    print("")
    user = input("Which will you visit: ")
    print("")
    if user == "1":
        print(
            "You see a funny looking fellow with a big,big beard, You get down to bussines quickly"
        )
        print(
            '"Howdy young fellow you might need a bigger weapon than that little kitchen knife"'
        )
        print("")
        print("1.- Yes")
        print("2.- No")
        print("")
        user1 = input('"Are you going to buy something or what: "')
        print("")
        if user1 == "1":
            print('"Nice, I have a prime selection of weapons"')
            print("")
            print("1.- Scimitar + 50 strength / 6 coins")
            print("2.- lance + 80 strength / 10 coins")
            print("3.- lightsaber + 700 strength / 500 coins")
            print("")
            user2 = input("Which looks the best for you:")
            print("")
            if coins < 6:
                print("Not enough cash stranger")
                continue
            if user2 == "1":
                print("nice choice")
                strength = strength + 50
                coins = coins - 6
                print("your strength has increased 50 points")
                print("You current strenght is:", strength)
                print("You spent 6 coins, your remaining coins are:", coins)
            elif user2 == "2":
                print("You like the big stuff,nice")
                strength = strength + 80
                coins = coins - 10
                print("your strength has increased 80 points")
                print("You current strenght is:", strength)
                print("You spent 10 coins, your remaining coins are:", coins)
            elif user2 == "3":
                print(
                    "That thing is something else, I do not know where it came from but looked cool and with a price to match"
                )
                print(
                    "Sadly you don't have enough money, and probably you never will haha"
                )
        elif user1 == "2":
            print("Fine, but you are missing out big time")
            continue
        else:
            print("What?")
            continue
    elif user == "2":
        print(
            "You go to the armor shop looking for something useful and the owner of the shop greets you with a very big smile"
        )
        print('"Hello young man, How can I help you')
        print("")
        print("1.- I would like to buy something:")
        print("2.- Emm, I got confused, see ya")
        print("")
        user1 = input("What will you say: ")
        print("")
        if user1 == "1":
            print("Sure, I,ve got a fine collection just for you")
            print("")
            print("1.- Light vest + 70 defense / 7 coins")
            print("2.- Copper vest + 120 defense / 9 coins")
            print("3.- Combat vest + 30 defense + 50 strength / 10 coins")
            user2 = input("What will you buy: ")
            print("")
            if user2 == "1":
                print(
                    "Good, good, you could buy something better but it is affordable so I can't judge you"
                )
                defense = defense + 70
                coins = coins - 7
                print("Your current defense is:", defense)
                print("You spent 7 coins, your remaining coins are:", coins)
            elif user2 == "2":
                print("Nice choice, this thing can even parry arrows")
                defense = defense + 120
                coins = coins - 9
                print("Your current defense is:", defense)
                print("You spent 9 coins, your remaining coins are:", coins)
            elif user2 == "3":
                print(
                    "This is my favorite, agrresive and defensive, just how I like them"
                )
                defense = defense + 30
                strength = strength + 30
                coins = coins - 10
                print("Your current defense is:", defense)
                print("Your current strength is:", strength)
                print("You spent 10 coins, your remaining coins are:", coins)
            else:
                print("You're wasting my time kid")
                continue

        elif user1 == "2":
            print("Move along boy, I've got shit to sell")
            continue
        else:
            print("Move along boy, I've got shit to sell")
            break
    elif user == "4":
        lineas()
        stats()
        lineas()
        continue

    elif user == "6":
        break

print("asdasd")
