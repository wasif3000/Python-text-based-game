from time import sleep
import os
import random
from random import randint
import threading
import time
import sys

msg=""
inventory={}
maxzombi = 10  #Max value for health bar
minzombi= 0
playerzombi = 1 # players current health
survivor_count = 0 # tracks number of survivors with player
max_hunger=10 #max hunger before player dies
player_hunger= 10 #tracks players current hunger level
game_over = False #this is what we will use for all deaths and use for function to restart game
hpdisplay = chr(0x2588) + chr(0x2502)
dashdisplay = chr(0x2591) + chr(0x2502)
hunger_message = ""

locations = {
    "landing_room": {
        "description": "You are in the landing room. You quickly glance around the room taking in the surrounding area.\n It appears to be a regular living room but with funtiure smashed to pieces.  You can look around or leave the house.",
        "options": {
            "1": {"description": "Look around the room", "next": "searched_room"},
            "2": {"description": "Leave the house", "next": "outside"}
        }
    },
    "searched_room": {
        "description": f"You rummage around the room and found a few items in a pile of rubble.", 
        "item": "Medkit",
        "options": {
            "2": {"description": "Leave the house", "next": "outside"}
        }
    },
    "outside": {
        "description": "You are outside the house. You see a path leading to the forest and another to the town.",
        "item": "Ration",
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
def add_to_inventory(item):
    if item in inventory:
        inventory[item] += 1
    else:
        inventory[item] = 1
    print(f"You found {item} and added it to your inventory.")

def remove_from_inventory(item):
    if item in inventory and inventory[item] > 0:
        inventory[item] -= 1
        if inventory[item] == 0:
            del inventory[item]  # Remove the item if the quantity is 0
        print(f"You used {item}.")
        return True
    else:
        # Simulate the ValueError if the item doesn't exist
        raise ValueError(f"You have no {item}.")

def show_description(description):
    lines = description.split("\n")
    for line in lines:
        print(line)
        time.sleep(2)
        clear() 

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') # call this function to clear the players screen before progressing

def show_controls_menu():
    clear()
    print("############## CONTROLS MENU ##############")
    print("Use Number buttons to navigate between scenarios")
    print("Press 'B' to use Bandages - Heal 1HP")
    print("Press 'M' to use Medkit - Heal 2HP")
    print("Press 'R' to eat Ration - Fill 1 hunger")
    print("Press 'F' to drink Fasting Potion - Fill 2 hunger and pay respect")
    print("\nPress 'Q' to go back to the game...")
    input("Press Enter to go back to the game...")  # Pauses until the player presses Enter
    clear()

def game_loop():
    while True:
        clear()
        print("Game running...")
        print("Press 'H' anytime to show the controls menu")
        print("\n[1] Continue playing")
        print("[C] Show controls menu")

def rush():
    global inventory
    global playerzombi
    chances=["fail","fail","fail","fail","fail","fail","fail","success","success","success"]
    randnum=randint(0,len(chances))        
    if randnum <= 7:
        playerzombi +=2
        print("You tried to rush through the store and grab everything you could.\n You tripped and fell and were attacked by 2 zombies,they got you good")
    elif randnum> 7:
        add_to_inventory("Medkit")
        add_to_inventory("Fasting_potion")
def stealth():
    global inventory
    global playerzombi
    chances2=["fail","fail","success","success","success","success","success","success","success","success"]
    randnum2= randint(0,len(chances2))
    if randnum2<=2:
        playerzombi +=1
        print("you were sneaking about when a zombie casts detect, pinpointing your location\n You escape with just a scratch ")
    elif randnum2>2:
        add_to_inventory("Bandages")
        add_to_inventory("Ration")

def zombification():
    global playerzombi
    totalzombi = maxzombi - playerzombi
    dishp = hpdisplay * playerzombi
    dashzero = dashdisplay * totalzombi
    overall_health = dishp + dashzero

    # Ensure health can't go below minimum
    if playerzombi < minzombi:
        playerzombi = minzombi
    elif playerzombi > maxzombi:
        playerzombi = maxzombi

    return overall_health  # Always return the overall health string for display

def hunger():
    global player_hunger
    total_hunger = max_hunger - player_hunger
    dishp = hpdisplay * player_hunger
    dashzero = dashdisplay * total_hunger
    overall_hunger = dishp + dashzero

    # Ensure hunger can't go below minimum
    if player_hunger < 0:
        player_hunger = 0
    elif player_hunger > max_hunger:
        player_hunger = max_hunger

    return overall_hunger  # Always return the overall hunger string for display

def hunger_timer():
    global player_hunger, game_over
    while not game_over:
        time.sleep(60)  # Set to 30 seconds for the real game
        if player_hunger > 0:
            player_hunger -= 1
            print(f"\rYou have been on the move for a while. Hunger increased! Current hunger: {player_hunger}", end="")
            sys.stdout.flush()
            time.sleep(2)
            # Overwrite the line by moving the cursor back and clearing it
            print("\r" + " " * 80 + "\r", end="")
        if player_hunger == 0:
            print("\nYou starved to death: GAME OVER")
            game_over = True  # Set the game_over flag to end the game
            display_game_over_screen()
            break

def display_game_over_screen():
    clear()
    print("############################")
    print("#         GAME OVER        #")
    print("############################")
    print("\nRestarting the game in 5 seconds...")
    sleep(5)
    restart_game()

def restart_game():
    global player_hunger, playerzombi, game_over, survivor_count, inventory
    player_hunger = 10
    playerzombi = 1
    survivor_count = 0
    inventory = []
    game_over = False
    clear()
    start_game()

def print_status(current_location):
    
    print("ZOMBIFICATION:", zombification())
    print("")
    print("HUNGER:       ", hunger())
    print("INVENTORY:")
    for item, quantity in inventory.items():
        print(f" - {item}: {quantity}")
    print(f"Survivor count = {survivor_count}\n{'-' * 27}")
    print("LOCATION:      ", current_location.replace("_", " ").title())
    print(msg)

def start_game():
    hunger_thread = threading.Thread(target=hunger_timer, daemon=True)
    hunger_thread.start()
    navigate_location("landing_room", 0)

def navigate_location(current_location, turns_taken):
    global msg, playerzombi, player_hunger, inventory
    clear()
    location = locations[current_location]
    show_description(location["description"])

    print_status(current_location)

    if not zombification() or game_over:
        return  # Exit the function if the player is dead
    if not hunger() or game_over:
        return

    if "item" in location:
        add_to_inventory(location["item"])

    for key, option in location["options"].items():
        print(f"[{key}] {option['description']}")

    user_input = input("Choose an option: ")

    if user_input == 'H' or user_input == 'h':
        show_controls_menu()
        navigate_location(current_location, turns_taken)  # Return to the same location after showing menu

    # Process item usage
    if user_input == "B" or user_input == "b":
        try:
            remove_from_inventory("Bandages")
            playerzombi -= 1
            print("You have used a bandage.")
            sleep(2.0)
        except ValueError as e:
            print(e)

    if user_input == "M" or user_input == "m":
        try:
            remove_from_inventory("Medkit")
            playerzombi -= 2
            print("You have used a Medkit.")
            sleep(2.0)
        except ValueError as e:
            print(e)

    if user_input == "R" or user_input == "r":
        try:
            remove_from_inventory("Ration")
            player_hunger += 1
            print("You have eaten a ration.")
            sleep(2.0)
        except ValueError as e:
            print(e)

    if user_input == "F" or user_input == "f":
        try:
            remove_from_inventory("Fasting_potion")
            player_hunger += 2
            print("You pay your respects.")
            sleep(2.0)
        except ValueError as e:
            print(e)

    # user_input = input("Choose an option: ")

    if user_input in location["options"]:
        msg = f"You chose: {location['options'][user_input]['description']}."
        next_location = location["options"][user_input]["next"]

        # Check for a random encounter
        if random.random() < encounter_chance(turns_taken):
            random_encounter()  # Call the encounter function
            
            # Check if the player died during the encounter
            if not zombification() or game_over:
                return  # Exit the function if the player is dead

            sleep(1)

        # Continue to the next location
        navigate_location(next_location, turns_taken + 1)
    else:
        msg = "Not a valid input. Try again."
        sleep(1)
        navigate_location(current_location, turns_taken)

def random_encounter():
    global player_hunger
    global playerzombi
    global survivor_count
    encounters = [
        "A zombie jumps out at you!","A zombie attacks you!",
        "You find a mysterious item on the ground.",
        "A group of survivors approach you cautiously.",
        "You hear a distant scream and feel uneasy.",
    ]
    encounter= randint(0,len(encounters)-1)
    if encounter == 0 or encounter == 1:
        playerzombi +=1 ; print("A zombie jumps out at you!")

    elif encounter==2:
        add_to_inventory("Bandages"); 
        print("You found bandages and added them to your inventory")

    elif encounter==3:
        survivor_count +=1
        print("A group of survivors approach you cautiously.")
    elif encounter==4:  
        print("You hear a distant scream and feel... more hungry???.")
        player_hunger-=1

    # Function to determine the chance of an encounter
def encounter_chance(turns):
    base_chance = 0.1  # Initial chance of encounter
    max_chance = 0.8  # Maximum chance
    return min(base_chance + (turns * 0.05), max_chance)

clear()
def prompt():
    print("\t\tWelcome to Magic Zombie Land!!!\n\n")
    print("\t\tControls\n\n")
    print("\t\tPress 'B' to use Bandages - Heal 1HP\n")
    print("\t\tPress 'M' to use Medkit - Heal 2HP\n")
    print("\t\tPress 'R' to eat Ration - Fill 1 hunger\n")
    print("\t\tPress 'F' to drink Fasting Potion - Fill 2 hunger and pay respect\n")
    input("\t\tPress enter to continue...") #input with no use will pause the continuation until user input
    clear()
prompt()
hunger()
start_game()
navigate_location()
    # Function to navigate between locations


        
    # Main game loop, starting with the landing room IMPORTANT!
turns_taken = 0
navigate_location("landing_room", turns_taken)

