from time import sleep
import os
import random
from random import randint
from status_screen import print_status, zombification, hunger


msg=""
inventory=[]
maxzombi = 10  #Max value for health bar
playerzombi = 1 # players current health
survivor_count = 0 # tracks number of survivors with player
max_hunger=10 #max hunger before player dies
player_hunger= 10 #tracks players current hunger level
totalzombi= maxzombi - playerzombi
hpdisplay = chr(0x2588) + chr(0x2502)
dashdisplay = chr(0x2591) + chr(0x2502)
total_hunger= max_hunger - player_hunger


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
        player_hunger-=1
    elif encounter==1:
        inventory.append("Bandages"); 
        print("You found bandages and added them to your inventory")
        playerzombi+=1
        player_hunger-=1
    elif encounter==2:
        survivor_count +=1
        print("A group of survivors approach you cautiously.")
        playerzombi+=1
        player_hunger-=1
    elif encounter==3:  
        print("You hear a distant scream and feel uneasy.")
        playerzombi+=1
        player_hunger-=1
        

    # Function to determine the chance of an encounter
def encounter_chance(turns):
    base_chance = 0.1  # Initial chance of encounter
    max_chance = 0.8  # Maximum chance
    return min(base_chance + (turns * 0.05), max_chance)