# Dictionary of locations
locations = {
    "landing_room": {
        "description": "You are in the landing room. You quickly glance around the room taking in the surrounding area. It appears to be a regular living room but with funtiure smashed to pieces and thrown agross the room as if they were after something or in a voilent rage. The only a few things our still standing in the room. You can look around or leave the house.",
        "options": {
            "1": {"description": "Look around the room", "next": "landing_room"},
            "2": {"description": "Leave the house", "next": "outside"}
        }
    },
    "outside": {
        "description": "You are outside the house. You see a path long winding path with flowers covering most of it leading towards a mysterious looking forest with tall dark trees making it hard to see into. Whilst next to it you see another path one more moden looking with the classic brick like path with a nearly broken looking street lights down on along the path flickering randomly on and off allumintaing a sign pointing towards the nearest town.",
        "options": {
            "1": {"description": "Go to the forest", "next": "forest"},
            "2": {"description": "Go to the town", "next": "town"}
        }
    },
    "forest": {
        "description": "The forest is dense and eerie. The trees block out most of the sun only allowing small amount of light to peer in.  You feel like someones watching you whilst you slowly walk your way through. Its as though your seeing faces in trees or were they just past the trees. You see an abandond cabin not that far away.",
        "options": {
            "1": {"description": "Approach the cabin", "next": "cabin"},
            "2": {"description": "Return to the house", "next": "landing_room"}
        }
    },
     "cabin": {
        "description": "As you approch the cabin you a standing mail post by the fence of the proerty with a massive heart on the side of it. Inside the heart is written D+I proberbly the inteals of the previous owners. Sat out on the porch are two bowls on dog size and another cat size with the names Shy and Loki written on them respectively. As you slowly enture the cabin you take in the interior of the room. You see against a wall a massive sword next to a bow above a a fire place with a photo of one the owners on a majestic horse. Across from the fire place sits a cute coffee table with some books stacked on top of eachother at the top you see The song of Achilles. You can tell the owners loved this place dearly",
        "options": {
        }
     }
    "town": {
        "description": "The town is deserted basicaly no noise anywhere the only thing heard is the sound of rats scurrying around looking for trash to eat. You see an old abandoned store with its windows smashed in creating a hole to climb through to get in. You see that they still have some supplies left which could help you in your journey.",
        "options": {
            "1": {"description": "Enter the store", "next": "store"},
            "2": {"description": "Explore further into the town", "next": "explore_town"}
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