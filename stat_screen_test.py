msg=""
inventory=[]
maxzombi = 10  #Max value for health bar
playerzombi = 1 # players current health
survivor_count = 0 # tracks number of survivors with player
max_hunger=10 #max hunger before player dies
player_hunger= 10 #tracks players current hunger level
hpdisplay = chr(0x2588) + chr(0x2502)
dashdisplay = chr(0x2591) + chr(0x2502)

def zombification():
    global playerzombi
    global totalzombi
    global hpdisplay
    global dashdisplay
    totalzombi= maxzombi - playerzombi
    dishp = hpdisplay * playerzombi
    dashzero = dashdisplay * totalzombi
    overall_health= dishp + dashzero
    # zombification_total="zombification: "(overall_health)
    if playerzombi < 0:
        playerzombi = 0
    elif playerzombi< maxzombi:
        return (overall_health)
    elif playerzombi == maxzombi:
        print("You were unable to contain the zombie virus any longer: GAME OVER")          # keeps the health from going below 0 and above 10
        return False

    return True

def hunger():
    global player_hunger
    global total_hunger
    global hpdisplay
    global dashdisplay
    total_hunger= max_hunger - player_hunger
    dishp = hpdisplay * player_hunger
    dashzero = dashdisplay * total_hunger
    overall_hunger=dishp + dashzero

    if player_hunger > 10:
        player_hunger = 10
    elif player_hunger <= max_hunger:
        return overall_hunger
    elif player_hunger == 0:
        print("You starved to death")          # keeps the health from going below 0 and above 10
        return False
    return True

def print_status():
    print ("ZOMBIFICATION:",(zombification()))
    print("")
    print ("HUNGER:       ",(hunger()))
    print(f"INVENTORY {inventory}\nSurvivor count={survivor_count}\n{'-' * 27}")
    print(msg)


print_status()

