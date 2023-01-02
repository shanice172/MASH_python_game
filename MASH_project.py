import time
import random


def game_intro():
    print("\n --------------------------------------------")
    print("|                  M.A.S.H.                  |")
    print("|   Mansion    Apartment    Shack    House   |")
    print(" --------------------------------------------")

    print("\nWelcome to the game of M.A.S.H., the fortune-telling game!")

    print("\nIn this game, we'll explore a few life categories.")
    print("But we'll need your help along the way!\n")

    while True:
        prompt = input("Are you ready? Yes or No: \n")

        if prompt.lower() == "yes":
            print("\nPerfect. Let's discover what the future has in stored for you.\n")
            play_through()
            break

        elif prompt.lower() == "no":
            print("\nYour future awaits you another day.\n")
            break

        else:
            print("\nInvalid response. Try again\n")


def play_through():
    player_name = input("What is your name? ")
    print("Okay", player_name +
          ", let's look at our first fortune-telling category...\n")

    time.sleep(2)
    print("\n --------------------------------------")
    print("|    Category 1: Your Future Spouse    |")
    print(" --------------------------------------")

    print("\nWe need you to enter 3 celebrities whom you'd like to marry.")
    spouse1 = input("Celebrity 1: ")
    spouse2 = input("Celebrity 2: ")
    spouse3 = input("Celebrity 3: ")

    print("\nNow, we will pick your 4th possible spouse...")
    spouse4_options = ["Kim Kardashian", "Kanye", "Jada Smith",
                       "Will Smith", "Jeffree Star", "Donald Trump", "Hilary Clinton"]
    spouse4 = random.choice(spouse4_options)
    time.sleep(3)
    print("It's", spouse4 + "!")
    time.sleep(2)
    print("\nLet's look at the next category\n")
    spouse_list = [spouse1, spouse2, spouse3, spouse4]

    time.sleep(3)
    print("\n ---------------------------------------")
    print("|    Category 2: Your Future Vehicle    |")
    print(" ---------------------------------------")

    print("\nEnter your top 3 dream vehicles.")
    vehicle1 = input("Vehicle 1: ")
    vehicle2 = input("Vehicle 2: ")
    vehicle3 = input("Vehicle 3: ")

    print("\nNow, we will pick your 4th possible vehicle...")
    vehicle4_options = ["rocket ship", "monster truck", "school bus",
                        "scooter", "bicycle", "firetruck"]
    vehicle4 = random.choice(vehicle4_options)
    time.sleep(3)
    print("It's a", vehicle4 + "!")
    time.sleep(2)
    print("\nWe are halfway there. Let's look at the next category\n")
    vehicle_list = [vehicle1, vehicle2, vehicle3, vehicle4]

    time.sleep(4)
    print("\n ----------------------------------------")
    print("|    Category 3: Your Future Children    |")
    print(" ----------------------------------------")

    print("\nNow, we will predict the number of children you will have.\n")
    print("Enter your 3 favorite numbers")
    children1 = input("1st favorite number: ")
    children2 = input("2nd favorite number: ")
    children3 = input("3rd favorite number: ")

    print("\nNow, we will chose a number for you...")
    children4 = random.randint(100, 10000)

    time.sleep(3)
    print("It's {}!".format(children4))
    time.sleep(2)
    children_list = [children1, children2, children3, children4]
    print("\nLet's look at our last category.\n")

    time.sleep(3)
    print("\n ----------------------------------------")
    print("|    Category 4: Your Future Hometown    |")
    print(" ----------------------------------------")

    print("\nEnter 3 cities that you would LOVE to live in")
    city1 = input("City 1: ")
    city2 = input("City 2: ")
    city3 = input("City 3: ")

    print("\nNow, we will chose a city for you... ")
    city4_options = ["Pompeii", "Silent Hill",
                     "Schitt's Creek", "The Jersey Shore", "Bikini Bottom", "Gotham"]
    city4 = random.choice(city4_options)

    time.sleep(3)
    print("It's", city4 + "!")
    time.sleep(2)
    city_list = [city1, city2, city3, city4]

    spouse = random.choice(spouse_list)
    vehicle = random.choice(vehicle_list)
    children = random.choice(children_list)
    city = random.choice(city_list)

    dwelling_list = ["mansion", "apartment", "house", "shack"]
    dwelling = random.choice(dwelling_list)

    print("\nThank you for your responses! We have everything we need.\n")

    time.sleep(3)
    print("\n ----------------------------------------")
    print("|              Your Fortune              |")
    print(" ----------------------------------------")
    print("\nOur experienced fortune-tellers will now predict your future...\n")
    time.sleep(5)

    print(player_name + ", you will marry", spouse, "and have", children,
          "kids. You will drive a", vehicle, "and live in a", dwelling, "in", city + "!\n")

    play_again()


def play_again():
    while True:
        try_again = input("Would you like to try again? Yes or No\n")
        if try_again.lower() == "yes":
            game_intro()
            break
        elif try_again.lower() == "no":
            print("Goodbye!")
            break
        else:
            print("\nInvalid response.\n")


game_intro()
