from time import sleep
"\n"= sleep(5.0)
# of locations
locations = {
    "landing_room": {
        "description": "You are in the landing room. You quickly glance around the room taking in the surrounding area.\n It appears to be a regular living room but with funtiure smashed to pieces and thrown agross the room as if they were after something or in a voilent rage.\n The only a few things our still standing in the room. You can look around or leave the house.",
        "options": {
            "1": {"description": "Look around the room", "next": "landing_room"},
            "2": {"description": "Leave the house", "next": "outside"}
        }
    },
    "landing_room2": {
        "description": f"You rummage around the room and found a few items in a pile of rubble.", 
        "item": "Medkit",
        "options": {
            "2": {"description": "Leave the house", "next": "outside"}
        }
    },
    "outside": {
        "description": "You are outside the house.\n You see a path long winding path with flowers covering most of it leading towards a mysterious looking forest with tall dark trees making it hard to see into.\n Whilst next to it you see another path one more moden looking with the classic brick like path with a nearly broken looking street lights down on along the path flickering randomly on and off allumintaing a sign pointing towards the nearest town.",
        "options": {
            "1": {"description": "Go to the forest", "next": "forest"},
            "2": {"description": "Go to the town", "next": "town"}
        }
    },
    "forest": {
        "description": "The forest is dense and eerie. The trees block out most of the sun only allowing small amount of light to peer in.\n  You feel like someones watching you whilst you slowly walk your way through.\n Its as though your seeing faces in trees or were they just past the trees.\n You see an abandond cabin not that far away.",
        "options": {
            "1": {"description": "Approach the cabin", "next": "cabin"},
            "2": {"description": "Return to the house", "next": "outside"}
        }
    },
    "cabin": {
        "description": "As you approch the cabin you a standing mail post by the fence of the proerty with a massive heart on the side of it.\n Inside the heart is written D+I proberbly the inteals of the previous owners.\n Sat out on the porch are two bowls on dog size and another cat size with the names Shy and Loki written on them respectively.\n As you slowly enture the cabin you take in the interior of the room.\n You see against a wall a massive sword next to a bow above a a fire place with a photo of one the owners on a majestic horse.\n Across from the fire place sits a cute coffee table with some books stacked on top of eachother at the top you see The song of Achilles.\n You can tell the owners loved this place dearly",
        "options": {
            "1": {"description": "leaves", "next": "outside"},
        }
    },
    "town": {
        "description": "The town is deserted basicaly no noise anywhere the only thing heard is the sound of rats scurrying around looking for trash to eat.\n You see an old abandoned store with its windows smashed in creating a hole to climb through to get in.\n You see that they still have some supplies left which could help you in your journey.",
        "options": {
            "1": {"description": "Enter the store", "next": "store"},
            "2": {"description": "Explore further into the town", "next": "explore_town"}
        }
    },
    "local spoons": {
        "description": "As you continue walking through the remains of the town you. Every place looks closed down and abandoned, windows broken. Cars abandond on the streets. As you wander round the town you start giving up hope of finding others till you heard that noise. It sounded like screams nut not scared screams it sound like joy. You started running towards it and as you turned the corner you see a bar open with people in. The windows have table up against them blocking people from breaking them down and the only entrance you can see is a massive door with people staiond infrount of them probably watching out for zombies.",
        "options": {
            "1": {"description": "Enter the store", "next": "players home"},
            "2": {"description": "Explore further into the town", "next": "characters school school"}
        }
    },
    "players home": {
        "description": "As you walk up to your home, memoires of the place come flooding back to you.\n You remeber when you first bought it with your partner,\n your remeber walking into the house after your wedding with your wife in your arms,\n when you brought your child home for the first time.\n It looks exactly as you rember it except from all the damages from the zombie attacks.\n You lookaround the interiour of the room and your eyes lock onto the door leading to what your remember being a basement\n but if it was just a basement why does the door looks so metalic likes its trying to keep people out?",
        "options": {
            "1": {"description": "Enter the store", "next": "charcters sons school"},
            "2": {"description": "Enter the store", "next": "museum"},
            "3": {"description": "Explore further into the town", "next": "players home basement"}
        }
    },
    "players home basement": {
        "description": "As you slowly open the heavy door you see nothing but a metalic stair case with nothing else but a few dimmly lit bulbs hanging above it eerierly inviting you down to see what it has instore for you.\n As you slowly make your way to the end of the stair case panic starts to set in what if this is where it all started?\n What if there is nothing left in?\n What if?\n. As you slowly open the last door you see walls lined with selfs and draws with food, bandages and supplies everywhere this isnt where it started\n this is a panic room for you and your family to hide incase of this such scenario.",
        "options": {
            "1": {"description": "Enter the store", "next": "store"},
            "2": {"description": "Explore further into the town", "next": "explore_town"}
        }
    },
"charcters sons school": {
        "description": "You arrive at what you remeber being your sons school.\n It looks different from how you remember most of the doors are boarded up except for one set of double doors.\n From closer inseption you are able to work out thats its become a tempoary safe place.\n However you see zombies trying to break in from the sides to many for the people to handle.\n You desicde you have to rsuh in and try to warn people.",
        "options": {
            "1": {"description": "Enter the store", "next": "players home"},
            "2": {"description": "Explore further into the town", "next": "museum"}
        }
    },
    "museum": {
        "description": "You approch the massive building looking older than any of the other buildings in the area.\n The building looked as if its been untouched throughout all of this madness.\n As you reach the door you notice there is people inside hiding ",
        "options": {
            "1": {"description": "Enter the store", "next": "players home"},
            "2": {"description": "Explore further into the town", "next": "charcters son school"}
        }
    },
}
    # Additional locations can be added here

def random_encounter():
    encounters = [
        "A zombie jumps out at you!",
        "You find a mysterious item on the ground.",
        "A group of survivors approach you cautiously.",
        "You hear a distant scream and feel uneasy."
    ]
"journal": {
"discrption": "",
}