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
        "description": "You are in the landing room. You quickly glance around the room taking in the surrounding area.\n It appears to be a regular living room but with funtiure smashed to pieces and thrown agross the room as if they were after something or in a voilent rage.\n The only a few things our still standing in the room. You can look around or leave the house.",
        "options": {
            "1": {"description": "Look around the room", "next": "searched room"},
            "2": {"description": "Leave the house", "next": "outside"}
        },
        "visited": False
    },
    "searched room": {
        "description": f"You rummage around the room and found a few items in a pile of rubble.", 
        "item": "Medkit",
        "options": {
            "2": {"description": "Leave the house", "next": "outside"}
        },
        "visited": False
        
    },
    "outside": {
        "description": "You are outside the house.\n You see a path long winding path with flowers covering most of it leading towards a mysterious looking forest with tall dark trees making it hard to see into.\n Whilst next to it you see another path one more moden looking with the classic brick like path with a nearly broken looking street lights down on along the path flickering randomly on and off allumintaing a sign pointing towards the nearest town.",
        "item": "Filler",
        "options": {
            "1": {"description": "Go to the forest", "next": "forest"},
            "2": {"description": "Go to the town", "next": "town"}
        },
        "visited": False
        
    },
    "forest": {
        "description": "The forest is dense and eerie. The trees block out most of the sun only allowing small amount of light to peer in.\n  You feel like someones watching you whilst you slowly walk your way through.\n Its as though your seeing faces in trees or were they just past the trees.\n You see an abandond cabin not that far away.",
        "item": "Filler",
        "options": {
            "1": {"description": "Approach the cabin", "next": "cabin"},
            "2": {"description": "Return to the house", "next": "outside"}
        },
        "visited": False

    },
    "cabin": {
        "description": "As you approch the cabin you a standing mail post by the fence of the proerty with a massive heart on the side of it.\n Inside the heart is written D+I proberbly the inteals of the previous owners.\n Sat out on the porch are two bowls on dog size and another cat size with the names Shy and Loki written on them respectively.\n As you slowly enture the cabin you take in the interior of the room.\n You see against a wall a massive sword next to a bow above a a fire place with a photo of one the owners on a majestic horse.\n Across from the fire place sits a cute coffee table with some books stacked on top of eachother at the top you see The song of Achilles.\n You can tell the owners loved this place dearly",
        "item": "Filler", 
        "options": {
            "1": {"description": "leaves", "next": "outside"},
        },
        "visited": False

    },
    "town": {
        "description": "The town is deserted basicaly no noise anywhere the only thing heard is the sound of rats scurrying around looking for trash to eat.\n You see an old abandoned store with its windows smashed in creating a hole to climb through to get in.\n You see that they still have some supplies left which could help you in your journey.",
        "item": "Key", 
        "options": {
            "1": {"description": "Enter the store", "next": "store"},
            "2": {"description": "Explore further into the town", "next": "explore town"},
            "3": {"description": "Go to the basement", "next": "players home basement", "requires": "Key"}
        },
        "visited": False

    },
    "local spoons": {
        "description": "As you continue walking through the remains of the town you. Every place looks closed down and abandoned, windows broken. Cars abandond on the streets. As you wander round the town you start giving up hope of finding others till you heard that noise. It sounded like screams nut not scared screams it sound like joy. You started running towards it and as you turned the corner you see a bar open with people in. The windows have table up against them blocking people from breaking them down and the only entrance you can see is a massive door with people staiond infrount of them probably watching out for zombies.",
        "item": "Filler", 
        "options": {
            "1": {"description": "Enter the store", "next": "players home"},
            "2": {"description": "Explore further into the town", "next": "characters school school"}
        },
        "visited": False

    },
    "players home": {
        "description": "As you walk up to your home, memoires of the place come flooding back to you.\n You remeber when you first bought it with your partner,\n your remeber walking into the house after your wedding with your wife in your arms,\n when you brought your child home for the first time.\n It looks exactly as you rember it except from all the damages from the zombie attacks.\n You lookaround the interiour of the room and your eyes lock onto the door leading to what your remember being a basement\n but if it was just a basement why does the door looks so metalic likes its trying to keep people out?",
        "item": "Key", 
        "options": {
            "1": {"description": "Enter the store", "next": "charcters sons school"},
            "2": {"description": "Enter the store", "next": "museum"},
            "3": {"description": "Go to the basement", "next": "players home basement", "requires": "Key"}
        },
        "visited": False

    },
    "players home basement": {
        "description": "As you slowly open the heavy door you see nothing but a metalic stair case with nothing else but a few dimmly lit bulbs hanging above it eerierly inviting you down to see what it has instore for you.\n As you slowly make your way to the end of the stair case panic starts to set in what if this is where it all started?\n What if there is nothing left in?\n What if?\n. As you slowly open the last door you see walls lined with selfs and draws with food, bandages and supplies everywhere this isnt where it started\n this is a panic room for you and your family to hide incase of this such scenario.",
        "item": "Filler", 
        "options": {
            "1": {"description": "Enter the store", "next": "store"},
            "2": {"description": "Explore further into the town", "next": "explore_town"}
        },
        "visited": False

    },
"charcters sons school": {
        "description": "You arrive at what you remeber being your sons school.\n It looks different from how you remember most of the doors are boarded up except for one set of double doors.\n From closer inseption you are able to work out thats its become a tempoary safe place.\n However you see zombies trying to break in from the sides to many for the people to handle.\n You desicde you have to rsuh in and try to warn people.",
        "item": "Filler", 
        "options": {
            "1": {"description": "Enter the store", "next": "players home"},
            "2": {"description": "Explore further into the town", "next": "museum"}
        },
        "visited": False

    },
    "museum": {
        "description": "You approch the massive building looking older than any of the other buildings in the area.\n The building looked as if its been untouched throughout all of this madness.\n As you reach the door you notice there is people inside hiding ",
        "item": "Filler", 
        "options": {
            "1": {"description": "Enter the store", "next": "players home"},
            "2": {"description": "Explore further into the town", "next": "charcters son school"}
        },
        "visited": False

    },
}
def add_to_inventory(item):
    if item in inventory:
        inventory[item] += 1
    else:
        inventory[item] = 1

def remove_from_inventory(item):
    if item in inventory and inventory[item] > 0:
        inventory[item] -= 1
        if inventory[item] == 0:
            del inventory[item]  # Remove the item if the quantity is 0
        print(f"You used {item}.")
        return True
    else:
        raise ValueError(f"You have no {item}.")


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
    # Ensure health is always clamped within the range but allow it to exceed for display purposes
    display_zombi = min(playerzombi, maxzombi)
    totalzombi = maxzombi - display_zombi
    dishp = hpdisplay * display_zombi
    dashzero = dashdisplay * totalzombi
    overall_health = dishp + dashzero
    return overall_health  # Always return the overall health string for display

def hunger():
    global player_hunger
    # Ensure hunger is clamped within the range but allow it to exceed for display purposes
    display_hunger = min(player_hunger, max_hunger)
    total_hunger = max_hunger - display_hunger
    dishp = hpdisplay * display_hunger
    dashzero = dashdisplay * total_hunger
    overall_hunger = dishp + dashzero
    return overall_hunger  # Always return the overall hunger string for display

def hunger_timer():
    global player_hunger, game_over
    while not game_over:
        time.sleep(60)  # Set to 60 seconds for the real game
        if player_hunger > 0:
            player_hunger -= 1
            player_hunger = max(0, player_hunger)  # Clamp to ensure it doesn't go negative
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
    player_hunger = max_hunger  # Set to max_hunger
    playerzombi = maxzombi  # Set to maxzombi
    survivor_count = 0
    inventory = {}
    game_over = False
    clear()
    start_game()

def show_description(description):
    lines = description.split("\n")
    for line in lines:
        print(line)
        time.sleep(0.5)
        clear() 

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
    
    location = locations[current_location]

    # Clear the screen first before showing the description or status
    clear()
    
    # Show the description only if the location hasn't been visited
    if not location.get("visited", False):
        show_description(location["description"])
        location["visited"] = True  # Mark as visited

    if not zombification() or game_over:
        return  # Exit the function if the player is dead
    if not hunger() or game_over:
        return

    # Check for items in the location and add to inventory
    if "item" in location:
        item = location["item"]
        if item not in inventory:
            add_to_inventory(item)
            # Display the message about finding the item and add a delay
            print(f"You found a {item} and added it to your inventory.")
            sleep(2.0)
            clear()  # Clear the screen after the message and before showing the status
            del location["item"]  # Remove the item from the location to prevent multiple pickups

    # Call print_status to display the updated inventory
    print_status(current_location)

    # Display the available options
    for key, option in location["options"].items():
        # Check if the option has a requirement and if the player has the item
        if "requires" in option and option["requires"] not in inventory:
            print(f"[{key}] {option['description']} (You need a {option['requires']} to access this)")
        else:
            print(f"[{key}] {option['description']}")

    user_input = input("Choose an option: ")

    if user_input == 'H' or user_input == 'h':
        show_controls_menu()
        navigate_location(current_location, turns_taken)  # Return to the same location after showing menu

    # Process item usage
    if user_input == "B" or user_input == "b":
        try:
            remove_from_inventory("Bandages")
            playerzombi = max(minzombi, playerzombi - 1)  # Heal but keep within bounds
            print("You have used a bandage.")
            sleep(2.0)
        except ValueError as e:
            print(e)

    if user_input == "M" or user_input == "m":
        try:
            remove_from_inventory("Medkit")
            playerzombi = max(minzombi, playerzombi - 2)  # Heal but keep within bounds
            print("You have used a Medkit.")
            sleep(2.0)
        except ValueError as e:
            print(e)

    if user_input == "R" or user_input == "r":
        try:
            remove_from_inventory("Ration")
            player_hunger = min(max_hunger, player_hunger + 1)  # Increase but keep within max_hunger
            print("You have eaten a ration.")
            sleep(2.0)
        except ValueError as e:
            print(e)

    if user_input == "F" or user_input == "f":
        try:
            remove_from_inventory("Fasting_potion")
            player_hunger = min(max_hunger, player_hunger + 2)  # Increase but keep within max_hunger
            print("You pay your respects.")
            sleep(2.0)
        except ValueError as e:
            print(e)

    if user_input in location["options"]:
        option = location["options"][user_input]
        if "requires" in option and option["requires"] not in inventory:
            msg = f"You need a {option['requires']} to access this area."
            sleep(2)
            navigate_location(current_location, turns_taken)  # Return to the same location

        msg = f"You chose: {option['description']}."
        next_location = option["next"]

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

