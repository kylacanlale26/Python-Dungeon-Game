from combine import hero, adventure

# GAME OVERALL SYSTEM
def game():
    
    print("\n====== PYTHON DUNGEON QUEST ======") #game name

    player = hero() #calls hero name and stats choice input and stats display

    print(f"\nWelcome to Python Dungeon Quest, Hero {player.name} the {player.player_class}!") #welcome

    print("\nExplore dangerous dungeons, defeat enemies, and become the strongest hero!") #game description
   
    print("\n========================")

    print("\nEntering the dungeon...")

    print("\n========================")

    # menu

    adventure(player) # calls adventure function

game()