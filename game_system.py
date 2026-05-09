from combine import hero, adventure

# GAME OVERALL SYSTEM
def game():
    
    print("\n====== PYTHON DUNGEON QUEST ======") #game name

    print("\nWelcome to Python Dungeon Quest!") #welcome

    print("\nExplore dangerous dungeons, defeat enemies, and become the strongest hero!") #game description

    player = hero() #calls hero name and stats choice input and stats display

    # game objectives

    # menu

    adventure(player) # calls adventure function

game()