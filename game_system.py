# Group Members
    # Bayani, JD
    # Lacanlale, Kyla
    # Mercado, Luis
    # Mohammad, Harry
    # Nisperos, Joy
    # Ocampo, Cassey
    # Quiambao, Justin

from hero import hero
from adventure import adventure

# run game here
def game():
    
    print("\n~ PYTHON DUNGEON QUEST ~") #game name

    player = hero() #calls hero name and stats choice input and stats display

    print(f"\nWelcome to Python Dungeon Quest, Hero {player.name} the {player.player_class}!") #welcome

    print("\nExplore dangerous dungeons, defeat enemies, and become the strongest hero!\n") #game description
   
    print("=" * 24) #boarder

    print("\nEntering the dungeon...\n")

    print("=" * 24) #boarder

    adventure(player) # calls adventure function

game()