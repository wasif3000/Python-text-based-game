from time import sleep
import os
import random
from random import randint
from status_screen import print_status, zombification, hunger

# Dictionary of locations
locations = {
    "landing_room": {
        "description": "You are in the landing room. You quickly glance around the room taking in the surrounding area. It appears to be a regular living room but with funtiure smashed to pieces.  You can look around or leave the house.",
        "options": {
            "1": {"description": "Look around the room", "next": "landing_room"},
            "2": {"description": "Leave the house", "next": "outside"}
        }
    },
    "outside": {
        "description": "You are outside the house. You see a path leading to the forest and another to the town.",
        "options": {
            "1": {"description": "Go to the forest", "next": "forest"},
            "2": {"description": "Go to the town", "next": "town"}
        }
    },
    "forest": {
        "description": "The forest is dense and eerie. You see a cabin in the distance.",
        "options": {
            "1": {"description": "Approach the cabin", "next": "cabin"},
            "2": {"description": "Return to the house", "next": "landing_room"}
        }
    },
    "town": {
        "description": "The town is deserted. You see an old store that might have supplies.",
        "options": {
            "1": {"description": "Enter the store", "next": "store"},
            "2": {"description": "Explore further into the town", "next": "explore_town"}
        }
    },
    # Additional locations can be added here
}


#Clears the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear') # call this function to clear the players screen before progressing
    
msg=""
inventory=[]
maxzombi = 10  #Max value for health bar
playerzombi = 1 # players current health
survivor_count = 0 # tracks number of survivors with player
max_hunger=10 #max hunger before player dies
player_hunger= 0 #tracks players current hunger level
totalzombi= maxzombi - playerzombi
hpdisplay = chr(0x2588) + chr(0x2502)
dashdisplay = chr(0x2591) + chr(0x2502)
total_hunger= max_hunger - player_hunger

#The healthbar function
# def zombification():
#     global playerzombi
#     global totalzombi
#     global hpdisplay
#     global dashdisplay
#     dishp = hpdisplay * playerzombi
#     dashzero = dashdisplay * totalzombi
#     overall_health= dishp + dashzero
#     if playerzombi < 0:
#         playerzombi = 0
#     elif playerzombi< maxzombi:
#         return overall_health
#     elif playerzombi == maxzombi:
#         print("You were unable to contain the zombie virus any longer: GAME OVER")          # keeps the health from going below 0 and above 10
#         return False

#     return True

# def print_status():
#     print (zombification())


# clear()

# # Hunger meter
# def hunger():
#     global player_hunger
#     global total_hunger
#     global hpdisplay
#     global dashdisplay
#     dishp = hpdisplay * player_hunger
#     dashzero = dashdisplay * total_hunger
#     overall_hunger=dishp*dashzero
#     if player_hunger < 0:
#         player_hunger = 0
#     elif player_hunger < max_hunger:
#         return overall_hunger
#     elif player_hunger == max_hunger:
#         print("You starved to death")          # keeps the health from going below 0 and above 10
#         return False
#     return True



clear()

# will pop up before the game starts, a little intro
def prompt():
    print("\t\t Welcome to our game!!!\n\n\
    There are multiple endings for you to discover along the way\n\n")
prompt()
input("Press enter to continue...") #input with no use will pause the continuation until user input
clear()


def random_encounter():
    global player_hunger
    global playerzombi
    global survivor_count
    encounters = [
        "A zombie jumps out at you!",
        "You find a mysterious item on the ground.",
        "A group of survivors approach you cautiously.",
        "You hear a distant scream and feel uneasy.",
    ]
    encounter= randint(0,len(encounters)-1)
    if encounter == 0:
        playerzombi +=1 ; print("A zombie jumps out at you!")
    elif encounter==1:
        inventory.append("Bandages"); 
        print("You found bandages and added them to your inventory")
        playerzombi+=1
        player_hunger+=1
    elif encounter==2:
        survivor_count +=1
        print("A group of survivors approach you cautiously.")
        playerzombi+=1
        player_hunger+=1
    elif encounter==3:  
        print("You hear a distant scream and feel uneasy.")
        playerzombi+=1
        player_hunger+=1
        

    # Function to determine the chance of an encounter
def encounter_chance(turns):
    base_chance = 0.1  # Initial chance of encounter
    max_chance = 0.8  # Maximum chance
    return min(base_chance + (turns * 0.05), max_chance)



    # Function to navigate between locations
def navigate_location(current_location, turns_taken):
    global msg, playerzombi, player_hunger
    clear()
    if not zombification():
        return  # Exit the function if the player is dead
    if not hunger():
        return

    # print(f"INVENTORY {inventory}\nSurvivor count={ survivor_count}\n{'-' * 27}")
    # print(msg)

        # Check for a random encounter
    if random.random() < encounter_chance(turns_taken):
        random_encounter()
        if not zombification():
            return  # Exit the function if the player is dead
        sleep(1)

        # Get location data from the dictionary
    location = locations[current_location]
    print_status()
    print(location["description"])
    for key, option in location["options"].items():
        print(f"[{key}] {option['description']}")

    user_input = input("Choose an option: ")

    if user_input in location["options"]:
        msg = f"You chose: {location['options'][user_input]['description']}."
        next_location = location["options"][user_input]["next"]
        navigate_location(next_location, turns_taken + 1)
        msg = "Not a valid input. Try again."
        sleep(1)
        navigate_location(current_location, turns_taken)
        
    # Main game loop, starting with the landing room IMPORTANT!
turns_taken = 0
navigate_location("landing_room", turns_taken)
